import pygame
# 存储游戏已运行帧数
t = 0 

# 定义帧数
FPS = 25

# 定义头像宽度高度
Hwid = 60
Hhgt = 60

# 蹲立y值变化
mul = 80

# HP
colorHP = (0, 221, 17, 60)  #设置HP提示条RBG值
# MP
colorMP = (34, 238, 255) #设置MP提示条RBG值

# 是否播放音乐
mus = True # 是否播放音乐


# 初始化参数区
Wid = 1280 # 窗口宽度
Hgt = 719  # 窗口高度

# 绘制头像参数
txA = pygame.image.load('其他\图标.jpg')    # 加载图标图片
txARect = txA.get_rect()    # 获取图标图片的rect属性
txARect.top = 15    # 重新赋值图标y坐标
txARect.left = 10   # 重新赋值图标x坐标
txB = pygame.image.load('其他\图标.jpg')
txBRect = txB.get_rect()
txBRect.top = 15
txBRect.right = Wid - 19

pDHgt = 29       # 玩家弹幕高度 
pDWid = 48       #玩家弹幕宽度

pAAtmentx = [0]   #玩家A弹幕水平坐标列表
pAAtmenty = [0]   #玩家A弹幕垂直坐标列表
pAAtmentd = [0]   #玩家A弹幕方向列表
pAAtmentTF = [0]  #玩家A弹幕命中判断列表

pBAtmentx = [0]   #玩家B弹幕水平坐标列表
pBAtmenty = [0]   #玩家B弹幕垂直坐标列表
pBAtmentd = [0]   #玩家B弹幕方向列表
pBAtmentTF = [0]  #玩家B弹幕命中判断列表

pAm = 0 # 玩家A移动计帧器
pAatt = 0    # 玩家A普攻计帧器
pAsk1t = 1   # 玩家A一技能计帧器
pAsk2t = 1   # 玩家A二技能计帧器
AS1CD = 3    # 玩家A一技能CD
AS2CD = 5    # 玩家A二技能CD
AS1CDMP = 10    # 玩家A一技能耗能
AS2CDMP = 15    # 玩家A二技能耗能

pBm = 0 # 玩家B移动计帧器
pBatt =0    # 玩家B普攻计帧器
pBsk1t = 1   # 玩家B一技能计帧器
pBsk2t = 1   # 玩家B二技能计帧器
BS1CD = 3    # 玩家B一技能CD
BS2CD = 5    # 玩家B二技能CD
BS1CDMP = 10    # 玩家B一技能耗能
BS2CDMP = 15    # 玩家B二技能耗能

# 玩家伤害
# 玩家A
Askill1ion = 3 # 玩家A技能一每帧伤害
Askill2ion = 18 # 玩家A技能二每帧伤害

# 玩家A一技能回复生命值（每帧）
AddHP = 50

# 人物初始化生命值
allHP = 1000

# 是否进入游戏
gameb = False # 是否进入游戏

# 开场“朱天”
sx = 0 # “朱天”x坐标
sy = 0 # “朱天”y坐标
dspeedx = 25 # 朱天移速(x轴)
dspeedy = 25 # 朱天移速(y轴)
ztwid = 410 # 朱天宽度
zthgt = 236 # 朱天高度

# 玩家B技能一增强比例
BS1up = 15 # 伤害
# 玩家B技能一增强比例
BS2 = 10

# 玩家移速
mvs = 8

# 玩家B二技能每帧伤害
BS2SH = 4