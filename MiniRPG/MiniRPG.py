#
# MiniRGP.py 2022/9/15
#
import random
import pyxel
import mrfont

BUTTON_NUM = 4
ABC_KEY = (pyxel.KEY_Z, pyxel.KEY_X, pyxel.KEY_C, pyxel.KEY_V)
NUM_KEY = (pyxel.KEY_1, pyxel.KEY_2, pyxel.KEY_3, pyxel.KEY_4)
ARW_KEY = (pyxel.KEY_LEFT, pyxel.KEY_UP, pyxel.KEY_RIGHT, pyxel.KEY_DOWN)
DPAD = (pyxel.GAMEPAD1_BUTTON_DPAD_LEFT, pyxel.GAMEPAD1_BUTTON_DPAD_UP, pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT, pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)
ABXY = (pyxel.GAMEPAD1_BUTTON_Y, pyxel.GAMEPAD1_BUTTON_X, pyxel.GAMEPAD1_BUTTON_A, pyxel.GAMEPAD1_BUTTON_B)
MOUSE_OFF, MOUSE_PUSH, MOUSE_RELEASE = 1, 2, 3

MSG_LINE = 6
ENEMY_X, ENEMY_Y, ENEMY_WIDTH, ENEMY_HEIGHT = 2, 2, 70, 77
PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT = ENEMY_X+ENEMY_WIDTH+2, ENEMY_Y, 126, ENEMY_HEIGHT  # 74,2,126,77
MSG_X, MSG_Y, MSG_WIDTH, MSG_HEIGHT = ENEMY_X, ENEMY_Y+ENEMY_HEIGHT+2, ENEMY_WIDTH+PLAYER_WIDTH+2, MSG_LINE*9+4  # 2,81,198,58
WINDOW_WIDTH, WINDOW_HEIGHT = MSG_X+MSG_WIDTH+2, MSG_Y+MSG_HEIGHT+18  # 202,157

WALK_MSG = ('少し明るくなって視界が開けてきた。', '辺りはしんと静まり返っている。', '冷たい風がどこからか吹いている。', 
        'すみ切った空気がどこから流れてくる。', 'さわやかな風で、むし暑さが消えた。', 'うす暗く物静かだ。', 
        'きりが立ち込めて遠くまで見えない。', 'むし暑く少し息苦しい。', 'かすかな光が遠くに見える。',
        '足元がゴツゴツして歩きづらい。', '周りの壁は今にも崩れそうだ。', '天井からポタポタとしずくが落ちている。', )
HINT_MSG = ('の方はスタート地点のようだ。', 'に進むとスタートに戻るようだ。', 'はスタートに戻る道だ。',
        'に目印の看板が見える。', 'に行くと最初からだ。', 'には進まない方がよい。', )
MISS_MSG = ('スタート地点に戻った。', '目印の看板に戻ってきた。', 'ここからまたスタートだ。',
        'スタートからやり直しだ。', 'また同じところに戻った。', '階段までは遠い。', )
UP_MSG = ('上への階段がある。', )
DOWN_MSG = ('下への階段がある。', )
GAMEOVER_MSG = ('力尽きた。ゲームオーバー！', 'ゲームオーバー！', )

