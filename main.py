import pygame
from random import randint


def attackm(k):
    '''

    :param k: int
    :return: massive with random x and y for attacks
    '''
    m = []
    for i in range(k):
        if randint(1, 2) == 1:
            m.append([0, randint(1, 150)])
        else:
            m.append([randint(1, 150), 0])
    return m

def musicsetter(bosshappyflags,bosssadflags):
    if bosshappyflags == 0 and bosssadflags == 0:
        pygame.mixer.music.load('Music/mus_menu0.ogg')
        pygame.mixer.music.play(-1)
    elif bosssadflags == 1:
        pygame.mixer.music.load('Music/mus_f_6s_1.ogg')
        pygame.mixer.music.play(-1)
    elif bosssadflags == 2:
        pygame.mixer.music.load('Music/mus_f_6s_2.ogg')
        pygame.mixer.music.play(-1)
    elif bosssadflags == 3:
        pygame.mixer.music.load('Music/mus_f_6s_3.ogg')
        pygame.mixer.music.play(-1)
    elif bosshappyflags == 1:
        pygame.mixer.music.load('Music/mus_menu1.ogg')
        pygame.mixer.music.play(-1)
    elif bosshappyflags == 2:
        pygame.mixer.music.load('Music/mus_menu2.ogg')
        pygame.mixer.music.play(-1)
    elif bosshappyflags == 3:
        pygame.mixer.music.load('Music/mus_menu3.ogg')
        pygame.mixer.music.play(-1)




def fpsset(playerslideflag,choosefase):
    '''
    :param playerslideflag: bool
    :param choosefase: bool
    :return: 10 if it is choosefase and playerslideflag is 1; 60 if it isn`t choosefase
    '''
    if playerslideflag == 1 and choosefase == 1:
        return 10
    elif choosefase == 0 and playerslideflag == 1:
        return 60
    elif (playerslideflag == 0 and choosefase == 0) or (choosefase == 1 and playerslideflag == 0):
        return 80
    else:
        return 'Wrong input'

def hp_decor(hp):
    '''
    :param hp:int
    :return: hp or 0(if hp is 0 or lower)
    '''
    if hp <= 0:
        return 0
    else:
        return hp

class Boss:
    def __init__(self, hp, anim, attacks, phrasesF, attack, act, actT, actF, actleft, actright, attack_speed, strength):
        '''

        :param hp: int hp amount
        :param anim: list with images for boss
        :param attacks: list with lists with two int for x and y realisation
        :param phrasesF: tuple with str prhases
        :param attack: image for boss attack
        :param act: list with lists containing bool to understand the right act to choose
        :param actT: list with boss answers for right act
        :param actF: list with boss answers for wrong act
        :param actleft: list with player acts displayed on the left
        :param actright: list with player acts displayed on the right
        :param attack_speed: int speed of base boss attack
        :param strength: int strength of boss attacks
        '''
        self.hp = hp
        self.anim = anim
        self.attacks = attacks
        self.phrasesF = phrasesF
        self.attack = attack
        self.actT = actT
        self.actF = actF
        self.act = act
        self.actleft = actleft
        self.actright = actright
        self.attack_speed = attack_speed
        self.strength = strength

