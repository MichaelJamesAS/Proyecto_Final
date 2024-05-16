import pygame
import os
import random
import sqlite3

base1 = sqlite3.connect('dino2')

punts = base1.cursor()

puntuacio_guardada = False

pygame.init()

# Nuestras constantes globales
ALTURA_PANTALLA = 600
ANCHURA_PANTALLA = 1100
PANTALLA = pygame.display.set_mode((ANCHURA_PANTALLA, ALTURA_PANTALLA))

# Guardamos las imagenes relacionadas con diferentes objetos y acciones del juego
CORRER = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
SALTAR = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
AGACHAR = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

CACTUS_P = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
CACTUS_G = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

VOLADOR = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

NUBE = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Dinosaurio:
    X_POS = 80
    Y_POS = 310
    Y_POS_AGACHADO = 340
    VEL_SALTO = 8.5

    def __init__(self):
        self.agachar_img = AGACHAR
        self.correr_img = CORRER
        self.saltar_img = SALTAR

        self.dino_agachar = False
        self.dino_correr = True # Este esta configurado com True porque, cuando comienza el juego o justo antes de empezar, el dinosaurio esta corriendo.
        self.dino_saltar = False

        self.step_index = 0
        self.vel_salto = self.VEL_SALTO
        self.image = self.correr_img[0]
        self.dino_rect = self.image.get_rect() # Rect se refiere a rectangulo
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput): # Se actualiza segun el input del usuario 
        if self.dino_agachar:
            self.agachar()
        if self.dino_correr:
            self.correr()        
        if self.dino_saltar:
            self.saltar()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_saltar: # Saltamos al pulsar la tecla hacia arriba
            self.dino_agachar = False
            self.dino_correr = False
            self.dino_saltar = True
        elif userInput[pygame.K_DOWN] and not self.dino_saltar: # Nos agachamos al pulsar la tecla hacia abajo
            self.dino_agachar = True
            self.dino_correr = False
            self.dino_saltar = False
        elif not (self.dino_saltar or userInput[pygame.K_DOWN]): # Nos mantenemos corriendo si no nos agachamos ni saltamos
            self.dino_agachar = False
            self.dino_correr = True
            self.dino_saltar = False

    def agachar(self):
        self.image = self.agachar_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_AGACHADO # Igual que el run, pero cambiando la posicion_y por la posicion_y_agachado
        self.step_index += 1

    def correr(self):
        self.image = self.correr_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1 # Del 1 al 5 seran un Sprite, de 5 a 10 el otro, dando la isluion de que el personaje esta animado

    def saltar(self):
        self.image = self.saltar_img
        if self.dino_saltar:
            self.dino_rect.y -= self.vel_salto * 4
            self.vel_salto -= 0.8 # Se reduce la velocidad cuando salta
        if self.vel_salto < - self.VEL_SALTO:
            self.dino_saltar = False
            self.vel_salto = self.VEL_SALTO

    def draw(self, PANTALLA):
        PANTALLA.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Nube:  # La clase se encarga de mover las nubes de derecha a izquierda
    def __init__(self):
        self.x = ANCHURA_PANTALLA + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = NUBE
        self.anchura = self.image.get_width()

    def update(self):
        self.x -= vel_juego
        if self.x < -self.anchura:
            self.x = ANCHURA_PANTALLA + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, PANTALLA):
        PANTALLA.blit(self.image, (self.x, self.y))

class Obstaculo: # La clase se encarga de definir los atributos de un obstaculo en general
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = ANCHURA_PANTALLA

    def update(self):
        self.rect.x -= vel_juego
        if self.rect.x < -self.rect.width:
            obstaculos.pop()

    def draw(self, PANTALLA):
        PANTALLA.blit(self.image[self.type], self.rect)


