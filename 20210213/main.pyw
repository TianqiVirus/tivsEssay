# tianqiVirus's Essay
# by TianqiVirus
# https://github.com/TianqiVirus
# Released under a "Simplified BSD" license

width=600
height=600
title="tianqiVirusEssay"
icon="clown.ico"
fps=32

import pygame
from random import randint

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption(title)
pygame.display.set_icon(pygame.image.load(icon))
timer = pygame.time.Clock()

keepGoing=True
doingTime=0

emojiCount=10
emojiSize=40

class emoji(pygame.sprite.Sprite):
	def __init__(self,x,y,size,status=0):
		super().__init__()
		self.x = x
		self.y = y
		self.size = size
		self.imageBase = pygame.image.load("clown.png")
		self.image = pygame.transform.smoothscale(self.imageBase,(self.size,self.size))
		if status==0:
			self.update = self.normalUpdate
		elif status==1:
			self.update = self.specialUpdate
	def normalUpdate(self,screen):
		if (not -self.size<=self.x<=width) or (not -self.size<=self.y<=height):
			self.x = width/2-self.size/2
			self.x = height/2-self.size/2
		self.x+=randint(-10,10)
		self.y+=randint(-10,10)
		screen.blit(self.image,(self.x,self.y))
	def specialUpdate(self,screen):
		self.x-=1
		self.y-=1
		self.size+=2
		if self.size>=200:
			self.size=2
			self.x=width/2-1
			self.y=height/2-1
		self.image = pygame.transform.smoothscale(self.imageBase,(self.size,self.size))
		screen.blit(self.image,(self.x,self.y))

normalEmoji = pygame.sprite.Group()
for i in range(emojiCount):
	normalEmoji.add(emoji(randint(200,400)-emojiSize/2,randint(200,400)-emojiSize/2,emojiSize))
emojiBoss=emoji(width/2-1,height/2-1,2,1)

while keepGoing:
	doingTime+=1
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			keepGoing=False

	emojiBoss.update(screen)
	normalEmoji.update(screen)
	pygame.display.update()
	timer.tick(fps)

pygame.quit()
