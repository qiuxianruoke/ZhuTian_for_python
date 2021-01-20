from canshu import mvs
# 设置人物A类
class player:
    def __init__(self):
        self.HP = 1000
        self.MP = 120
        self.S1CD = 0 #技能一CD
        self.S2CD = 0 #技能二CD
        self.atspeed = 25 #普通攻击速度
        self.attcktion = 50
        self.mvspeed = mvs #角色人物移动速度
        self.respeed = 1 #能量恢复速度
        self.body = 'stand' #身体状态，参数一共由stand,down,run三个，表示立、蹲
        self.direction = True
        #self.movel = False #是否向左
        #self.mover = True #是否向右
        self.atskill = 'not' #是否进行普攻释放技能，参数还有attck,skill1,skill2
        self.x = 0 # 角色水平坐标
        self.y = 400 #角色垂直坐标
# 创建类player的对象playerA
playerA = player()
playerB = player()
playerB.x = 1060
playerB.y = 460
playerB.direction = False