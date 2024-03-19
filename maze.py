from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.set_volume(0.1)

money = mixer.Sound('money.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player (GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >          5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width -80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <=450:
            self.direction = 'right'
        if self.rect.x >= 620:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
       #  self.color_1 = color_1
       #  self.color_2 = color_2
       #  self.color_3 = color_3 
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.x = wall_y
    def draw_wall(self):
        window.blit(self.image, self.rect)
      



win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player = Player('hero.png', 5,420, 4)
monster = Enemy('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 590, 420, 0)
w1 = Wall(99,116,131,100,20,450,10)
w2 = Wall(138,106,131,70,480,300,5)
w3 = Wall(143,211,116,300,20,10,360)

mixer.init()
mixer.music.load('kick.ogg')
mixer.music.play()

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    if not finish:
        window.blit(background,(0, 0))
        player.reset()
        monster.reset()
        final.reset()
        player.update()
        monster.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish  = True
            window.blit(lose, (200,200))
            kick.play()


    display.update() 
    time.delay(20)











