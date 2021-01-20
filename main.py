# 初始化
# 函数库导入
import sys

# 导入第三方库
import pygame
from pygame.locals import*

# 导入私有库
from canshu import*
from renwu import*
from shijian import*
from myFunction import*


# 初始化创建游戏窗口
pygame.mixer.init() # 混音器初始化
pygame.init() #不可或缺，使用Pygame必写
window = pygame.display.set_mode((Wid, Hgt)) # 设置窗口属性，默认居中
pygame.display.set_caption("朱天") # 将游戏窗口命名为“朱天”
tubiao = pygame.image.load("其他\图标.jpg")  # 加载图标
pygame.display.set_icon(tubiao) #设置图标


# 设置计时器文本
tCter = pygame.font.SysFont(None, 36) # 创建font对象tCter，用于设置计时器字体（默认）、字号
# 将现实计时器数值功能封装
def timer(t):
    # t为游戏运行帧数
    scond = t*4/100 # 计算游戏运行时间
    timeText = str(scond) # scond是整型，将其转化为字符串
    tCtertext = tCter.render(timeText+'s', True, (34, 153, 204)) #将游戏时间打印，抗锯齿，文字颜色，文本背景颜色;返回一个surface对象
    tCtertextRect = tCtertext.get_rect() # 返回rect对象，其属性为tCtertext的属性
    tCtertextRect.centerx = 640 # 修改计时器文本水平坐标
    tCtertextRect.centery = 32  # 修改计时器文本垂直坐标
    window.blit(tCtertext, tCtertextRect) # 绘制计时器文本


# 定义图片加载绘制函数
def loadimg(str1, num, t='.png', x=0, y=0, jx=False): 
    # str1为图片分类（如玩家A普攻），num为图片序号，t为文件后缀名，x,y为坐标（图片左上角）
    # jx判断是否镜像
     # 将图片加载到对象imgSurface
    imgSurface = pygame.image.load(str1 + str(num) + t) # 加载图片
    if jx == False:
        imgSurface = pygame.transform.flip(imgSurface, True, False)
   # if playerA.x + 90 <= 0 or playerA.x - 90 <= Wid + 90:
   #     imgSurface = pygame.transform.flip(imgSurface, True, False)
    imgRect = imgSurface.get_rect()
    imgRect.left = x #修改图片水平坐标
    imgRect.top = y #修改图片垂直坐标
    window.blit(imgSurface, imgRect) # 绘制图片


# 播放/停止背景音乐
pygame.mixer.music.load('其他\背景音.mp3') # 加载背景音乐
pygame.mixer.music.set_volume(0.4)  # 设置背景音乐音量（0~1）
pygame.mixer.music.play(-1)  # 循环播放背景音乐
    

# 玩家A释放的激光画面
def playAskillOne(i):   # i作为图片序号
        pAsOs = pygame.image.load('玩家A\A技能一\激光\激光'+str(i)+'.png')
        pAsOsRect = pAsOs.get_rect()
        if  playerA.direction == True:  # 玩家A向右
            pAsOsRect.left = playerA.x
            pAsOsRect.top = playerA.y 
        else:   # 玩家A向左
            pAsOs = pygame.transform.flip(pAsOs, True, False) # 图片水平镜像
            pAsOsRect.right = playerA.x
            pAsOsRect.top = playerA.y
        window.blit(pAsOs, pAsOsRect)


# 创建时钟
FPSclock = pygame.time.Clock() # 用于后面设置每秒帧数
        
        
while True:
    bgloadplay(window)  # 调用绘制背景图片函数
    zhutian(t, window)  # 调用“朱天”组件
    for event in pygame.event.get():    # 检测操作
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:
                chuchang(window, FPSclock, FPS) # 调用人物出场绘制函数
                gameb = True
                break
            if  event.key == K_m:
                global mus
                mus = not mus
                if mus == False:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1)
    t = t + 1 # 新局游戏第一帧
    pygame.display.flip()
    pygame.display.update()
    FPSclock.tick(FPS)
    if gameb == True: 
        break


