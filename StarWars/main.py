import pygame
import os
import time 
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 750
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("STARWARS")

#variable image
redSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
greenSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
blueSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
#variable player ship
yellowSpaceShip = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#variable lasers
redLaser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
greenLaser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
blueLaser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
yellowLaser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#variable background
BG =pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, heigth):
        return self.y < heigth and self.y >= 0

    def collision(self, obj):
        return collide(obj, self)

class Ship:
    def __init__(self, x, y, health = 100):
        self.x = x 
        self.y = y
        self.health = health
        self.ship_img = None
        self.leser_img = None
        self.lesers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

# /////
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = yellowSpaceShip
        self.leser_img = yellowLaser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

# /////
class Enemy(Ship):
    COLOR_MAP = {
                "red": (redSpaceShip, redLaser),
                "green": (greenSpaceShip, greenLaser),
                "blue": (blueSpaceShip, blueLaser)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

def collide(obj1, obj2):
    pass

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5

    player = Player(300, 650)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        # insert background
        win.blit(BG, (0, 0))

        # daraw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        
        win.blit(lives_label, (10, 10))
        win.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(win)

        player.draw(win)

        if lost:
            lost_label = lost_font.render("YOU LOST!!!", 1, (255, 255, 255))
            win.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Scroll button
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player_vel > 0:
            player.x -= player_vel
        
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
                
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0:
            player.y -= player_vel
                
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel
                
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

main()
