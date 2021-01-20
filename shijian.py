import pygame
import sys
from pygame.locals import *
from renwu import *
from canshu import *

global mus
def shijianjiance():
    print("shijian")
    for event in pygame.event.get():
    # 退出游戏检测
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()   
            # 静音/音效
            if  event.key == K_m:
                global mus
                #print(mus)
                mus = not mus
                if mus == False:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1)       
         
            # 检测玩家A操作
            # 移动检测          
            if event.key == K_a:
                playerA.body = 'run'
                playerA.direction = False       
            if event.key == K_d:
                print("d")
                playerA.body = 'run'
                playerA.direction = True
            if event.key == K_s:
                playerA.body = 'down'
                playerA.y = playerA.y + mul # mul为人物y坐标变化值
            # 攻击检测    
            if event.key == K_j:
                if pAatt == 0 and playerA.body != 'down':
                    playerA.atskill = 'attck'
            if event.key == K_u:
            # 许可释放玩家A一技能
                if (playerA.S1CD == 0 and playerA.MP >= AS1CDMP) and pAsk1t == 1 and playerA.body != 'down':
                    playerA.atskill = 'skill1'
            if event.key == K_i:
            # 许可玩家A释放二技能
                if (playerA.S2CD == 0 and playerA.MP >= AS2CDMP) and pAsk2t == 1 and playerA.body != 'down':
                    playerA.atskill = 'skill2'                                  
            # 对于人物B的事件检测                      
            if event.key == K_LEFT:
                playerB.body = 'run'
                playerB.direction = False   
            if event.key == K_RIGHT:
                playerB.body = 'run'
                playerB.direction = True
            if event.key == K_DOWN:
                playerB.body = 'down'
                playerB.y = playerB.y + mul
            # 攻击检测 
            if event.key == K_1:
                if pBatt == 0 and playerB.body != 'down':
                 playerB.atskill = 'attck'   
            if event.key == K_4:
            # 许可释放玩家B一技能
                if playerB.S1CD == 0 and playerB.MP >= BS1CDMP and playerB.body != 'down':
                    playerB.atskill = 'skill1'
            if event.key == K_5:
            # 许可玩家B释放二技能
                if playerB.S2CD == 0 and playerB.MP >= BS2CDMP and playerB.body != 'down':
                    playerB.atskill = 'skill2'
        if event.type == KEYUP:
            #if playerA.atskill == 'not':
            if event.key == K_a :
                    playerA.body = 'stand'
            if event.key == K_d :
                    playerA.body = 'stand'
            if event.key == K_LEFT :
                    playerB.body = 'stand'
            if event.key == K_RIGHT :
                    playerB.body = 'stand'                    
            if event.key == K_s:
                playerA.body = 'stand'
                playerA.y = playerA.y - mul 
            if event.key == K_DOWN:
                playerB.body = 'stand'
                playerB.y = playerB.y - mul

        # 控制台输出信息区
        if event.type == KEYDOWN:
            if event.key == K_v:
                #print('playerA.x: ', playerA.x)
                #print('playerB.x:', playerB.x)
                hhh = pygame.image.load('m1.png')
                hhhr = hhh.get_rect() 
                #print('playerAimg height:', hhhr.height)
    return mus