# 游戏循环
while gameb:    # gameb为True时循环
    bgloadplay(window) # 绘制背景图
    toux(window)  # 绘制头像
    #bjtx(t)  # 绘制背景特效
    # 绘制人物A站立
    if playerA.body == 'stand' and playerA.atskill == 'not': # 人物A站立不攻击时
        loadimg('玩家A\A移动\m', 10, '.png', playerA.x, playerA.y, not playerA.direction)  
    if playerB.body == 'stand' and playerB.atskill == 'not': # 人物B站立不攻击时
        loadimg('玩家B\B普通攻击\图层 ', 10, '.png', playerB.x, playerB.y,not  playerB.direction)  
   
    # 操作检测和记录
    
    mus = shijianjiance() # 调用函数函数将检测操作，并返回一个bool值
    #print(mus)
    # 测试图片大小
    #loadimg('WPS图片-修改尺寸', 1, '.png', playerA.x, playerA.y-200, playerA.direction)
    #loadimg('玩家A\出场\组 ', 1, '.png', playerA.x, playerA.y, playerA.direction)
      
# （部分）算法区
    # A
    # 普通攻击（弹幕）发出判断
    if playerA.atskill == 'attck' and pAatt == 0:
    # 攻击键按下且普通攻击计帧器值为零时
        pAAtmentx.append(playerA.x)     # 给玩家A 弹幕水平列表添加元素
        pAAtmenty.append(playerA.y)     # 为玩家A 弹幕垂直列表添加元素
        if playerA.direction == False:      # False表示弹幕向左，True表示向右
            pAAtmentdi = False
        else:
            pAAtmentdi = True
        pAAtmentd.append(pAAtmentdi)    # 为玩家A弹幕方向列表添加元素
        pAAtmentTF.append(False)        # 为玩家A弹幕命中集合添加元素
    
    if len(pAAtmentx) >= 1:  
        # 弹幕移动计算
        for i in range(len(pAAtmentx) - 1, 0, -1):
            if pAAtmentd[i] == True:
                pAAtmentx[i] = pAAtmentx[i] + playerA.atspeed  
            else:
                pAAtmentx[i] = pAAtmentx[i] - playerA.atspeed            
        # 普通攻击命中/出界判断区
        # 检测命中
        for i in range(len(pAAtmentx) - 1, 0, -1):
            if ((playerB.x <= pAAtmentx[i] + pDWid <= playerB.x + pDWid) or playerB.x <= pAAtmentx[i] <= playerB.x + pDWid) and playerB.body != 'down':
                pAAtmentTF[i] = True
                loadsound('玩家B\B音效\被攻击', '.mp3', mus)
        # 弹幕移除区
        for i in range(len(pAAtmentx) - 1, 0, -1):
            if (pAAtmentx[i] <= 0 or pAAtmentx[i] >= Wid - pDWid or pAAtmentTF[i]):
            # 弹幕出界或者命中敌人
                if pAAtmentTF[i]:
                    playerB.HP = playerB.HP - playerA.attcktion
                    pAAtmentx.remove(pAAtmentx[i])
                    pAAtmenty.remove(pAAtmenty[i])
                    pAAtmentd.remove(pAAtmentd[i])
                    pAAtmentTF.remove(pAAtmentTF[i])
    # B
    # 普通攻击（弹幕）发出判断
    if playerB.atskill == 'attck' and pBatt == 0:
    # 攻击键按下且普通攻击计帧器值为零时
        pBAtmentx.append(playerB.x)     # 给玩家B 弹幕水平列表添加元素
        pBAtmenty.append(playerB.y)     # 为玩家B 弹幕垂直列表添加元素
        if playerB.direction == False:      # False表示弹幕向左，True表示向右
            pBAtmentdi = False
        else:
            pBAtmentdi = True
        pBAtmentd.append(pBAtmentdi)    # 为玩家A弹幕方向列表添加元素
        pBAtmentTF.append(False)        # 为玩家A弹幕命中集合添加元素                    
    if len(pBAtmentx) >= 1:  
        # 弹幕移动计算
        for i in range(len(pBAtmentx) - 1, 0, -1):
            if pBAtmentd[i] == True:
                pBAtmentx[i] = pBAtmentx[i] + playerB.atspeed  
            else:
                pBAtmentx[i] = pBAtmentx[i] - playerB.atspeed                    
        # 普通攻击命中/出界判断区
        # 检测命中            
        for i in range(len(pBAtmentx) - 1, 0, -1):
            if ((playerA.x <= pBAtmentx[i] + pDWid <= playerA.x + pDWid) or playerA.x <= pBAtmentx[i] <= playerA.x + pDWid) and playerA.body != 'down':
                pBAtmentTF[i] = True
                loadsound('玩家A\A音效\木大', '.mp3', mus) 
        # 弹幕移除区      
        for i in range(len(pBAtmentx) - 1, 0, -1):
            if (pBAtmentx[i] <= 0 or pBAtmentx[i] >= Wid - pDWid or pBAtmentTF[i]):
            # 弹幕出界或者命中敌人
                # 弹幕命中
                if pBAtmentTF[i]:
                    playerA.HP = playerA.HP - playerB.attcktion
                    pBAtmentx.remove(pBAtmentx[i])
                    pBAtmenty.remove(pBAtmenty[i])
                    pBAtmentd.remove(pBAtmentd[i])
                    pBAtmentTF.remove(pBAtmentTF[i])


    # 人物A行走
    if playerA.body == 'run' :
        if playerA.direction == False and playerA.x > -64:
            playerA.x = playerA.x - playerA.mvspeed    
        if playerA.direction == True and playerA.x < 1168:
            playerA.x = playerA.x + playerA.mvspeed
            
    # 人物B行走
    if playerB.body == 'run':
        if playerB.direction == False and playerB.x > -64:
            playerB.x = playerB.x - playerB.mvspeed    
        if playerB.direction == True and playerB.x < 1168:
            playerB.x = playerB.x + playerB.mvspeed
            
            