class PCactus(Obstaculo): # Definimos las qualidades de los cactus pequeños
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class GCactus(Obstaculo): # Definimos las qualidades de los cactus grandes
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Volador(Obstaculo): # Definimos las qualidades del objeto volador (Pterodactilo). 
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, PANTALLA): # Esta parte de aqui esta incluida porque el pajaro este animado
        if self.index >= 9:
            self.index = 0
        PANTALLA.blit(self.image[self.index//5], self.rect) # Los cinco primeros ticks,  aparece el primer esprite. Los otro cinco siguientes, el segundo sprite Se resetea al tick 10 (Onceavo tick)
        self.index += 1


def main():
    global vel_juego, x_pos_bg, y_pos_bg, puntos, obstaculos
    run = True
    reloj = pygame.time.Clock()
    jugador = Dinosaurio()  # Instancia de la classe Dinosaur
    nube = Nube() # Instancia de la classe Nube
    vel_juego = 20
    x_pos_bg = 0
    y_pos_bg = 380
    puntos = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstaculos = []
    cont_muertes = 0

    def puntuacion(): # Función que se encarga de la puntuacion del jugador
        global puntos, vel_juego
        puntos += 1
        if puntos % 100 == 0:
            vel_juego += 1

        texto = font.render("Puntos: " + str(puntos), True, (0, 0, 0)) # Parte de la funcion que nos muestra los puntos mientras jugamos
        textoRect = texto.get_rect()
        textoRect.center = (1000, 40)
        PANTALLA.blit(texto, textoRect)

    def background(): # Funcion que se encarga en el desplazamiento del fondo
        global x_pos_bg, y_pos_bg
        anchura_imagen = BG.get_width()
        PANTALLA.blit(BG, (x_pos_bg, y_pos_bg))
        PANTALLA.blit(BG, (anchura_imagen + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -anchura_imagen:
            PANTALLA.blit(BG, (anchura_imagen + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= vel_juego

    while run: # Cuando pulsamos la X de la ventana, acaba el loop de forma segura
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        PANTALLA.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        jugador.draw(PANTALLA)
        jugador.update(userInput)

        if len(obstaculos) == 0:
            if random.randint(0, 2) == 0:
                obstaculos.append(PCactus(CACTUS_P))
            elif random.randint(0, 2) == 1:
                obstaculos.append(GCactus(CACTUS_G))
            elif random.randint(0, 2) == 2:
                obstaculos.append(Volador(VOLADOR))

        for obstaculo in obstaculos: # Nos encargamos de no sobre saturar la pantalla con obstaculos. Nos aseguramos de que sea pasable.
            obstaculo.draw(PANTALLA)
            obstaculo.update()
            if jugador.dino_rect.colliderect(obstaculo.rect):
                pygame.time.delay(2000)
                cont_muertes += 1
                menu(cont_muertes)

        background()

        nube.draw(PANTALLA)
        nube.update()

        puntuacion()

        reloj.tick(30)
        pygame.display.update()

def guardar_puntuacio(puntos, nom):
    global puntuacio_guardada
    if puntuacio_guardada == False:
        punts.execute("insert into punts (nom, puntuacio) values (?, ?)", (nom, puntos))
        base1.commit()
        puntuacio_guardada = True

def menu(cont_muertes): # Muestra la puntuacion al finalizar la partida y da la opcion de empezar una nueva
    global puntos, puntuacio_guardada 
    run = True

    while run:
        PANTALLA.fill((255, 255, 255))
        font = pygame.font.Font(None, 30)

        if cont_muertes == 0:
            texto = font.render("Press any Key to Start", True, (0, 0, 0))

        elif cont_muertes > 0:        
            guardar_puntuacio(puntos, "test")            
            texto = font.render("Press any Key to Restart", True, (0, 0, 0))
            punto = font.render("Your Score: " + str(puntos), True, (0, 0, 0))
            puntoRect = punto.get_rect()
            puntoRect.center = (ANCHURA_PANTALLA // 2, ALTURA_PANTALLA // 2 + 50)
            PANTALLA.blit(punto, puntoRect)

        
        textoRect = texto.get_rect()
        textoRect.center = (ANCHURA_PANTALLA // 2, ALTURA_PANTALLA // 2)
        PANTALLA.blit(texto, textoRect)
        PANTALLA.blit(CORRER[0], (ANCHURA_PANTALLA // 2 - 20, ALTURA_PANTALLA // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get(): #Opcion segura para salir del juego
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
             
            if event.type == pygame.KEYDOWN:
                puntuacio_guardada = False
                main()



menu(cont_muertes=0)