# Параметры
FPS = 60
animk = 0
animn = 0
animkc = 20
boss1_flag = 0
boss2_flag = 0
boss3_flag = 0
direction = 0
screenx = 1000
screeny = 700
xbackground = 0
ybackground = 0
xboss1 = 100
yboss1 = 100
xboss2 = 200
yboss2 = 300
xboss3 = 500
yboss3 = 600
clock = pygame.time.Clock()
playerspeed = 1
playerspeedbase = playerspeed
px = 500
py = 500
fpx = 100
fpy = 620
playerhp = 100
boss1_defeated = 0
bosshappyflags = 0
bosssadflags = 0
bosshappyflags_check = 0
bosssadflags_check = 0
# атаки первого босса массивом массивов
boss1attacks = attackm(200)
boss2attacks = attackm(200)
boss3attacks = attackm(200)
boss2phrasesF = [ 'ARHGR', 'STOP IT', 'I`M GONNA BEAT YOU UP', 'DAMN IT']
boss2actT = ['You interferred me!', 'I was hammering nails', 'Yes? What is it?', 'OH THATS VERY GOOD']
boss2actF = ['APESTAS', '¿A QUIEN LLAMASTE PERRO?','I CAN READ MINDS','ARGH UN TONTO' ]
boss2actsleft = ['Why are you  mad?', 'Un perro ;D', 'I have something to calm down you', 'It`s a vinyl record of Linkin park']
boss2actsright = ['Tu es rojo como un tomate', 'From what?', '(Where did she even hammer them?)', 'Un sedante para perros xD']
boss2act = [[1, 0], [0, 1], [1, 0], [1, 0]]
boss3phrasesF = [ 'OoooOOoo', 'DoN`t BeAt mE', 'StOp iT', 'WoWowWo :(']
boss3actT = ['I am thirsty', 'It would be very nice', 'I see a bottle in your pocket', 'OH THATS VERY GOOD']
boss3actF = ['Seems like that', 'Que duro...','Oh no','Ohhh nooo...' ]
boss3actsleft = ['Hey, what`s wrong?', 'Flower don`t talk', 'So you need water...', 'Oh right,take it']
boss3actsright = ['A big talking flower?', 'Can I help you?', 'Maybe I should eat you', 'I`ll need it to wash you down >:)']
boss3act = [[1, 0], [0, 1], [1, 0], [1, 0]]
boss1phrasesF = ['Damn it...', 'Hey, why are you attacking me', 'Stop it','It isn`t cool.']
boss1actT = ['Yes, mate', 'My moustache are feeling bad', 'I need some moustache potion', 'Great, thank you!']
boss1actF = ['Bro, don`t bully me', 'You go away' ]
boss1actsleft = ['Want to talk?', 'Go away', 'Oh, I used to have great moustache', 'I have one, take it']
boss1actsright = ['You`re ugly', 'Something happened?', 'Your moustache are bad', 'So what?']
boss1act = [[1, 0], [0, 1], [1, 0], [1, 0]]
##########################Дисплей,картинки#####################################
pygame.init()
screen = pygame.display.set_mode((screenx, screeny))
# заданы размеры окна игры
pygame.display.set_caption("Underfight")
background_shirm = pygame.image.load('images/backgr.jpeg')
background = pygame.image.load('images/background.png')
icon = pygame.image.load('images/icon.jpg')
boss2attack = pygame.image.load('Sprites/Boss1/attack.png')
boss1attack = pygame.image.load('Sprites/Boss2/attack.png')
boss3attack = pygame.image.load('Sprites/Boss3/attack.png')
pygame.display.set_icon(icon)
#############################АНИМАЦИИ###############################################
pwalkup = [
    pygame.image.load('Sprites/PlayerAnimation/walkup1.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkup2.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkup3.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkup4.png'),
]
pwalkdown = [
    pygame.image.load('Sprites/PlayerAnimation/walkdown1.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkdown2.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkdown3.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkdown4.png'),
]
pwalkleft = [
    pygame.image.load('Sprites/PlayerAnimation/walkleft1.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkleft2.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkleft3.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkleft4.png'),
]
pwalkright = [
    pygame.image.load('Sprites/PlayerAnimation/walkright1.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkright2.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkright3.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkright4.png'),
]
pidle = [
    pygame.image.load('Sprites/PlayerAnimation/walkleftidle.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkrightidle.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkupidle.png'),
    pygame.image.load('Sprites/PlayerAnimation/walkdownidle.png')
]
boss2fight = [
    pygame.image.load('Sprites/Boss1/boss1sadbattle.png'),
    pygame.image.load('Sprites/Boss1/boss1happybattle.png'),
    pygame.image.load('Sprites/Boss1/boss1battledead.png')
]
boss2menu = [
    pygame.image.load('Sprites/Boss1/boss1sadstart.png'),
    pygame.image.load('Sprites/Boss1/boss1happystart.png'),
    pygame.image.load('Sprites/Boss1/boss1menudead.png')
]
boss1fight = [
    pygame.image.load('Sprites/Boss2/boss2sad.png'),
    pygame.image.load('Sprites/Boss2/boss2happy.png'),
    pygame.image.load('Sprites/Boss2/boss2dead.png')
    ]
boss1menu = [
    pygame.image.load('Sprites/Boss2/boss2sadmenu.png'),
    pygame.image.load('Sprites/Boss2/boss2happymenu.png'),
    pygame.image.load('Sprites/Boss2/boss2deadmenu.png')
    ]
