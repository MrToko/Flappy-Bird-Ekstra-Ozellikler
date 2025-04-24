import sys

import pygame
import random
import time
from pygame.locals import *

pygame.init()


def ekrana_yaz(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

class Kus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f'bird{i}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.tiklandi_mi = False
        self.zipladimi = False
        self.ses = pygame.mixer.Sound("kanat.mp3")
        self.ses.set_volume(0.1)
    def update(self):

        if ucus == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if oyun_bitti == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.tiklandi_mi == False :
                self.tiklandi_mi = True
                self.vel  = -10
                self.ses.play()
            if pygame.mouse.get_pressed()[0] == 0:
                self.tiklandi_mi = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]and self.zipladimi == False:
                self.zipladimi = True
                self.vel  = -10
                self.ses.play()
            if not keys[pygame.K_SPACE]:
                self.zipladimi = False

            self.counter += 1
            flap_dusme = 5

            if self.counter > flap_dusme:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -4)
        else :
            self.image = pygame.transform.rotate(self.images[self.index], -80)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y,pozisyon):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()


        if pozisyon == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x,y -int(pipe_gap/2)]
        if pozisyon == -1:
            self.rect.topleft = [x, y+int(pipe_gap/2)]

    def update(self):
        self.rect.x -= hareket_hizi
        if self.rect.right < 0:
            self.kill()


