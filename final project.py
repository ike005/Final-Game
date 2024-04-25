# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:19:09 2024

@author: chibuike
"""
"""
 Asteroid sound - https://opengameart.org/content/bombexplosion8bit
Bullet sound - https://opengameart.org/content/space-shoot-sounds
Intro background - https://opengameart.org/content/space-backgrounds-3
The space ships, asteroids, game background and bullet - https://opengameart.org/content/space-shooter-art
"""

import pygame, simpleGE, random

class Player(simpleGE.Sprite):
    """ player is stationary,
        at the center left of the screen
    """ 
    
    def __init__(self, scene):
        super().__init__(scene)
        #self.setImage("player.png")
        self.images = {
            "cruise": pygame.image.load("player.png"),
            "left":   pygame.image.load("player.png"),
            "right":  pygame.image.load("player.png"),
            "thrust": pygame.image.load("player.png")}
        self.copyImage(self.images["cruise"])
        #self.setSize(70,50)
        #self.imageAngle = 270
        self.position = (150,240)
        self.moveSpeed = 6
        
        
    def process(self):
           
        self.copyImage(self.images["cruise"])
        if self.isKeyPressed(pygame.K_LEFT):
            self.imageAngle += 5
            if self.left > 0:
                self.x -= 5
          
        if self.isKeyPressed(pygame.K_RIGHT):
            #self.addForce(.2, self.imageAngle)
            self.imageAngle -= 5
            if self.right < self.screenWidth:
                self.copyImage(self.images["left"])
                self.x += 5
               
        if self.isKeyPressed(pygame.K_UP):
            if self.y > 0:
                self.y -= self.moveSpeed
           
        if self.isKeyPressed(pygame.K_DOWN):
            #self.addForce(.2, self.imageAngle)
            if self.y < self.screenHeight:
                self.copyImage(self.images["thrust"])
                self.y += self.moveSpeed
    
class Astroid(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("meteorBig.png")
        self.setSize(98,50)
        self.position = (500,240)
        self.minSpeed = 1
        self.maxSpeed = 4
        self.dx -= random.randint(self.minSpeed, self.maxSpeed)
        self.reset()
    def reset(self):
        self.x = 600
        self.y = random.randint(100,429)
        self.dx - random.randint(self.minSpeed, self.maxSpeed)
        self.CONTINUE
    def checkBounds(self):
        if -self.right > self.screenWidth:
            self.reset()
            
class SMastroid(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("meteorSmall.png")
        self.setSize(80,50)
        self.position = (500,240)
        self.minSpeed = 2
        self.maxSpeed = 6
        self.dx -= random.randint(self.minSpeed, self.maxSpeed)
        self.reset()
    def reset(self):
        self.x = 500
        self.y = random.randint(100,420)
        self.dx - random.randint(self.minSpeed, self.maxSpeed)
        self.CONTINUE
    def checkBounds(self):
        if -self.right > self.screenWidth:
            self.reset()
            
class EnemyA(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("enemyShip.png")
        #self.setSize(70,50)
        self.position = (-20,240)
        self.imageAngle = 270
        self.minSpeed = 3           
        self.maxSpeed = 6
        self.dx -= random.randint(self.minSpeed, self.maxSpeed)
    def process(self):
        randNUM = random.randint(1, 30)
        if randNUM <= 5:
            self.scene.bullet2.fire()
        
    def reset(self):
        self.x = 500
        self.y = random.randint(100,420)
        self.dx - random.randint(self.minSpeed, self.maxSpeed)
        self.CONTINUE
    def checkBounds(self):  
        if -self.right > self.screenWidth:
            self.reset()
   
class EnemyB(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("enemyUFO.png")
        self.setSize(50,50)
        self.position = (320,460)
        self.minSpeed = 1         
        self.maxSpeed = 2
        self.dx = random.randint(self.minSpeed, self.maxSpeed)
        self.imageAngle = -180
        self.dx = -self.dx
        self.setBoundAction(self.BOUNCE)
 
        
class Bullet(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("laserGreen.png")
        self.imageAngle = -90
        self.setSize(26,9)
        #self.colorRect("white", (5, 5))
        self.setBoundAction(self.HIDE)
        self.hide()

    def process(self):
        if self.collidesWith(self.scene.enemyA):
           self.scene.enemyA.reset()
           #self.score -= 2
           #self.lblScore.text = f"Score: {self.score}"
        if self.collidesWith(self.scene.bigAstroid):
           self.scene.bigAstroid.reset()
        if self.collidesWith(self.scene.smallAstroid):
           self.scene.smallAstroid.reset()

    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.imageAngle = self.parent.imageAngle
            self.speed = 50
     
    def reset(self):
        self.hide()
            
        
            
class Bullet1(simpleGE.Sprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("laserRed.png")
        self.setSize(9,26)
        #self.colorRect("white", (10, 5))
        self.setBoundAction(self.HIDE)
        self.hide()

    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
            self.moveAngle = self.parent.imageAngle-90
            self.imageAngle = self.parent.imageAngle
            self.speed = 20
            
    def reset(self):
        self.hide()
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time: 20"
        self.center = (120,100)
        
class LblDurability(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "HP: 0"
        self.center = (500,100)
     

class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        
        self.prevScore = score
        
        self.setImage("Background-3.png")
        self.response = "Quit"
                                                 
        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [ 
        "Space Wars", "Your a space warrior", "Try and survive the wave of enemy ships"]
       
        
        self.directions.center = (320, 200)
        self.directions.size = (400, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100,400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540,400)
        
        #self.lblScore = simpleGE.Label()
        #self.lblScore.text = "Last score: 0"
        #self.lblScore.center = (320,400)

        #self.lblScore.text = f"Last score: {self.prevScore}"
        
        
        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
            
            
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
        
        
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("starBackground.png")
        self.sndBullet = simpleGE.Sound("alienshoot1.wav")
        self.sndAstroid = simpleGE.Sound("bombSound.wav")
        self.player = Player(self)
        self.bigAstroid = Astroid(self)
        self.smallAstroid = SMastroid(self)
        self.enemyA = EnemyA(self)
        self.enemyb = EnemyB(self)
        self.bullets = Bullet(self, self.player)
        self.bullet1 = Bullet1(self, self.enemyb)
        self.bullet2 = Bullet1(self, self.enemyA)
        self.NUM_BULLETS = 10
        self.currentBullet = 0
        self.bullet = []
        self.enemya = []
        self.bigastroid = []
        self.smallastroid = []
        
        self.hp = 100
        self.lblHp = LblDurability()
        
        #self.score = 0
        # self.lblScore = LblScore()
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 30
        self.lblTime = LblTime()
        
        
        
        for enemy in range(4):
            self.enemya.append(self.enemyA)
            self.enemya.append(self.bullet2)
            
        for astroid in range(2):
            self.bigastroid.append(self.bigAstroid)
            
        for astroid in range(4):
            self.smallastroid.append(self.smallAstroid)
        
        
        for i in range(self.NUM_BULLETS):
            self.bullet.append(Bullet(self, self.player))
            
            
        self.sprites = [
            self.player, self.enemya, self.enemyb, self.bullet, self.bullet1,
            self.bigastroid, self.smallastroid, self.lblHp, self.lblTime]
        

        if self.player.x <= 40:
            self.player.x = 35
        if self.player.x >= 600:
            self.player.x = 600
        if self.player.y <= 43:
            self.player.y = 43
        if self.player.y >= 450:
            self.player.y = 450
        
    def process(self):
        self.bullet1.fire()
        if self.hp <= 0:
            if self.timer == 0:
                self.stop()
        if self.bullet1.collidesWith(self.player):
           self.sndBullet.play()
           self.bullet1.reset()
           self.hp -= 5 
           self.lblHp.text = f"HP: {self.hp:.2f}"
           #self.score -= 5
        elif self.bullet2.collidesWith(self.player):
           self.sndBullet.play()
           self.bullet2.reset()
           self.hp -= 5
        elif self.player.collidesWith(self.bigAstroid):
           self.sndAstroid.play()
           self.bigAstroid.reset()
           self.hp -= 2  
           self.lblHp.text = f"Score: {self.hp:.2f}"
          
        elif self.player.collidesWith(self.smallAstroid):
           self.sndAstroid.play()
           self.smallAstroid.reset()
           self.hp -= 2  
           self.lblHp.text = f"Score: {self.hp:.2f}"
           #self.score -= 2
           
        self.lblTime.text = f"Time left: {self.timer.getTimeLeft():.2f}"
        
        
    def processEvent(self, event):      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.currentBullet += 1
                if self.currentBullet >= self.NUM_BULLETS:
                   self.currentBullet = 0
                   print(self.currentBullet)
                self.bullet[self.currentBullet].fire()
                #self.bullet.fire()
            #if event.key == pygame.K_RIGHT:
                   
            
        
def main():
    keepGoing = True
    lastScore = 0
    
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()
        
        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
            
        else:
            keepGoing = False
   #game = Game()
   #game.start()
           
if __name__ == "__main__":
    main()
         