# 绘图区
    # 玩家A普通攻击
    if playerA.atskill == 'attck':
        # 1和16是玩家A普通攻击的起止编号
        pAatt = pAatt + 1        
        loadimg('玩家A\A普通攻击\图层 ', pAatt,'.png',playerA.x, playerA.y, not playerA.direction)
        loadsound('玩家A\A音效\欧拉a', '.mp3', mus)    
    if pAatt == 21:
        pAatt = 0
        playerA.atskill = "not"
        
    # 玩家B普通攻击
    if playerB.atskill == 'attck':
        # 1和16是玩家B普通攻击的起止编号 
        pBatt = pBatt + 1       
        loadimg('玩家B\B普通攻击\图层 ', pBatt,'.png', playerB.x, playerB.y, not playerB.direction)
        loadsound('玩家B\B音效\B普攻', '.mp3', mus)
    if pBatt == 17:
        pBatt = 0
        playerB.atskill = "not"
        
    # 玩家A下蹲
    if playerA.body == 'down':
        loadimg('玩家A\A下蹲\图层 ', t%11,'.png', playerA.x, playerA.y, not playerA.direction)

    # 玩家B下蹲
    if playerB.body == 'down':
        loadimg('玩家B\B蹲下\BD', t%22 + 1,'.png', playerB.x, playerB.y, playerB.direction)
        
    # 玩家A移动
    if playerA.body == 'run' and playerA.atskill == 'not':
        pAm = pAm + 1
        loadimg('玩家A\A移动\m', pAm, '.png', playerA.x, playerA.y, not playerA.direction)
        if pAm == 10:
            pAm = 0  
 
    # 玩家B移动
    if playerB.body == 'run' and playerB.atskill == 'not':
        loadimg('玩家B\B移动\图层 ', t%4, '.png', playerB.x, playerB.y-40, playerB.direction)
    

    # 绘制弹幕
    # 玩家A弹幕
    for i in range(1, len(pAAtmentx)):
        #pygame.draw.rect(window, (152, 85, 152),(pAAtmentx[i], pAAtmenty[i], pDWid, pDHgt))
        #print("弹幕", i,':',pAAtmentx[i])
        das = pygame.image.load('玩家A\A普通攻击\未标题-' + str(t % 3 + 1) + '.png')#用das接受弹幕
        dasr = das.get_rect()
        dasr.left = pAAtmentx[i]
        dasr.top = pAAtmenty[i] + 60
        window.blit(das, dasr)   
    # 玩家B弹幕
    for i in range(1, len(pBAtmentx)):
        #pygame.draw.rect(window, (152, 85, 152),(pAAtmentx[i], pAAtmenty[i], pDWid, pDHgt))
        #print("弹幕", i,':',pAAtmentx[i])
        das1 = pygame.image.load('玩家B\B普通攻击\B' + str(t % 3 + 1) + '.png')#用das接受弹幕
        dasr1 = das1.get_rect() 
        dasr1.left = pBAtmentx[i]
        dasr1.top = pBAtmenty[i] + 60
        window.blit(das1, dasr1)      
        
            
    # 玩家A释放一技能画面
    if playerA.atskill =='skill1':
        if pAsk1t == 1:
            # 计帧器为一说明是刚开始释放技能
            loadsound('玩家A\A音效\guipI', '.mp3', mus)
            playerA.S1CD = AS1CD # 技能一进入CD  
            playerA.MP = playerA.MP - AS1CDMP # 扣除能量
        loadimg('玩家A\A技能一\气波功\qb', pAsk1t, '.png', playerA.x, playerA.y - 60, not playerA.direction)
        if (playerA.direction == True and playerB.x >= playerA.x) or (playerA.direction == False and playerB.x <= playerA.x):
            playerB.HP = playerB.HP - Askill1ion
        playAskillOne(pAsk1t % 3)
        pAsk1t = pAsk1t + 1 # 计帧器加一，表示已播放一张
        if pAsk1t == 46:
            playerA.atskill = 'not' # 释放技能一状态结束
            pAsk1t = 1
            
    # 玩家A释放二技能画面
    if playerA.atskill == 'skill2':
        if pAsk2t == 1:
            loadsound('玩家A\A音效\飞雷神', '.mp3', mus)
            playerA.S2CD = AS2CD
            playerA.MP = playerA.MP - AS2CDMP
        if pAsk2t <= 5:
            loadimg('玩家A\A技能二\AS2-', pAsk2t, '.png', playerA.x, playerA.y, not playerA.direction)
        if 6 <= pAsk2t <= 18:
            if playerB.direction == True:
                loadimg('玩家A\A技能二\AS2-', pAsk2t, '.png', playerB.x - 90, playerB.y, playerB.direction)                
            if playerB.direction == False:
                loadimg('玩家A\A技能二\AS2-', pAsk2t, '.png', playerB.x - 90, playerB.y, playerB.direction)
            playerB.HP = playerB.HP - Askill2ion
        pAsk2t = pAsk2t + 1
        if pAsk2t == 19:
            pAsk2t = 1
            playerA.atskill = 'not'
    # B 技能一 
    if playerB.atskill =='skill1':      
        if pBsk1t == 1:
            # 计帧器为一说明是刚开始释放技能
            loadsound('玩家B\B音效\B2','.mp3', mus)
            playerB.S1CD = BS1CD # 技能一进入CD  
            playerB.MP = playerB.MP - BS1CDMP # 扣除能量
            playerB.mvspeed = 12 #角色人物移动速度
            playerB.attcktion = playerB.attcktion + BS1up
        pBsk1t = pBsk1t + 1
        if  pBsk1t < 47: #//todo 
            loadimg('玩家B\B技能二\图层 ', pBsk1t, '.png', playerB.x, playerB.y, playerB.direction) # up
        if pBsk1t == 47:
            playerB.mvspeed = 8 #角色人物移动速度
            playerB.attcktion = playerB.attcktion - BS1up
            playerB.atskill = 'not' # 释放技能一状态结束
            pBsk1t = 1
    #b技能2
    if playerB.atskill == 'skill2':
        if pBsk2t == 1:
            loadsound('玩家B\B音效\B2', '.mp3', mus)
            playerB.S2CD = BS2CD
            playerB.MP = playerB.MP - BS2CDMP
            playerA.mvspeed = playerA.mvspeed - mvs
            playerB.atspeed = playerB.atspeed + BS2
        pBsk2t = pBsk2t + 1 
        playerA.HP = playerA.HP - BS2SH 
        if  pBsk2t < 47: #//todo
            loadimg('玩家B\B技能二\图层 ', pBsk2t, '.png', playerB.x, playerB.y,  not playerA.direction) # 动作
            loadimg('玩家B\B技能二\道具', t%3 + 1, '.png', playerA.x, playerA.y+100, playerA.direction) # 道具 
        if pBsk2t == 47:
            playerA.mvspeed = playerA.mvspeed + mvs
            playerB.atspeed = playerB.atspeed - BS2
            pBsk2t = 1
            playerB.atskill = 'not'
            print("nnnn")

    # CD消减区
    playerA.S1CD = playerA.S1CD - 1.0 / FPS
    playerA.S2CD = playerA.S2CD - 1.0 / FPS
    playerB.S1CD = playerB.S1CD - 1.0 / FPS
    playerB.S2CD = playerB.S2CD - 1.0 / FPS
    
    # 检测刷新玩家A技能CD
    if playerA.S1CD <= 0:
        playerA.S1CD = 0 # 技能一CD归零
    if playerA.S2CD <= 0:
        playerA.S2CD = 0 # 技能二CD归零
    # 检测刷新玩家B技能CD
    if playerB.S1CD <= 0:
        playerB.S1CD = 0 # 技能一CD归零
    if playerB.S2CD <= 0:
        playerB.S2CD = 0 # 技能二CD归零
    # 恢复能量
    if playerA.MP <= 120:
        playerA.MP = playerA.MP + playerA.respeed
    if playerB.MP <= 120:
        playerB.MP = playerB.MP + playerB.respeed
    
               
    # 绘制提示条
    DrawAHP(window)
    DrawAMP(window)
    DrawBHP(window)
    DrawBMP(window)
    t = t + 1
    timer(t)
    
    # 游戏胜负判断
    if playerA.HP <= 0:
        t = 1 # 游戏帧数归一
        print(t)
        gameb = gameO(True, window, FPSclock, FPS) # 调用函数将绘制终局画面，并返回一个bool值
        if gameb == True: # 初始化playerA,playerB
            playerA.HP = 1000
            playerA.MP = 120
            playerA.S1CD = 0 #技能一CD
            playerA.S2CD = 0 #技能二CD
            playerA.atspeed = 25 #普通攻击速度
            playerA.attcktion = 50
            playerA.mvspeed = mvs #角色人物移动速度
            playerA.respeed = 1 #能量恢复速度
            playerA.body = 'stand' #身体状态，参数一共由stand,down,run三个，表示立、蹲
            playerA.direction = True
            #self.movel = False #是否向左
            #self.mover = True #是否向右
            playerA.atskill = 'not' #是否进行普攻释放技能，参数还有attck,skill1,skill2
            playerA.x = 0 # 角色水平坐标
            playerA.y = 400 #角色垂直坐标
            playerB.x = 1060
            playerB.y = 460
            playerB.direction = False
            playerB.HP = 1000
            playerB.MP = 120
            playerB.S1CD = 0 #技能一CD
            playerB.S2CD = 0 #技能二CD
            playerB.atspeed = 25 #普通攻击速度
            playerB.attcktion = 50
            playerB.mvspeed = mvs #角色人物移动速度
            playerB.respeed = 1 #能量恢复速度
            playerB.body = 'stand' #身体状态，参数一共由stand,down,run三个，表示立、蹲
            #self.movel = False #是否向左
            #self.mover = True #是否向右
            playerB.atskill = 'not' #是否进行普攻释放技能，参数还有attck,skill1,skill2
            chuchang(window, FPSclock, FPS)            
            
            chuchang(window, FPSclock, FPS)
    if playerB.HP <= 0:
        t = 1
        gameb = gameO(False, window, FPSclock, FPS)
        if gameb == True:
            playerA.HP = 1000
            playerA.MP = 120
            playerA.S1CD = 0 #技能一CD
            playerA.S2CD = 0 #技能二CD
            playerA.atspeed = 25 #普通攻击速度
            playerA.attcktion = 50
            playerA.mvspeed = mvs #角色人物移动速度
            playerA.respeed = 1 #能量恢复速度
            playerA.body = 'stand' #身体状态，参数一共由stand,down,run三个，表示立、蹲
            playerA.direction = True
            #self.movel = False #是否向左
            #self.mover = True #是否向右
            playerA.atskill = 'not' #是否进行普攻释放技能，参数还有attck,skill1,skill2
            playerA.x = 0 # 角色水平坐标
            playerA.y = 400 #角色垂直坐标
            playerB.x = 1060
            playerB.y = 460
            playerB.direction = False
            playerB.HP = 1000
            playerB.MP = 120
            playerB.S1CD = 0 #技能一CD
            playerB.S2CD = 0 #技能二CD
            playerB.atspeed = 25 #普通攻击速度
            playerB.attcktion = 50
            playerB.mvspeed = mvs #角色人物移动速度
            playerB.respeed = 1 #能量恢复速度
            playerB.body = 'stand' #身体状态，参数一共由stand,down,run三个，表示立、蹲
            #self.movel = False #是否向左
            #self.mover = True #是否向右
            playerB.atskill = 'not' #是否进行普攻释放技能，参数还有attck,skill1,skill2
            chuchang(window, FPSclock, FPS)
    
    
    # 刷新画面
    pygame.display.flip()
    pygame.display.update()
    FPSclock.tick(FPS)