class Kalkan(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('kalkan.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, ekran_genislik - 50)
        self.rect.y = random.randint(50, ekran_yukseklik - 250)
        if self.rect.y > ekran_yukseklik - 150:
            self.rect.y = ekran_yukseklik - 300

    def update(self):
        self.rect.x -= hareket_hizi
        if self.rect.right < 0:
            self.kill()

kalkan_group = pygame.sprite.Group()

def kalkan_olustur():
    while True:
        kalkan = Kalkan()
        if not pygame.sprite.spritecollideany(kalkan, pipe_group):
            kalkan_group.add(kalkan)
            break
class Altin_elma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('altın_elma.png')
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(50, ekran_genislik - 50)
        self.rect.y = random.randint(50, ekran_yukseklik - 250)
        if self.rect.y > ekran_yukseklik - 150:
            self.rect.y = ekran_yukseklik - 250


    def update(self):
        self.rect.x -= hareket_hizi
        if self.rect.right < 0:
            self.kill()


altin_elma_group = pygame.sprite.Group()

def elma_olustur():
    while True:
        elma = Altin_elma()
        if not pygame.sprite.spritecollideany(elma, pipe_group):
            altin_elma_group.add(elma)
            break

class Yatay_ok(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ok2.png')
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(50, ekran_genislik - 50)
        self.rect.y = random.randint(50, ekran_yukseklik - 250)
        if self.rect.y > ekran_yukseklik - 150:
            self.rect.y = ekran_yukseklik - 250


    def update(self):
        self.rect.x -= hareket_hizi
        if self.rect.right < 0:
            self.kill()

ok_group = pygame.sprite.Group()
def ok_olustur():
    while True:
        ok = Yatay_ok()
        if not pygame.sprite.spritecollideany(ok, pipe_group):

            ok_group.add(ok)
            break

class Simsek(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('simsek2.png')
        self.rect = self.image.get_rect()
        self.rect.x =random.randint(50, ekran_genislik - 50)
        self.rect.y = random.randint(50, ekran_yukseklik - 250)
        if self.rect.y > ekran_yukseklik - 150:
            self.rect.y = ekran_yukseklik - 250


    def update(self):
        self.rect.x -= hareket_hizi
        if self.rect.right < 0:
            self.kill()

simsek_group = pygame.sprite.Group()
def simsek_olustur():
    while True:
        simsek = Simsek()
        if not pygame.sprite.spritecollideany(simsek, pipe_group):
            simsek_group.add(simsek)
            break


class buton():
    def __init__(self, x, y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


clock = pygame.time.Clock()
fps = 60
ekran_genislik = 864
ekran_yukseklik = 936

font = pygame.font.SysFont('Bauhaus 93', 60)
font2 = pygame.font.SysFont('arial.ttf', 30)
white = (255, 255, 255)
black = (0, 0, 0)

bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Kus(100, int(ekran_genislik / 2))
bird_group.add(flappy)

def oyunu_yeniden_baslat():
    global fps
    global kalkan_aktif
    global simsek_aktif
    global pipe_frekans
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(ekran_yukseklik/2)
    score = 0
    fps = 60
    pipe_frekans = 1500
    kalkan_aktif = False
    simsek_aktif = False
    return score


screen = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
pygame.display.set_caption('Flippy Bird')

pygame.mixer.music.load("muzik.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
olum_sesi = pygame.mixer.Sound("ölüm.mp3")
olum_ses_calindi = False
bombasesi = pygame.mixer.Sound("bomba_sesi.mp3")
bombasesi.set_volume(0.1)

yer_hareketi = 0
hareket_hizi = 4
ucus = False
oyun_bitti = False

pipe_gap = 150
pipe_frekans = 2000
son_pipe = pygame.time.get_ticks() - pipe_frekans
pipe_gectimi = False

score= 0

simsek_frekans = random.randint(10000,20000)
simsek_olusturma_zamani = pygame.time.get_ticks()
simsek_aktif = False
simsek_hit_time = 0

ok_frekans = 30000000#random.randint(10000,20000)
ok_olustrma_zamani = pygame.time.get_ticks()
ok_baslangic_zamani = None
ok_gecerlilik_suresi = 5000

elma_frekans = random.randint(10000,20000)
elma_olusturma_zamani = pygame.time.get_ticks()

kalkan_frekans = random.randint(10000,20000)
kalkan_olusturma_zamani = pygame.time.get_ticks()
kalkan_koruma_suresi = 5000
kalkan_koruma_baslama_zamani = 0
kalkan_aktif = False


ekran_ust_kisim = pygame.image.load('bg.png')
ekran_alt_kisim = pygame.image.load('ground.png')
restart_butonu_resmi = pygame.image.load('restart.png')
restart_butonu = buton(ekran_genislik//2 -50 ,ekran_yukseklik//2-100,restart_butonu_resmi)



run = True

while run:


    calisiyor = True
    clock.tick(fps)

    screen.blit(ekran_ust_kisim, (0, 0))
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)

    screen.blit(ekran_alt_kisim, (yer_hareketi, 768))
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
            and pipe_gectimi == False:
            pipe_gectimi = True

        if pipe_gectimi == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pipe_gectimi = False


    for kalkan in kalkan_group:
        if pygame.sprite.collide_rect(kalkan, flappy):
            kalkan_aktif = True
            kalkan.kill()

    if kalkan_aktif:
        ekrana_yaz("Kalkan Aktif", font2, black, 0, 150)

    collided_pipes = pygame.sprite.spritecollide(flappy, pipe_group, False)
    if collided_pipes:
        if kalkan_aktif:
            collided_pipes[0].kill()
            kalkan_aktif = False
            bombasesi.play()


    for elma in altin_elma_group:
        if pygame.sprite.collide_rect(elma, flappy):
            score += 2
            elma.kill()

    for ok in ok_group:
        if pygame.sprite.collide_rect(ok, flappy):
            if ok_baslangic_zamani is None:
                ok_baslangic_zamani = pygame.time.get_ticks()
            current_ticks = pygame.time.get_ticks()
            if current_ticks - ok_baslangic_zamani < ok_gecerlilik_suresi:
                pipe_frekans = 3500
            else:
                pipe_frekans = 2000
                ok_baslangic_zamani = None
            ok.kill()
            break
    else:
        if ok_baslangic_zamani is not None:
            current_ticks = pygame.time.get_ticks()
            if current_ticks - ok_baslangic_zamani >= ok_gecerlilik_suresi:
                pipe_frekans = 2000
                ok_baslangic_zamani = None


    for simsek in simsek_group:

        if pygame.sprite.collide_rect(simsek, flappy):
            simsek_aktif = True
            simsek.kill()
            fps = 120
            simsek_hit_time = pygame.time.get_ticks()

        if simsek_hit_time != 0 and pygame.time.get_ticks() - simsek_hit_time >= 10000:
            fps = 60
            simsek_hit_time = 0
            simsek_aktif = False


    if simsek_aktif:
        ekrana_yaz("Ekstra Hız Aktif", font2, black, 0, 175)


    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        oyun_bitti = True
        if not olum_ses_calindi:
            olum_sesi.play()
            olum_ses_calindi = True

    if flappy.rect.bottom >= 768:
        oyun_bitti= True
        ucus = False
        if not olum_ses_calindi:
            olum_sesi.play()
            olum_ses_calindi = True

    ekrana_yaz("Skor :", font, white, 650, 20)
    ekrana_yaz(str(score),font,white,800,20)

    if oyun_bitti == False and ucus == True:

        if pygame.time.get_ticks() - elma_olusturma_zamani > elma_frekans:
            elma_olustur()
            elma_olusturma_zamani = pygame.time.get_ticks()

        if pygame.time.get_ticks() - kalkan_olusturma_zamani > kalkan_frekans:
            kalkan_olustur()
            kalkan_olusturma_zamani = pygame.time.get_ticks()

        if pygame.time.get_ticks() - simsek_olusturma_zamani > simsek_frekans:
            simsek_olustur()
            simsek_olusturma_zamani = pygame.time.get_ticks()

        if pygame.time.get_ticks() - ok_olustrma_zamani > ok_frekans:
            ok_olustur()
            ok_olustrma_zamani = pygame.time.get_ticks()

        time_now = pygame.time.get_ticks()
        if time_now - son_pipe > pipe_frekans:
            pipe_yukseklik = random.randint(-100, 100)
            btmpipe = Pipe(ekran_genislik, int(ekran_yukseklik / 2) + pipe_yukseklik, -1)
            toppipe = Pipe(ekran_genislik, int(ekran_yukseklik / 2) + pipe_yukseklik - 7 , 1)
            pipe_group.add(btmpipe)
            pipe_group.add(toppipe)
            son_pipe = time_now

        yer_hareketi -= hareket_hizi
        if abs(yer_hareketi) > 35:
            yer_hareketi = 0

        kalkan_group.update()
        kalkan_group.draw(screen)

        pipe_group.update()

        altin_elma_group.update()
        altin_elma_group.draw(screen)

        ok_group.update()
        ok_group.draw(screen)

        simsek_group.update()
        simsek_group.draw(screen)


    if oyun_bitti == True:
        if restart_butonu.draw() == True:
            oyun_bitti = False
            olum_ses_calindi = False
            score = oyunu_yeniden_baslat()


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
            calisiyor = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE and ucus == False and oyun_bitti == False:
                ucus = True
        if i.type == pygame.MOUSEBUTTONDOWN and  ucus == False and oyun_bitti == False:
            ucus = True
    pygame.display.update()

pygame.quit()