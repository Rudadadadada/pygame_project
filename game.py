import os
import pygame

screen = pygame.display.set_mode((773, 450))
clock = pygame.time.Clock()

'''Переменные для отключения кнопок'''
startmenu = True
game_run = True

'''Константы для Никиты'''
ruda_life = 3
ruda_dead = False
ruda_gothit = False
ruda_left = False
ruda_right = True
ruda_stay = True
ruda_sit = False
ruda_jump = False
ruda_side = 1
ruda_jump_count = 10
ruda_count_of_animation = 0
ruda_x, ruda_y = 150, 300
ruda_fireball_x, ruda_fireball_y = ruda_x, ruda_y

'''Константы для Севы'''
seva_life = 3
seva_dead = False
seva_gothit = False
seva_left = True
seva_right = False
seva_stay = True
seva_sit = False
seva_jump = False
seva_side = -1
seva_jump_count = 10
seva_count_of_animation = 0
seva_x, seva_y = 600, 300
seva_fireball_x, seva_fireball_y = seva_x, seva_y


'''Севин файербол'''


class SFireBall:
    def __init__(self, seva_fireball_x, seva_fireball_y, seva_side, seva_count_of_animation):
        self.x = seva_fireball_x
        self.y = seva_fireball_y
        self.speed = 5 * seva_side
        self.seva_count_of_animation = seva_count_of_animation

    def fire(self):
        if seva_side == 1:
            screen.blit(fireballRight[(self.seva_count_of_animation // 3) % 8], (seva_fireball_x, seva_fireball_y))
            self.seva_count_of_animation += 1
        else:
            screen.blit(fireballLeft[(self.seva_count_of_animation // 3) % 8], (seva_fireball_x, seva_fireball_y))
            self.seva_count_of_animation += 1


'''Никитин файербол'''


class RFireBall:
    def __init__(self, ruda_fireball_x, ruda_fireball_y, ruda_side, ruda_count_of_animation):
        self.x = ruda_fireball_x
        self.y = ruda_fireball_y
        self.speed = 5 * ruda_side
        self.ruda_count_of_animation = ruda_count_of_animation

    def fire(self):
        if ruda_side == 1:
            screen.blit(fireballRight[(self.ruda_count_of_animation // 3) % 8],
                        (ruda_fireball_x, ruda_fireball_y))
            self.ruda_count_of_animation += 1
        else:
            screen.blit(fireballLeft[(self.ruda_count_of_animation // 3) % 8],
                        (ruda_fireball_x, ruda_fireball_y))
            self.ruda_count_of_animation += 1


'''Здесь загружаю фоны'''


def load_image(name, colorkey=None):
    fullname = os.path.join('pictures', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


'''Загружаю анимацию для Севы'''

sevaGoRight = [pygame.image.load(f'pictures\\seva\\sevarun\\right\\srr{str(i)}.png')
               for i in range(1, 11)]

sevaGoLeft = [pygame.image.load(f'pictures\\seva\\sevarun\\left\\srl{str(i)}.png')
              for i in range(1, 11)]

sevaStayRight = [pygame.image.load(f'pictures\\seva\\sevastay\\right\\ssr{str(i)}.png')
                 for i in range(1, 6)]

sevaStayLeft = [pygame.image.load(f'pictures\\seva\\sevastay\\left\\ssl{str(i)}.png')
                for i in range(1, 6)]

sevaSitRight = [pygame.image.load(f'pictures\\seva\\sevasit\\right\\ssitr{str(i)}.png')
                for i in range(1, 5)]

sevaSitLeft = [pygame.image.load(f'pictures\\seva\\sevasit\\left\\ssitl{str(i)}.png')
               for i in range(1, 5)]

sevaJumpRight = [pygame.image.load(f'pictures\\seva\\sevajump\\right\\sjr{str(i)}.png')
                 for i in range(1, 8)]

sevaJumpLeft = [pygame.image.load(f'pictures\\seva\\sevajump\\left\\sjl{str(i)}.png')
                for i in range(1, 8)]

sevaGotHitRight = [pygame.image.load(f'pictures\\seva\\sevagothit\\right\\sghr{str(i)}.png')
                   for i in range(1, 7)]

sevaGotHitLeft = [pygame.image.load(f'pictures\\seva\\sevagothit\\left\\sghl{str(i)}.png')
                  for i in range(1, 7)]

sevaHealth = [pygame.image.load(f'pictures\\health\\rudahealth\\rh{str(i)}.png')
              for i in range(1, 5)]

'''Загружаю анимацию для Никиты'''

rudaGoRight = [pygame.image.load(f'pictures\\ruda\\rudarun\\right\\rrr{str(i)}.png')
               for i in range(1, 11)]

rudaGoLeft = [pygame.image.load(f'pictures\\ruda\\rudarun\\left\\rrl{str(i)}.png')
              for i in range(1, 11)]

rudaStayRight = [pygame.image.load(f'pictures\\ruda\\rudastay\\right\\rsr{str(i)}.png')
                 for i in range(1, 6)]

rudaStayLeft = [pygame.image.load(f'pictures\\ruda\\rudastay\\left\\rsl{str(i)}.png')
                for i in range(1, 6)]

rudaSitRight = [pygame.image.load(f'pictures\\ruda\\rudasit\\right\\rsitr{str(i)}.png')
                for i in range(1, 5)]

rudaSitLeft = [pygame.image.load(f'pictures\\ruda\\rudasit\\left\\rsitl{str(i)}.png')
               for i in range(1, 5)]

rudaJumpRight = [pygame.image.load(f'pictures\\ruda\\rudajump\\right\\rjr{str(i)}.png')
                 for i in range(1, 8)]

rudaJumpLeft = [pygame.image.load(f'pictures\\ruda\\rudajump\\left\\rjl{str(i)}.png')
                for i in range(1, 8)]

fireballRight = [pygame.image.load(f'pictures\\fireball\\right\\fr{str(i)}.png')
                 for i in range(1, 9)]

fireballLeft = [pygame.image.load(f'pictures\\fireball\\left\\fl{str(i)}.png')
                for i in range(1, 9)]

rudaGotHitRight = [pygame.image.load(f'pictures\\ruda\\rudagothit\\right\\rghr{str(i)}.png')
                   for i in range(1, 7)]

rudaGotHitLeft = [pygame.image.load(f'pictures\\ruda\\rudagothit\\left\\rghl{str(i)}.png')
                  for i in range(1, 7)]

rudaHealth = [pygame.image.load(f'pictures\\health\\rudahealth\\rh{str(i)}.png')
              for i in range(1, 5)]

'''Подгружаю музыку'''
run = True
pygame.mixer.init()

pygame.mixer.music.load('music\\4.ogg')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

'''Цикл для меню'''
while run:
    screen.blit(load_image('startmenufon.jpg'), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 590 <= x <= 750 and 75 <= y <= 120:
                startmenu = False
                run = False
            elif 590 <= x <= 750 and 130 <= y <= 175:
                exit(0)
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.mixer.music.pause()

'''Запускаю главную мелодию'''
if not startmenu:
    pygame.mixer.music.load('music\\1.ogg')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()


'''Здесь хранятся звуки'''
if not startmenu:
    sound_bruh = pygame.mixer.Sound('music\\2.ogg')
    sound_win = pygame.mixer.Sound('music\\3.ogg')

'''Загружаю фон'''
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("fon.png")
pygame.display.set_caption('Смертельная битва')
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
sprite.rect.x = 0
sprite.rect.y = 0

'''Здесь храню файерболы'''
Sfireballs = []
Rfireballs = []

running = True

'''Здесь рисую почти все анимации'''

if not startmenu:
    def draw():
        global seva_count_of_animation, ruda_count_of_animation
        all_sprites.draw(screen)
        all_sprites.update()

        '''Тут реализованы жизни'''
        screen.blit(sevaHealth[(seva_life - 1) % 4], (seva_x - 15, seva_y - 100))
        screen.blit(rudaHealth[(ruda_life - 1) % 4], (ruda_x - 15, ruda_y - 100))

        '''Тут утсанавливаю фпс для анимации'''
        if seva_count_of_animation + 1 >= 60:
            seva_count_of_animation = 0
        if ruda_count_of_animation + 1 >= 60:
            ruda_count_of_animation = 0

        '''Анимация Севы'''
        if seva_left and seva_stay:
            screen.blit(sevaStayLeft[(seva_count_of_animation // 3) % 5], (seva_x, seva_y))
            seva_count_of_animation += 1
        elif seva_right and seva_stay:
            screen.blit(sevaStayRight[(seva_count_of_animation // 3) % 5], (seva_x, seva_y))
            seva_count_of_animation += 1
        else:
            if seva_left and not seva_stay and not seva_sit and not seva_jump:
                screen.blit(sevaGoLeft[(seva_count_of_animation // 3) % 10], (seva_x, seva_y))
                seva_count_of_animation += 1
            elif seva_right and not seva_stay and not seva_sit and not seva_jump:
                screen.blit(sevaGoRight[(seva_count_of_animation // 3) % 10], (seva_x, seva_y))
                seva_count_of_animation += 1
            elif seva_left and not seva_stay and seva_sit and not seva_jump:
                screen.blit(sevaSitLeft[(seva_count_of_animation // 3) % 4], (seva_x, seva_y))
                seva_count_of_animation += 1
            elif seva_right and not seva_stay and seva_sit and not seva_jump:
                screen.blit(sevaSitRight[(seva_count_of_animation // 3) % 4], (seva_x, seva_y))
                seva_count_of_animation += 1
            elif seva_right and not seva_stay and not seva_sit and seva_jump:
                screen.blit(sevaJumpRight[(seva_count_of_animation // 3) % 7], (seva_x, seva_y))
                seva_count_of_animation += 1
            elif seva_left and not seva_stay and not seva_sit and seva_jump:
                screen.blit(sevaJumpLeft[(seva_count_of_animation // 3) % 7], (seva_x, seva_y))
                seva_count_of_animation += 1
        if seva_gothit and seva_right:
            screen.blit(sevaGotHitRight[(seva_count_of_animation // 3) % 3], (seva_x, seva_y))
            seva_count_of_animation += 1
        elif seva_gothit and seva_left:
            screen.blit(sevaGotHitLeft[(seva_count_of_animation // 3) % 3], (seva_x, seva_y))
            seva_count_of_animation += 1

        '''Анимация Никиты'''
        if ruda_left and ruda_stay:
            screen.blit(rudaStayLeft[(ruda_count_of_animation // 3) % 5], (ruda_x, ruda_y))
            ruda_count_of_animation += 1
        elif ruda_right and ruda_stay:
            screen.blit(rudaStayRight[(ruda_count_of_animation // 3) % 5], (ruda_x, ruda_y))
            ruda_count_of_animation += 1
        else:
            if ruda_left and not ruda_stay and not ruda_sit and not ruda_jump:
                screen.blit(rudaGoLeft[(ruda_count_of_animation // 3) % 10], (ruda_x, ruda_y))
                ruda_count_of_animation += 1
            elif ruda_right and not ruda_stay and not ruda_sit and not ruda_jump:
                screen.blit(rudaGoRight[(ruda_count_of_animation // 3) % 10], (ruda_x, ruda_y))
                ruda_count_of_animation += 1
            elif ruda_left and not ruda_stay and ruda_sit and not ruda_jump:
                screen.blit(rudaSitLeft[(ruda_count_of_animation // 3) % 4], (ruda_x, ruda_y))
                ruda_count_of_animation += 1
            elif ruda_right and not ruda_stay and ruda_sit and not ruda_jump:
                screen.blit(rudaSitRight[(ruda_count_of_animation // 3) % 4], (ruda_x, ruda_y))
                ruda_count_of_animation += 1
            elif ruda_right and not ruda_stay and not ruda_sit and ruda_jump:
                screen.blit(rudaJumpRight[(ruda_count_of_animation // 3) % 7], (ruda_x, ruda_y))
                ruda_count_of_animation += 1
            elif ruda_left and not ruda_stay and not ruda_sit and ruda_jump:
                screen.blit(rudaJumpLeft[(ruda_count_of_animation // 3) % 7], (ruda_x, ruda_y))
                ruda_count_of_animation += 1
        if ruda_gothit and ruda_right:
            screen.blit(rudaGotHitRight[(ruda_count_of_animation // 3) % 3], (ruda_x, ruda_y))
            ruda_count_of_animation += 1
        elif ruda_gothit and ruda_left:
            screen.blit(rudaGotHitLeft[(ruda_count_of_animation // 3) % 3], (ruda_x, ruda_y))
            ruda_count_of_animation += 1

        '''Тут происходит анимация файербола'''
        for fireball in Sfireballs:
            fireball.fire()
        for fireball in Rfireballs:
            fireball.fire()


    x = -773
    step = 4
    while running:
        seva_gothit = False
        ruda_gothit = False

        '''Если Никита или Сева умер'''
        if ruda_life == 0:
            game_run = False
            ruda_dead = True
            ruda_stay = False
            ruda_gothit = False
            ruda_sit = False
            ruda_jump = False
            ruda_right = False
            ruda_left = False
        elif seva_life == 0:
            game_run = False
            seva_dead = True
            seva_stay = False
            seva_gothit = False
            seva_sit = False
            seva_jump = False
            seva_right = False
            seva_left = False

        '''Тут реализовано столкновение файерболов'''
        if seva_fireball_x in [i for i in range(ruda_fireball_x - 10, ruda_fireball_x + 10)] or \
                ruda_fireball_x in [i for i in range(seva_fireball_x - 10, seva_fireball_x + 10)]:
            if ruda_fireball_y == seva_fireball_y:
                Sfireballs = []
                Rfireballs = []

        '''Если в Никиту или Севу прилетает файербол'''
        if seva_fireball_x in [i for i in range(ruda_x - 10, ruda_x + 10)]:
            if seva_fireball_y in [i for i in range(int(ruda_y) - 35, int(ruda_y) + 35)]:
                if not seva_x == ruda_x and Sfireballs:
                    sound_bruh.play()
                    ruda_life -= 1
                    ruda_stay = False
                    ruda_gothit = True
                    Sfireballs = []
                    seva_fireball_x = -100
        elif ruda_fireball_x in [i for i in range(seva_x - 10, seva_x + 10)]:
            if ruda_fireball_y in [i for i in range(int(seva_y) - 35, int(seva_y) + 35)]:
                if not ruda_x == seva_x and Rfireballs:
                    sound_bruh.play()
                    seva_life -= 1
                    seva_stay = False
                    seva_gothit = True
                    Rfireballs = []
                    ruda_fireball_x = -100
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                running = False

        '''Движение файербола'''
        for fireball in Sfireballs:
            if 773 > seva_fireball_x > 0:
                fireball.x += fireball.speed
                seva_fireball_x += fireball.speed
            else:
                Sfireballs = []
        for fireball in Rfireballs:
            if 773 > ruda_fireball_x > 0:
                fireball.x += fireball.speed
                ruda_fireball_x += fireball.speed
            else:
                Rfireballs = []
        keys = pygame.key.get_pressed()

        '''Движение игроков'''
        if game_run:
            if not seva_dead:

                '''Выстрел Севиного файербола'''
                if keys[pygame.K_RCTRL]:
                    if len(Sfireballs) == 1 and len(Rfireballs) == 0:
                        ruda_fireball_x = ruda_x
                        ruda_fireball_y = ruda_y
                    if len(Sfireballs) < 2:
                        if seva_right:
                            seva_side = 1
                            seva_fireball_x = seva_x + 20
                            if seva_sit:
                                seva_fireball_y = seva_y - 20
                            elif seva_jump:
                                seva_fireball_y = seva_y
                            else:
                                seva_fireball_y = seva_y - 35
                        else:
                            seva_side = -1
                            seva_fireball_x = seva_x - 20
                            if seva_sit:
                                seva_fireball_y = seva_y - 20
                            elif seva_jump:
                                seva_fireball_y = seva_y
                            else:
                                seva_fireball_y = seva_y - 35
                        Sfireballs.append(SFireBall(seva_fireball_x, seva_fireball_y,
                                                    seva_side, seva_count_of_animation))
                    all_sprites.update()
                if keys[pygame.K_LEFT]:
                    seva_y = 300
                    seva_jump_count = 10
                    seva_stay = False
                    seva_left = True
                    seva_right = False
                    seva_jump = False
                    if seva_x >= 0:
                        if not seva_jump and not seva_sit:
                            seva_x -= step
                        elif not seva_jump and seva_sit:
                            seva_x -= 1
                elif keys[pygame.K_RIGHT]:
                    seva_y = 300
                    seva_jump_count = 10
                    seva_stay = False
                    seva_left = False
                    seva_right = True
                    seva_jump = False
                    if seva_x <= 773 - 40:
                        if not seva_jump and not seva_sit:
                            seva_x += step
                        elif not seva_jump and seva_sit:
                            seva_x += 1
                elif keys[pygame.K_DOWN]:
                    seva_stay = False
                    seva_jump = False
                    seva_sit = True
                    if seva_left:
                        seva_left = True
                        seva_right = False
                    elif seva_right:
                        seva_left = False
                        seva_right = True
                elif keys[pygame.K_UP]:
                    seva_stay = False
                    seva_jump = True
                    seva_sit = False
                    if seva_left:
                        seva_left = True
                        seva_right = False
                    elif seva_right:
                        seva_left = False
                        seva_right = True
                    if seva_jump_count >= -10:
                        if seva_jump_count < 0:
                            seva_y += (seva_jump_count ** 2) / 2
                        else:
                            seva_y -= (seva_jump_count ** 2) / 2
                        seva_jump_count -= 1
                    else:
                        seva_jump_count = 10
                else:
                    seva_jump_count = 10
                    seva_y = 300
                    seva_stay = True
                    seva_jump = False
                    seva_sit = False
                    if seva_left:
                        seva_right = False
                        seva_left = True
                    elif seva_right:
                        seva_right = True
                        seva_left = False
            if not ruda_dead:

                '''Выстрел Никитиного файербола'''
                if keys[pygame.K_f]:
                    if len(Sfireballs) == 0 and len(Rfireballs) == 1:
                        seva_fireball_x = seva_x
                        seva_fireball_y = seva_y
                    if len(Rfireballs) < 2:
                        if ruda_right:
                            ruda_side = 1
                            ruda_fireball_x = ruda_x + 20
                            if ruda_sit:
                                ruda_fireball_y = ruda_y - 20
                            elif ruda_jump:
                                ruda_fireball_y = ruda_y
                            else:
                                ruda_fireball_y = ruda_y - 35
                        else:
                            ruda_side = -1
                            ruda_fireball_x = ruda_x - 20
                            if ruda_sit:
                                ruda_fireball_y = ruda_y - 20
                            elif ruda_jump:
                                ruda_fireball_y = ruda_y
                            else:
                                ruda_fireball_y = ruda_y - 35
                        Rfireballs.append(RFireBall(ruda_fireball_x, ruda_fireball_y,
                                                    ruda_side, ruda_count_of_animation))
                    all_sprites.update()
                if keys[pygame.K_a]:
                    ruda_y = 300
                    ruda_jump_count = 10
                    ruda_stay = False
                    ruda_left = True
                    ruda_right = False
                    ruda_jump = False
                    if ruda_x >= 0:
                        if not ruda_jump and not ruda_sit:
                            ruda_x -= step
                        elif not ruda_jump and ruda_sit:
                            ruda_x -= 1
                elif keys[pygame.K_d]:
                    ruda_y = 300
                    ruda_jump_count = 10
                    ruda_stay = False
                    ruda_left = False
                    ruda_right = True
                    ruda_jump = False
                    if ruda_x <= 773 - 40:
                        if not ruda_jump and not ruda_sit:
                            ruda_x += step
                        elif not ruda_jump and ruda_sit:
                            ruda_x += 1
                elif keys[pygame.K_s]:
                    ruda_stay = False
                    ruda_jump = False
                    ruda_sit = True
                    if ruda_left:
                        ruda_left = True
                        ruda_right = False
                    elif ruda_right:
                        ruda_left = False
                        ruda_right = True
                elif keys[pygame.K_w]:
                    ruda_stay = False
                    ruda_jump = True
                    ruda_sit = False
                    if ruda_left:
                        ruda_left = True
                        ruda_right = False
                    elif ruda_right:
                        ruda_left = False
                        ruda_right = True
                    if ruda_jump_count >= -10:
                        if ruda_jump_count < 0:
                            ruda_y += (ruda_jump_count ** 2) / 2
                        else:
                            ruda_y -= (ruda_jump_count ** 2) / 2
                        ruda_jump_count -= 1
                    else:
                        ruda_jump_count = 10
                else:
                    ruda_jump_count = 10
                    ruda_y = 300
                    ruda_stay = True
                    ruda_jump = False
                    ruda_sit = False
                    if ruda_left:
                        ruda_right = False
                        ruda_left = True
                    elif ruda_right:
                        ruda_right = True
                        ruda_left = False
        else:
            try:
                '''Загружаю фон победителя'''
                if ruda_life == 0:
                    image = load_image('seva.png')
                elif seva_life == 0:
                    image = load_image('nikita.png')
                if x < 0:
                    x += 5
                screen.blit(image, (x, 0))
                pygame.mixer.music.pause()
                sound_win.play()
                sound_win.set_volume(0.1)
            except:
                game_run = True
                ruda_dead = False
                ruda_life = 3
                seva_dead = False
                seva_life = 3
        if not ruda_dead and not seva_dead:

            '''Функция рисующая анимации'''
            draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()