boss3fight = [
    pygame.image.load('Sprites/Boss3/boss3sad.png'),
    pygame.image.load('Sprites/Boss3/boss3happy.png'),
    pygame.image.load('Sprites/Boss3/boss3dead.png')
    ]
boss3menu = [
    pygame.image.load('Sprites/Boss3/boss3sadmenu.png'),
    pygame.image.load('Sprites/Boss3/boss3happymenu.png'),
    pygame.image.load('Sprites/Boss3/boss3deadmenu.png')
    ]
# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

# Боссы
boss1 = Boss(100, boss1fight, boss1attacks, boss1phrasesF, boss1attack,
             boss1act, boss1actT, boss1actF, boss1actsleft,
             boss1actsright,2,10)
boss2 = Boss(150, boss2fight, boss2attacks, boss2phrasesF, boss2attack,
             boss2act, boss2actT, boss2actF, boss2actsleft,
             boss2actsright,3,15)
boss3 = Boss(200, boss3fight, boss3attacks, boss3phrasesF, boss3attack,
             boss3act, boss3actT, boss3actF, boss3actsleft,
             boss3actsright,4,20)
# Переменные

player = pwalkdown[0]
myfont = pygame.font.Font('fonts/KdamThmorPro-Regular.ttf', 20)
textsurface = myfont.render('Press E to start fight', True, 'white', 'black')


# временно^^^

