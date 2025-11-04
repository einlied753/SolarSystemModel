Blender as B
from Blender.Mathutils import *
from Blender.BGL import *
from Blender import Draw
import time
import math
from math import sin,cos,sqrt,pi

ob=B.Object.Get('Sphere')
msh=ob.getData(False,True)
fs=msh.faces
a=70
X1=20

pi=math.pi

buffP=Buffer(GL_FLOAT,4,[40.,0.1,0,1.]) 


def key(evt,val):
	if evt==Draw.ESCKEY: Draw.Exit()
		
		
def ChangeA():
	global a
	a +=0.4
	time.sleep(0.01)	
	Draw.Redraw(1)
	


def Sun(d):
	
	glEnable(GL_LIGHTING)

	glEnable(GL_LIGHT1)
	buffS=Buffer(GL_FLOAT,4,[0.7,0.6,0.3,1.0])
	glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, buffS)
	
	glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, buffS)
		
	glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
	for ff in fs:
		if len(ff.verts)==4:
			glColor3f(1,0,0)
			glBegin(GL_QUADS)
			glNormal3f(*ff.no)
			for pt in ff.verts:
				glVertex3f(d*pt.co.x,d*pt.co.y,d*pt.co.z)
			glEnd()
		if len(ff.verts)==3:
			glBegin(GL_TRIANGLES)
			glNormal3f(*ff.no)
			for pt in ff.verts:
				glVertex3f(d*pt.co.x,d*pt.co.y,d*pt.co.z)		
			glEnd()

	
	
	glDisable(GL_LIGHT1)
	return



def Sphere(d):

	for ff in fs:
		
		if len(ff.verts)==4:
			glBegin(GL_QUADS)
			glNormal3f(*ff.no)
			for pt in ff.verts:
				glVertex3f(d*pt.co.x,d*pt.co.y,d*pt.co.z)
			glEnd()
		if len(ff.verts)==3:
			glBegin(GL_TRIANGLES)
			glNormal3f(*ff.no)
			for pt in ff.verts:
				glVertex3f(d*pt.co.x,d*pt.co.y,d*pt.co.z)		
			glEnd()

	return

def circle(x,y,z,r):
	i=0
	glBegin(GL_LINE_LOOP)
	while i<=2*pi:
		glVertex3f(x+r*cos(i),y+r*sin(i),r*sin(i)/4)
		i+=0.1
	glEnd()
	return



def pounts(x,y,z,r):
	i=0
	glPointSize(2)
	glColor3f(0.2, 0.2, 0.2)
	glBegin(GL_POINTS)
	while i<=2*pi:
		glVertex3f(r*cos(i),r*sin(i),z)
		glVertex3f(1.5+r*cos(i),r*sin(i),z)
		glVertex3f(3+r*cos(i),-1+r*sin(i),z)
		glVertex3f(-2+r*cos(i),r*sin(i),z)
		glVertex3f(-2.5+r*cos(i),-1.6+r*sin(i),z)
		i+=0.1
	glEnd()
	return

	
