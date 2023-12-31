#
# mrfont.py 2022/6/16
#
# https://aburi6800.hatenablog.com/entry/2020/06/13/132328
# https://qiita.com/mochitetris/items/7ef934e565b000bf1932
# https://littlelimit.net/misaki.htm
#
import pyxel
def text(x, y, txt, col=7):
    FONT_DIC = {
        '　' : (),
        '、' : (0,5,1,6,),
        '。' : (1,4,0,5,2,5,1,6,),
        '，' : (1,4,2,4,2,5,1,6,),
        '．' : (1,5,2,5,1,6,2,6,),
        '・' : (2,3,3,3,2,4,3,4,),
        '：' : (2,1,3,1,2,2,3,2,2,4,3,4,2,5,3,5,),
        '？' : (2,0,3,0,4,0,5,0,1,1,6,1,6,2,4,3,5,3,3,4,3,6,),
        '！' : (3,0,3,1,3,2,3,3,3,4,3,6,),
        'ー' : (0,2,1,3,2,3,3,3,4,3,5,3,6,3,),
        '／' : (6,0,5,1,4,2,3,3,2,4,1,5,0,6,),
        '～' : (1,2,2,2,0,3,3,3,6,3,4,4,5,4,),
        '（' : (5,0,4,1,3,2,3,3,3,4,4,5,5,6,),
        '）' : (1,0,2,1,3,2,3,3,3,4,2,5,1,6,),
        '《' : (4,0,6,0,3,1,5,1,2,2,4,2,1,3,3,3,2,4,4,4,3,5,5,5,4,6,6,6,),
        '》' : (0,0,2,0,1,1,3,1,2,2,4,2,3,3,5,3,2,4,4,4,1,5,3,5,0,6,2,6,),
        '「' : (3,0,4,0,5,0,6,0,3,1,3,2,3,3,3,4,3,5,),
        '」' : (3,1,3,2,3,3,3,4,3,5,0,6,1,6,2,6,3,6,),
        '【' : (3,0,4,0,5,0,3,1,4,1,3,2,3,3,3,4,3,5,4,5,3,6,4,6,5,6,),
        '】' : (1,0,2,0,3,0,2,1,3,1,3,2,3,3,3,4,2,5,3,5,1,6,2,6,3,6,),
        '－' : (0,3,1,3,2,3,3,3,4,3,5,3,6,3,),
        '＝' : (0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,4,1,4,2,4,3,4,4,4,5,4,6,4,),
        '＜' : (5,1,6,1,2,2,3,2,4,2,0,3,1,3,2,4,3,4,4,4,5,5,6,5,),
        '＞' : (0,1,1,1,2,2,3,2,4,2,5,3,6,3,2,4,3,4,4,4,0,5,1,5,),
        '★' : (3,0,3,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,2,3,3,3,4,3,2,4,3,4,4,4,1,5,2,5,4,5,5,5,1,6,5,6,),
        'ヶ' : (2,2,2,3,3,3,4,3,5,3,1,4,4,4,4,5,3,6,),
        '…' : (0,3,3,3,6,3,),
        '％' : (1,0,6,0,0,1,2,1,5,1,1,2,4,2,3,3,2,4,5,4,1,5,4,5,6,5,0,6,5,6,),
        '↑' : (3,0,2,1,3,1,4,1,1,2,3,2,5,2,3,3,3,4,3,5,3,6,),
        '↓' : (3,0,3,1,3,2,3,3,1,4,3,4,5,4,2,5,3,5,4,5,3,6,),
        '←' : (2,1,1,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,2,5,),
        '→' : (4,1,5,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,5,4,4,5,),
        '⇔' : (2,1,4,1,1,2,2,2,3,2,4,2,5,2,0,3,6,3,1,4,2,4,3,4,4,4,5,4,2,5,4,5,),
        '√' : (3,0,4,0,5,0,6,0,3,1,2,2,2,3,0,4,1,4,2,4,1,5,1,6,),
        '㎡' : (5,0,6,0,6,1,0,2,1,2,3,2,5,2,0,3,2,3,4,3,5,3,6,3,0,4,2,4,4,4,0,5,2,5,4,5,0,6,2,6,4,6,),
        '０' : (2,0,3,0,4,0,5,0,1,1,6,1,1,2,5,2,6,2,1,3,3,3,4,3,6,3,1,4,2,4,6,4,1,5,6,5,2,6,3,6,4,6,5,6,),
        '１' : (3,0,2,1,3,1,3,2,3,3,3,4,3,5,2,6,3,6,4,6,),
        '２' : (2,0,3,0,4,0,5,0,1,1,6,1,6,2,4,3,5,3,2,4,3,4,1,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        '３' : (2,0,3,0,4,0,5,0,1,1,6,1,6,2,3,3,4,3,5,3,6,4,1,5,6,5,2,6,3,6,4,6,5,6,),
        '４' : (5,0,4,1,5,1,3,2,5,2,2,3,5,3,1,4,5,4,1,5,2,5,3,5,4,5,5,5,6,5,5,6,),
        '５' : (1,0,2,0,3,0,4,0,5,0,6,0,1,1,1,2,2,2,3,2,4,2,5,2,1,3,6,3,6,4,1,5,6,5,2,6,3,6,4,6,5,6,),
        '６' : (3,0,4,0,5,0,2,1,1,2,1,3,2,3,3,3,4,3,5,3,1,4,6,4,1,5,6,5,2,6,3,6,4,6,5,6,),
        '７' : (1,0,2,0,3,0,4,0,5,0,6,0,6,1,5,2,4,3,4,4,3,5,3,6,),
        '８' : (2,0,3,0,4,0,5,0,1,1,6,1,1,2,6,2,2,3,3,3,4,3,5,3,1,4,6,4,1,5,6,5,2,6,3,6,4,6,5,6,),
        '９' : (2,0,3,0,4,0,5,0,1,1,6,1,1,2,6,2,2,3,3,3,4,3,5,3,6,3,6,4,5,5,2,6,3,6,4,6,),
        
        'ぁ' : (3,1,2,2,3,2,4,2,5,2,3,3,2,4,3,4,4,4,5,4,1,5,3,5,4,5,6,5,2,6,3,6,6,6,),
        'あ' : (2,0,1,1,2,1,3,1,4,1,5,1,2,2,2,3,3,3,4,3,5,3,1,4,2,4,4,4,6,4,0,5,2,5,3,5,6,5,1,6,2,6,5,6,),
        'ぃ' : (1,2,4,2,1,3,5,3,1,4,5,4,1,5,3,5,2,6,),
        'い' : (0,1,4,1,0,2,5,2,0,3,6,3,0,4,6,4,1,5,3,5,2,6,),
        'ぅ' : (2,1,3,1,4,1,2,3,3,3,4,3,1,4,5,4,4,5,2,6,3,6,),
        'う' : (2,0,3,0,4,0,5,0,2,2,3,2,4,2,5,2,1,3,6,3,6,4,5,5,2,6,3,6,4,6,),
        'ぇ' : (2,1,3,1,4,1,1,3,2,3,3,3,4,3,3,4,2,5,3,5,1,6,4,6,5,6,),
        'え' : (2,0,3,0,4,0,5,0,1,2,2,2,3,2,4,2,5,2,4,3,3,4,4,4,2,5,4,5,1,6,5,6,6,6,),
        'ぉ' : (2,1,1,2,2,2,3,2,5,2,2,3,2,4,3,4,4,4,1,5,2,5,5,5,2,6,4,6,),
        'お' : (2,0,0,1,1,1,2,1,3,1,5,1,2,2,6,2,2,3,3,3,4,3,5,3,1,4,2,4,6,4,0,5,2,5,6,5,1,6,2,6,4,6,5,6,),
        'か' : (2,0,2,1,0,2,1,2,2,2,3,2,5,2,2,3,4,3,6,3,1,4,4,4,6,4,1,5,4,5,0,6,2,6,3,6,),
        'が' : (2,0,4,0,6,0,2,1,0,2,1,2,2,2,3,2,5,2,2,3,4,3,6,3,1,4,4,4,6,4,1,5,4,5,0,6,2,6,3,6,),
        'き' : (3,0,1,1,2,1,3,1,4,1,5,1,4,2,1,3,2,3,3,3,4,3,5,3,6,3,2,4,5,4,1,5,2,6,3,6,4,6,5,6,),
        'ぎ' : (3,0,5,0,1,1,2,1,3,1,4,1,5,1,4,2,1,3,2,3,3,3,4,3,5,3,6,3,2,4,5,4,1,5,2,6,3,6,4,6,5,6,),
        'く' : (5,0,4,1,2,2,3,2,1,3,2,4,3,4,4,5,5,6,),
        'ぐ' : (5,0,4,1,2,2,3,2,5,2,1,3,2,4,3,4,4,5,5,6,),
        'け' : (0,0,4,0,0,1,4,1,0,2,2,2,3,2,4,2,5,2,6,2,0,3,4,3,0,4,4,4,0,5,4,5,3,6,),
        'げ' : (0,0,4,0,6,0,0,1,4,1,0,2,2,2,3,2,4,2,5,2,6,2,0,3,4,3,0,4,4,4,0,5,4,5,3,6,),
        'こ' : (2,1,3,1,4,1,5,1,2,4,1,5,2,6,3,6,4,6,5,6,6,6,),
        'ご' : (4,0,6,0,2,1,3,1,4,1,5,1,2,4,1,5,2,6,3,6,4,6,5,6,6,6,),
        'さ' : (4,0,4,1,1,2,2,2,3,2,4,2,5,2,6,2,5,3,2,4,5,4,1,5,2,6,3,6,4,6,5,6,),
        'ざ' : (4,0,6,0,4,1,1,2,2,2,3,2,4,2,5,2,6,2,5,3,2,4,5,4,1,5,2,6,3,6,4,6,5,6,),
        'し' : (2,0,2,1,2,2,2,3,2,4,2,5,6,5,3,6,4,6,5,6,),
        'じ' : (2,0,4,0,6,0,2,1,2,2,2,3,2,4,2,5,6,5,3,6,4,6,5,6,),
        'す' : (4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,3,2,4,2,2,3,4,3,3,4,4,4,4,5,3,6,),
        'ず' : (4,0,6,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,3,2,4,2,2,3,4,3,3,4,4,4,4,5,3,6,),
        'せ' : (2,0,5,0,2,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,2,3,5,3,2,4,4,4,5,4,2,5,3,6,4,6,5,6,6,6,),
        'ぜ' : (2,0,4,0,6,0,2,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,2,3,5,3,2,4,4,4,5,4,2,5,3,6,4,6,5,6,6,6,),
        'そ' : (2,0,3,0,4,0,5,0,4,1,3,2,1,3,2,3,3,3,4,3,5,3,6,3,3,4,3,5,4,6,5,6,),
        'ぞ' : (2,0,3,0,4,0,5,0,4,1,6,1,3,2,1,3,2,3,3,3,4,3,5,3,6,3,3,4,3,5,4,6,5,6,),
        'た' : (2,0,0,1,1,1,2,1,3,1,2,2,4,2,5,2,6,2,1,3,1,4,4,4,1,5,3,5,0,6,4,6,5,6,6,6,),
        'だ' : (2,0,4,0,6,0,0,1,1,1,2,1,3,1,2,2,4,2,5,2,6,2,1,3,1,4,4,4,1,5,3,5,0,6,4,6,5,6,6,6,),
        'ち' : (4,0,1,1,2,1,3,1,4,1,5,1,6,1,3,2,3,3,4,3,5,3,2,4,6,4,6,5,3,6,4,6,5,6,),
        'ぢ' : (4,0,6,0,1,1,2,1,3,1,4,1,5,1,6,1,3,2,3,3,4,3,5,3,2,4,6,4,6,5,3,6,4,6,5,6,),
        'っ' : (3,3,4,3,1,4,2,4,5,4,5,5,3,6,4,6,),
        'つ' : (2,1,3,1,4,1,5,1,0,2,1,2,6,2,6,3,6,4,3,5,4,5,5,5,),
        'づ' : (4,0,6,0,2,1,3,1,4,1,5,1,0,2,1,2,6,2,6,3,6,4,3,5,4,5,5,5,),
        'て' : (4,0,5,0,6,0,1,1,2,1,3,1,5,1,4,2,3,3,3,4,4,5,5,6,6,6,),
        'で' : (4,0,5,0,6,0,1,1,2,1,3,1,5,1,4,2,6,2,3,3,3,4,4,5,5,6,6,6,),
        'と' : (2,0,2,1,2,2,5,2,3,3,4,3,2,4,1,5,2,6,3,6,4,6,5,6,6,6,),
        'ど' : (2,0,4,0,6,0,2,1,2,2,5,2,3,3,4,3,2,4,1,5,2,6,3,6,4,6,5,6,6,6,),
        'な' : (2,0,0,1,1,1,2,1,3,1,5,1,2,2,6,2,1,3,5,3,0,4,3,4,4,4,5,4,2,5,5,5,6,5,3,6,4,6,),
        'に' : (0,0,0,1,3,1,4,1,5,1,0,2,0,3,0,4,3,4,0,5,2,5,0,6,3,6,4,6,5,6,6,6,),
        'ぬ' : (4,0,1,1,4,1,1,2,3,2,4,2,5,2,1,3,2,3,4,3,6,3,0,4,2,4,3,4,6,4,0,5,2,5,5,5,6,5,1,6,3,6,5,6,6,6,),
        'ね' : (2,0,2,1,4,1,5,1,0,2,1,2,2,2,3,2,6,2,2,3,6,3,1,4,2,4,5,4,6,4,0,5,2,5,4,5,6,5,2,6,5,6,6,6,),
        'の' : (2,1,3,1,4,1,1,2,3,2,5,2,0,3,3,3,6,3,0,4,2,4,6,4,1,5,5,5,3,6,4,6,),
        'は' : (0,0,5,0,0,1,5,1,0,2,2,2,3,2,4,2,5,2,6,2,0,3,5,3,0,4,3,4,4,4,5,4,0,5,2,5,5,5,0,6,3,6,4,6,6,6,),
        'ば' : (0,0,4,0,6,0,0,1,5,1,0,2,2,2,3,2,4,2,5,2,6,2,0,3,5,3,0,4,3,4,4,4,5,4,0,5,2,5,5,5,0,6,3,6,4,6,6,6,),
        'ぱ' : (0,0,5,0,0,1,4,1,6,1,0,2,2,2,3,2,4,2,5,2,6,2,0,3,5,3,0,4,3,4,4,4,5,4,0,5,2,5,5,5,0,6,3,6,4,6,6,6,),
        'ひ' : (2,0,4,0,0,1,1,1,2,1,5,1,2,2,5,2,6,2,1,3,5,3,1,4,5,4,1,5,5,5,2,6,3,6,4,6,),
        'び' : (2,0,4,0,6,0,0,1,1,1,2,1,5,1,2,2,5,2,6,2,1,3,5,3,1,4,5,4,1,5,5,5,2,6,3,6,4,6,),
        'ぴ' : (2,0,4,0,5,0,0,1,1,1,2,1,4,1,6,1,2,2,5,2,6,2,1,3,5,3,1,4,5,4,1,5,5,5,2,6,3,6,4,6,),
        'ふ' : (3,0,4,1,3,2,3,3,1,4,4,4,5,4,1,5,4,5,6,5,0,6,2,6,3,6,6,6,),
        'ぶ' : (3,0,4,1,6,1,3,2,3,3,1,4,4,4,5,4,1,5,4,5,6,5,0,6,2,6,3,6,6,6,),
        'ぷ' : (3,0,5,0,4,1,6,1,3,2,5,2,3,3,1,4,4,4,5,4,1,5,4,5,6,5,0,6,2,6,3,6,6,6,),
        'へ' : (2,1,1,2,3,2,0,3,4,3,5,4,6,4,),
        'べ' : (4,0,6,0,2,1,1,2,3,2,0,3,4,3,5,4,6,4,),
        'ぺ' : (5,0,2,1,4,1,6,1,1,2,3,2,5,2,0,3,4,3,5,4,6,4,),
        'ほ' : (0,0,0,1,2,1,3,1,4,1,5,1,6,1,0,2,4,2,0,3,2,3,3,3,4,3,5,3,6,3,0,4,4,4,0,5,2,5,3,5,4,5,5,5,0,6,2,6,3,6,4,6,6,6,),
        'ぼ' : (0,0,4,0,6,0,0,1,2,1,3,1,4,1,5,1,6,1,0,2,4,2,0,3,2,3,3,3,4,3,5,3,6,3,0,4,4,4,0,5,2,5,3,5,4,5,5,5,0,6,2,6,3,6,4,6,6,6,),
        'ぽ' : (0,0,5,0,0,1,2,1,3,1,4,1,6,1,0,2,4,2,5,2,0,3,2,3,3,3,4,3,5,3,6,3,0,4,4,4,0,5,2,5,3,5,4,5,5,5,0,6,2,6,3,6,4,6,6,6,),
        'ま' : (4,0,1,1,2,1,3,1,4,1,5,1,6,1,4,2,1,3,2,3,3,3,4,3,5,3,6,3,4,4,1,5,2,5,3,5,4,5,5,5,1,6,2,6,3,6,4,6,6,6,),
        'み' : (1,0,2,0,3,0,3,1,2,2,5,2,1,3,2,3,3,3,4,3,5,3,0,4,2,4,5,4,6,4,0,5,1,5,5,5,3,6,4,6,),
        'む' : (2,0,0,1,1,1,2,1,3,1,5,1,2,2,6,2,1,3,2,3,0,4,2,4,1,5,2,5,6,5,2,6,3,6,4,6,5,6,),
        'め' : (4,0,1,1,4,1,1,2,3,2,4,2,5,2,1,3,2,3,4,3,6,3,0,4,2,4,3,4,6,4,0,5,2,5,6,5,1,6,3,6,5,6,),
        'も' : (3,0,1,1,2,1,3,1,4,1,5,1,2,2,1,3,2,3,3,3,4,3,5,3,2,4,6,4,2,5,6,5,3,6,4,6,5,6,),
        'ゃ' : (2,1,4,1,2,2,4,2,5,2,1,3,2,3,3,3,6,3,3,4,5,4,3,5,4,6,),
        'や' : (1,0,4,0,1,1,3,1,4,1,5,1,0,2,1,2,2,2,6,2,2,3,5,3,2,4,3,5,3,6,),
        'ゅ' : (3,1,1,2,3,2,4,2,1,3,2,3,3,3,5,3,1,4,3,4,5,4,3,5,4,5,2,6,),
        'ゆ' : (3,0,0,1,2,1,3,1,4,1,5,1,0,2,1,2,3,2,6,2,0,3,3,3,6,3,0,4,2,4,3,4,4,4,5,4,3,5,2,6,),
        'ょ' : (4,1,4,2,4,3,5,3,2,4,3,4,4,4,1,5,4,5,2,6,3,6,5,6,),
        'よ' : (4,0,4,1,4,2,5,2,6,2,4,3,2,4,3,4,4,4,1,5,4,5,5,5,2,6,3,6,6,6,),
        'ら' : (2,0,3,0,4,1,1,2,1,3,3,3,4,3,5,3,1,4,2,4,6,4,6,5,2,6,3,6,4,6,5,6,),
        'り' : (1,0,3,0,4,0,1,1,2,1,5,1,1,2,5,2,1,3,5,3,5,4,4,5,2,6,3,6,),
        'る' : (2,0,3,0,4,0,5,0,4,1,3,2,2,3,3,3,4,3,5,3,1,4,6,4,2,5,3,5,6,5,2,6,3,6,4,6,5,6,),
        'れ' : (2,0,2,1,4,1,5,1,0,2,1,2,2,2,3,2,5,2,2,3,5,3,1,4,2,4,5,4,0,5,2,5,5,5,2,6,6,6,),
        'ろ' : (2,0,3,0,4,0,5,0,4,1,3,2,2,3,3,3,4,3,5,3,1,4,6,4,6,5,2,6,3,6,4,6,5,6,),
        'わ' : (2,0,2,1,4,1,5,1,0,2,1,2,2,2,3,2,6,2,2,3,6,3,1,4,2,4,6,4,0,5,2,5,6,5,2,6,4,6,5,6,),
        'を' : (3,0,1,1,2,1,3,1,4,1,5,1,2,2,1,3,2,3,3,3,5,3,6,3,0,4,3,4,4,4,2,5,4,5,3,6,4,6,5,6,6,6,),
        'ん' : (3,0,3,1,2,2,2,3,1,4,3,4,1,5,3,5,6,5,0,6,4,6,5,6,),

        'ァ' : (1,2,2,2,3,2,4,2,5,2,3,3,5,3,3,4,4,4,3,5,2,6,),
        'ア' : (1,0,2,0,3,0,4,0,5,0,6,0,6,1,3,2,5,2,3,3,4,3,3,4,3,5,2,6,),
        'ィ' : (5,2,4,3,3,4,4,4,1,5,2,5,4,5,4,6,),
        'イ' : (6,0,5,1,4,2,3,3,4,3,1,4,2,4,4,4,4,5,4,6,),
        'ゥ' : (3,2,1,3,2,3,3,3,4,3,5,3,1,4,5,4,4,5,2,6,3,6,),
        'ウ' : (3,0,1,1,2,1,3,1,4,1,5,1,6,1,1,2,6,2,6,3,5,4,4,5,2,6,3,6,),
        'ェ' : (2,3,3,3,4,3,3,4,3,5,1,6,2,6,3,6,4,6,5,6,),
        'エ' : (1,1,2,1,3,1,4,1,5,1,3,2,3,3,3,4,0,5,1,5,2,5,3,5,4,5,5,5,6,5,),
        'ォ' : (4,2,1,3,2,3,3,3,4,3,5,3,3,4,4,4,1,5,2,5,4,5,3,6,4,6,),
        'オ' : (4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,4,2,3,3,4,3,2,4,4,4,0,5,1,5,4,5,3,6,4,6,),
        'カ' : (3,0,1,1,2,1,3,1,4,1,5,1,6,1,3,2,6,2,3,3,6,3,3,4,6,4,2,5,6,5,1,6,5,6,6,6,),
        'ガ' : (3,0,5,0,1,1,2,1,3,1,4,1,5,1,6,1,3,2,6,2,3,3,6,3,3,4,6,4,2,5,6,5,1,6,5,6,6,6,),
        'キ' : (3,0,1,1,2,1,3,1,4,1,5,1,3,2,3,3,1,4,2,4,3,4,4,4,5,4,6,4,4,5,4,6,),
        'ギ' : (3,0,5,0,1,1,2,1,3,1,4,1,5,1,3,2,3,3,1,4,2,4,3,4,4,4,5,4,6,4,4,5,4,6,),
        'ク' : (3,0,3,1,4,1,5,1,6,1,2,2,6,2,1,3,6,3,5,4,4,5,2,6,3,6,),
        'グ' : (3,0,5,0,3,1,4,1,5,1,6,1,2,2,6,2,1,3,6,3,5,4,4,5,2,6,3,6,),
        'ケ' : (1,0,1,1,2,1,3,1,4,1,5,1,6,1,1,2,4,2,0,3,4,3,4,4,3,5,2,6,),
        'ゲ' : (1,0,4,0,6,0,1,1,2,1,3,1,4,1,5,1,6,1,1,2,4,2,0,3,4,3,4,4,3,5,2,6,),
        'コ' : (1,1,2,1,3,1,4,1,5,1,6,1,6,2,6,3,6,4,6,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        'ゴ' : (4,0,6,0,1,1,2,1,3,1,4,1,5,1,6,1,6,2,6,3,6,4,6,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        'サ' : (2,0,5,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,5,2,2,3,5,3,5,4,4,5,2,6,3,6,),
        'ザ' : (2,0,4,0,6,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,5,2,2,3,5,3,5,4,4,5,2,6,3,6,),
        'シ' : (1,0,2,1,1,2,6,2,2,3,6,3,5,4,4,5,1,6,2,6,3,6,),
        'ジ' : (1,0,4,0,6,0,2,1,1,2,6,2,2,3,6,3,5,4,4,5,1,6,2,6,3,6,),
        'ス' : (1,1,2,1,3,1,4,1,5,1,5,2,4,3,4,4,2,5,3,5,5,5,0,6,1,6,6,6,),
        'ズ' : (4,0,6,0,1,1,2,1,3,1,4,1,5,1,5,2,4,3,4,4,2,5,3,5,5,5,0,6,1,6,6,6,),
        'セ' : (2,0,2,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,2,3,6,3,2,4,5,4,2,5,3,6,4,6,5,6,6,6,),
        'ソ' : (1,0,6,0,2,1,6,1,2,2,6,2,6,3,5,4,4,5,2,6,3,6,),
        'タ' : (3,0,3,1,4,1,5,1,6,1,2,2,6,2,1,3,3,3,4,3,6,3,5,4,4,5,2,6,3,6,),
        'ダ' : (3,0,5,0,3,1,4,1,5,1,6,1,2,2,6,2,1,3,3,3,4,3,6,3,5,4,4,5,2,6,3,6,),
        'チ' : (4,0,5,0,1,1,2,1,3,1,3,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,3,4,3,5,2,6,),
        'ッ' : (1,3,3,3,5,3,1,4,3,4,5,4,4,5,2,6,3,6,),
        'ツ' : (0,1,2,1,6,1,1,2,3,2,6,2,1,3,3,3,6,3,5,4,4,5,2,6,3,6,),
        'テ' : (1,0,2,0,3,0,4,0,5,0,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,3,4,3,5,2,6,),
        'デ' : (1,0,2,0,3,0,4,0,6,0,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,3,4,3,5,2,6,),
        'ト' : (2,0,2,1,2,2,2,3,3,3,4,3,2,4,5,4,2,5,2,6,),
        'ド' : (2,0,4,0,6,0,2,1,2,2,2,3,3,3,4,3,2,4,5,4,2,5,2,6,),
        'ナ' : (3,0,3,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,3,4,2,5,1,6,),
        'ニ' : (1,1,2,1,3,1,4,1,5,1,0,5,1,5,2,5,3,5,4,5,5,5,6,5,),
        'ヌ' : (1,0,2,0,3,0,4,0,5,0,5,1,2,2,3,2,5,2,4,3,3,4,4,4,2,5,5,5,0,6,1,6,),
        'ネ' : (3,0,1,1,2,1,3,1,4,1,5,1,4,2,3,3,2,4,3,4,5,4,0,5,1,5,3,5,6,5,3,6,),
        'ノ' : (5,0,5,1,5,2,4,3,3,4,2,5,0,6,1,6,),
        'ハ' : (2,1,4,1,2,2,5,2,2,3,5,3,1,4,6,4,1,5,6,5,0,6,6,6,),
        'バ' : (4,0,6,0,2,1,2,2,5,2,2,3,5,3,1,4,6,4,1,5,6,5,0,6,6,6,),
        'パ' : (5,0,2,1,4,1,6,1,2,2,5,2,2,3,5,3,1,4,6,4,1,5,6,5,0,6,6,6,),
        'ヒ' : (1,0,1,1,1,2,5,2,6,2,1,3,2,3,3,3,4,3,1,4,1,5,2,6,3,6,4,6,5,6,6,6,),
        'ビ' : (1,0,4,0,6,0,1,1,1,2,5,2,6,2,1,3,2,3,3,3,4,3,1,4,1,5,2,6,3,6,4,6,5,6,6,6,),
        'ピ' : (1,0,5,0,1,1,4,1,6,1,1,2,5,2,6,2,1,3,2,3,3,3,4,3,1,4,1,5,2,6,3,6,4,6,5,6,6,6,),
        'フ' : (1,1,2,1,3,1,4,1,5,1,6,1,6,2,6,3,5,4,4,5,2,6,3,6,),
        'ブ' : (4,0,6,0,1,1,2,1,3,1,4,1,5,1,6,1,6,2,6,3,5,4,4,5,2,6,3,6,),
        'プ' : (5,0,1,1,2,1,3,1,4,1,6,1,5,2,6,2,6,3,5,4,4,5,2,6,3,6,),
        'ヘ' : (2,1,1,2,3,2,0,3,4,3,5,4,6,5,),
        'ベ' : (4,0,6,0,2,1,1,2,3,2,0,3,4,3,5,4,6,5,),
        'ホ' : (3,0,3,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,1,4,3,4,5,4,0,5,3,5,6,5,2,6,3,6,),
        'ボ' : (3,0,4,0,6,0,3,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,1,4,3,4,5,4,0,5,3,5,6,5,2,6,3,6,),
        'ポ' : (3,0,5,0,3,1,4,1,6,1,0,2,1,2,2,2,3,2,5,2,3,3,1,4,3,4,5,4,0,5,3,5,6,5,2,6,3,6,),
        'マ' : (0,1,1,1,2,1,3,1,4,1,5,1,6,1,6,2,5,3,2,4,4,4,3,5,4,6,),
        'ミ' : (1,0,2,0,3,0,4,1,5,1,2,2,3,3,4,3,1,5,2,5,3,5,4,6,5,6,),
        'ム' : (3,0,3,1,2,2,2,3,1,4,4,4,1,5,5,5,0,6,1,6,2,6,3,6,4,6,6,6,),
        'メ' : (5,0,5,1,1,2,2,2,3,2,5,2,4,3,3,4,5,4,2,5,5,5,0,6,1,6,),
        'モ' : (2,0,3,0,4,0,5,0,3,1,3,2,1,3,2,3,3,3,4,3,5,3,6,3,3,4,3,5,4,6,5,6,6,6,),
        'ャ' : (2,2,2,3,3,3,4,3,5,3,1,4,2,4,5,4,3,5,3,6,),
        'ヤ' : (2,0,2,1,4,1,5,1,6,1,0,2,1,2,2,2,3,2,6,2,2,3,5,3,3,4,3,5,3,6,),
        'ュ' : (2,3,3,3,4,3,4,4,4,5,1,6,2,6,3,6,4,6,5,6,),
        'ユ' : (1,1,2,1,3,1,4,1,4,2,4,3,4,4,0,5,1,5,2,5,3,5,4,5,5,5,6,5,),
        'ョ' : (2,2,3,2,4,2,5,2,5,3,3,4,4,4,5,4,5,5,2,6,3,6,4,6,5,6,),
        'ヨ' : (1,1,2,1,3,1,4,1,5,1,6,1,6,2,2,3,3,3,4,3,5,3,6,3,6,4,6,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        'ラ' : (2,0,3,0,4,0,5,0,1,2,2,2,3,2,4,2,5,2,6,2,6,3,5,4,4,5,2,6,3,6,),
        'リ' : (1,0,5,0,1,1,5,1,1,2,5,2,1,3,5,3,5,4,4,5,2,6,3,6,),
        'ル' : (4,0,2,1,4,1,2,2,4,2,2,3,4,3,2,4,4,4,6,4,1,5,4,5,5,5,0,6,4,6,),
        'レ' : (2,0,2,1,2,2,2,3,6,3,2,4,5,4,2,5,4,5,2,6,3,6,),
        'ロ' : (1,1,2,1,3,1,4,1,5,1,6,1,1,2,6,2,1,3,6,3,1,4,6,4,1,5,6,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        'ワ' : (1,1,2,1,3,1,4,1,5,1,6,1,1,2,6,2,6,3,5,4,4,5,2,6,3,6,),
        'ヲ' : (1,0,2,0,3,0,4,0,5,0,6,0,6,1,2,2,3,2,4,2,5,2,6,2,6,3,5,4,4,5,2,6,3,6,),
        'ン' : (1,0,2,1,6,2,6,3,5,4,4,5,1,6,2,6,3,6,),

        '魔' : (4,0,1,1,2,1,3,1,4,1,5,1,6,1,1,2,3,2,5,2,1,3,2,3,3,3,4,3,5,3,6,3,1,4,3,4,4,4,5,4,1,5,3,5,4,5,5,5,0,6,2,6,5,6,6,6,),
        '具' : (1,0,2,0,3,0,4,0,5,0,1,1,5,1,1,2,2,2,3,2,4,2,5,2,1,3,5,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,0,6,1,6,5,6,6,6,),
        '逃' : (0,0,3,0,5,0,2,1,3,1,5,1,6,1,3,2,5,2,0,3,1,3,2,3,3,3,5,3,6,3,1,4,3,4,5,4,1,5,2,5,5,5,6,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '現' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,1,1,3,1,6,1,1,2,3,2,4,2,5,2,6,2,0,3,1,3,2,3,3,3,6,3,1,4,3,4,4,4,5,4,6,4,0,5,1,5,2,5,4,5,5,5,3,6,5,6,6,6,),
        '進' : (0,0,3,0,5,0,3,1,4,1,5,1,6,1,2,2,3,2,5,2,0,3,1,3,3,3,4,3,5,3,6,3,1,4,3,4,5,4,1,5,3,5,4,5,5,5,6,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '戻' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,1,1,5,1,1,2,2,2,3,2,4,2,5,2,1,3,4,3,1,4,2,4,3,4,4,4,5,4,6,4,1,5,4,5,0,6,2,6,3,6,5,6,6,6,),
        '階' : (0,0,1,0,2,0,5,0,0,1,2,1,3,1,5,1,6,1,0,2,1,2,2,2,5,2,0,3,2,3,3,3,5,3,6,3,0,4,2,4,4,4,0,5,1,5,3,5,4,5,5,5,0,6,3,6,4,6,5,6,),
        '暗' : (4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,5,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,0,4,2,4,0,5,1,5,2,5,4,5,5,5,4,6,5,6,),
        '地' : (1,0,5,0,1,1,3,1,5,1,0,2,1,2,3,2,4,2,5,2,6,2,1,3,2,3,3,3,5,3,6,3,1,4,3,4,5,4,0,5,1,5,3,5,6,5,3,6,4,6,5,6,6,6,),
        '下' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,3,1,3,2,4,2,3,3,5,3,3,4,3,5,3,6,),
        '体' : (2,0,4,0,1,1,2,1,3,1,4,1,5,1,6,1,0,2,1,2,4,2,1,3,3,3,4,3,5,3,1,4,2,4,4,4,6,4,1,5,3,5,4,5,5,5,1,6,4,6,),
        '力' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,3,2,6,2,2,3,6,3,2,4,6,4,1,5,6,5,0,6,5,6,6,6,),
        '空' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,4,2,6,2,1,3,4,3,5,3,2,4,3,4,4,4,3,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '持' : (1,0,4,0,0,1,1,1,3,1,4,1,5,1,1,2,4,2,1,3,2,3,3,3,4,3,5,3,6,3,0,4,1,4,5,4,1,5,2,5,3,5,4,5,5,5,6,5,0,6,1,6,3,6,5,6,),
        '物' : (0,0,1,0,3,0,0,1,1,1,3,1,4,1,5,1,6,1,0,2,1,2,2,2,4,2,5,2,6,2,1,3,4,3,5,3,6,3,0,4,1,4,3,4,5,4,6,4,1,5,2,5,4,5,6,5,1,6,3,6,5,6,6,6,),
        '戦' : (0,0,2,0,4,0,6,0,4,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,1,3,2,3,3,3,5,3,2,4,5,4,6,4,0,5,1,5,2,5,3,5,5,5,2,6,4,6,6,6,),
        '何' : (2,0,3,0,4,0,5,0,6,0,1,1,6,1,0,2,1,2,3,2,4,2,5,2,6,2,1,3,3,3,5,3,6,3,1,4,3,4,4,4,5,4,6,4,1,5,6,5,1,6,5,6,6,6,),
        '気' : (1,0,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,4,2,1,3,2,3,3,3,4,3,5,3,1,4,3,4,5,4,2,5,5,5,0,6,1,6,3,6,6,6,),       
        '足' : (1,0,2,0,3,0,4,0,5,0,1,1,5,1,1,2,2,2,3,2,4,2,5,2,3,3,1,4,3,4,4,4,5,4,1,5,3,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '元' : (1,0,2,0,3,0,4,0,5,0,0,2,1,2,2,2,3,2,4,2,5,2,6,2,2,3,4,3,2,4,4,4,1,5,4,5,6,5,0,6,4,6,5,6,6,6,),        
        '遠' : (0,0,4,0,3,1,4,1,5,1,2,2,3,2,4,2,5,2,6,2,0,3,1,3,3,3,5,3,1,4,3,4,4,4,5,4,1,5,2,5,4,5,6,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '物' : (0,0,1,0,3,0,0,1,1,1,3,1,4,1,5,1,6,1,0,2,1,2,2,2,4,2,5,2,6,2,1,3,4,3,5,3,6,3,0,4,1,4,3,4,5,4,6,4,1,5,2,5,4,5,6,5,1,6,3,6,5,6,6,6,),
        '暑' : (1,0,2,0,3,0,4,0,5,0,1,1,5,1,1,2,2,2,3,2,4,2,5,2,2,3,3,3,4,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,2,5,3,5,5,5,0,6,1,6,3,6,4,6,5,6,),
        '息' : (3,0,1,1,2,1,3,1,4,1,5,1,1,2,5,2,1,3,2,3,3,3,4,3,5,3,1,4,2,4,3,4,4,4,5,4,0,5,1,5,4,5,6,5,0,6,2,6,3,6,4,6,6,6,),
        '苦' : (2,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,4,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,3,4,1,5,2,5,3,5,4,5,5,5,1,6,2,6,3,6,4,6,5,6,),
        '光' : (3,0,1,1,3,1,5,1,3,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,2,4,4,4,2,5,4,5,6,5,0,6,1,6,4,6,5,6,6,6,),
        '見' : (1,0,2,0,3,0,4,0,5,0,1,1,5,1,1,2,2,2,3,2,4,2,5,2,1,3,5,3,1,4,2,4,3,4,4,4,5,4,2,5,4,5,6,5,0,6,1,6,4,6,5,6,6,6,),
        '風' : (1,0,2,0,3,0,4,0,5,0,1,1,3,1,5,1,1,2,2,2,3,2,4,2,5,2,1,3,2,3,3,3,4,3,5,3,1,4,3,4,5,4,1,5,3,5,4,5,5,5,0,6,2,6,3,6,5,6,6,6,),
        '吹' : (3,0,0,1,1,1,3,1,4,1,5,1,6,1,0,2,1,2,2,2,4,2,6,2,0,3,1,3,4,3,0,4,1,4,4,4,3,5,5,5,2,6,6,6,),
        '冷' : (0,0,4,0,3,1,5,1,2,2,4,2,5,2,6,2,0,4,2,4,3,4,4,4,5,4,6,4,0,5,4,5,6,5,0,6,4,6,),
        '先' : (1,0,3,0,1,1,2,1,3,1,4,1,5,1,0,2,3,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,2,4,4,4,2,5,4,5,6,5,0,6,1,6,4,6,5,6,6,6,),
        '前' : (1,0,5,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,3,1,3,2,3,4,3,6,3,0,4,2,4,4,4,6,4,0,5,1,5,2,5,6,5,0,6,2,6,5,6,6,6,),   
        '近' : (0,0,5,0,1,1,3,1,4,1,3,2,0,3,1,3,3,3,4,3,5,3,6,3,1,4,3,4,5,4,1,5,2,5,5,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '声' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,3,2,1,3,2,3,3,3,4,3,5,3,1,4,3,4,5,4,1,5,2,5,3,5,4,5,5,5,0,6,),
        '寒' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,4,2,6,2,1,3,2,3,3,3,4,3,5,3,1,4,2,4,3,4,4,4,5,4,0,5,2,5,3,5,6,5,4,6,),
        '法' : (0,0,4,0,3,1,4,1,5,1,0,2,4,2,2,3,3,3,4,3,5,3,6,3,0,4,4,4,0,5,3,5,5,5,0,6,2,6,3,6,4,6,6,6,),
        '道' : (0,0,3,0,5,0,2,1,3,1,4,1,5,1,6,1,4,2,0,3,1,3,3,3,5,3,1,4,3,4,4,4,5,4,1,5,3,5,5,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '取' : (0,0,1,0,2,0,3,0,1,1,3,1,4,1,5,1,6,1,1,2,2,2,3,2,6,2,1,3,2,3,3,3,4,3,6,3,1,4,3,4,5,4,0,5,1,5,2,5,3,5,4,5,6,5,3,6,),
        '突' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,4,2,6,2,1,3,4,3,5,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,3,5,0,6,1,6,2,6,4,6,5,6,6,6,),
        '出' : (3,0,1,1,3,1,5,1,1,2,3,2,5,2,1,3,2,3,3,3,4,3,5,3,0,4,3,4,6,4,0,5,3,5,6,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '少' : (3,0,1,1,3,1,5,1,1,2,3,2,6,2,0,3,3,3,2,4,3,4,5,4,3,5,4,5,0,6,1,6,2,6,),
        '上' : (3,0,3,1,3,2,4,2,5,2,3,3,3,4,3,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '落' : (2,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,4,2,5,2,2,3,3,3,5,3,0,4,4,4,2,5,3,5,5,5,6,5,0,6,3,6,4,6,5,6,),
        '辺' : (0,0,2,0,3,0,4,0,5,0,6,0,1,1,4,1,6,1,4,2,6,2,0,3,1,3,3,3,6,3,1,4,2,4,5,4,6,4,1,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '効' : (2,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,1,2,3,2,4,2,6,2,0,3,4,3,6,3,1,4,3,4,4,4,6,4,2,5,4,5,6,5,0,6,1,6,3,6,5,6,6,6,),
        '立' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,1,2,5,2,2,3,5,3,2,4,4,4,2,5,4,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '武' : (1,0,2,0,4,0,6,0,4,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,5,3,1,4,3,4,4,4,5,4,1,5,3,5,6,5,0,6,1,6,2,6,3,6,4,6,6,6,),
        '器' : (1,0,2,0,4,0,5,0,1,1,2,1,4,1,5,1,3,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,3,4,0,5,1,5,2,5,4,5,5,5,6,5,1,6,2,6,4,6,5,6,),
        '剣' : (2,0,6,0,1,1,3,1,5,1,6,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,2,3,4,3,5,3,6,3,0,4,1,4,2,4,3,4,4,4,6,4,2,5,6,5,0,6,1,6,3,6,4,6,6,6,),
        '炎' : (3,0,1,1,3,1,5,1,2,2,4,2,0,3,1,3,5,3,6,3,1,4,3,4,5,4,2,5,4,5,0,6,1,6,5,6,6,6,),
        '火' : (3,0,3,1,1,2,3,2,5,2,1,3,3,3,4,3,3,4,2,5,4,5,0,6,1,6,5,6,6,6,),
        '段' : (2,0,4,0,5,0,6,0,1,1,4,1,6,1,1,2,2,2,1,3,4,3,5,3,6,3,1,4,2,4,4,4,6,4,0,5,1,5,5,5,1,6,3,6,4,6,6,6,),
        '穴' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,6,2,2,3,4,3,2,4,4,4,1,5,5,5,0,6,6,6,),
        '拾' : (1,0,4,0,0,1,1,1,3,1,5,1,1,2,2,2,4,2,5,2,6,2,1,3,0,4,1,4,3,4,4,4,5,4,1,5,3,5,5,5,0,6,1,6,3,6,4,6,5,6,),
        '尽' : (1,0,2,0,3,0,4,0,5,0,1,1,5,1,1,2,2,2,3,2,4,2,1,3,3,3,5,3,1,4,5,4,0,5,2,5,3,5,6,5,4,6,),
        '直' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,3,2,0,3,2,3,3,3,4,3,5,3,0,4,2,4,5,4,0,5,2,5,3,5,4,5,5,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '冒' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,0,1,6,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,1,3,5,3,1,4,2,4,3,4,4,4,5,4,1,5,5,5,1,6,2,6,3,6,4,6,5,6,),
        '険' : (0,0,1,0,4,0,0,1,1,1,3,1,5,1,0,2,2,2,3,2,4,2,5,2,6,2,0,3,1,3,2,3,4,3,6,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,0,5,4,5,0,6,2,6,3,6,5,6,6,6,),
        '始' : (2,0,5,0,2,1,5,1,0,2,1,2,2,2,3,2,4,2,6,2,1,3,3,3,4,3,5,3,6,3,1,4,2,4,2,5,3,5,4,5,5,5,6,5,0,6,1,6,4,6,5,6,6,6,),
        '静' : (2,0,5,0,6,0,1,1,2,1,3,1,4,1,6,1,2,2,5,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,3,4,5,4,6,4,1,5,2,5,3,5,4,5,5,5,6,5,1,6,3,6,5,6,),
        '返' : (0,0,3,0,4,0,5,0,6,0,1,1,3,1,3,2,4,2,5,2,6,2,0,3,1,3,3,3,4,3,6,3,1,4,3,4,5,4,1,5,2,5,4,5,6,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '与' : (2,0,2,1,3,1,4,1,5,1,2,2,2,3,3,3,4,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,4,5,3,6,4,6,),
        '受' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,1,1,3,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,2,3,3,3,4,3,6,3,2,4,4,4,3,5,0,6,1,6,2,6,4,6,5,6,6,6,),
        '撃' : (2,0,4,0,5,0,6,0,0,1,1,1,2,1,3,1,4,1,6,1,1,2,2,2,3,2,5,2,0,3,1,3,2,3,4,3,6,3,2,4,3,4,4,4,5,4,0,5,1,5,2,5,3,5,4,5,5,5,6,5,2,6,3,6,),
        '当' : (1,0,3,0,6,0,2,1,3,1,5,1,1,2,2,2,3,2,4,2,5,2,6,2,6,3,2,4,3,4,4,4,5,4,6,4,6,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        '投' : (1,0,3,0,4,0,5,0,0,1,1,1,3,1,5,1,1,2,2,2,5,2,6,2,1,3,3,3,4,3,5,3,0,4,1,4,3,4,5,4,1,5,4,5,0,6,1,6,2,6,3,6,5,6,6,6,),
        '攻' : (4,0,0,1,1,1,2,1,4,1,5,1,6,1,1,2,3,2,4,2,6,2,1,3,4,3,6,3,1,4,2,4,4,4,6,4,0,5,1,5,5,5,3,6,4,6,6,6,),
        '防' : (0,0,1,0,2,0,5,0,0,1,2,1,3,1,4,1,5,1,6,1,0,2,1,2,4,2,0,3,2,3,4,3,5,3,6,3,0,4,2,4,4,4,6,4,0,5,1,5,4,5,6,5,0,6,3,6,5,6,6,6,),
        '素' : (3,0,1,1,2,1,3,1,4,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,2,3,5,3,0,4,1,4,2,4,3,4,4,4,6,4,3,5,0,6,3,6,6,6,),
        '手' : (4,0,5,0,1,1,2,1,3,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,3,5,2,6,3,6,),
        '服' : (1,0,2,0,3,0,4,0,5,0,6,0,1,1,3,1,6,1,1,2,2,2,3,2,1,3,3,3,4,3,5,3,6,3,1,4,2,4,3,4,4,4,6,4,1,5,3,5,5,5,0,6,2,6,3,6,4,6,6,6,),
        '石' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,2,1,2,2,1,3,2,3,3,3,4,3,5,3,0,4,2,4,5,4,2,5,5,5,2,6,3,6,4,6,5,6,),
        '切' : (1,0,3,0,4,0,5,0,6,0,1,1,4,1,6,1,0,2,1,2,2,2,4,2,6,2,1,3,4,3,6,3,1,4,4,4,6,4,1,5,2,5,4,5,6,5,3,6,5,6,6,6,),
        '氷' : (1,0,3,0,3,1,6,1,0,2,1,2,2,2,3,2,5,2,2,3,3,3,4,3,1,4,3,4,5,4,0,5,3,5,6,5,2,6,3,6,),
        '薬' : (2,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,4,2,6,2,1,3,2,3,4,3,5,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,2,5,3,5,4,5,0,6,1,6,3,6,5,6,6,6,),
        '草' : (2,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,1,2,2,2,3,2,4,2,5,2,1,3,5,3,1,4,2,4,3,4,4,4,5,4,0,5,1,5,2,5,3,5,4,5,5,5,6,5,3,6,),
        '回' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,0,1,6,1,0,2,2,2,3,2,4,2,6,2,0,3,2,3,4,3,6,3,0,4,2,4,3,4,4,4,6,4,0,5,6,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '復' : (1,0,3,0,0,1,3,1,4,1,5,1,6,1,1,2,2,2,4,2,5,2,0,3,1,3,4,3,5,3,1,4,3,4,5,4,1,5,4,5,1,6,2,6,3,6,5,6,6,6,),
        '雷' : (2,0,3,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,5,2,6,2,1,4,2,4,3,4,4,4,5,4,1,5,3,5,5,5,1,6,2,6,3,6,4,6,5,6,),
        '裏' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,1,2,3,2,5,2,1,3,2,3,3,3,4,3,5,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,1,5,2,5,4,5,0,6,2,6,3,6,5,6,6,6,),
        '弾' : (0,0,1,0,2,0,4,0,6,0,1,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,2,3,3,3,4,3,5,3,6,3,0,4,1,4,4,4,1,5,2,5,3,5,4,5,5,5,6,5,0,6,1,6,4,6,),
        '経' : (1,0,2,0,3,0,4,0,5,0,0,1,3,1,5,1,1,2,4,2,0,3,2,3,3,3,5,3,6,3,1,4,3,4,4,4,5,4,0,5,1,5,4,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        '験' : (0,0,1,0,2,0,4,0,0,1,1,1,3,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,1,3,2,3,4,3,6,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,2,5,4,5,0,6,2,6,3,6,5,6,6,6,),
        '強' : (0,0,1,0,4,0,1,1,3,1,6,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,3,3,4,3,5,3,0,4,1,4,3,4,4,4,5,4,1,5,4,5,6,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '明' : (0,0,1,0,2,0,4,0,5,0,6,0,0,1,2,1,4,1,6,1,0,2,1,2,2,2,4,2,5,2,6,2,0,3,2,3,4,3,6,3,0,4,1,4,2,4,4,4,5,4,6,4,3,5,6,5,2,6,5,6,6,6,),
        '視' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,2,1,3,1,6,1,2,2,3,2,4,2,5,2,6,2,1,3,3,3,6,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,1,5,4,5,5,5,1,6,3,6,5,6,6,6,),
        '界' : (1,0,2,0,3,0,4,0,5,0,1,1,3,1,5,1,1,2,2,2,3,2,4,2,5,2,1,3,3,3,5,3,1,4,2,4,3,4,4,4,5,4,0,5,2,5,4,5,6,5,1,6,4,6,),
        '開' : (0,0,1,0,2,0,4,0,5,0,6,0,0,1,1,1,2,1,4,1,5,1,6,1,0,2,6,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,0,4,2,4,4,4,6,4,0,5,1,5,2,5,3,5,4,5,5,5,6,5,0,6,2,6,4,6,6,6,),
        '周' : (1,0,2,0,3,0,4,0,5,0,6,0,1,1,3,1,6,1,1,2,2,2,3,2,4,2,6,2,1,3,3,3,6,3,1,4,2,4,3,4,4,4,5,4,6,4,1,5,2,5,4,5,6,5,0,6,2,6,3,6,4,6,6,6,),
        '玉' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,3,1,3,2,1,3,2,3,3,3,4,3,5,3,3,4,3,5,5,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '深' : (0,0,2,0,3,0,4,0,5,0,6,0,2,1,6,1,0,2,3,2,5,2,2,3,5,3,6,3,0,4,2,4,3,4,4,4,5,4,6,4,0,5,3,5,4,5,5,5,0,6,2,6,4,6,6,6,),
        '槍' : (1,0,4,0,0,1,1,1,3,1,5,1,1,2,2,2,3,2,4,2,6,2,0,3,1,3,3,3,4,3,0,4,1,4,3,4,1,5,2,5,4,5,5,5,1,6,4,6,5,6,),
        '左' : (2,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,2,3,3,3,4,3,5,3,1,4,4,4,0,5,4,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        '右' : (2,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,1,3,2,3,3,3,4,3,5,3,0,4,2,4,5,4,2,5,5,5,2,6,3,6,4,6,5,6,),
        '方' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,2,3,3,3,4,3,5,3,2,4,5,4,1,5,5,5,0,6,4,6,5,6,),
        '目' : (1,0,2,0,3,0,4,0,5,0,6,0,1,1,6,1,1,2,2,2,3,2,4,2,5,2,6,2,1,3,6,3,1,4,2,4,3,4,4,4,5,4,6,4,1,5,6,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        '消' : (0,0,2,0,4,0,6,0,4,1,0,2,2,2,3,2,4,2,5,2,6,2,2,3,6,3,0,4,2,4,3,4,4,4,5,4,6,4,0,5,2,5,6,5,0,6,2,6,5,6,6,6,),
        '流' : (0,0,4,0,2,1,3,1,4,1,5,1,6,1,0,2,3,2,5,2,2,3,3,3,4,3,6,3,0,4,3,4,4,4,0,5,3,5,4,5,6,5,0,6,2,6,4,6,6,6,),
        '込' : (0,0,3,0,4,0,1,1,4,1,4,2,0,3,1,3,3,3,5,3,1,4,2,4,6,4,1,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '危' : (2,0,3,0,4,0,0,1,1,1,4,1,1,2,2,2,3,2,4,2,5,2,6,2,1,3,3,3,4,3,5,3,1,4,3,4,5,4,1,5,3,5,6,5,0,6,3,6,4,6,5,6,6,6,),
        '行' : (1,0,3,0,4,0,5,0,0,1,1,2,2,2,3,2,4,2,5,2,6,2,0,3,1,3,5,3,1,4,5,4,1,5,5,5,1,6,4,6,5,6,),
        '入' : (1,0,2,0,3,0,3,1,3,2,2,3,4,3,2,4,4,4,1,5,5,5,0,6,6,6,),
        '事' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,1,2,3,2,5,2,0,3,1,3,2,3,3,3,4,3,5,3,3,4,5,4,6,4,0,5,1,5,2,5,3,5,4,5,5,5,2,6,3,6,),
        '宝' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,4,2,6,2,3,3,2,4,3,4,4,4,3,5,5,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '帰' : (1,0,3,0,4,0,5,0,0,1,1,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,1,3,2,3,4,3,6,3,1,4,3,4,4,4,5,4,1,5,3,5,4,5,5,5,0,6,4,6,),
        '骨' : (1,0,2,0,3,0,4,0,5,0,1,1,4,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,0,3,1,3,5,3,6,3,1,4,2,4,3,4,4,4,5,4,1,5,5,5,1,6,4,6,5,6,),
        '泥' : (0,0,2,0,3,0,4,0,5,0,6,0,2,1,6,1,0,2,2,2,3,2,4,2,5,2,6,2,2,3,4,3,0,4,2,4,4,4,5,4,6,4,0,5,2,5,4,5,0,6,1,6,4,6,5,6,6,6,),
        '提' : (1,0,4,0,5,0,0,1,1,1,2,1,4,1,5,1,1,2,3,2,4,2,5,2,6,2,1,3,5,3,0,4,1,4,3,4,5,4,6,4,1,5,3,5,5,5,0,6,1,6,2,6,4,6,5,6,6,6,),
        '灯' : (1,0,3,0,4,0,5,0,6,0,1,1,5,1,0,2,1,2,2,2,5,2,0,3,1,3,5,3,1,4,5,4,1,5,2,5,5,5,0,6,4,6,5,6,),
        '水' : (3,0,3,1,6,1,0,2,1,2,2,2,3,2,5,2,2,3,3,3,4,3,1,4,3,4,5,4,0,5,3,5,6,5,2,6,3,6,),
        '霊' : (2,0,3,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,5,2,6,2,0,4,2,4,3,4,4,4,6,4,1,5,3,5,5,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '株' : (1,0,3,0,4,0,0,1,1,1,3,1,4,1,5,1,1,2,2,2,4,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,0,4,1,4,4,4,1,5,3,5,4,5,5,5,1,6,2,6,4,6,6,6,),
        '姉' : (1,0,5,0,1,1,3,1,4,1,5,1,6,1,0,2,1,2,2,2,5,2,0,3,2,3,3,3,4,3,5,3,6,3,0,4,1,4,3,4,5,4,6,4,1,5,2,5,3,5,5,5,6,5,0,6,5,6,),
        '兄' : (1,0,2,0,3,0,4,0,5,0,1,1,5,1,1,2,5,2,1,3,2,3,3,3,4,3,5,3,2,4,4,4,2,5,4,5,6,5,0,6,1,6,4,6,5,6,6,6,),
        '洞' : (0,0,2,0,3,0,4,0,5,0,6,0,2,1,6,1,0,2,2,2,3,2,4,2,6,2,2,3,6,3,0,4,2,4,3,4,4,4,6,4,0,5,2,5,3,5,4,5,6,5,0,6,2,6,5,6,6,6,),
        '窟' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,5,2,6,2,1,3,2,3,3,3,4,3,5,3,1,4,2,4,3,4,4,4,5,4,1,5,2,5,4,5,6,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '化' : (2,0,3,0,1,1,3,1,0,2,1,2,3,2,6,2,1,3,3,3,4,3,5,3,1,4,3,4,1,5,3,5,6,5,1,6,3,6,4,6,5,6,6,6,),
        '王' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,3,1,3,2,1,3,2,3,3,3,4,3,5,3,3,4,3,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '士' : (3,0,3,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,3,4,3,5,1,6,2,6,3,6,4,6,5,6,),
        '兜' : (1,0,3,0,5,0,6,0,0,1,2,1,4,1,6,1,0,2,2,2,3,2,4,2,6,2,0,3,2,3,4,3,6,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,2,5,4,5,0,6,1,6,4,6,5,6,6,6,),
        '借' : (1,0,3,0,5,0,1,1,2,1,3,1,4,1,5,1,6,1,0,2,1,2,3,2,5,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,3,4,4,4,5,4,1,5,3,5,5,5,1,6,3,6,4,6,5,6,),
        '犬' : (3,0,5,0,3,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,3,4,2,5,4,5,0,6,1,6,5,6,6,6,),
        '食' : (3,0,2,1,4,1,0,2,1,2,3,2,5,2,6,2,2,3,3,3,2,4,3,4,5,4,2,5,4,5,1,6,2,6,3,6,5,6,6,6,),
        '根' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,2,1,3,1,6,1,1,2,3,2,4,2,5,2,6,2,0,3,1,3,2,3,3,3,6,3,0,4,1,4,3,4,4,4,5,4,6,4,1,5,3,5,5,5,1,6,3,6,4,6,6,6,),
        '再' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,1,1,3,1,5,1,1,2,2,2,3,2,4,2,5,2,1,3,3,3,5,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,1,5,5,5,1,6,4,6,5,6,),
        '挑' : (1,0,3,0,5,0,0,1,1,1,2,1,3,1,5,1,6,1,1,2,3,2,5,2,1,3,2,3,3,3,5,3,6,3,0,4,1,4,3,4,5,4,1,5,3,5,5,5,0,6,1,6,2,6,5,6,6,6,),
        '値' : (2,0,5,0,1,1,3,1,4,1,5,1,6,1,0,2,1,2,5,2,1,3,3,3,5,3,6,3,1,4,3,4,5,4,6,4,1,5,3,5,1,6,3,6,4,6,5,6,6,6,),
        '得' : (1,0,3,0,4,0,5,0,0,1,3,1,5,1,1,2,2,2,3,2,4,2,5,2,6,2,0,3,1,3,5,3,1,4,2,4,3,4,4,4,5,4,6,4,1,5,3,5,5,5,1,6,4,6,5,6,),
        '弱' : (0,0,1,0,2,0,4,0,5,0,6,0,2,1,6,1,0,2,1,2,2,2,4,2,5,2,6,2,0,3,4,3,1,4,2,4,5,4,6,4,0,5,2,5,4,5,6,5,1,6,2,6,5,6,6,6,),
        '点' : (3,0,3,1,4,1,5,1,3,2,1,3,2,3,3,3,4,3,5,3,1,4,2,4,3,4,4,4,5,4,0,6,2,6,4,6,6,6,),
        '看' : (4,0,5,0,1,1,2,1,3,1,2,2,3,2,4,2,5,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,2,4,3,4,4,4,5,4,0,5,2,5,5,5,2,6,3,6,4,6,5,6,),
        '板' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,3,1,1,2,3,2,4,2,5,2,6,2,0,3,1,3,3,3,4,3,6,3,0,4,1,4,3,4,4,4,6,4,1,5,2,5,5,5,1,6,3,6,4,6,6,6,),
        '印' : (2,0,4,0,5,0,6,0,0,1,1,1,4,1,6,1,0,2,4,2,6,2,0,3,1,3,2,3,4,3,6,3,0,4,4,4,6,4,0,5,1,5,2,5,4,5,4,6,),
        '耐' : (0,0,1,0,2,0,3,0,4,0,6,0,1,1,5,1,6,1,0,2,1,2,2,2,3,2,4,2,6,2,0,3,2,3,4,3,5,3,6,3,0,4,2,4,4,4,5,4,6,4,0,5,2,5,4,5,6,5,0,6,2,6,4,6,6,6,),
        '性' : (1,0,3,0,4,0,0,1,1,1,3,1,4,1,5,1,6,1,0,2,1,2,2,2,4,2,1,3,4,3,1,4,3,4,4,4,5,4,1,5,4,5,1,6,2,6,3,6,4,6,5,6,6,6,),
        '瀕' : (0,0,2,0,4,0,5,0,6,0,2,1,3,1,5,1,0,2,2,2,4,2,5,2,6,2,1,3,2,3,3,3,4,3,6,3,0,4,2,4,4,4,5,4,6,4,0,5,3,5,0,6,1,6,2,6,4,6,6,6,),
        '死' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,1,1,4,1,1,2,2,2,4,2,6,2,0,3,2,3,4,3,5,3,1,4,2,4,4,4,1,5,4,5,6,5,0,6,4,6,5,6,6,6,),
        '全' : (3,0,2,1,4,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,3,3,1,4,2,4,3,4,4,4,5,4,3,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '快' : (1,0,4,0,0,1,1,1,3,1,4,1,5,1,0,2,1,2,4,2,5,2,1,3,2,3,3,3,4,3,5,3,6,3,1,4,4,4,1,5,4,5,1,6,2,6,3,6,5,6,6,6,),
        '天' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,3,1,1,2,2,2,3,2,4,2,5,2,3,3,3,4,2,5,4,5,0,6,1,6,5,6,6,6,),
        '使' : (2,0,4,0,1,1,2,1,3,1,4,1,5,1,6,1,0,2,1,2,3,2,4,2,6,2,1,3,3,3,4,3,5,3,6,3,1,4,2,4,3,4,4,4,1,5,4,5,1,6,2,6,3,6,5,6,6,6,),
        '唱' : (3,0,4,0,5,0,0,1,1,1,2,1,3,1,5,1,0,2,2,2,3,2,4,2,5,2,6,2,0,3,2,3,6,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,2,5,6,5,2,6,3,6,4,6,5,6,6,6,),
        '送' : (0,0,3,0,5,0,2,1,3,1,4,1,5,1,6,1,4,2,0,3,1,3,3,3,4,3,5,3,1,4,4,4,1,5,3,5,5,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '招' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,2,1,4,1,6,1,1,2,3,2,6,2,1,3,2,3,5,3,6,3,0,4,1,4,3,4,4,4,5,4,6,4,1,5,3,5,6,5,0,6,1,6,3,6,4,6,5,6,6,6,),
        '半' : (3,0,1,1,3,1,5,1,3,2,1,3,2,3,3,3,4,3,5,3,3,4,0,5,1,5,2,5,3,5,4,5,5,5,6,5,3,6,),
        '分' : (2,0,4,0,2,1,4,1,1,2,5,2,0,3,2,3,3,3,4,3,5,3,6,3,3,4,5,4,2,5,5,5,0,6,1,6,4,6,5,6,),
        '猫' : (0,0,3,0,5,0,1,1,2,1,3,1,4,1,5,1,6,1,0,2,1,2,3,2,5,2,1,3,2,3,3,3,4,3,5,3,6,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,1,5,2,5,4,5,6,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '極' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,2,1,4,1,1,2,4,2,5,2,0,3,1,3,2,3,3,3,5,3,6,3,0,4,1,4,3,4,5,4,6,4,1,5,5,5,1,6,3,6,4,6,5,6,6,6,),
        '熱' : (2,0,4,0,1,1,2,1,4,1,5,1,0,2,1,2,2,2,3,2,5,2,1,3,2,3,4,3,5,3,0,4,2,4,3,4,5,4,6,4,0,6,2,6,4,6,6,6,),
        '極' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,2,1,4,1,1,2,4,2,5,2,0,3,1,3,2,3,3,3,5,3,6,3,0,4,1,4,3,4,5,4,6,4,1,5,5,5,1,6,3,6,4,6,5,6,6,6,),
        '雪' : (2,0,3,0,4,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,5,2,6,2,1,4,2,4,3,4,4,4,5,4,5,5,1,6,2,6,3,6,4,6,5,6,),
        '崩' : (0,0,3,0,6,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,1,2,2,2,3,2,4,2,5,2,6,2,1,3,3,3,4,3,6,3,1,4,2,4,3,4,4,4,5,4,6,4,1,5,3,5,4,5,6,5,0,6,2,6,3,6,5,6,6,6,),
        '破' : (0,0,1,0,2,0,5,0,1,1,3,1,4,1,5,1,6,1,1,2,3,2,5,2,6,2,0,3,3,3,4,3,5,3,6,3,1,4,2,4,3,4,4,4,6,4,1,5,2,5,3,5,5,5,4,6,6,6,),
        '壊' : (1,0,4,0,1,1,2,1,3,1,4,1,5,1,6,1,0,2,1,2,3,2,4,2,6,2,1,3,3,3,4,3,5,3,6,3,1,4,2,4,3,4,4,4,5,4,6,4,0,5,1,5,2,5,3,5,5,5,3,6,4,6,6,6,),
        '飛' : (0,0,1,0,2,0,3,0,4,0,5,0,1,1,3,1,5,1,0,2,1,2,3,2,6,2,1,3,2,3,3,3,4,3,5,3,0,4,1,4,3,4,5,4,6,4,1,5,3,5,5,5,0,6,3,6,6,6,),
        '蹴' : (0,0,1,0,3,0,5,0,6,0,0,1,2,1,3,1,4,1,5,1,0,2,1,2,2,2,4,2,5,2,6,2,1,3,2,3,3,3,4,3,5,3,0,4,1,4,3,4,5,4,0,5,1,5,2,5,3,5,4,5,5,5,0,6,1,6,3,6,6,6,),
        '盗' : (0,0,3,0,3,1,4,1,5,1,6,1,2,2,4,2,6,2,0,3,3,3,5,3,1,4,2,4,3,4,4,4,5,4,1,5,3,5,5,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '振' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,3,1,1,2,3,2,5,2,6,2,1,3,3,3,0,4,1,4,3,4,4,4,5,4,6,4,1,5,2,5,3,5,5,5,0,6,1,6,3,6,4,6,6,6,),
        '羽' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,3,1,6,1,1,2,3,2,4,2,6,2,3,3,6,3,2,4,3,4,5,4,6,4,0,5,1,5,3,5,4,5,6,5,2,6,3,6,5,6,6,6,),
        '岩' : (1,0,3,0,5,0,1,1,2,1,3,1,4,1,5,1,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,0,5,2,5,3,5,4,5,5,5,2,6,3,6,4,6,5,6,),
        '状' : (1,0,4,0,6,0,1,1,4,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,1,3,4,3,0,4,1,4,4,4,1,5,3,5,5,5,1,6,2,6,6,6,),
        '態' : (1,0,3,0,5,0,0,1,1,1,2,1,3,1,5,1,6,1,1,2,3,2,1,3,2,3,3,3,5,3,1,4,3,4,5,4,6,4,0,5,1,5,4,5,0,6,2,6,3,6,4,6,6,6,),
        '次' : (0,0,3,0,3,1,4,1,5,1,6,1,2,2,4,2,6,2,4,3,0,4,4,4,0,5,3,5,5,5,0,6,2,6,6,6,),
        '起' : (2,0,4,0,5,0,6,0,0,1,1,1,2,1,3,1,6,1,2,2,4,2,5,2,6,2,0,3,1,3,2,3,3,3,4,3,1,4,2,4,4,4,5,4,6,4,1,5,2,5,0,6,3,6,4,6,5,6,6,6,),
        '冠' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,0,1,6,1,1,2,2,2,5,2,4,3,5,3,6,3,0,4,1,4,2,4,3,4,5,4,1,5,2,5,4,5,5,5,0,6,2,6,3,6,4,6,5,6,6,6,),
        '倒' : (2,0,3,0,4,0,6,0,1,1,3,1,5,1,6,1,0,2,1,2,2,2,5,2,6,2,1,3,2,3,3,3,4,3,5,3,6,3,1,4,3,4,6,4,1,5,2,5,3,5,4,5,6,5,1,6,5,6,6,6,),
        '箱' : (1,0,4,0,1,1,2,1,4,1,5,1,6,1,0,2,2,2,3,2,5,2,2,3,4,3,6,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,1,5,2,5,3,5,4,5,6,5,0,6,2,6,4,6,5,6,6,6,),
        '封' : (2,0,6,0,1,1,2,1,3,1,4,1,5,1,6,1,2,2,6,2,0,3,1,3,2,3,3,3,4,3,6,3,1,4,2,4,5,4,6,4,2,5,3,5,6,5,0,6,1,6,5,6,6,6,),
        '伸' : (2,0,4,0,1,1,2,1,3,1,4,1,5,1,6,1,0,2,1,2,2,2,4,2,6,2,1,3,2,3,3,3,4,3,5,3,6,3,1,4,2,4,4,4,6,4,1,5,2,5,3,5,4,5,5,5,6,5,1,6,4,6,),
        '最' : (1,0,2,0,3,0,4,0,5,0,1,1,5,1,0,2,1,2,2,2,3,2,4,2,5,2,6,2,1,3,3,3,6,3,1,4,3,4,4,4,6,4,0,5,1,5,2,5,3,5,5,5,3,6,4,6,6,6,),
        '初' : (1,0,3,0,4,0,5,0,6,0,0,1,1,1,2,1,4,1,6,1,2,2,4,2,6,2,1,3,4,3,6,3,0,4,1,4,2,4,4,4,6,4,1,5,2,5,4,5,6,5,1,6,3,6,5,6,6,6,),
        '闇' : (0,0,1,0,2,0,4,0,5,0,6,0,0,1,1,1,2,1,4,1,5,1,6,1,0,2,3,2,6,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,0,4,2,4,4,4,6,4,0,5,1,5,2,5,3,5,4,5,5,5,6,5,0,6,2,6,3,6,4,6,6,6,),
        '変' : (3,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,4,2,0,3,2,3,3,3,4,3,6,3,1,4,2,4,4,4,3,5,0,6,1,6,2,6,4,6,5,6,6,6,),
        '壁' : (1,0,2,0,5,0,1,1,2,1,3,1,4,1,5,1,6,1,1,2,4,2,6,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,2,4,5,4,3,5,0,6,1,6,2,6,3,6,4,6,5,6,6,6,),
        '今' : (3,0,2,1,4,1,0,2,1,2,3,2,4,2,5,2,6,2,1,4,2,4,3,4,4,4,5,4,4,5,2,6,3,6,),
        '崩' : (0,0,3,0,6,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,1,2,2,2,3,2,4,2,5,2,6,2,1,3,3,3,4,3,6,3,1,4,2,4,3,4,4,4,5,4,6,4,1,5,3,5,4,5,6,5,0,6,2,6,3,6,5,6,6,6,),        
        '歩' : (3,0,1,1,3,1,4,1,5,1,1,2,3,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,3,4,5,4,0,5,3,5,4,5,6,5,1,6,2,6,3,6,),
        '井' : (2,0,5,0,0,1,1,1,2,1,3,1,4,1,5,1,6,1,2,2,5,2,2,3,5,3,0,4,1,4,2,4,3,4,4,4,5,4,6,4,2,5,5,5,1,6,5,6,),
        '溶' : (0,0,4,0,2,1,3,1,4,1,5,1,6,1,0,2,2,2,3,2,5,2,6,2,4,3,0,4,3,4,5,4,0,5,2,5,4,5,5,5,6,5,0,6,4,6,5,6,),
        '同' : (0,0,1,0,2,0,3,0,4,0,5,0,6,0,0,1,6,1,0,2,2,2,3,2,4,2,6,2,0,3,6,3,0,4,2,4,3,4,4,4,6,4,0,5,2,5,4,5,6,5,0,6,2,6,3,6,4,6,6,6,),
        '恐' : (0,0,1,0,2,0,4,0,5,0,1,1,4,1,5,1,1,2,2,2,4,2,5,2,0,3,1,3,3,3,5,3,6,3,0,5,1,5,4,5,6,5,0,6,2,6,3,6,4,6,6,6,),
        '敵' : (2,0,5,0,0,1,1,1,2,1,3,1,5,1,6,1,1,2,3,2,4,2,6,2,0,3,1,3,2,3,3,3,4,3,6,3,0,4,2,4,4,4,6,4,0,5,1,5,3,5,4,5,5,5,0,6,1,6,2,6,3,6,4,6,6,6,),
        '狂' : (0,0,2,0,4,0,5,0,6,0,1,1,5,1,0,2,2,2,5,2,1,3,2,3,4,3,5,3,6,3,0,4,2,4,5,4,2,5,5,5,0,6,1,6,3,6,4,6,5,6,6,6,),
        '暴' : (1,0,2,0,3,0,4,0,5,0,1,1,2,1,3,1,4,1,5,1,2,2,4,2,0,3,1,3,2,3,3,3,4,3,5,3,6,3,1,4,3,4,5,4,2,5,3,5,4,5,0,6,1,6,3,6,5,6,6,6,),

    }
    
    init_x = x
    init_col = col
    for ch in txt:
        if col == -1:
            if ch == '*':
                col = init_col
            else:
                col = int(ch, 16)
            continue
        elif ch == '*':
            col = -1
            continue
        if ch == '\n':
            x = init_x
            y += 8
        else:
            font_data = FONT_DIC.get(ch)
            if font_data == None:
                pyxel.text(x, y+1, ch, col)
                x += 4
            else:
                for dx, dy in zip(*[iter(font_data)]*2):
                    pyxel.pset(x+dx, y+dy, col)
                x += 8
