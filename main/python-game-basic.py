import pygame
import random
import time
import math
from pygame import Vector2, Vector3, sprite
from pygame.locals import (
    K_UP, 
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
    K_s,
    K_w,
    K_d,
)
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((15,15))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center= (
                random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
                random.randint(0,SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(1,5)
        
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((255,255,99))
        self.rect = self.surf.get_rect(center= (100,40))
        #self.rect.move_ip(0.0, -1.0)
        self.t0 = time.time()
        #self.speed = 9,826*(time.time-self.t0)
    def collision_behave(self,sprite2):
        col = pygame.sprite.collide_rect(self, sprite2)
        if col == True:
            #if self.rect.left < coll.rect.right:
            #    self.rect.left = coll.rect.right
            #if self.rect.right > coll.rect.left and  coll.rect.right > self.rect.right:
            #    self.rect.right = coll.rect.left
            if self.rect.right >= sprite2.rect.left and self.rect.left < sprite2.rect.left:
                self.rect.right = sprite2.rect.left
            if self.rect.right >= sprite2.rect.left and self.rect.left < sprite2.rect.left and self.rect.top > sprite2.rect.top:
                self.rect.right = sprite2.rect.left
            if self.rect.left <= sprite2.rect.right and self.rect.right > sprite2.rect.right:
                self.rect.left = sprite2.rect.right
            if self.rect.top <= sprite2.rect.bottom and self.rect.bottom > sprite2.rect.bottom:
                self.rect.top = sprite2.rect.bottom
            if self.rect.bottom >= sprite2.rect.top and self.rect.top <= sprite2.rect.top:
                self.rect.bottom = sprite2.rect.top



    def update(self):
        col = pygame.sprite.collide_rect(self, ground)
        if col:
            self.t0 = time.time()
            self.collision_behave(player)

            self.collision_behave(ground)
        elif not col : 
            self.rect.move_ip(0,0.3*9.8266*(time.time()-self.t0)**2)
            if self.rect.bottom > SCREEN_HEIGHT:  
                self.rect.bottom = SCREEN_HEIGHT          
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super(Ground, self).__init__()
        self.surf = pygame.Surface((70,70))
        self.surf.fill((205,34,120))
        self.rect = self.surf.get_rect(center= (200,200))
class Bullet(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""
    
    def __init__(self, vector, player):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((10,10))
        self.surf.fill((255,255,99))
        self.rect = self.surf.get_rect(center= player)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        #self.player = player
    
    def update(self):
        #if pressed_keys(K_LEFT):
         #   newpos = self.calcnewpos(self.rect,-self.vector)
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos
        #self.collision_rigid()

    def collision_rigido(self,sprite2):
        col = pygame.sprite.collide_rect(self, sprite2)
        tt = True
        
        if col==True:
            if self.rect.right >= sprite2.rect.left and self.rect.left < sprite2.rect.left:
                self.rect.right = sprite2.rect.left
            if self.rect.right >= sprite2.rect.left and self.rect.left < sprite2.rect.left and self.rect.top > sprite2.rect.top:
                self.rect.right = sprite2.rect.left
            if self.rect.left <= sprite2.rect.right and self.rect.right > sprite2.rect.right:
                self.rect.left = sprite2.rect.right
            if self.rect.top <= sprite2.rect.bottom and self.rect.bottom > sprite2.rect.bottom:
                self.rect.top = sprite2.rect.bottom
            if self.rect.bottom >= sprite2.rect.top and self.rect.top <= sprite2.rect.top:
                self.rect.bottom = sprite2.rect.top

    
    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        self.v = 2
        #self.bull = Bullet((1,1),)
    def adjust_on_collision(self, collide):
        """
        Adjust player's position if colliding with a solid block.
        """
        if self.rect < collide.rect:
            self.rect = collide.rect-self.rect.size
        else:
            self.rect = collide.rect+collide.rect.size
    def collision_rigid(self,sprite2):
        col = pygame.sprite.collide_rect(self, sprite2)
        tt = True
        
        if col==True:
            if self.rect.right >= sprite2.rect.left and self.rect.left < sprite2.rect.left:
                self.rect.right = sprite2.rect.left
            if self.rect.right >= sprite2.rect.left and self.rect.left < sprite2.rect.left and self.rect.top > sprite2.rect.top:
                self.rect.right = sprite2.rect.left
            if self.rect.left <= sprite2.rect.right and self.rect.right > sprite2.rect.right:
                self.rect.left = sprite2.rect.right
            if self.rect.top <= sprite2.rect.bottom and self.rect.bottom > sprite2.rect.bottom:
                self.rect.top = sprite2.rect.bottom
            if self.rect.bottom >= sprite2.rect.top and self.rect.top <= sprite2.rect.top:
                self.rect.bottom = sprite2.rect.top
    
        #self.collision_rigid(ground,1)
        #self.collision_rigid(ground1)
        
        #if(vect != (1,1)):
         #   self.bull = Bullet(vect,(self.rect.centerx,self.rect.centery))
        
            #self.bull.collision_rigid()


    def update(self, pressed_keys):
        a = 2
        vect = (1,1)
        #player movement:
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -a*self.v)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, a*self.v)
        if pressed_keys[K_a]:
            self.rect.move_ip(-a*self.v, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(a*self.v, 0)
        #keep player on the screen
        if self.rect.left < 0 :
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        #Bullet handling and shooting
        if pressed_keys[K_RIGHT]:
            vect = (0,2)
        if pressed_keys[K_LEFT]:
           vect = (0,-2)
        if pressed_keys[K_UP]:
             vect = (-2,2)
        if pressed_keys[K_DOWN]:
             vect = (2,2)
        
        if(vect != (1,1)):
            self.bull = Bullet(vect,(self.rect.centerx,self.rect.centery))
            self.bull.collision_rigido(ground)

            just.add(self.bull)
            
ground = Ground()

player = Player()
ground1 = Ground()
ball = Ball()
enem = Enemy()
ground.rect.center = (100,200)
ground1.rect.center = (300,200)

enemies = pygame.sprite.Group()
just = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(ground,ground1,ball,)
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
running = True

while running:
    
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


            elif event.type == QUIT:
                running = False
            
 
    pressed_keys = pygame.key.get_pressed()
               
    all_sprites.update()
    player.update(pressed_keys)
    just.update()
    

    screen.fill((0,0,0))
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)
    for entity in just:
        screen.blit(entity.surf, entity.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if sprite.spritecollideany(player, all_sprites):
        player.surf.fill((32,250, 120))
        player.collision_rigid(ground)
        player.collision_rigid(ground1)
        ball.collision_behave(player)
    

        #player.collision_rigid(ground_group)


        #player.collision_rigid(ground1,0)

    screen.blit(player.surf, player.rect)
    pygame.display.flip()
pygame.quit()