def fight(
        boss, startplayerx=fpx, startplayery=fpy, xplayer=fpx, yplayer=fpy,
        myfont=myfont, px=px, py=py,
        bkgx=xbackground, bkgy=ybackground, FPS=FPS, screenx=screenx, screeny=screeny):
    '''

    :param boss: class
    :param startplayerx: int
    :param startplayery: int
    :param xplayer: int
    :param yplayer: int
    :param myfont: pygame.font
    :param px: int
    :param py: int
    :param bkgx: int
    :param bkgy: int
    :param FPS: int
    :param screenx: int
    :param screeny: int
    :return: 0,1 or 2 depending on how fight ends
    '''
    screen = pygame.display.set_mode((screenx, screeny))
    background = pygame.image.load('images/fightingbackground.png')
    battlewindow = pygame.image.load('images/battlewindow.webp')
    attackblackwindow = pygame.image.load('Sprites/Battle/attackblackwindow.png')
    fightingwindow = pygame.image.load('images/fightingwindow.jpg')
    attackimage = boss.attack
    fightingplayer = pygame.image.load('Sprites/Battle/fightingplayer.webp')

    # параметры
    battlefont = pygame.font.Font('Fonts/KdamThmorPro-Regular.ttf', 40)
    battlespeed = 3
    battle_going = True
    global running
    playerhp = 100
    playerslideflag = 0
    battlewindowx1 = 100
    battlewindowy1 = 400
    fightingwindowx = battlewindowx1 + 325
    fightingwindowy = battlewindowy1 + 25
    battlechoose = 0
    attacktry = 0
    actchoose = 0
    itemchoose = 0
    quitchoose = 0
    oncetp = 0
    bossflag = 0
    start_tp = 0
    choosefase = 1
    actchoose = 0
    battlefase = 1
    attacklinex = 0
    linespeed = 4
    # параметры босса
    bosshp = boss.hp
    bossanim = boss.anim
    bossattacks = boss.attacks
    attackcount = 0
    battlecount = 0
    attackmove = 0
    bossphrasesF = boss.phrasesF
    phrasechange = 0
    attackcooldown = 0
    attackcooldownk = 100
    _attackmovespeed = boss.attack_speed
    _boss_strength = boss.strength
    attackmovespeed = boss.attack_speed
    boss_strength = boss.strength
    rightact = boss.act
    actsum = 0
    actend = 0
    actsleft = boss.actleft
    actsright = boss.actright
    actT = boss.actT
    actF = boss.actF
    actcount = 0
    fightendcount = 0
    bosssay = battlefont.render(bossphrasesF[0], True, 'white')
    actfont = pygame.font.Font('Fonts/KdamThmorPro-Regular.ttf', 20)
    attacksk = 0
    while battle_going:
        playerhp = hp_decor(playerhp)
        bosshp = hp_decor(bosshp)
        pressed = pygame.key.get_pressed()

        # дошел ли  игрок до начальной позиции или нет
        if px == xplayer and py == yplayer:
            playerslideflag = 1

        FPS = fpsset(playerslideflag,choosefase)

        # хитбоксы

        battlebutton = pygame.draw.line(background, 'blue', (xplayer, yplayer + 14), (xplayer + 180, yplayer + 14), 40)
        actbutton = pygame.draw.line(background, 'blue', (xplayer + 200, yplayer + 14), (xplayer + 380, yplayer + 14),
                                     40)
        itembutton = pygame.draw.line(background, 'blue', (xplayer + 400, yplayer + 14), (xplayer + 580, yplayer + 14),
                                      40)
        quitbutton = pygame.draw.line(background, 'blue', (xplayer + 600, yplayer + 14), (xplayer + 800, yplayer + 14),
                                      40)
        # продолжить

        if playerslideflag == 0:
            px = (px // 10) * 10
            py = (py // 10) * 10
            if px < xplayer:
                px += 10
            if px > xplayer:
                px -= 10
            if py < yplayer:
                py += 10
            if py > yplayer:
                py -= 10

        # атака босса правильным нажатием
        if battlechoose == 1 and choosefase == 0 and attacktry == 0:
            blackbackground = pygame.draw.line(attackblackwindow, 'black', (0, 90), (600, 90), 190)
            redline = pygame.draw.line(attackblackwindow, 'red', (300, 20), (300, 160), 20)
            orangeline1 = pygame.draw.line(attackblackwindow, 'orange', (275, 30), (275, 150), 30)
            orangeline2 = pygame.draw.line(attackblackwindow, 'orange', (325, 30), (325, 150), 30)
            yellowline1 = pygame.draw.line(attackblackwindow, 'yellow', (240, 40), (240, 140), 40)
            yellowline2 = pygame.draw.line(attackblackwindow, 'yellow', (360, 40), (360, 140), 40)
            greenline1 = pygame.draw.line(attackblackwindow, 'green', (195, 50), (195, 130), 50)
            greenline2 = pygame.draw.line(attackblackwindow, 'green', (405, 50), (405, 130), 50)
            whiteline1 = pygame.draw.line(attackblackwindow, 'white', (135, 60), (135, 120), 70)
            whiteline2 = pygame.draw.line(attackblackwindow, 'white', (465, 60), (465, 120), 70)
            attackline = pygame.draw.line(attackblackwindow, (135, 0, 0), (attacklinex, 0), (attacklinex, 200), 3)
            attacklinex += linespeed
            if attackline.colliderect(blackbackground):
                if attackline.colliderect(whiteline1) and pressed[pygame.K_SPACE]:
                    bosshp -= 5
                    attacktry = 1
                elif attackline.colliderect(greenline1) and pressed[pygame.K_SPACE]:
                    bosshp -= 10
                    attacktry = 1
                elif attackline.colliderect(yellowline1) and pressed[pygame.K_SPACE]:
                    bosshp -= 15
                    attacktry = 1
                elif attackline.colliderect(orangeline1) and pressed[pygame.K_SPACE]:
                    bosshp -= 20
                    attacktry = 1
                elif attackline.colliderect(redline) and pressed[pygame.K_SPACE]:
                    bosshp -= 25
                    attacktry = 1
                elif attackline.colliderect(orangeline2) and pressed[pygame.K_SPACE]:
                    bosshp -= 20
                    attacktry = 1
                elif attackline.colliderect(yellowline2) and pressed[pygame.K_SPACE]:
                    bosshp -= 15
                    attacktry = 1
                elif attackline.colliderect(greenline2) and pressed[pygame.K_SPACE]:
                    bosshp -= 10
                    attacktry = 1
                elif attackline.colliderect(whiteline2) and pressed[pygame.K_SPACE]:
                    bosshp -= 5
                    attacktry = 1
            else:
                bosshp -= 1
                attacktry = 1
        if bosshp <= 0:
            bossflag = 2
            bosssay = battlefont.render('...',True,'white')
            fightendcount += 1
            if fightendcount < 3:
                pygame.mixer.music.load('Music/mus_f_saved.ogg')
                pygame.mixer.music.play()
            if fightendcount > 300:
                return 2

        if actcount == 4:
            bossflag = 1
            fightendcount += 1
            px = startplayerx
            py = startplayery
            if fightendcount > 400:
                return 1




        # дальше написать чтобы при нажатии на пробел сносилось определенное кол-во хп в завис от прямоуг

        # выбран бой
        # здесь же дописать действия к разговору, ведь после разговора тоже идет бой
        if (battlechoose == 1 and choosefase == 0 and attacktry == 1 and bosshp > 0) or\
                (actchoose == 1 and choosefase == 0 and actend == 1 and actcount < 4):
            # разная скорость атак для боя и разговора
            if battlechoose == 1 and choosefase == 0 and attacktry == 1:
                attackmovespeed = _attackmovespeed + 2
                boss_strength = _boss_strength + 5
                attacksk = 20 * battlefase
            elif actchoose == 1 and choosefase == 0 and actend == 1:
                attackmovespeed = _attackmovespeed
                boss_strength = _boss_strength
                attacksk = 10 * battlefase
            attackcooldown += 1
            fightingwindowhitbox = pygame.draw.line(background, (66, 68, 90, 0),
                                                    (fightingwindowx, fightingwindowy + 75),
                                                    (fightingwindowx + 150, fightingwindowy + 75), 150)
            playerhitbox = pygame.draw.circle(background, 'black', (px + 13, py + 13), 14)

            battlecount += 1
            if oncetp == 0:
                px = 500
                py = 500
                oncetp = 1
            if pressed[pygame.K_LEFT] and px > fightingwindowx:
                px -= battlespeed
            if pressed[pygame.K_RIGHT] and px < fightingwindowx + 125:
                px += battlespeed
            if pressed[pygame.K_DOWN] and py < fightingwindowy + 125:
                py += battlespeed
            if pressed[pygame.K_UP] and py > fightingwindowy:
                py -= battlespeed
            if attackcount < attacksk:
                fightingwindow.fill('black')
                if bossattacks[attackcount][1] != 0 and bossattacks[attackcount][0] == 0:
                    attackhitbox = pygame.draw.line(screen, 'white', (
                        fightingwindowx + attackmove, fightingwindowy + boss1attacks[attackcount][1]),
                                                    (fightingwindowx + attackmove,
                                                     fightingwindowy + bossattacks[attackcount][1] + 5), 15)
                    fightingwindow.blit(attackimage, (attackmove, bossattacks[attackcount][1]))

                    if attackhitbox.colliderect(fightingwindowhitbox):
                        attackmove += attackmovespeed
                    else:
                        attackcount += 1
                        attackmove = 0
                    if attackhitbox.colliderect(playerhitbox) and attackcooldown > attackcooldownk:
                        attackcooldown = 0
                        playerhp -= boss_strength
                elif bossattacks[attackcount][0] != 0 and bossattacks[attackcount][1] == 0:
                    attackhitbox = pygame.draw.line(screen, 'white', (
                        fightingwindowx + bossattacks[attackcount][0], fightingwindowy - 5 + attackmove),
                                                    (fightingwindowx + bossattacks[attackcount][0] + 5,
                                                     fightingwindowy - 5 + attackmove), 15)

                    fightingwindow.blit(attackimage, (bossattacks[attackcount][0], attackmove), )

                    if attackhitbox.colliderect(fightingwindowhitbox):
                        attackmove += attackmovespeed
                    else:
                        attackcount += 1
                        attackmove = 0
                    if attackhitbox.colliderect(playerhitbox) and attackcooldown > attackcooldownk:
                        attackcooldown = 0
                        playerhp -= boss_strength

            # выход из боя совершается после завершения фазы
            else:
                choosefase = 1
                start_tp = 0
                oncetp = 0
                battlefase += 1
                attacktry = 0
                attacklinex = 0
                battlechoose = 0
                actchoose = 0
                actend = 0
                # прописано на будущее
            # завершение боя кнопкой для теста
            #admin button
            if pressed[pygame.K_l]:
                choosefase = 1
                start_tp = 0
                oncetp = 0
                battlefase += 1
                attacktry = 0
                attacklinex = 0
                battlechoose = 0
                actchoose = 0
                actend = 0

        # прописываю кнопку разговора
        # в конце по сути бой так или иначе будет продолжаться
        # но можно сделать атаки слабее
        if actchoose == 1 and choosefase == 0 and actend == 0 and actcount < len(rightact):
            if oncetp == 0:
                px = 300
                py = 550
                oncetp = 1
            if pressed[pygame.K_RIGHT] and px < 700:
                px += 400
            if pressed[pygame.K_LEFT] and px > 300:
                px -= 400
            if px == 300 and pressed[pygame.K_e]:
                actsum += rightact[actcount][0]
                actend = 1
                oncetp = 0
                if rightact[actcount][0] == 1:
                    attackmovespeed = 2
                    if actcount <= len(actT):
                        bosssay = battlefont.render(actT[actcount], True, 'white')
                    else:
                        bosssay = battlefont.render(actT[-1], True, 'white')
                    actcount += 1
                else:
                    attackmovespeed = 4
                    if actcount <= len(actF):
                        bosssay = battlefont.render(actF[actcount], True, 'white')
                    else:
                        bosssay = battlefont.render(actF[-1], True, 'white')

            if px == 700 and pressed[pygame.K_e]:
                actsum += rightact[actcount][1]
                actend = 1
                oncetp = 0
                if rightact[actcount][1] == 1:
                    attackmovespeed = 2
                    if actcount <= len(actT):
                        bosssay = battlefont.render(actT[actcount], True, 'white')
                    else:
                        bosssay = battlefont.render(actT[-1], True, 'white')
                    actcount += 1
                else:
                    attackmovespeed = 4
                    if battlefase <= len(actF):
                        bosssay = battlefont.render(actF[actcount], True, 'white')
                    else:
                        bosssay = battlefont.render(actF[-1], True, 'white')
        elif actchoose == 1 and choosefase == 0 and actend == 0:
            bosssay = battlefont.render('It`s too late to try to fix something', True, 'white')
            actend = 1

        if choosefase == 1 and playerslideflag == 1:
            playerhitbox = pygame.draw.circle(background, 'white', (px + 13, py + 10), 18)
            battlebutton = pygame.draw.line(background, 'blue', (xplayer, yplayer + 14), (xplayer + 180, yplayer + 14),
                                            40)
            actbutton = pygame.draw.line(background, 'blue', (xplayer + 200, yplayer + 14),
                                         (xplayer + 380, yplayer + 14),
                                         40)
            itembutton = pygame.draw.line(background, 'blue', (xplayer + 400, yplayer + 14),
                                          (xplayer + 580, yplayer + 14),
                                          40)
            quitbutton = pygame.draw.line(background, 'blue', (xplayer + 600, yplayer + 14),
                                          (xplayer + 800, yplayer + 14),
                                          40)
            if start_tp == 0:
                px = startplayerx
                py = startplayery
                start_tp = 1

            if pressed[pygame.K_LEFT] and px > 100:
                px -= 200

            if pressed[pygame.K_RIGHT] and px < 600:
                px += 200

            # Прописываем все кнопки
            if pygame.Rect.colliderect(playerhitbox, battlebutton) and pressed[pygame.K_e]:
                battlechoose = 1
                choosefase = 0
            if pygame.Rect.colliderect(playerhitbox, actbutton) and pressed[pygame.K_e]:
                actchoose = 1
                choosefase = 0
            '''if pygame.Rect.colliderect(playerhitbox,itembutton) and pressed[pygame.K_e]:
                itemchoose = 1
                choosefase = 0'''
            if pygame.Rect.colliderect(playerhitbox, quitbutton) and pressed[pygame.K_e]:
                # тут будет какой-то текст перед тем, как герой убежит но пока резкое окончание боя
                battle_going = 0
                choosefase = 0

        # battle_going приравнять к нулю когда бой прошел все фазы, если босс убит, менять картинку, если нет,
        if playerhp<=0:
            return 0

        # выбор фразы
        if choosefase == 0:
            if battlechoose == 1:
                if battlefase < len(bossphrasesF):
                    bosssay = battlefont.render(bossphrasesF[battlefase], True, 'white')
                else:
                    bosssay = battlefont.render(bossphrasesF[-1], True, 'white')
        screen.blit(background, (bkgx, bkgy))  # фон

        # текстуры
        screen.blit(battlewindow, (battlewindowx1, battlewindowy1))  # окно боя
        if (battlechoose == 1 and choosefase == 0 and attacktry == 1) or (choosefase == 0 and actend == 1):
            screen.blit(fightingwindow, (fightingwindowx, fightingwindowy))
        if battlechoose == 1 and choosefase == 0 and attacktry == 0 and actcount < 4:
            screen.blit(attackblackwindow, (battlewindowx1 + 100, battlewindowy1 + 10))
        if choosefase == 1 or actcount == 4:
            screen.blit(bosssay, (400, 100))
        if actchoose == 1 and actend == 0 and actcount < len(rightact):
            actleft = actfont.render(actsleft[actcount], True, 'white')
            actright = actfont.render(actsright[actcount], True, 'white')
            screen.blit(actleft, (200, 500))
            screen.blit(actright, (600, 500))

        #admin buttons
        if pressed[pygame.K_z] and pressed[pygame.K_b]:
            bosshp -= 10
        if pressed[pygame.K_z] and pressed[pygame.K_p]:
            playerhp -= 10

        screen.blit(fightingplayer, (px, py))
        # тексты на кнопках:
        screen.blit((myfont.render('BATTLE', True, 'white')), (xplayer + 30, yplayer))
        screen.blit((myfont.render('ACT', True, 'white')), (xplayer + 230, yplayer))
        screen.blit((myfont.render('ITEM', True, 'white')), (xplayer + 430, yplayer))
        screen.blit((myfont.render('FLEE', True, 'white')), (xplayer + 630, yplayer))
        screen.blit(bossanim[bossflag], (400, 200))
        # хп босса и игрока
        screen.blit((myfont.render('BOSS HP', True, 'Purple')), (100, 200))
        screen.blit((myfont.render(str(bosshp), True, 'Purple')), (100, 230))
        screen.blit((myfont.render('PLAYER HP', True, 'Red')), (100, 300))
        screen.blit((myfont.render(str(playerhp), True, 'Red')), (100, 330))
        pygame.display.update()
        # обновление дисплея происходит предпоследним этапом
        clock.tick(FPS)
        for event in pygame.event.get():
            # event проходит по возможным событиям
            if event.type == pygame.QUIT:
                battle_going = False
                running = False


###############################^^^^^ПОДПРОГРАММА НА БОИ^^^^^################################################################


running = True
pygame.mixer.music.load('Music/mus_menu0.ogg')
pygame.mixer.music.play(-1, fade_ms=3)
while running:
    # пока запущена
    player_rect = pygame.Rect(px, py, 30, 50)

    boss1_rect = pygame.Rect(xboss1, yboss1, 40, 40)

    boss2_rect = pygame.Rect(xboss2,yboss2,40,40)

    boss3_rect = pygame.Rect(xboss3,yboss3,40,40)

    pressed = pygame.key.get_pressed()

    if animk >= animkc:
        animk = 0
        if animn < 3:
            animn += 1
        else:
            animn = 0
    else:
        animk += 1

    if pressed[pygame.K_LSHIFT]:
        playerspeed = 4
        animkc = 10
    else:
        playerspeed = playerspeedbase
        animkc = 20
    if pressed[pygame.K_LEFT] and px > 0:
        px -= playerspeed
        player = pwalkleft[animn]
        direction = 0

    if pressed[pygame.K_RIGHT] and px < screenx:
        px += playerspeed
        player = pwalkright[animn]
        direction = 1

    if pressed[pygame.K_UP] and py > 0:
        py -= playerspeed
        player = pwalkup[animn]
        direction = 2

    if pressed[pygame.K_DOWN] and py < screeny:
        py += playerspeed
        player = pwalkdown[animn]
        direction = 3
    if pressed[pygame.K_LEFT] == 0 and pressed[pygame.K_RIGHT] == 0 and pressed[pygame.K_UP] == 0 and pressed[
        pygame.K_DOWN] == 0:
        player = pidle[direction]

    if boss1_flag == None:
        boss1_flag = 0


    pygame.draw.rect(background_shirm, 'white', boss1_rect)

    pygame.draw.rect(background_shirm, 'red', player_rect)
    # Сверху хитбоксы

    screen.blit(background, (xbackground, ybackground))
    screen.blit(boss1menu[boss1_flag], (xboss1, yboss1))
    screen.blit(boss2menu[boss2_flag],(xboss2,yboss2))
    screen.blit(boss3menu[boss3_flag], (xboss3, yboss3))
    screen.blit(player, (px, py))

    #проверка, чтобы музыка не менялась постоянно
    if bosshappyflags!=bosshappyflags_check or bosssadflags!=bosssadflags_check:
        musicsetter(bosshappyflags,bosssadflags)

    bosshappyflags_check = bosshappyflags
    bosssadflags_check = bosssadflags



    if player_rect.colliderect(boss1_rect) == 1 and boss1_flag == 0:
        pressetextx = 30
        pressetexty = 10
        screen.blit(textsurface, (pressetextx, pressetexty))
        if pressed[pygame.K_e]:
            pygame.mixer.music.load('Music/mus_amalgam.ogg')
            pygame.mixer.music.play(-1)
            boss1_flag = fight(boss1)
            if boss1_flag == 2:
                bosssadflags += 1
            elif boss1_flag == 1:
                bosshappyflags += 1
            else:
                boss1_flag = 0
                pygame.mixer.music.load('Music/mus_menu0.ogg')
                pygame.mixer.music.play(-1)
    elif player_rect.colliderect(boss1_rect) == 1 and boss1_flag == 1:
        screen.blit((myfont.render('Hey!',True,'Gray')),(xboss1 + 40,yboss1 - 10))


    if player_rect.colliderect(boss2_rect) == 1 and boss2_flag == 0 and boss1_flag != 0:
        pressetextx = 30
        pressetexty = 10
        screen.blit(textsurface, (pressetextx, pressetexty))
        if pressed[pygame.K_e]:
            pygame.mixer.music.load('Music/mus_amalgam.ogg')
            pygame.mixer.music.play(-1)
            boss2_flag = fight(boss2)
            if boss2_flag == 2:
                bosssadflags += 1
            elif boss2_flag == 1:
                bosshappyflags += 1
            else:
                boss2_flag = 0
                pygame.mixer.music.load('Music/mus_menu0.ogg')
                pygame.mixer.music.play(-1)
    elif player_rect.colliderect(boss2_rect) == 1 and boss2_flag == 1:
        screen.blit((myfont.render('THAT RECORD IS FIRE!!!',True,'Gray')),(xboss2 + 40,yboss2 - 10))

    if player_rect.colliderect(boss3_rect) == 1 and boss3_flag == 0 and boss1_flag != 0 and boss2_flag != 0:
        pressetextx = 30
        pressetexty = 10
        screen.blit(textsurface, (pressetextx, pressetexty))
        if pressed[pygame.K_e]:
            pygame.mixer.music.load('Music/mus_amalgam.ogg')
            pygame.mixer.music.play(-1)
            boss3_flag = fight(boss3)
            if boss3_flag == 2:
                bosssadflags += 1
            elif boss3_flag == 1:
                bosshappyflags += 1
            else:
                boss3_flag = 0
                pygame.mixer.music.load('Music/mus_menu0.ogg')
                pygame.mixer.music.play(-1)
    elif player_rect.colliderect(boss3_rect) == 1 and boss3_flag == 1:
        screen.blit((myfont.render('That water was good!',True,'Gray')),(xboss3 + 40,yboss3 - 10))


    #admin buttons
    if pressed[pygame.K_z] and pressed[pygame.K_1]:
        boss1_flag = 1
        bosshappyflags = 1
        bosssadflags = 0
    if pressed[pygame.K_z] and pressed[pygame.K_2]:
        boss2_flag = 1
        bosshappyflags = 2
        bosssadflags = 0
    if pressed[pygame.K_z] and pressed[pygame.K_3]:
        boss3_flag = 1
        bosshappyflags = 3
        bosssadflags = 0
    # для грустных флажков проверка необзательна, т.к музыка при убийстве итак в приоритете
    if pressed[pygame.K_x] and pressed[pygame.K_1]:
        boss1_flag = 2
        bosssadflags = 1
    if pressed[pygame.K_x] and pressed[pygame.K_2]:
        boss2_flag = 2
        bosssadflags = 2
    if pressed[pygame.K_x] and pressed[pygame.K_3]:
        boss3_flag = 2
        bosssadflags = 3
    if pressed[pygame.K_z] and pressed[pygame.K_x] and pressed[pygame.K_r]:
        boss1_flag=0
        boss2_flag=0
        boss3_flag=0
        bosssadflags=0
        bosshappyflags=0




    ######################## КОНЕЦ КОДА НЕ ЛЕЗЬ ###################################################
    pygame.display.update()
    # обновление дисплея происходит предпоследним этапом
    clock.tick(FPS)

    for event in pygame.event.get():
        # event проходит по возможным событиям
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            running = False
            # Чтобы цикл закончился и не возвращалась ошибка
            pygame.quit()
    # в последнюю очередь проверяется выход из игры