def Scene():
	
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)

	
	
	glViewport(30,30,500,500)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()		
	glOrtho(-50, 50,-50,50,-100,700)
	glRotatef(75,1 , 0, 1)
	glRotatef(20,0,-1,0)
	glTranslatef(0,0,-10)
	  
	
 	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()	
	
	
	glPushMatrix()
	glLoadIdentity()
	glTranslatef(1.0, 1.0, 1.0)	
	light0_position =Buffer(GL_FLOAT,4, [ 0.0, 0.0, 0.0, 1.0] )   #null light in (1.0, 1.0, 1.0) in world system of coordinates
	glLightfv(GL_LIGHT0, GL_POSITION, light0_position)		
	glPopMatrix()
	
	
	buffL=Buffer(GL_FLOAT,4,[1,1,0.7,1.]) # color of Mercury
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)		
	glRotatef(a*4.8, 0, 0, -1)           # speed orbit of Mercury
	glTranslatef( 0.38*X1, 0, 0)    #distance from the Sun
	Sphere(0.2439700)                    # Mercury's radius
	glTranslatef( -0.38*X1, 0, 0)
	glRotatef(a*4.8, 0, 0, 1)
	
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*3.5, 0, 0, -1)                
	glTranslatef( 0.43*X1, 0, 0)
	Sphere(0.60518)                                   # Venus
	glTranslatef( -0.43*X1, 0, 0)	
	glRotatef(a*3.5, 0, 0, 1)
	
	buffL=Buffer(GL_FLOAT,4,[0.5,0.6,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*2.9783, 0, 0, -1)                
	glTranslatef( 0.5343*X1, 0, 0)
	glRotatef(a*1.45656, 0, 0, -1)
	Sphere(0.63781)                                             # Earth  
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glTranslatef( 1, 0, 0)   
	Sphere(0.1737)  
	glTranslatef( -1, 0, 0)                            # Moon
	glRotatef(a*1.45656, 0, 0, 1)
	glTranslatef( -0.5343*X1, 0, 0)
	glRotatef(a*2.9783, 0, 0, 1)  
	
	
	buffL=Buffer(GL_FLOAT,4,[1,0.4,0.2,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*2.413, 0, 0, -1)                
	glTranslatef( 0.7618*X1, 0, 0)
	Sphere(0.33895)                                     #Mars
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*1.52345, 0, 0, -1)
	glTranslatef( 0.8, 0, 0)   
	Sphere(0.0011)  
	glTranslatef( -0.8, 0, 0)                            # Fobos
	glRotatef(a*1.52345, 0, 0, 1)
	glRotatef(a*1.34512, 0, 0, -1)
	glTranslatef( 2.0337, 0, 0)   
	Sphere(0.0013)  
	glTranslatef( -2.0337, 0, 0)                          # Deimos
	glRotatef(a*1.34512, 0, 0, 1)	
	glTranslatef( -0.7618*X1, 0, 0)
	glRotatef(a*2.413, 0, 0, 1)  
	
	
	
	glRotatef(a*2, 0, 0, -1)           # asteroids
	glDisable(GL_LIGHTING)            
	pounts(0,0,0, 1.15*X1)
	pounts(0,0,-1, 1.2*X1)
	pounts(0,0,1.5, 1.27*X1)
	pounts(0,0,2.5, 1.35*X1)
	glEnable(GL_LIGHTING) 	
	glRotatef(a*2, 0, 0, 1)  
	
	
	buffL=Buffer(GL_FLOAT,4,[1,0.4,0.2,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*1.307, 0, 0, -1)                
	glTranslatef( 1.73475567*X1,  0, 0)
	glRotatef(a*1.7334, 0, 0, -1)
	Sphere(4.6607)                                  #Jupiter
	
	buffL=Buffer(GL_FLOAT,4,[1,1,0,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glTranslatef( 6.1, 0, 0)   
	Sphere(0.18213)  
	glTranslatef( -6.1, 0, 0)                            # Io
	glRotatef(a*1.7334, 0, 0, 1)

	buffL=Buffer(GL_FLOAT,4,[1,0.5,0.2,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*4.94761, 0, 0, -1)
	glTranslatef( 5.8, 0, 0)   
	Sphere(0.15608)                                  # Europe
	glTranslatef( -5.8, 0, 0)                            
	glRotatef(a*4.94761, 0, 0, 1)
	
	buffL=Buffer(GL_FLOAT,4,[0.9,0.9,0.9,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*1.0880, 0, 0, -1)
	glTranslatef( 6.2, 0, 0)   
	Sphere(0.26341)                                  # Ganymede
	glTranslatef( -6.2, 0, 0)                            
	glRotatef(a*1.0880, 0, 0, 1)
	
	buffL=Buffer(GL_FLOAT,4,[0.8,0.8,0.7,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*0.8204, 0, 0, -1)
	glTranslatef(6.0, 0, 0)   
	Sphere(0.24103)                                  # Callisto
	glTranslatef( -6.0, 0, 0)                            
	glRotatef(a*0.8204, 0, 0, 1)
		                             
	glTranslatef( - 1.73475567*X1,  0, 0)
	glRotatef(a*1.307, 0, 0, 1)  
	
	

	
	buffL=Buffer(GL_FLOAT,4,[1,1,0.8,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*0.969, 0, 0, -1)                
	glTranslatef(3.194*X1,  0, 0)
	Sphere(4.0179)    
	
	glDisable(GL_LIGHTING)
	glColor3f(0.1,0.1,0.1)          # rings of Saturn
	circle (0,0,0,5.6)
	circle (0,0,0,4.1)
	circle (0,0,0,4.2)
	circle (0,0,0,4.3)
	circle (0,0,0,4.4)
	circle (0,0,0,4.5)
	circle (0,0,0,4.6)
	circle (0,0,0,4.7)
	glColor3f(0,0,0)
	circle (0,0,0,4.8)
	circle (0,0,0,4.9)
	glColor3f(0.1,0.1,.1)
	circle (0,0,0,5.5)
	circle (0,0,0,5.4)
	circle (0,0,0,5.3)
	circle (0,0,0,5.2)
	circle (0,0,0,5)
	circle (0,0,0,5.1)
	glEnable(GL_LIGHTING)
	
	buffL=Buffer(GL_FLOAT,4,[1,1,0.3,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a, 0, 0, -1)
	glTranslatef(5.5, 0, 0)   
	Sphere(0.2575)                                  # Titan
	glTranslatef( -5.5, 0, 0)                            
	glRotatef(a, 0, 0, 1)
	                                
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*4, 0, 0, -1)
	glTranslatef(5.5, 0, 0)   
	Sphere(0.1528)                                  # Rea
	glTranslatef( -5.5, 0, 0)                            
	glRotatef(a*4, 0, 0, 1)
	
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*0.2, 0, 0, -1)
	glTranslatef(5.6, 0, 0)   
	Sphere(0.1436)                                  # Yapet
	glTranslatef( -5.6, 0, 0)                            
	glRotatef(a*0.2, 0, 0, 1)
	
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*8, 0, 0, -1)
	glTranslatef(5.6, 0, 0)   
	Sphere(0.1118)                                  # Diona
	glTranslatef( -5.6, 0, 0)                            
	glRotatef(a*8, 0, 0, 1)
		
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*8.5, 0, 0, -1)
	glTranslatef(5.6, 0, 0)   
	Sphere(0.1060)                                  # Tefia
	glTranslatef( -5.6, 0, 0)                            
	glRotatef(a*8.5, 0, 0, 1)
	     
	glTranslatef( -3.194*X1, 0, 0)
	glRotatef(a*0.969, 0, 0, 1)
	
	
	
	buffL=Buffer(GL_FLOAT,4,[0.8,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*0.681, 0, 0, -1) 
	glRotatef(98, 0, 0, -1)                
	glTranslatef( 4.80735*X1, 0, 0)
	Sphere(1.68667)                                     #Uran
	
	buffL=Buffer(GL_FLOAT,4,[1,0.7,0.2,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a, 0, 0, -1)
	glTranslatef(5.2, 0, 0)   
	Sphere(0.07884)                                  # Titania
	glTranslatef( -5.2, 0, 0)                            
	glRotatef(a, 0, 0, 1)
	     
	buffL=Buffer(GL_FLOAT,4,[1,0.8,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*0.7, 0, 0, -1)
	glTranslatef(4.8, 0, 0)   
	Sphere(0.07614)                                  # Oberon
	glTranslatef( -4.8, 0, 0)                            
	glRotatef(a*0.7, 0, 0, 1)
	
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*4, 0, 0, -1)
	glTranslatef(3, 0, 0)   
	Sphere(0.05789)                                  # Ariel	
	glTranslatef( -3, 0, 0)                            
	glRotatef(a*4, 0, 0, 1)
	
	glRotatef(a*2, 0, 0, -1)
	glTranslatef(3, 0, 0)   
	Sphere(0.05847)                                  # Umbriel	
	glTranslatef( -3, 0, 0)                            
	glRotatef(a*2, 0, 0, 1)
	
	glTranslatef( -4.80735*X1, 0, 0)
	glRotatef(a*0.681, 0, 0, 1)  
	glRotatef(98, 0, 0, 1)
	
	
	

	buffL=Buffer(GL_FLOAT,4,[0.2,0,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*0.543, 0, 0, -1)                
	glTranslatef( 6.020732*X1,  0, 0)
	Sphere(1.64)                                     #Neptun
	
	buffL=Buffer(GL_FLOAT,4,[1,0.9,0.9,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*1.36, 0, 0, 1)
	glTranslatef(2.2, 0, 0)   
	Sphere(0.1353)                                  # Triton	
	glTranslatef( -2.2, 0, 0)                            
	glRotatef(a*1.36, 0, 0, -1)
	
	buffL=Buffer(GL_FLOAT,4,[1,1,1,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(90+a*0.02, 0, 0, -1)
	glTranslatef(3, 0, 0)   
	Sphere(0.0340)                                  # 	Nereida
	glTranslatef( -3, 0, 0)                            
	glRotatef(90+a*0.02, 0, 0, 1)
	
	glTranslatef( -6.020732*X1,  0, 0)
	glRotatef(a*0.543, 0, 0, 1)  
	
	
	buffL=Buffer(GL_FLOAT,4,[1,0.7,0,1.]) 
	glLightfv(GL_LIGHT0,GL_DIFFUSE,buffL)
	glRotatef(a*0.4666, 0, 0, -1)                
	glTranslatef( 6.580281*X1,  0, 0)
	Sphere(0.1195)                                     #Pluton
	glTranslatef( -6.580281*X1, 0, 0)
	glRotatef(a*0.4666, 0, 0, 1)  

	
	
	glRotatef(a*1.7666, 0, 0, -1)
	Sun(6.8)                                            #Sun


		
def gui():
	glClearColor(0,0,0,1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	
	Scene()
	
	
	ChangeA()
	
	
	
Draw.Register(gui,key,None)