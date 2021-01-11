import logging

logging.getLogger('discord')
logger = logging.getLogger('bot').getChild('myfunction')
formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def getLogger(name, level= logging.DEBUG, saveName= 'mainnoname.log',path='.'):
    if '.' in name:
        raise NameError('name is not root')
        return
    #ロガーの定義
    def_logger = logging.getLogger(name)
    def_logger.setLevel(level)
    #ファイル書き込み用
    fh = logging.FileHandler(path + '/' + saveName, encoding='utf-8')
    fh.setFormatter(formatter)
    fh.setLevel(logging.NOTSET)
    def_logger.addHandler(fh)
    #最上位ロガー専用
    warningSaveName = path + '/' + 'warning' + saveName
    fhw = logging.FileHandler(warningSaveName, encoding='utf-8')
    fhw.setFormatter(formatter)
    fhw.setLevel(logging.WARNING)
    #コンソール出力用
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.NOTSET)
    #それぞれロガーに追加
    def_logger.addHandler(sh)
    def_logger.addHandler(fhw)
    return def_logger

def getChild(root, child, level= logging.NOTSET, file= 'mainnoname.log'):
    def_logger= logging.getLogger(root).getChild(child)
    def_logger.setLevel(level)
    fh= logging.FileHandler(file)
    fh.setFormatter(formatter)
    fh.setLevel(logging.NOTSET)
    def_logger.addHandler(fh)
    return def_logger

def userinfo(ctx):
    return ctx.author.name + ' _ ' + str(ctx.author.id)