# 名前, HP,経験値, 逃げられる率10=100%, (攻撃方法確率,...),((攻撃,ダメージ),...), 魔法ダメージ(声火氷風雷), 弱点,耐性
ENEMY = (
        ('*dスライム**',1, 15,3, 9, (1,), ((0,'ドロドロ攻撃！',3,3),), (3,1,1,1,1), 0,6,),  # 0
        ('*dおばけ**',1, 16,4, 8, (1,), ((0,'攻撃してきた。',4,3),), (1,2,1,1,1), 1,6),
        ('*d泥の手**',1, 18,5, 9, (5,1), ((0,'手招きしている。',5,3),(1,'わしづかみ攻撃！',2)), (1,1,2,1,1), 2,6),
        ('*eにせ魔王**', 0, 600,400, 6, (1,4), ((0,'ムチで攻撃してきた。',400,100),(2,'恐ろしい魔法を唱えた。')), (1,1,1,-3,2), 4,3),

        ('*d切り株**', 1, 21,8, 8, (1,), ((0,'根を伸ばしてきた。',8,5),), (1,2,1,1,1), 1,6),  # 4
        ('*d提灯おばけ**',1, 28,10, 7, (1,), ((0,'体当たりしてきた。',9,4),), (1,-3,2,1,1), 2,1),
        ('*dマンドラニンジン**',1, 32,15, 9, (5,1), ((0,'攻撃してきた。',10,4),(7,'道具をうばってきた。')), (3,1,-3,1,1), 0,2),
        ('*eぼうしおばけ**', 0, 120,58, 7, (1,3), ((0,'攻撃してきた。',72,4),(1,'辺りを暗闇に変えた。',4)), (1,2,1,1,1), 1, 6),

        ('*dゴーレム**',1, 40,25, 8, (3,1), ((0,'岩石落とし！',16,18),(5,'武器の破壊！')), (1,-3,1,2,1), 3,1),  # 8
        ('*d水霊**',1, 52,36, 7, (3,1), ((0,'ブリザード攻撃！',22,8),(0,'極寒雪崩！',34,8)), (1,2,-3,1,1), 1,2),
        ('*d火霊**',1, 66,41, 7, (3,1), ((0,'ファイア攻撃！',25,6),(0,'極熱マグマ！',32,6)), (1,-3,2,1,1), 2,1),
        ('*eゴブリン**', 0, 230,130, 8, (1,2), ((0,'槍を突いてきた。',92,28),(1,'突進してきた。',4)), (5,1,-3,1,1), 0,2),

        ('*d目玉姉さん**',1, 88,60, 8, (8,1), ((0,'攻撃してきた。',29,11),(6,'魔法をうばってきた。')), (1,1,-3,2,1), 3,2),  # 12
        ('*d兜借り**',1, 93,57, 7, (8,1), ((0,'体当たりしてきた。',34,6),(8,'防具の破壊！')), (1,-3,1,1,2), 4,1),
        ('*dウサギノコ**',1, 96,64, 7, (1,), ((0,'飛び蹴りしてきた。',50,4),), (3,-3,1,1,1), 0,1),
        ('*eかぼちゃおばけ**', 0,320,240, 6, (5,1), ((0,'攻撃してきた。',64,14),(0,'タネをとばしてきた。',150,80)), (1,1,2,-3,1), 2,3),

        ('*dイエティ**',1, 120,85, 7, (7,1), ((0,'攻撃してきた。',48,7),(5,'武器の弾き飛ばし！')), (1,2,-3,1,1), 1,2),  # 16
        ('*dしにがみ**',1, 110,96, 7, (8,1), ((0,'カマを振り下ろした。',69,11),(8,'防具の弾き飛ばし！')), (1,-3,1,2,1), 3,1),
        ('*dプリン犬**',1, 140,130, 7, (9,1), ((0,'かみついてきた。',78,24),(4,'突進してきた。')), (1,2,1,1,-3), 1,4),
        ('*e魔王もどき**', 0, 700,500, 6, (1,3), ((0,'ムチで攻撃してきた。',450,75),(1,'恐ろしい魔法を唱えた。',10)), (1,1,1,-3,2), 4,3),

        ('*dシャドウ**',1, 140,170, 7, (8,1), ((0,'攻撃してきた。',73,28),(2,'瀕死の攻撃！',120,32)), (1,-3,2,1,1), 2,1),  # 20
        ('*dミミスライム**',1, 160,180, 7, (8,1), ((0,'ベトベト攻撃！',120,18),(6,'魔法溶かし！',142,12)), (5,1,1,-3,1), 0,3),
        ('*d洞窟コウモリ**',1, 140,190, 8, (8,1), ((0,'攻撃してきた。',130,12),(4,'羽ばたきレベルダウン！')), (1,1,-3,2,1), 3,2),
        ('*eスケルトン**', 0, 520,470, 7, (1,), ((0,'骨を投げてきた。',190,26),), (1,1,-3,2,1), 3,2),

        ('*dくちさけお化け**',1, 230,210, 8, (8,1), ((0,'攻撃してきた。',150,10), (6,'魔法封じ！')), (10,-3,1,1,1), 0,1),  # 24
        ('*dイエティゴート**',1, 250,220, 7, (9,1), ((0,'体当たりしてきた。',120,14), (1,'クォーター攻撃！',4)), (1,2,1,-3,1), 1,3),
        ('*d魔王の手先**',1, 270,230, 8, (7,1), ((0,'わしづかみ攻撃！',120,28), (5,'武器をうばってきた。')), (1,1,2,1,-3), 2,4),
        ('',0, 0,0, 0, (0,), ((0,'',0,0),), (0,0,0,0,0), 6,6),

        ('*dマンドラゴラ**',1, 300,240, 7, (6,1), ((0,'攻撃してきた。',120,8),(6,'魔法をうばってきた。')), (10,-3,1,1,1), 0,1),  # 28
        ('*dハムキノコ**',1, 340,260, 7, (6,1), ((0,'攻撃してきた。',130,48),(1,'1/2攻撃！',2)), (1,1,2,-3,1), 2,3),
        ('*dメタルスピリット**',1, 430,270, 7, (7,1), ((0,'攻撃してきた。',155,22),(7,'道具をうばってきた。')), (1,1,1,2,-3), 3,4),
        ('',0, 0,0, 0, (0,), ((0,'',0,0),), (0,0,0,0,0), 6,6),

        ('*e魔王**', 0, 900,700, 5, (3,1), ((0,'ムチで攻撃してきた。',200,100),(1,'魔法を唱えた。',10)), (1,1,1,-3,2), 4,3),  # 32
        ('*d戦士兜借り**',1, 560,360, 6, (5,1), ((0,'攻撃してきた。',180,25),(8,'防具の破壊！')), (1,1,-3,2,1), 3,2),
        ('*d強気な火**',1, 470,270, 8, (3,1), ((0,'攻撃してきた。',190,8),(1,'1/3攻撃！',3)), (1,-3,2,1,1), 2,1),
        ('*d目玉兄さん**',1, 520,310, 7, (4,1), ((0,'攻撃してきた。',170,18),(2,'瀕死の攻撃！')), (1,1,-3,2,1), 3,2),

        ('*b天使クマ**',0, 1000,1000, 1, (5,1), ((3,'ほほえんだ。'),(9,'にっこりとほほえんだ。')), (-3,-3,-3,-3,-3), 6,5),  # 36
        ('*b天使猫**',0, 2000,2000, 1, (5,1), ((3,'ほほえんだ。'),(10,'にっこりとほほえんだ。')), (-3,-3,-3,-3,-3), 6,5),
        )
FLOOR_ENEMY = ((0,1,2,3),(4,5,6,7),(8,9,10,11,36),(12,13,14,15),(16,17,18,19,37),(20,21,22,23),(24,25,26,37),(28,29,30,36),(32,33,34,35,36))
TREASURE = (32, '*a宝物**')  # 魔王の宝物

MODE_START, MODE_WALK, MODE_BATTLE, MODE_FIND, MODE_UP, MODE_DOWN = 1, 2, 3, 4, 5, 6
MODE_WARP, MODE_PIT, MODE_GAMEOVER ,MODE_GAMECLEAR = 7, 8, 9, 10
BUTTON_NAME = {
        MODE_START:('', '', '', ''),
        MODE_WALK:('← 左へ', '↑ 前へ', '→ 右へ', ''),
        MODE_BATTLE:('← 武器', '↑ 魔法', '→ 道具', '↓逃げる'), 
        MODE_FIND:('← 拾う', '', '→やめる', ''), 
        MODE_UP:('←上がる', '', '→やめる', ''), 
        MODE_DOWN:('←下りる', '', '→やめる', ''), 
        MODE_WARP:('', '', '', ''), 
        MODE_PIT:('', '', '', ''), 
        MODE_GAMEOVER:('', '', '', '↓再挑戦'), 
        MODE_GAMECLEAR:('', '', '', '↓再挑戦'), 
        }
