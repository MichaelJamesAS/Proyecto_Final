import pygame
import os

pygame.init()

#Constantes globales
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

Clouds = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))]

BG = [pygame.image.load(os.path.join("Assets/Other", "Track.png"))]

class Dinosaur:
    x_pos = 80
    y_pos = 310

    def __init__(self):
        self.duck_img = Ducking
        self.run_img = Running
        self.jump_img = Jumping

        self.dino_duck = False
        self.dino_run = True #Este es true debido a que cuando comienza el juego o justo antes de empezar el dinosaurio esta correindo
        self.dino_jump =  False

        self.step_index = 0
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
        pass

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1 #del 1 al 5 seran un sprite, de 5 a 10 el otro, dando la isluion de que estan animados

    def jump(self):
        pass

    def draw(self, Screen):
        Screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur() #Instancia de la classe Dinosaur

    while run: #Cuando pulsamo la X de la ventana, acaba el loop de forma segura
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        Screen.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        player.draw(Screen)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()
    




main()