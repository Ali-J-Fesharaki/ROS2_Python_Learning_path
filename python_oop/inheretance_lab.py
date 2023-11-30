# Declare the Hexagon class here
class Hexagon:
  def __init__(self,center,radius,window,init_angle):
    self.center=center
    self.radius=radius
    self.window=window
    self.points=6
    self.angle=math.radians(360/self.points)
    self.init_angle=init_angle
    self.color=(179,55,113)
    self.stroke_weight=3
  def calculate_vertices(self):
    vertices=[]
    for i in range(self.points):
      vertices.append((self.radius*math.cos(i*self.angle+self.init_angle)+self.center[0],self.radius*math.sin(i*self.angle+self.init_angle)+self.center[1]))
    return vertices
  def draw(self):
    pygame.draw.polygon(self.window,self.color,self.calculate_vertices(),self.stroke_weight)
# Declare the child class here

import pygame
import math
# pygame setup
pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Polygon Animation")
clock = pygame.time.Clock()
# Declare the Hexagon class here
class Hexagon:
  def __init__(self,center,radius,window,init_angle):
    self.center=center
    self.radius=radius
    self.window=window
    self.points=6
    self.angle=math.radians(360/self.points)
    self.init_angle=init_angle
    self.color=(179,55,113)
    self.stroke_weight=3
  def calculate_vertices(self):
    vertices=[]
    for i in range(self.points):
      vertices.append((self.radius*math.cos(i*self.angle+self.init_angle)+self.center[0],self.radius*math.sin(i*self.angle+self.init_angle)+self.center[1]))
    return vertices
  def draw(self):
    pygame.draw.polygon(self.window,self.color,self.calculate_vertices(),self.stroke_weight)
# Declare the child class here   
# global variables    
run = True
hex_shapes=[]
num_shapes=4
for i in range(num_shapes):
  hex_shapes.append(Hexagon((200,200),125,window,i*math.radians(360/num_shapes)))
# main loop
while run:
  pygame.time.delay(100)
  window.fill((55, 55, 55))
  for shape in hex_shapes:
    shape.draw()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  pygame.display.update() 
  clock.tick(30)
pygame.quit()