ARMS  = (('*dきたえた素手**',3,2), ('*fソード**',4,3), ('*fランス**',5,4), ('*fアロー**',7,8), ('*fアックス**',8,3), ('*fハンマー**',9,4), )
ARMS_PICKUP = ((1,2),(1,2),(1,2,3),(1,2,3),(1,2,3,4),(1,2,3,4,5),(2,3,4,5),(2,3,4,5),(3,4,5))
MAGIC = (('*dどなり声**',2,4), ('*eファイア**',4,8), ('*cフリーズ**',5,7), ('*bウィンド**',4,10), ('*aサンダー**',10,6), )
MAGIC_PICKUP = ((1,2),(1,2),(1,2,3),(1,2,3,4),(1,2,3,4),(2,3,4),(3,4),(3,4),(1,2,3,4))
MAGIC_STR = ('*d声**', '*e炎**', '*c氷**', '*b風**', '*a雷**', '*5全**', '*7－**')
ITEM  = (('*dただの石**',1,6), ('*f手りゅう弾**',15,4), ('*f火炎びん**',17,5), ('*fどくガス弾**',19,6), ('*f手裏剣**',21,9), ('*fブーメラン**',5,27), ('*fトマホーク**',15,29), )
ARMOR = (('*dいつもの服**',1), ('*fレザーアーマー**',2), ('*fスケイルメイル**',4), ('*fチェインメイル**',12), ('*fプレートメイル**',32), ('*fドラコンメイル**',64), )
ARMOR_PICKUP = ((1,2),(1,2),(1,2,3),(1,2,3),(1,2,3,4),(1,2,3,4,5),(2,3,4,5),(2,3,4,5),(3,4,5))
MAX_LEVEL = 6

WALK_MODE_LIST = (MODE_WALK, MODE_BATTLE, MODE_FIND, MODE_WARP, MODE_PIT)
WALK_MODE_RATE = (70, 20, 25, 1, 1)
KIND = ('武器', '防具', '魔法', '道具', '薬草', '*a宝箱**')
FIND_MODE_RATE = (2, 3, 2, 4, 5, 0)
WALK_HINT_RATE = (7,6,5,4,4,3,3,2,2) # n*10%
UPDOWN_MODE_LIST = (MODE_UP, MODE_DOWN)
UP_MODE_RATE = (4,1)
DOWN_MODE_RATE = (1,2)

STEP_HP_DOWN, STEP_ENEMY_ESCAPE, STEP_ENEMY_TREASURE = 500, 600, 700
MID_POINT, END_POINT = 4, 7
CLS_COLOR = 3

class Message:
    def __init__(self, x, y, width, line, frcol=7, bgcol=0, height=0):
        self.msg_x = x
        self.msg_y = y
        self.msg_width = width
        self.msg_line = line
        self.msg_frcol = frcol
        self.msg_bgcol = bgcol
        if height < line*9+4:
            self.msg_height = line*9+4
        else:
            self.msg_height = height
        self.msg_scrl = 0
        self.msg_str = ['']*line
    
    def in_message(self, new_msg, keep=False):
        if keep or self.msg_str[0]=='':
            self.msg_str[0] = new_msg
        elif new_msg:
            for i in reversed(range(self.msg_line-1)):
                self.msg_str[i+1] = self.msg_str[i]
            self.msg_str[0] = new_msg
            self.msg_scrl = 9
    
    def draw_message(self):
        pyxel.rectb(self.msg_x, self.msg_y, self.msg_width, self.msg_height, self.msg_frcol)
        pyxel.rect(self.msg_x+1, self.msg_y+1, self.msg_width-2, self.msg_height-2, self.msg_bgcol)
        for i in range(1, self.msg_line):
            mrfont.text(self.msg_x+3, self.msg_y+3+(self.msg_line-i-1)*9+self.msg_scrl, self.msg_str[i], 5)
        if self.msg_scrl==0:
            mrfont.text(self.msg_x+3, self.msg_y+3+(self.msg_line-1)*9, self.msg_str[0], 7)

    def scroll(self):
        if self.msg_scrl > 0:
            self.msg_scrl -= 1
            return True
        return False

