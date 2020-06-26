import logging

def getLogger(name, level= logging.DEBUG, saveName= 'mainnoname.log',path='.'):
    #フォーマットの定義
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #ロガーの定義
    logger = logging.getLogger(name)
    logger.setLevel(level)
    #ファイル書き込み用
    fh = logging.FileHandler(path + '/' + saveName, encoding='utf-8')
    fh.setFormatter(formatter)
    fh.setLevel(logging.NOTSET)
    logger.addHandler(fh)
    if not '.' in name:
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
        logger.addHandler(sh)
        logger.addHandler(fhw)
    return logger
