import discord
from discord.ext import commands
import logging

logging.getLogger('discord')
logger = logging.getLogger('bot').getChild(__name__)

class Help(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        self.no_category = "カテゴリ未設定"
        self.command_attrs["short_doc"] = "このメッセージを表示します。"
        self.command_attrs["help"] = "このBOTのヘルプコマンドです。"
        self.color = 0x54c3f1
        self.description = 'IBMproject専用BOTです。銀行機能、銀行間連携機能等の機能があります。'

    async def create_category_tree(self,category,enclosure):
        """
        コマンドの集まり（Group、Cog）から木の枝状のコマンドリスト文字列を生成する。
        生成した文字列は enlosure 引数に渡された文字列で囲われる。
        """
        content = ""
        command_list = category.walk_commands()
        for cmd in await self.filter_commands(command_list,sort=False):
            if cmd.root_parent:
                # cmd.root_parent は「根」なので、根からの距離に応じてインデントを増やす
                index = cmd.parents.index(cmd.root_parent)
                indent = "\t" * (index + 1)
                if indent:
                    content += f"{indent}- {cmd.name} : {cmd.short_doc}\n"
                else:
                    # インデントが入らない、つまり木の中で最も浅く表示されるのでprefixを付加
                    content += f"{self.context.prefix}{cmd.name} : {cmd.short_doc}\n"
            else:
                # 親を持たないコマンドなので、木の中で最も浅く表示する。prefixを付加
                content += f"{self.context.prefix}{cmd.name} : {cmd.short_doc}\n"

        min_level = float("inf")
        adjusted_content = ""

        for line in content.split("\n"):
            # 各行のインデントを、最も浅いレベルまで削る
            if not line:
                # 空行は削る必要がないので、無視
                continue
            level = 0  #  その行のインデントレベル
            for char in line:
                if char == "\t":
                    level += 1
                else:
                    break
            if level < min_level:
                min_level = level
        if min_level == 0:
            # 無駄なインデントは無かったので、削る必要もない
            adjusted_content = content
        else:
            for line in content.split("\n"):
                if not line.startswith("\t"):
                    adjusted_content += line + "\n"
                    continue
                adjusted_content += "".join(line.split("\t" * min_level)[1:]) + "\n"

        return enclosure + adjusted_content + enclosure

    async def send_bot_help(self,mapping):
        embed = discord.Embed(title="helpコマンド", color=self.color)
        if self.description:
            embed.description = self.description
        for cog in mapping:
            if cog:
                cog_name = cog.qualified_name
            else:
                cog_name = self.no_category
            command_list = await self.filter_commands(mapping[cog],sort=True)
            content = ""
            for cmd in command_list:
                if not(cog_name == self.no_category and cmd.short_doc == ''):
                    content += f"`{self.context.prefix}{cmd.name}` - {cmd.short_doc}\n"
            embed.add_field(name=cog_name,value=content,inline=False)
        embed.set_footer(text= self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self,cog):
        embed = discord.Embed(title=cog.qualified_name,description=cog.description,color=self.color)
        embed.add_field(name="コマンドリスト",value=await self.create_category_tree(cog,"```"))
        embed.set_footer(text= self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_group_help(self,group):
        embed = discord.Embed(title=f"{self.context.prefix}{group.qualified_name}",
            description=group.description,color=self.color)
        if group.aliases:
            embed.add_field(name="有効なエイリアス",value="`" + "`, `".join(group.aliases) + "`",inline=False)
        if group.help:
            embed.add_field(name="ヘルプテキスト",value=group.help,inline=False)
        embed.add_field(name="サブコマンドリスト",value=await self.create_category_tree(group,"```"),inline=False)
        embed.set_footer(text= self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_command_help(self,command):
        params = " ".join(command.clean_params.keys())
        embed = discord.Embed(title=f"{self.context.prefix}{command.qualified_name} {params}",
            description=command.description,color=self.color)
        if command.aliases:
            embed.add_field(name="有効なエイリアス：",value="`" + "`, `".join(command.aliases) + "`",inline=False)
        if command.help:
            embed.add_field(name="ヘルプテキスト：",value=command.help,inline=False)
        embed.set_footer(text= self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_error_message(self, error):
        embed = discord.Embed(title="ヘルプ表示のエラー",description=error,color=self.color)
        embed.set_footer(text= self.get_ending_note())
        await self.get_destination().send(embed=embed)

    def get_ending_note(self):
        """Returns help command's ending note. This is mainly useful to override for i18n purposes."""
        command_name = self.invoked_with
        return "{0}{1} command と打ち込むことでコマンドについてのヘルプを閲覧できます。\n" \
               "{0}{1} category とすることでカテゴリーの詳細情報を閲覧できます。".format(self.clean_prefix, command_name)

    def command_not_found(self,string):
        return f"{string} というコマンドは存在しません。"

    def subcommand_not_found(self,command,string):
        if isinstance(command, commands.Group) and len(command.all_commands) > 0:
            # もし、そのコマンドにサブコマンドが存在しているなら
            return f"{command.qualified_name} に {string} というサブコマンドは登録されていません。"
        return f"{command.qualified_name} にサブコマンドは登録されていません。"
