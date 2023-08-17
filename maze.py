from pygame import *
' ' 'Required classes' ' '

#parent class for sprites
class GameSprite(sprite.Sprite):
   #class constructor
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()

       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed

       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update(self):
       keys_pressed = key.get_pressed()
       if keys_pressed[K_UP] and self.rect.y >= 5:
           hero.rect.y -= self.speed
       if keys_pressed[K_DOWN] and self.rect.y <= win_height - self.rect.height:
           hero.rect.y += self.speed
       if keys_pressed[K_LEFT] and self.rect.x >= 5:
           hero.rect.x -= self.speed
       if keys_pressed[K_RIGHT] and self.rect.x <= win_width - self.rect.width:
           hero.rect.x += self.speed

class Enemy(GameSprite):
   def update(self):
       global direction
       if direction == "left":
           self.rect.x -= self.speed
       if direction == "right":
           self.rect.x += self.speed


       if self.rect.x <=500:
           direction = "right"
       if self.rect.x >= win_width - self.rect.width:
           direction = "left"

class Wall(sprite.Sprite):
   def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color = color
       self.image = Surface((wall_width, wall_height))
       self.image.fill(self.color)
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw_wall(self):
       self.color = self.color
       window.blit(self.image, (self.rect.x, self.rect.y))


w1 = Wall((87, 166, 61),100, 20, 450, 10)
w2 = Wall((87, 166, 61),100, 480, 350, 10)
w3 = Wall((87, 166, 61),100, 20, 10, 380)
w4 = Wall((87, 166, 61),200, 130, 10, 350)
w5 = Wall((87, 166, 61),450, 130, 10, 360)
w6 = Wall((87, 166, 61),300, 20, 10, 350)
w7 = Wall((87, 166, 61),390, 120, 130, 10)
walls = [w1, w2, w3, w4, w5, w6, w7]

font.init()
font = font.Font(None, 70)
loseText= font.render("You Lose", True, (255, 0 ,0))
winText= font.render("You Win", True, (255, 0 ,0))


#Game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Game characters:
hero = Player("hero.png", 25, 400, 5)
enemy = Enemy("hero.png",500, 250, 2)
treasure = GameSprite("treasure.png", 550, 400, 5)



game = True
clock = time.Clock()
FPS = 60
direction = 'left'

#music
mixer.init()
mixer.music.load('jungles.ogg')
#mixer.music.play()
finish = False
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
   if not finish:
       #DRAWING
       window.blit(background,(0, 0))
       hero.reset()
       enemy.reset()
       treasure.reset()
       for w in walls:
           w.draw_wall()
           if sprite.collide_rect(hero, w,  ):
               w.image.fill((255, 0, 0))
               finish = True
               window.blit(loseText, (200, 200))
               display.update()
               clock.tick(FPS)
           if sprite.collide_rect(hero, enemy,  ):
               w.image.fill((255, 0, 0))
               finish = True
               window.blit(loseText, (200, 200))
               display.update()
               clock.tick(FPS)
           if sprite.collide_rect(hero, treasure,  ):
               w.image.fill((255, 0, 0))
               finish = True
               window.blit(winText, (200, 200))
               display.update()
               clock.tick(FPS)
           else:
               w.image.fill((87, 166, 61))
       #METHODS
       hero.update()
       enemy.update()
       #Collision
       


   display.update()
   clock.tick(FPS)


