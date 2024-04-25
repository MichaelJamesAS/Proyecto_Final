import pygame
import os
import random

pygame.init()

# Constantes globales
Screen_height = 600
Screen_width = 1100
Screen = pygame.display.set_mode((Screen_width, Screen_width))

Running = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))] #Guarda las imagenes relacionadas con correr
Jumping = [pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))]
Ducking = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

Small_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
          pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
          pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
Large_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
          pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
          pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

Bird = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

cloud = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))]

BG = [pygame.image.load(os.path.join("Assets/Other", "Track.png"))]

class Dinosaur:
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    jump_vel = 0.5

    def __init__(self):
        self.duck_img = Ducking
        self.run_img = Running
        self.jump_img = Jumping

        self.dino_duck = False
        self.dino_run = True #Este es true debido a que cuando comienza el juego o justo antes de empezar el dinosaurio esta correindo
        self.dino_jump =  False

        self.step_index = 0
        self.jump_vel = self.jump_vel
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect() #rect viene de rectangulo
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, userInput): #se actualiza segun el input del usuario
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False 
            self.dino_jump =  True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False 
            self.dino_jump =  False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True 
            self.dino_jump =  False

    def duck(self):
        self.image = self.duck_img[self.step_index// 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck #igual que el run pero cambiando la posicion y por la posicion y en agachado
        self.step_index += 1 

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1 #del 1 al 5 seran un sprite, de 5 a 10 el otro, dando la isluion de que estan animados

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8 #se reduce la velocidad cuando salta
        if  self.jump_vel < - self.jump_vel:
            self.dino_jump = False

    def draw(self, Screen):
        Screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud: #Las nubes van pasando de derecha a izquierda
    def __init__(self):
            self.x = Screen_width + random.randint(800, 1000)
            self.y = random.randint(50, 100)
            self.image = cloud
            self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = Screen_width + random.randint (2500, 3000)
            self.y = random.randint(50,100)

    def draw(self, SCREEN):
        Screen.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = Screen_width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, Screen):
        Screen.blit(self.image[self.type], self.rect)
    
class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle): #Solo un tipo que es animado
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, Screen): #Diferente porque el pajaro es animado
        if self.index >= 9:
            self.index = 0
        Screen.blit(self.image[self.index//5], self.rect) #Las cinco primeras, primer esprite, despues el segunod, y se resetea al 10
    
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur() #Instancia de la classe Dinosaur
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score(): #Puntuacion del personaje
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        
        text = font.render("Points: " + str(points), True, (0,0,0)) #Display de los puntos en la pantalla
        textRect = text.get_rect()
        textRect.center = (1000,40)
        Screen.blit(text, textRect)
    
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        Screen.blit(BG, (x_pos_bg, y_pos_bg))
        Screen.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            Screen.blit (BG, image_width + x_pos_bg, y_pos_bg)
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run: #Cuando pulsamos la X de la ventana, acaba el loop de forma segura
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Screen.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        player.draw(Screen)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(SmallCactus(Small_cactus))
            if random.randint(0,2) == 1:
                obstacles.append(LargeCactus(Large_cactus))
            if random.randint(0,2) == 2:
                obstacles.append(Bird(Bird))

        for obstacle in obstacles:
            obstacle.draw(Screen)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(Screen)
        Cloud.update()

        score()
        
        clock.tick(30)
        pygame.display.update()
    

def menu(death_count): #Muestra la puntuacion al finalizar la partida y da la opcion de empezar una nueva
    global points
    run = True
    while run:
        Screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Pulsa cualquier Tecla para Empezar", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Pulsa cualquier Tecla para Empezar de Nuevo", True, (0, 0, 0))
            score = font.render("Tu puntuacion: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (Screen_width // 2, Screen_height // 2 + 50)
            Screen.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (Screen_width // 2, Screen_height // 2)
        Screen.blit(text, textRect)
        Screen.blit(Running[0], (Screen_width // 2 - 20, Screen_height // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get(): #Opcion segura para salir del juego
            if event.type == pygame.quit:
                run = False
            if event.type == pygame.keydown:
                main()


menu(death_count = 0)