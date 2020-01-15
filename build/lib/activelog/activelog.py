#-*- coding:utf-8 -*-
import datetime
import inspect
import time
import sys
import os


class Logger:
    # log mode
    DEBUG  = 0
    INFO   = 1
    WARN   = 2
    ERROR  = 3
    STDOUT = 4
    STDERR = 5
    TYPES  = ['DEBUG', 'INFO', 'WARN', 'ERROR']

    def __init__(self, logdev, shift_freq=None, shift_size=1048576,
                 level=DEBUG, init=False, datetime_format=None,
                 shift_period_suffix='_%Y-%m-%d'):
        ## -----*----- コンストラクタ -----*----- ##
        #
        # logdev              -> filepath / self.STDOUT / self.STDERR
        # shift_freq          -> 0 ~  (≠ 0) [sec]
        # shift_size          -> 0 ~  (≠ 0) [byte]
        # init                -> clear log file?
        # datetime_format     -> Default is %Y-%m-%d %H:%M:%S.%f
        # shift_period_suffix -> Default is _%Y-%m-%d

        self.logdev = logdev
        if self.logdev != self.STDOUT and self.logdev != self.STDERR:
            # ディレクトリを作成（無い場合）
            dirname = os.path.dirname(self.logdev)
            if dirname != '': os.makedirs(dirname, exist_ok=True)
            # ログファイルの初期化
            if init: self.__clear()

        # 出力レベル
        self.level = level

        # datetimeの出力フォーマット
        if datetime_format == None:
            self.datetime_format = '%Y-%m-%d %H:%M:%S.%f'
        else:
            self.datetime_format= datetime_format

        # 切り替え頻度
        self.shift_freq = shift_freq

        # 切り替えサイズ
        self.shift_size = shift_size

        # ログファイル名の末尾に追加する文字列フォーマット
        self.shift_period_suffix = shift_period_suffix


    def __clear(self):
        ## -----*----- ログ削除 -----*----- ##
        with open(self.logdev, 'w') as f:
            f.write('')


    def __add(self, msg, level):
        # スタックフレーム解析
        frame = inspect.stack()[2][0]
        info = inspect.getframeinfo(frame)
        # 現在時刻
        dt_now = datetime.datetime.now().strftime(self.datetime_format)
        # 出力テキスト
        out_text = '[%s #%s line:%s] %-5s -- : %s' %(dt_now, info.filename, info.lineno, self.TYPES[level], msg)

        if self.logdev == self.STDOUT:
            print(out_text, file=sys.stdout)

        elif self.logdev == self.STDERR:
            print(out_text, file=sys.stderr)
            sys.exit(1)

        else:
            if self.level > level:
                return

            file = self.logdev
            is_new_file = False
            if os.path.exists(self.logdev):

                # ログファイルをサイズで分割
                if os.path.getsize(self.logdev) > self.shift_size:
                    is_new_file = True

                # ログファイルを指定頻度で分割
                if self.shift_freq != None:
                    if (time.time() - os.stat(self.logdev).st_birthtime) > self.shift_freq:
                        is_new_file = True

            if is_new_file:
                dt = datetime.datetime.now().strftime(self.shift_period_suffix)
                file = dt.join(os.path.splitext(self.logdev))

            # ファイルにログを追記
            with open(file, 'a') as f:
                f.write(out_text + '\n')

    ## ===== OUTPUT ==============
    def debug(self, msg):
        ## -----*----- output debug -----*----- ##
        self.__add(msg, self.DEBUG)
    def info(self, msg):
        ## -----*----- output info -----*----- ##
        self.__add(msg, self.INFO)
    def warn(self, msg):
        ## -----*----- output warning -----*----- ##
        self.__add(msg, self.WARN)
    def error(self, msg):
        ## -----*----- output error -----*----- ##
        self.__add(msg, self.ERROR)