class App:
    def restart(self):
        self.msg = Message(MSG_X, MSG_Y, MSG_WIDTH, MSG_LINE, 7, 0)
        self.st_button = [MOUSE_OFF]*BUTTON_NUM
        self.button_x = [2, 42, 82, 122]
        self.button_y = WINDOW_HEIGHT-16
        self.cmd_trend = [[random.randrange(3) for _ in range(3)] for _ in range(3)]
        self.cmd_hist1 = random.randrange(3)
        self.cmd_hist2 = random.randrange(3)
        self.cmd_hist_diff = 0
        self.floor = 1
        self.level = 1
        self.maxexp = 1
        self.exp = 0
        self.levelup()
        self.hp = self.maxhp
        self.arms = self.armor = self.magic = self.item = 0
        self.arms_level = [0]*len(ARMS)
        self.armor_level = [0]*len(ARMOR)
        self.magic_level = [0]*len(MAGIC)
        self.item_level = [0]*len(ITEM)
        self.arms_level[0] = self.armor_level[0] = self.magic_level[0] = self.item_level[0] = 1
        self.have_treasure = False
        self.msg.in_message('さあ冒険の始まりだ。')
        self.msg.in_message(ENEMY[TREASURE[0]][0]+'を倒して、'+TREASURE[1]+'を手に入れよう。')
        self.mode = MODE_START
        self.push_button, self.step, self.wait = 0, 0, 10

    def levelup(self):
        ret = False
        if self.exp >= self.maxexp:
            self.level += 1
            self.exp -= self.maxexp
            ret = True
        self.maxhp  = (self.level**2)*10
        self.maxexp = (self.level**3)*10
        return ret

    #0:通常攻撃, 1:体力1/n, 2:瀕死, 3:体力回復, 4:強さダウン, 5:武器破壊, 6:魔法破壊, 7:アイテム破壊, 8:防具破壊, 9:強さアップ, 10:宝箱ドロップ
    def special_attack(self, way):
        if way[0] == 0:
            damage = way[2]+random.randrange(way[3])-ARMOR[self.armor][1]-(self.armor_level[self.armor]**2)*self.level
            if self.have_treasure:
                damage = way[2]*2+random.randrange(way[3]*2)-ARMOR[self.armor][1]-(self.armor_level[self.armor]**2)*self.level
            if damage <= 0:
                self.msg.in_message(way[1]+'しかしダメージを受けない。')
            else:
                self.msg.in_message(way[1]+f'*e{damage}のダメージ**を受けた。')
                self.hp -= damage
            return STEP_HP_DOWN
        elif way[0] == 1:
            div = way[2]
            if self.have_treasure:
                div *= 2
            self.hp //= div
            if div == 2:
                self.msg.in_message(way[1]+f'*e体力が半分**になった。')
            else:
                self.msg.in_message(way[1]+f'*e体力が1/{div}**になった。')
            return STEP_HP_DOWN
        elif way[0] == 2:
            self.hp = 1
            self.msg.in_message(way[1]+'*8瀕死**の状態。')
            return STEP_ENEMY_ESCAPE
        elif way[0] == 3:
            if self.hp < self.maxhp:
                self.hp = self.maxhp
                self.msg.in_message(way[1]+'なんと*3体力が回復**した。')
            else:
                self.msg.in_message(way[1]+'*3体力は全快**だ。')
            return STEP_ENEMY_ESCAPE
        elif way[0] == 4:
            if self.level > 1:
                self.level -= 1
                self.exp = 0
                self.msg.in_message(way[1]+'*8強さが下がった**。')
                return STEP_ENEMY_ESCAPE
            else:
                self.msg.in_message(way[1]+'これ以上強さは下がらない。')
                return STEP_HP_DOWN
        elif way[0] == 5:
            if self.arms != 0:
                self.msg.in_message(way[1]+ARMS[self.arms][0]+'は*8なくなった**。')
                self.arms = 0
                return STEP_ENEMY_ESCAPE
            else:
                self.msg.in_message(way[1]+'しかし武器は持っていない。')
                return STEP_HP_DOWN
        elif way[0] == 6:
            if self.magic != 0:
                self.msg.in_message(way[1]+MAGIC[self.magic][0]+'は*8なくなった**。')
                self.magic = 0
                return STEP_ENEMY_ESCAPE
            else:
                self.msg.in_message(way[1]+'しかし魔法は持っていない。')
                return STEP_HP_DOWN
        elif way[0] == 7:
            if self.item != 0:
                self.msg.in_message(way[1]+ITEM[self.item][0]+'は*8なくなった**。')
                self.item = 0
                return STEP_ENEMY_ESCAPE
            else:
                self.msg.in_message(way[1]+'しかし道具は持っていない。')
                return STEP_HP_DOWN
        elif way[0] == 8:
            if self.armor != 0:
                self.msg.in_message(way[1]+ARMOR[self.armor][0]+'は*8なくなった**。')
                self.armor = 0
                return STEP_ENEMY_ESCAPE
            else:
                self.msg.in_message(way[1]+'しかし防具は持っていない。')
                return STEP_HP_DOWN
        elif way[0] == 9:
            self.level += 1
            self.exp = 0
            self.msg.in_message(way[1]+'なんと*a強さが上がった**。')
            return STEP_ENEMY_ESCAPE
        elif way[0] == 10:
            return STEP_ENEMY_TREASURE

    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title='MiniRPG')
        pyxel.load('assets/MiniRPG.pyxres')
        pyxel.mouse(True)
        self.restart()
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.msg.scroll():
            return
        if self.wait > 0:
            self.wait -= 1
            return
        if self.levelup():
            self.msg.in_message(f'*aレベルアップ**した。*a強さが{self.level}**になった。')
            return

        if self.mode == MODE_START:
            self.msg.in_message(f'【地下{self.floor}階】スタートの目印として看板を立てた。')
            self.mode = MODE_WALK
            self.cmd_hist_diff = -1
        elif self.mode == MODE_WALK:
            if self.step == 0:
                self.r1, self.rx1, self.ry1 = random.randrange(4), random.randrange(4), random.randrange(4)
                self.r2, self.rx2, self.ry2 = random.randrange(4), random.randrange(4), random.randrange(4)
                self.hp += (self.maxhp//100)+1
                if self.hp > self.maxhp:
                    self.hp = self.maxhp
                self.reset_select = self.cmd_trend[self.cmd_hist1][self.cmd_hist2]
                if self.cmd_hist_diff > 2 and random.randrange(10) < WALK_HINT_RATE[self.floor-1]:
                    direct = '《右》'
                    if self.reset_select == 0:
                        direct = '《左》'
                    elif self.reset_select == 1:
                        direct = '《前》'
                    self.msg.in_message(direct+random.choice(HINT_MSG))
                    self.hint = True
                else:
                    if self.cmd_hist_diff > 0:
                        self.msg.in_message(random.choice(WALK_MSG))
                    elif self.cmd_hist_diff < 0:
                        self.cmd_hist_diff = 0
                    else:
                        self.msg.in_message(random.choice(MISS_MSG))
                    self.hint = False
                self.step = 1
            elif self.step == 1:
                if self.push_button in range(1,4):
                    if self.cmd_hist_diff > 2 and self.cmd_trend[self.cmd_hist1][self.cmd_hist2] == self.push_button-1:
                        self.cmd_hist_diff = 0
                    else:
                        self.cmd_hist_diff += 1
                    if self.cmd_hist_diff >= END_POINT:
                        if self.have_treasure:
                            self.mode = random.choices(UPDOWN_MODE_LIST, UP_MODE_RATE, k=1)[0]
                        else:
                            self.mode = random.choices(UPDOWN_MODE_LIST, DOWN_MODE_RATE, k=1)[0]
                        self.cmd_hist_diff = 3
                    else:
                        self.mode = random.choices(WALK_MODE_LIST, WALK_MODE_RATE, k=1)[0]
                    self.cmd_trend[self.cmd_hist1][self.cmd_hist2] = self.push_button-1
                    self.cmd_hist1, self.cmd_hist2 = self.cmd_hist2, self.push_button-1
                    self.push_button, self.step = 0, 0
        elif self.mode == MODE_BATTLE:
            if self.step == 0:
                self.enemy_num = random.choice(FLOOR_ENEMY[self.floor-1])
                self.enemy_name = ENEMY[self.enemy_num][0]
                self.enemy_bgcolor = ENEMY[self.enemy_num][1]
                self.enemy_maxhp = self.enemy_hp = ENEMY[self.enemy_num][2]
                if self.have_treasure:
                    self.enemy_maxhp = self.enemy_hp = ENEMY[self.enemy_num][2]*2
                self.enemy_exp = ENEMY[self.enemy_num][3]
                self.enemy_escape = ENEMY[self.enemy_num][4]
                self.enemy_attack_rate = ENEMY[self.enemy_num][5]
                self.enemy_attack = ENEMY[self.enemy_num][6]
                self.enemy_magic_damage = ENEMY[self.enemy_num][7]
                self.enemy_weak = ENEMY[self.enemy_num][8]
                self.enemy_strong = ENEMY[self.enemy_num][9]
                if random.randrange(3) == 0:
                    self.msg.in_message(self.enemy_name+'が現れた！*eいきなりおそってきた**。')
                    self.step, self.wait = 3, 10
                else:
                    self.msg.in_message(self.enemy_name+'が現れた！')
                    self.step = 1
            elif self.step == 1:
                if self.push_button in (1, 2, 3):
                    if self.push_button == 1:  # 戦う
                        attack = ARMS[self.arms][0]+'で、'
                        damage = (ARMS[self.arms][1]+self.arms_level[self.arms]**2)*self.level \
                                +random.randrange(ARMS[self.arms][2]*self.level)
                    elif self.push_button == 2:  # 魔法
                        attack = MAGIC[self.magic][0]
                        damage = (MAGIC[self.magic][1]+self.magic_level[self.magic]**2)*self.level \
                                +random.randrange(MAGIC[self.magic][2]*self.level)
                        damage_add = self.enemy_magic_damage[self.magic]
                        if damage_add > 1:
                            attack += 'は*aよく効いた**。'
                            damage *= damage_add
                        elif damage_add < 0:
                            attack += 'は*eあまり効かない**。'
                            damage //= -damage_add
                        else:
                            attack += 'で、'
                    elif self.push_button == 3:  # 道具
                        attack = ITEM[self.item][0]+'で、'
                        damage = (ITEM[self.item][1]+self.item_level[self.item]**2)*self.level \
                                +random.randrange(ITEM[self.item][2]*self.level)
                        self.item = 0
                    self.msg.in_message(attack+f'*a{damage}のダメージ**を与えた。')
                    self.enemy_hp -= damage
                    if self.enemy_hp < 0:
                        self.enemy_hp = 0
                    self.step, self.wait = 2, 10
                elif self.push_button == 4:  # 逃げる
                    if random.randrange(10) < self.enemy_escape:
                        self.msg.in_message('何とか逃げ切った。')
                        self.mode = MODE_WALK
                        self.step = 0
                    else:
                        self.msg.in_message('逃げられない。')
                        self.step = 2
                    self.wait = 10
                self.push_button = 0
            elif self.step == 2:
                if self.enemy_hp <= 0:
                    self.msg.in_message(self.enemy_name+f'をたおした。*a{self.enemy_exp}の経験**を得た。')
                    self.exp += self.enemy_exp
                    if self.enemy_num == TREASURE[0] and self.have_treasure == False:
                        self.step, self.wait = 4, 20
                    else:
                        self.mode, self.step, self.wait = MODE_WALK, 0, 10
                else:
                    self.step = 3
            elif self.step == 3:
                way = random.choices(self.enemy_attack, self.enemy_attack_rate, k=1)[0]
                self.step = self.special_attack(way)
                if self.hp < 0:
                    self.hp = 0
            elif self.step == 4:  # 宝ドロップ
                self.msg.in_message(ENEMY[TREASURE[0]][0]+'の'+TREASURE[1]+'を手に入れた！地上にもどろう。')
                self.msg.in_message('どうやら*e敵が狂暴化**したようだ。')
                self.have_treasure = True
                self.mode, self.step = MODE_WALK, 0
            elif self.step == STEP_HP_DOWN:
                if self.hp <= 0:
                    self.msg.in_message(self.enemy_name+'にやられた。')
                    self.mode = MODE_GAMEOVER
                    self.push_button, self.step, self.wait = 0, 0, 10
                else:
                    self.step = 1
            elif self.step == STEP_ENEMY_ESCAPE:  # 敵逃げる
                self.msg.in_message(self.enemy_name+'は逃げていった。')
                self.mode, self.step = MODE_WALK, 0
            elif self.step == STEP_ENEMY_TREASURE:  # 宝箱ドロップ
                self.msg.in_message(self.enemy_name+'逃げていった。*a宝箱**を見つけた。')
                self.mode, self.step, self.kind = MODE_FIND, 1, 5
        elif self.mode == MODE_FIND:
            if self.step == 0:
                self.kind = random.choices(range(len(FIND_MODE_RATE)), FIND_MODE_RATE, k=1)[0]
                self.msg.in_message(KIND[self.kind]+'を見つけた。')
                self.step = 1
            elif self.step == 1:
                if self.push_button in range(1,5):
                    self.mode = random.choices(WALK_MODE_LIST, WALK_MODE_RATE, k=1)[0]
                    if self.push_button == 1:
                        if self.kind == 0:
                            self.arms = random.choice(ARMS_PICKUP[self.floor-1])
                            self.arms_level[self.arms] += 1
                            if self.arms_level[self.arms] > MAX_LEVEL:
                                self.arms_level[self.arms] = MAX_LEVEL
                            self.msg.in_message(ARMS[self.arms][0]+'を拾った')
                        elif self.kind == 1:
                            self.armor = random.choice(ARMOR_PICKUP[self.floor-1])
                            self.armor_level[self.armor] += 1
                            if self.armor_level[self.armor] > MAX_LEVEL:
                                self.armor_level[self.armor] = MAX_LEVEL
                            self.msg.in_message(ARMOR[self.armor][0]+'を拾った')
                        elif self.kind == 2:
                            self.magic = random.choice(MAGIC_PICKUP[self.floor-1])
                            self.magic_level[self.magic] += 1
                            if self.magic_level[self.magic] > MAX_LEVEL:
                                self.magic_level[self.magic] = MAX_LEVEL
                            self.msg.in_message(MAGIC[self.magic][0]+'を拾った')
                        elif self.kind == 3:
                            self.item = random.randrange(1, len(ITEM))
                            self.item_level[self.item] += 1
                            if self.item_level[self.item] > MAX_LEVEL:
                                self.item_level[self.item] = MAX_LEVEL
                            self.msg.in_message(ITEM[self.item][0]+'を拾った')
                        elif self.kind == 4:
                            self.hp = self.maxhp
                            self.msg.in_message('薬草を拾って食べた。*3体力が回復**した。')
                        elif self.kind == 5:
                            self.arms = random.choice(ARMS_PICKUP[self.floor-1])
                            self.arms_level[self.arms] += 1
                            self.armor = random.choice(ARMOR_PICKUP[self.floor-1])
                            self.armor_level[self.armor] += 1
                            self.magic = random.choice(MAGIC_PICKUP[self.floor-1])
                            self.magic_level[self.magic] += 1
                            self.item = random.randrange(1, len(ITEM))
                            self.item_level[self.item] += 1
                            self.msg.in_message('なんと'+ARMS[self.arms][0]+'、'+MAGIC[self.magic][0]+'を拾った。')
                            self.msg.in_message('さらに'+ITEM[self.item][0]+'、'+ARMOR[self.armor][0]+'を拾った。')
                    else:
                        if self.kind == 5:
                            getexp = self.maxexp // 2
                        else:
                            getexp = self.maxexp // 10
                        self.msg.in_message(f'拾わずに進んだ。*a{getexp}の経験**を得た。')
                        self.exp += getexp
                    self.push_button, self.step, self.wait = 0, 0, 10
        elif self.mode == MODE_UP:
            if self.step == 0:
                self.msg.in_message(random.choice(UP_MSG))
                self.step = 1
            elif self.step == 1:
                if self.push_button in range(1,5):
                    if self.push_button == 1:
                        if self.floor == 1:
                            if self.have_treasure:
                                self.msg.in_message('地上に出た。')
                                self.mode = MODE_GAMECLEAR
                            else:
                                self.msg.in_message(TREASURE[1]+'を見つけずに、帰るわけにはいかない。')
                                self.mode = MODE_WALK
                        else:
                            self.floor -= 1
                            self.mode = MODE_START
                    else:
                        self.mode = MODE_WALK
                    self.push_button, self.step, self.wait = 0, 0, 10
        elif self.mode == MODE_DOWN:
            if self.step == 0:
                self.msg.in_message(random.choice(DOWN_MSG))
                self.step = 1
            elif self.step == 1:
                if self.push_button in range(1,5):
                    if self.push_button == 1:
                        if self.floor == 9:
                            self.msg.in_message('さらに深い地下には行けなった。')
                            self.mode = MODE_WALK
                        else:
                            self.floor += 1
                            self.mode = MODE_START
                    else:
                        self.mode = MODE_WALK
                    self.push_button, self.step, self.wait = 0, 0, 10
        elif self.mode == MODE_WARP:
            if self.step == 0:
                self.msg.in_message('おっと*8ワープ**だ。')
                self.step, self.wait = 1, 20
            elif self.step == 1:
                if self.floor == 1:
                    self.msg.in_message('何も起こらなかった。')
                    self.mode = MODE_WALK
                else:
                    self.floor -= 1
                    self.msg.in_message(f'地下{self.floor}階にワープした。')
                    self.mode = MODE_START
                self.push_button, self.step = 0, 0
        elif self.mode == MODE_PIT:
            if self.step == 0:
                self.msg.in_message('おっと*8落とし穴**だ。')
                self.step, self.wait = 1, 20
            elif self.step == 1:
                if self.floor == 9:
                    self.msg.in_message('つまずいた。')
                    self.mode = MODE_WALK
                else:
                    self.floor += 1
                    self.msg.in_message(f'地下{self.floor}階に落ちた。')
                    self.mode = MODE_START
                self.push_button, self.step = 0, 0
        elif self.mode == MODE_GAMEOVER:
            if self.step == 0:
                self.msg.in_message(random.choice(GAMEOVER_MSG))
                self.step = 1
            elif self.step == 1:
                if self.push_button == 4:
                    self.restart()
        elif self.mode == MODE_GAMECLEAR:
            if self.step == 0:
                self.msg.in_message('見事に'+TREASURE[1]+'を持ち帰った。*aゲームクリア！**')
                self.step = 1
            elif self.step == 1:
                if self.push_button == 4:
                    self.restart()
        for i in range(BUTTON_NUM):
            if BUTTON_NAME[self.mode][i] and \
                    self.button_x[i]<=pyxel.mouse_x<self.button_x[i]+38 and self.button_y<=pyxel.mouse_y<self.button_y+14:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or (pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.st_button[i]==MOUSE_PUSH):
                    self.st_button[i] = MOUSE_PUSH
                elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and self.st_button[i]==MOUSE_PUSH:
                    self.st_button[i] = MOUSE_RELEASE
                    self.push_button = i+1
                else:
                    self.st_button[i] = MOUSE_OFF
            else:
                self.st_button[i] = MOUSE_OFF
            if BUTTON_NAME[self.mode][i]:
                if pyxel.btn(ABC_KEY[i]) or pyxel.btn(NUM_KEY[i]) or pyxel.btn(ARW_KEY[i]) or pyxel.btn(DPAD[i]) or pyxel.btn(ABXY[i]):
                    self.st_button[i] = MOUSE_PUSH
                elif pyxel.btnr(ABC_KEY[i]) or pyxel.btnr(NUM_KEY[i]) or pyxel.btnr(ARW_KEY[i]) or pyxel.btnr(DPAD[i]) or pyxel.btnr(ABXY[i]):
                    self.st_button[i] = MOUSE_RELEASE
                    self.push_button = i+1

    def draw_enemy(self):
        pyxel.rectb(ENEMY_X,   ENEMY_Y,   ENEMY_WIDTH,   ENEMY_HEIGHT,   7)
        pyxel.rect( ENEMY_X+1, ENEMY_Y+1, ENEMY_WIDTH-2, ENEMY_HEIGHT-2, 0)
        if self.mode in (MODE_START, MODE_WALK, MODE_FIND, MODE_UP, MODE_DOWN, MODE_WARP, MODE_PIT, MODE_GAMEOVER) and self.step != 0:
            if self.floor < 6:
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3, 1, 0, 192, 32, 32, 0)
                pyxel.blt(ENEMY_X+3+32, ENEMY_Y+3, 1, 0, 192, 32, 32, 0)
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3+32, 1, 0, 192, 32, 30, 0)
                pyxel.blt(ENEMY_X+3+32, ENEMY_Y+3+32, 1, 0, 192, 32, 30, 0)
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3, 1, 0, 224, 16, 16, 0)
                pyxel.blt(ENEMY_X+3+48, ENEMY_Y+3, 1, 16, 224, 16, 16, 0)
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3+48, 1, 0, 240, 16, 14, 0)
                pyxel.blt(ENEMY_X+3+48, ENEMY_Y+3+48, 1, 16, 240, 16, 14, 0)
            else:
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3, 1, 32, 192, 32, 32, 0)
                pyxel.blt(ENEMY_X+3+32, ENEMY_Y+3, 1, 32, 192, 32, 32, 0)
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3+32, 1, 32, 192, 32, 30, 0)
                pyxel.blt(ENEMY_X+3+32, ENEMY_Y+3+32, 1, 32, 192, 32, 30, 0)
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3, 1, 32, 224, 16, 16, 0)
                pyxel.blt(ENEMY_X+3+48, ENEMY_Y+3, 1, 48, 224, 16, 16, 0)
                pyxel.blt(ENEMY_X+3, ENEMY_Y+3+48, 1, 32, 240, 16, 14, 0)
                pyxel.blt(ENEMY_X+3+48, ENEMY_Y+3+48, 1, 46, 240, 16, 14, 0)
            pyxel.blt(ENEMY_X+3+16+self.rx1*8, ENEMY_Y+3+16+self.ry1*8, 1, self.r1*8, 184, 8, 8, 1)

        if self.mode == MODE_BATTLE and self.step == 5:  # 魔王の宝物
            pyxel.blt(ENEMY_X+20, ENEMY_Y+4, 1, 160, 0, 32, 32, 3)  # 宝箱閉じ
            mrfont.text(ENEMY_X+4, ENEMY_Y+40, ENEMY[TREASURE[0]][0]+'の'+TREASURE[1], 7)
        elif self.mode == MODE_BATTLE and self.step != 0:
            p, q = self.enemy_num%8, self.enemy_num//8
            pyxel.blt(ENEMY_X+20, ENEMY_Y+4, 0, p*32, q*32, 32, 32, self.enemy_bgcolor)
            mrfont.text(ENEMY_X+4, ENEMY_Y+40, self.enemy_name, 7)
            mrfont.text(ENEMY_X+4, ENEMY_Y+49, f'体力:{self.enemy_hp}／{self.enemy_maxhp}', 7)
            mrfont.text(ENEMY_X+4, ENEMY_Y+58, f'経験:{self.enemy_exp}', 7)
            mrfont.text(ENEMY_X+4, ENEMY_Y+67, '弱点:'+MAGIC_STR[self.enemy_weak]+'／耐性:'+MAGIC_STR[self.enemy_strong], 7)
        elif self.mode == MODE_FIND and self.step != 0:
            pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, self.kind*32, 0, 32, 32, 3 if self.kind==5 else 2)  # 武器,魔法,道具,防具,薬草,宝箱閉じ
            mrfont.text(ENEMY_X+12, ENEMY_Y+67, '←'+KIND[self.kind]+'を拾う', 7)
        elif self.mode == MODE_UP and self.step != 0:
            pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, 64, 32, 32, 32, 0)  # 上り階段
            mrfont.text(ENEMY_X+14, ENEMY_Y+67, '  ←地上へ' if self.floor == 1 else f'←地下{self.floor-1}階へ', 7)
        elif self.mode == MODE_DOWN and self.step != 0:
            pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, 32, 32, 32, 32, 0)  # 下り階段
            mrfont.text(ENEMY_X+14, ENEMY_Y+67, f'←地下{self.floor+1}階へ', 7)
        elif self.mode == MODE_WARP and self.step != 0:
            pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, 128, 32, 32, 32, 2)  # ワープ
            mrfont.text(ENEMY_X+24, ENEMY_Y+67, 'ワープ', 7)
        elif self.mode == MODE_PIT and self.step != 0:
            pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, 96, 32, 32, 32, 1)  # 落とし穴
            mrfont.text(ENEMY_X+20, ENEMY_Y+67, '落とし穴', 7)
        elif self.mode == MODE_GAMEOVER and self.step != 0:
            p, q = self.enemy_num%8, self.enemy_num//8
            pyxel.blt(ENEMY_X+3+24, ENEMY_Y+3+4, 0, p*32, q*32, 32, 32, self.enemy_bgcolor)
            pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+20, 1, 160, 32, 32, 32, 0)  # 墓
            mrfont.text(ENEMY_X+4, ENEMY_Y+67, 'ゲームオーバー！', 8)
        elif self.mode == MODE_GAMECLEAR and self.step != 0:
            pyxel.blt(ENEMY_X+3, ENEMY_Y+3, 1, 160, 64, 64, 64, 0)  # シート
            pyxel.blt(ENEMY_X+3+10, ENEMY_Y+3+6, 1, 0, 64, 32, 32, 3)  # 宝箱開き
            pyxel.blt(ENEMY_X+3+26, ENEMY_Y+3+8, 1, 32, 64, 32, 32, 0)  # 熊
            pyxel.blt(ENEMY_X+3+4, ENEMY_Y+3+30, 1, 64, 64, 32, 16, 0)  # 冠
            pyxel.blt(ENEMY_X+3+30, ENEMY_Y+3+30, 1, 128, 64, 32, 24, 0)  # 玉
            pyxel.blt(ENEMY_X+3+12, ENEMY_Y+3+34, 1, 96, 64, 32, 24, 0)  # 金
            mrfont.text(ENEMY_X+8, ENEMY_Y+67, 'ゲームクリア！', 10)
        elif self.mode == MODE_WALK and self.step != 0:
            if self.hint:
                if self.reset_select == 0:  # 左
                    pyxel.blt(ENEMY_X+3, ENEMY_Y+3+16+self.ry2*8, 1, self.r2*8, 184, 8, 8, 1)
                elif self.reset_select == 1:  # 上
                    pyxel.blt(ENEMY_X+3+16+self.rx2*8, ENEMY_Y+3, 1, self.r2*8, 184, 8, 8, 1)
                else:  # 右
                    pyxel.blt(ENEMY_X+3+56, ENEMY_Y+3+16+self.ry2*8, 1, self.r2*8, 184, 8, 8, 1)
            else:
                pyxel.blt(ENEMY_X+3+16+self.rx2*8, ENEMY_Y+3+16+self.ry2*8, 1, self.r2*8, 184, 8, 8, 1)
            if self.cmd_hist_diff == 0:
                pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, 0, 32, 32, 32, 0)  # 看板
                mrfont.text(ENEMY_X+6, ENEMY_Y+67, f'地下{self.floor}階スタート', 7)
            elif self.cmd_hist_diff == MID_POINT:
                pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, 192, 32, 32, 32, 2)  # 岩
            elif self.cmd_hist_diff == END_POINT-1:
                pyxel.blt(ENEMY_X+3+16, ENEMY_Y+3+16, 1, 224, 32, 32, 32, 2)  # 岩

    def draw_player(self):
        pyxel.rectb(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, 7)
        pyxel.rect( PLAYER_X+1, PLAYER_Y+1, PLAYER_WIDTH-2, PLAYER_HEIGHT-2, 0)
        s = f'【地下{self.floor}階】'
        if self.have_treasure:
            s += ENEMY[TREASURE[0]][0]+'の'+TREASURE[1]
        mrfont.text(PLAYER_X+4, PLAYER_Y+4, s, 7)
        mrfont.text(PLAYER_X+4, PLAYER_Y+13, f'強さ:{self.level}', 7)
        mrfont.text(PLAYER_X+4, PLAYER_Y+22, f'体力:{self.hp}／{self.maxhp}', 8 if self.hp*4 < self.maxhp else 14 if self.hp*2 < self.maxhp else 7)
        mrfont.text(PLAYER_X+4, PLAYER_Y+31, f'経験:{self.exp}／{self.maxexp}', 7)
        attack_min = (ARMS[self.arms][1]+self.arms_level[self.arms]**2)*self.level
        attack_max = attack_min+ARMS[self.arms][2]*self.level-1
        mrfont.text(PLAYER_X+4, PLAYER_Y+40, 
                '武器:'+ARMS[self.arms][0]+f':{attack_min}～{attack_max}' if self.arms_level[self.arms]<=1 else 
                '武器:'+ARMS[self.arms][0]+f'*{4 if self.arms_level[self.arms]<MAX_LEVEL else 9}+{self.arms_level[self.arms]-1}**:{attack_min}～{attack_max}', 7)
        attack_min = (MAGIC[self.magic][1]+self.magic_level[self.magic]**2)*self.level
        attack_max = attack_min+MAGIC[self.magic][2]*self.level-1
        mrfont.text(PLAYER_X+4, PLAYER_Y+49, 
                '魔法:'+MAGIC[self.magic][0]+f':{attack_min}～{attack_max}' if self.magic_level[self.magic]<=1 else 
                '魔法:'+MAGIC[self.magic][0]+f'*{4 if self.magic_level[self.magic]<MAX_LEVEL else 9}+{self.magic_level[self.magic]-1}**:{attack_min}～{attack_max}', 7)
        attack_min = (ITEM[self.item][1]+self.item_level[self.item]**2)*self.level
        attack_max = attack_min+ITEM[self.item][2]*self.level-1
        mrfont.text(PLAYER_X+4, PLAYER_Y+58, 
                '道具:'+ITEM[self.item][0]+f':{attack_min}～{attack_max}' if self.item_level[self.item]<=1 else 
                '道具:'+ITEM[self.item][0]+f'*{4 if self.item_level[self.item]<MAX_LEVEL else 9}+{self.item_level[self.item]-1}**:{attack_min}～{attack_max}', 7)
        mrfont.text(PLAYER_X+4, PLAYER_Y+67, 
                '防具:'+ARMOR[self.armor][0]+f':{ARMOR[self.armor][1]+(self.armor_level[self.armor]**2)*self.level}' if self.armor_level[self.armor]<=1 else 
                '防具:'+ARMOR[self.armor][0]+f'*{4 if self.armor_level[self.armor]<MAX_LEVEL else 9}+{self.armor_level[self.armor]-1}**:{ARMOR[self.armor][1]+(self.armor_level[self.armor]**2)*self.level}', 7)

    def draw_button(self):
        for i in range(BUTTON_NUM):
            if BUTTON_NAME[self.mode][i]:
                p = 1 if self.st_button[i]==MOUSE_PUSH else 0
                pyxel.rectb(3+40*i, WINDOW_HEIGHT-15, 37, 13, 1)
                pyxel.rectb(2+40*i+p, WINDOW_HEIGHT-16+p, 37, 13, 7)
                pyxel.rect( 3+40*i+p, WINDOW_HEIGHT-15+p, 35, 11, 2*p)
                mrfont.text(5+40*i+p, WINDOW_HEIGHT-13+p, BUTTON_NAME[self.mode][i], 7)

    def draw(self):
        pyxel.cls(CLS_COLOR)
        self.draw_enemy()
        self.draw_player()
        self.msg.draw_message()
        self.draw_button()

App()