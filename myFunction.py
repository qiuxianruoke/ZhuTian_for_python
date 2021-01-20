import pygame,sys
from pygame.locals import*
from canshu import*
from renwu import*


# 绘制头像函数
def toux(window):   
    window.blit(txA, txARect)
    window.blit(txB, txBRect)


# 定义加载播放音效函数
def loadsound(str1, t='.mp3', mus=False):
    # str1为音频分类（如玩家A普攻），num为音频序号
    if mus == True:
        psound = pygame.mixer.Sound(str1 + t) # 加载音频
        psound.play() # 播放音乐


# 加载背景图
def bgloadplay(window): # window为要加载背景图的surface对象
    bgimg = pygame.image.load('其他\\bg.png') #加载图片
    bgRect = bgimg.get_rect()
    window.blit(bgimg, bgRect) # 绘制图片


# 背景特效
def bjtx(t, window):
    bgimg = pygame.image.load('其他\激光' + str(t % 3) + '.png')
    bgimgRect = bgimg.get_rect()
    bgimgRect.top = -100
    bgimgRect.left = -250
    window.blit(bgimg, bgimgRect)


# 游戏提示组件
# 绘制玩家HP提示
def DrawAHP(window): # 参数为玩家A的HP值*0.2
    if playerA.HP <= 0:
        pygame.draw.rect(window, colorHP, (50, 20, 0, 18))
    else:
        pygame.draw.rect(window, colorHP, (50, 20, playerA.HP*0.4, 18))


def DrawBHP(window): # 参数为玩家B的HP值*0.2
    if playerB.HP <= 0:
        pygame.draw.rect(window, colorHP, (50, 20, 0, 18))
    else:
        pygame.draw.rect(window, colorHP, ( Wid - Hwid - playerB.HP*0.4, 20, playerB.HP*0.4, 18))


# 绘制玩家MP提示条
def DrawAMP(window): # 参数为玩家A的'MP'值
    if playerA.MP <= 0:
        pygame.draw.rect(window, colorMP, (50, 44, 0, 6))
    else:
        pygame.draw.rect(window, colorMP, (50, 44, playerA.MP*2.8, 6))


def DrawBMP(window): # 参数为玩家B的'MP'值
    if playerB.MP <= 0:
        pygame.draw.rect(window, colorMP, (50, 44, 0, 6))
    else:
        pygame.draw.rect(window, colorMP, (Wid - Hwid - playerB.MP*2.8, 44, playerB.MP*2.8, 6))


# 游戏确认界面       
def zhutian(t, window):
    # 全局变量申明
    global sx
    global sy
    global dspeedx
    global dspeedy
    if sx < 0 or sx > Wid - ztwid: # sx超出x轴边界
        dspeedx = - dspeedx
    if sy < 0 or sy > Hgt - zthgt: # sx超出y轴边界
        dspeedy = - dspeedy
    sx = sx + dspeedx
    sy = sy + dspeedy
    sur = pygame.image.load('其他\朱天\未标题-' + str(t % 8 + 1) + '.png')
    surRect = sur.get_rect()
    surRect.top = sy
    surRect.left = sx
    surT = pygame.image.load('其他\朱天\提示-' + str(t % 3 + 1) + '.png')
    surTRect = surT.get_rect()  
    surTRect.top = 100
    surTRect.left = 0
    window.blit(sur, surRect) # 绘制移动的“朱天”
    window.blit(surT, surTRect) # 绘制提示文字
    
# 人物出场
def chuchang(window, FPSclock, FPS):
    for i in range(1, 36):
        bgloadplay(window)
        global t
        t = t + 1
        global mus
        if i == 1:
            loadsound('玩家A\A音效\出场', '.mp3', mus)
            #loadsound('玩家B\B音效\B出场', '.mp3', mus)
        if i <= 15:
            beginImgA = pygame.image.load('玩家A\出场\组 '+ str(i-1) + '.png')
            beginImgArect = beginImgA.get_rect()
            beginImgArect.top = playerA.y + 80
            beginImgArect.left = playerA.x
            window.blit(beginImgA, beginImgArect) # 绘制人物出场图
        else:
            beginImgA = pygame.image.load('玩家A\A移动\m10.png')
            beginImgArect = beginImgA.get_rect()
            beginImgA = pygame.transform.flip(beginImgA,True, False)
            beginImgArect.top = playerA.y
            beginImgArect.left = playerA.x
            window.blit(beginImgA, beginImgArect) # 绘制人物站立图
        if i <= 35:
            beginImgB = pygame.image.load('玩家B\B出场\图层 '+ str(i) + '.png')
            beginImgB = pygame.transform.flip(beginImgB, True,False)
            beginImgBrect = beginImgB.get_rect()
            beginImgBrect.top = playerB.y - 40
            beginImgBrect.left = playerB.x
            window.blit(beginImgB, beginImgBrect)
        pygame.display.flip()
        pygame.display.update()
        FPSclock.tick(FPS)
        
        
# 游戏结束
def gameO(bl, window, FPSclock, FPS):
    bgloadplay(window) # 绘制背景
    global t
    global mus
    global gameb
    t1 = t
    while True:  
        if bl == False:
            str1 = '其他\朱天\end-'
        else:
            str1 = '其他\朱天\endB-'
        sur = pygame.image.load(str1 + str(t1%3+1) + '.png')
        t1 = t1 + 1
        surrect = sur.get_rect()
        window.blit(sur, surrect)
        pygame.display.flip()
        pygame.display.update()
        FPSclock.tick(FPS)
        for event in pygame.event.get():
            print("for")  
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                    pygame.quit()
                if event.key == K_m:
                    mus = not mus
                    if mus == False:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)
                if event.key == K_SPACE:
                    toux(window)
                    return True
                    
            

                         