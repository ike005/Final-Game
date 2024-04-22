# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:19:09 2024

@author: chibuike
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
            #self.imageAngle += 5
            #self.copyImage(self.images["right"])
            self.x -= self.moveSpeed
            self.scene.currentBullet += 1
            if self.scene.currentBullet >= self.scene.NUM_BULLETS:
               self.scene.currentBullet = 0

        if self.isKeyPressed(pygame.K_SLASH):
            #self.addForce(.2, self.imageAngle)
            self.imageAngle -= 5
            self.copyImage(self.images["left"])
            self.x += self.moveSpeed
            self.scene.currentBullet += 1
            if self.scene.currentBullet >= self.scene.NUM_BULLETS:
               self.scene.currentBullet = 0
               
        if self.isKeyPressed(pygame.K_RIGHT):
            #self.addForce(.2, self.imageAngle)
            #self.imageAngle -= 5
            self.copyImage(self.images["left"])
            self.x += self.moveSpeed
            self.scene.currentBullet += 1
            if self.scene.currentBullet >= self.scene.NUM_BULLETS:
               self.scene.currentBullet = 0
               
        if self.isKeyPressed(pygame.K_UP):
            #self.addForce(.2, self.imageAngle)
            #self.copyImage(self.images["thrust"])
            self.y -= self.moveSpeed
            self.scene.currentBullet += 1
            if self.scene.currentBullet >= self.scene.NUM_BULLETS:
               self.scene.currentBullet = 0
            
        if self.isKeyPressed(pygame.K_DOWN):
            #self.addForce(.2, self.imageAngle)
            self.copyImage(self.images["thrust"])
            self.y += self.moveSpeed
            self.scene.currentBullet += 1
            if self.scene.currentBullet >= self.scene.NUM_BULLETS:
               self.scene.currentBullet = 0
    
        
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
        #self.setSize(80,50)
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
        self.setSize(70,50)
        self.position = (-20,240)
        self.imageAngle = -90
        self.minSpeed = 3           
        self.maxSpeed = 6
        #self.dx = -self.dx
        self.dx -= random.randint(self.minSpeed, self.maxSpeed)
        
    #def process(self):
        
        
    def reset(self):
        self.x = 500
        self.y = random.randint(100,420)
        self.dx - random.randint(self.minSpeed, self.maxSpeed)
        self.CONTINUE
    def checkBounds(self):  
        if -self.right > self.screenWidth:
            self.reset()
    #def process():
        #randNUM = random.randint(1,100)
        
       # keepGoing = True
        #while keepGoing:
    
        #if randNUM <= 25:
        #self.bullet.fire()
       

        
class EnemyB(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("enemyUFO.png")
        self.setSize(50,50)
        self.position = (320,460)
        self.minSpeed = 1         
        self.maxSpeed = 2
        self.dx = random.randint(self.minSpeed, self.maxSpeed)
        self.imageAngle = -270
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

    def fire(self):
        if not self.visible:
            self.show()
            self.position = self.parent.position
            self.moveAngle = self.parent.imageAngle
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
            self.speed = 20
            
    def reset(self):
        self.hide()
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("starBackground.png")
        self.player = Player(self)
        self.bigastroid = Astroid(self)
        self.smallastroid = SMastroid(self)
        self.enemya = EnemyA(self)
        self.enemyb = EnemyB(self)
        self.bullet = Bullet(self, self.player)
        self.bullet1 = Bullet1(self, self.enemyb)
        self.NUM_BULLETS = 10
        self.currentBullet = 0
        self.bullet = []
        self.enemya = []
        self.bigastroid = []
        self.smallastroid = []
        
        for enemy in range(4):
            self.enemya.append(EnemyA(self))
            
        for astroid in range(2):
            self.bigastroid.append(Astroid(self))
            
        for astroid in range(4):
            self.smallastroid.append(SMastroid(self))
        
        
        for i in range(self.NUM_BULLETS):
            self.bullet.append(Bullet(self, self.player))
            
            
        self.sprites = [
            self.player, self.enemya, self.enemyb, self.bullet, self.bullet1,
            self.bigastroid, self.smallastroid]
        

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
        if self.bullet1.collidesWith(self.player): 
           self.bullet1.reset() 
       
       #for bullets in self.bullet:    
           #for enemy in self.enemya:
               #if bullets.collidesWith(enemy):
                   #bullets.reset()
           
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
   game = Game()
   game.start()
           
if __name__ == "__main__":
    main()
         