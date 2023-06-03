
import pygame
import random
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load('Include/graphics/fighterJet/resources/bullets.jpg').convert_alpha()
        self.active = False

    def move(self):
        if self.active:
            self.y -= 3
        #when the status is active it will go upwards
        if self.y < 0:
            self.active = False
        #When the bullet flys outside the screen, the status is not active

    def restart(self):
        #restarts the position of the bullet
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width() / 2
        self.y = mouseY - self.image.get_height() / 2
        self.active = True

class Enemy:
    def restart(self):
        self.x = random.randint(50, 1500)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.3
        #position and speed of each reborn enemy plane
    def __init__(self):
        self.restart()
        self.image = pygame.image.load('Include/graphics/fighterJet/resources/enemy.png').convert_alpha()
        #initialize and load the enemy plane picture
    def move(self):
        if self.y < 800:
            #go down
            self.y += self.speed
        else:
            #restart
            self.restart()

score = 0

def checkHit(enemy, bullet):
    # determines collision of bullet and enemy,and make the enemy disappear
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()*1.1) and (
            bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()*0.6):
        enemy.restart()
        #initialize the enemy plane
        bullet.active = False
        #initialize the bullet
        return True
    return False

pygame.init()
screen = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption("Fighter Jet!")

background = pygame.image.load('Include/graphics/fighterJet/resources/background.jpg').convert()

plane = pygame.image.load('Include/graphics/fighterJet/resources/player.jpg').convert_alpha()
pygame.mixer.music.load('Include/graphics/fighterJet/resources/backgroundmusic.mp3')
pygame.mixer.music.play(loops=0, start=0.0)

bullets = []
#creates a list for the ammo
for i in range(5):
    #the total amount of ammo is 5 and once finished it will replenish 5 bullets
    bullets.append(Bullet())
count_b = len(bullets)
index_b = 0
#the index number of the bullet that will become active
interval_b = 0
#the interval between two bullets
enemy = Enemy()
enemies =[]
#create a list for the enemies
for i in range(5):
    enemies.append(Enemy())
#the total amount of enemy is 5 and once finished 5 will be replenished

while True:
    #the main while loop for the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.blit(background, (0, 0))
    interval_b -= 1
    #the interval of the firing speed is decreasing
    if interval_b < 0:
        bullets[index_b].restart()
        interval_b = 100
        #restart the interval time
        index_b = (index_b + 1) % count_b
        #the index of the bullet is decreasing
    for b in bullets:
        #check the status of each bullet
        if b.active:
            b.move()
            screen.blit(b.image, (b.x, b.y))
            #the bullet that is active will move and it will appear on the screen
    for b in bullets:
        if b.active:
            for e in enemies:
                if checkHit(e,b):
                    score += 100
            b.move()
            screen.blit(b.image, (b.x, b.y))
        #determine the collision between the bullet and the enemy plane
    for e in enemies:
        e.move()
        screen.blit(e.image,(e.x,e.y))
    enemy.move()
    screen.blit(enemy.image, (enemy.x, enemy.y))
    x,y = pygame.mouse.get_pos()
    #get the position of the mouse
    x-=plane.get_width()/2
    y-= plane.get_height()/2
    #get the position of the plane
    screen.blit(plane,(x,y))
    #put the plane on the screen
    font = pygame.font.Font(None, 60)
    text = font.render("Socre: %d" % score, 0, (255,255,0))
    screen.blit(text, (0, 0))
    #keep score
    pygame.display.update()
    #refresh the image
