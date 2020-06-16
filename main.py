"""
    SmashOmakase.py

    スマブラのキャラをおまかせで選んで、配信用に文字画像生成する。
    Python3.6.8 64-bitで作成。
"""


from logging import getLogger, DEBUG
from kivy.app import App
from kivy.uix.label import Label
from PIL import Image, ImageDraw, ImageFont
import csv
import random as ra

# 画像周りの定数
IMG_SIZE_X = 550
IMG_SIZE_Y = 50
FNT_COLOR = "yellow"
BG_COLOR = (0, 0, 0, 0)
def main():
    mode = 0
    end_flg = False
    fc = FighterChooser("character.csv")
    while(end_flg != True):
        print(
            """
            機能を選択↓
            ********************
            1.おまかせ
            2.データ追加
            0.終了
            ********************
            """
        )
        mode = int(input())
        if(mode == 1):
            fc.random_select_g(IMG_SIZE_X,IMG_SIZE_Y,FNT_COLOR,BG_COLOR)
        elif(mode == 2):
            fc.add_fighter()
        elif(mode == 0):
            end_flg = True
        else:
            print("入力された機能番号が正しくありません。")

class FighterChooser:

    def __init__(self,filename):
        """コンストラクタ
        インスタンス変数を宣言し、ファイター一覧のcsvファイルを読み込んでdict型に変換します。
        """
        self.dic_len = 0
        self.filename = filename
        with open(filename,encoding='utf8') as f:
            self.fi_dic = {}
            self.fi_read = csv.DictReader(f)
            for row in self.fi_read:
                self.fi_dic[row['no']] = row['name']
    
    def add_fighter(self):
        """ キャラCSV書き込みメソッド
        csvファイルを読み込んでキャラクターを一件挿入します。
        """
        with open(self.filename,encoding='utf8',mode='a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([len(self.fi_dic) + 1,input("ファイター名 >> ")])
            print("新しいファイターを一件追加しました。")

    def random_select_g(self,x,y,color,bg_color):
        """ ランダムキャラ名出力メソッド(画像表示版)
        ランダムにキャラクター名を出力します。
        """
        img = Image.new('RGBA',(x,y),bg_color)
        draw = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("msgothic.ttc",50) 
        random_no = ra.randint(1,len(self.fi_dic))
        name_text = (self.fi_dic.get(str(random_no)))
        draw.text((0,0),name_text,FNT_COLOR,font=fnt)
        img.save("./omakase_name.png")
        print("『%s』を出力しました。"%name_text)

if __name__ == "__main__":
    main()