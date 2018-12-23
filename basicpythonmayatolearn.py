Note:
Show results = Drag all code and highlight the line you want to run, Press Ctrl + Enter 
Zoom screen = Ctrl + e
Str = alphabet (string)
Int = number (don’t have decimal)
Flot = number (have decimal)

	myX = 10				# myX equal to 10
	myY = 20				:#myY equal to 20
	myXY = myX * myY
	print (‘The result is’ + str(myXY))	#myXY is number = 200
	
	print (‘WHAT IS YOUR NAME’)
	#next get input
	yourName = str (raw_input())
	print (yourName)

	print (‘WHAT IS YOUR NAME’)
	yourName = str (raw_input()) #togetaninput
	print (‘HELLO’ +’  ‘+ yourName) #addtwovariable
	print (‘YOUR NAME HAVE’ + str (len(yourName)) + ‘Characters’) 
	
.	myInt = int (float (‘3.1’))	 #tochange string to float and to int
	Print (myInt)

Operators =  + ,  - ,  * ,  /
Values = -88.8 ,  5 ,  ‘hello’
.	if	10 = = ’10.0’:
		print (‘True’)
		print (‘Very True’)
		print (‘Super Equal’)
	else:
		print (’10 = = \’10\’  is not equal’)
		print (’10 = = \’10\’  Not True’)
		print (’10 = = \’10\’  Never Equal’)
Standard data type
1.	Number	# 6.33j  , 37.j , 4.33e – 22j	: j = complex
2.	String		

	myString = ‘ABCDEFGHJKLMNO’
	print (myString)			#(ABCDEFGHJKLMNO)
	print (myString [ 0 ])		#(A)
	print (myString [ 2 ]) 	 	#(c)  #which character you can see
	print (myString [ 0:5 ])		#(ABCDE)  #0 to 5
	print (myString[ 10: ])		
	print (myString *2)		#ABCDEFGHJKLMNOABCDEFGHJKLMNO
#double multiply



List (can add more)
myList = [‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91]	:#count 0 , 1 , 2 , 3 , 4
myList2 = [‘Sam’ , 1978]			:#count 0 , 1
print (myList)				:#[‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91]
print (myList[ 3 ])			:#Sam
print (myList [ 1:4 ])			: #1234 , 11.0 , ‘Sam’]  #count 1 to 3
print (myList + myList2)			: #‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91 , ‘Sam’ , 1978
myList = [‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91]
myList2 = [‘Sam’ , 1978]
print (myList)				: ‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91
myList.append (‘COOKIE’)		: av’ , 1234 , 11.0 , ‘Sam’ , 3.91 , ‘COOKIE’
					#add more data
myList.remove (‘Sam’)			: [‘av’ , 1234 , 11.0 , 3.91]  
					#delete some data
myList [ 0 ]				: ’va’


Tuples (cann’t do anything ,fix data)  *changes [ ] to () from List
myList = (‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91)	: (0 , 1 , 2 , 3 , 4)
myList2 = (‘Sam’ , 1978)			: (0 , 1)
print (myList)				: (‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91)
print (myList( 3 ))			: Sam
print (myList ( 1:4 ))			: (1234 , 11.0 , ‘Sam’)  #count 1 to 3
print (myList + myList2)			: (‘av’ , 1234 , 11.0 , ‘Sam’ , 3.91 , ‘Sam’ , 1978)


Dictionary (key + values)
myDictionary = {‘name’ : ‘Sam’ , ‘Age’:30 , ‘Weight’ : 88 ‘Height’ : 177.5}
print (myDictionary.keys ( ))
print (myDictionary.values ( ))
print (myDictionary [‘Age’])

My name is Sam I am 30 years old My weight and my height are 88 177.5
	print  (‘My name is’ + \
	myDictionary [‘name’] + ‘I am’ + str(myDictionary [‘Age’]) + ‘years old My weight and my height 	are’ + str (myDictionary[‘Weight’]) + str (myDictionary [‘Height’])


import maya.cmds as mx
	dataFromUser = input (‘Please enter number only’)
	print (dataFromUser)
	if 	dataFromUser >= 50:
	   	print (‘Your Data is more than 50’)
	else:
		print (‘Your Data is less than 50’)

import maya.cmds as mx
	dataFromUser = input (‘Please enter number only’)
	print (dataFromUser)
	if	dataFromUser >= 50
		mx.nurbsCube ()
	else:
		mx.sphere()

import maya.cmds as mx
	dataFromUser = input (‘Please enter number only’)
	print (dataFromUser)
	if	dataFromUser = =1:
		mx.nurbsCube()
	elif	dataFromUser = =2:
		mx.sphere()
	elif	dataFromUser = =3:
		mx.cylinder()
	elif	dataFromUser = =4:
		mx.cone()
	elif	dataFromUser = =5:
		mx.torus()
	else:
		mx. plane()
2nd Part

The For Loop
EX.      	import maya.cmds as mx
            	for i in range (1 , 10):
                            	print (‘this is i =  ’str(i))
 
Make box and move
EX.      	import maya.cmds as mx                                                      		# your name
            	nameOfItems = [‘Box2’ , ‘Box3’ , ‘Box4’ , ‘Box5’]
 
            	# for i in range (1 , 10):
 
            	for nameItem in nameOfItems:
                            	print (“Data is ” + nameItem)
            	   	mx.nurbsCube (n = nameItem)
            	 	mx.move (10 , 0 , 0)                                #position x ,y , z
 

Make box 4 directions
EX.1   	import maya.cmds as mx
            	nameOfItems = [‘Box2’ , ‘Box3’ , ‘Box4’ , ‘Box5’]
 
            	# for i in range (1 , 10):
 
            	#for nameItem in nameOfItems:
            	#         	print (“Data is ” + nameItem)
            	     	  	mx.nurbsCube (n = nameOfItems[0])
            	     	  	mx.move (0 , 0 , 5)    
   	
mx.nurbsCube (n = nameOfItems[0])
            	     	  	mx.move (5 , 0 , 0)       	
 
            	   	    	mx.nurbsCube (n = nameOfItems[0])
            	    	   	mx.move (0 , 0 ,- 5)
 
            	     	  	mx.nurbsCube (n = nameOfItems[0]) 
            	    	   	mx.move (-5 , 0 , 0) 



EX.2   	import maya.cmds as mx
            	nameOfItems = [‘Box2’ , ‘Box3’ , ‘Box4’ , ‘Box5’]
            	for nameItem in nameOfItems:
            	            	mx.nurbsCube (n = nameItem)
                            	if nameItem == ‘Box2’:
                            	            	mx.move (5 , 0 , 0)

                            	if nameItem == ‘Box3’:
                                            mx.move (-5 , 0 , 0)

                            	if nameItem == ‘Box4’:
                                            mx.move (0 , 0 , 5)

                            	if nameItem == ‘Box5’:
                                            mx.move (0 , 0 ,- 5)


EX.      	import maya.cmds as mx
            	nameOfItems = [‘Box2’ , ‘Box3’ , ‘Box4’ , ‘Box5’]
            	for i in range (0 , 4):
                            	mx.nurbsCube (n = nameOfItems[i])
                            	mx.move (i , 0 , 0)

                            	mx.nurbsCube (n = nameOfItems[i]) 
                            	mx.move (-i , 0 , 0)

                            	mx.nurbsCube (n = nameOfItems[i])
                            	mx.move (0 , i , 0) 

                            	mx.nurbsCube (n = nameOfItems[i])
mx move (0 ,- i , 0) 
 







EX.      	import maya.cmds as mx
            	nameOfItems = [‘Box2’ , ‘Box3’ , ‘Box4’ , ‘Box5’]
            	for i in range (0 , 11)
                            	mx.nurbsCube()
                            	mx.move (i , i , 0)
                            	mx.nurbsCube()
                            	mx.move (-i , -i , 0) 
                            	mx.nurbsCube()
                            	mx.move (-i , 0 , 0) 
                            	m..nurbsCube()
                            	mx.move (i , -i , 0) 


Make box from 4 directions up from 4
EX.      	import maya.cmds as mx
            	for i in range (0 , 11)
                            	mx.nurbsCube()
            	               mx.move (i , i , 0) 
                            	mx.nurbsCube()
                            	mx move (0 , i , i)
                            	mx.nurbsCube()
                            	mx.move (-i , i , 0) 
                            	mx.nurbsCube()
                            	mx.move (0 , i , -i) 
 

 EX.	    import maya.cmds as mx
    for i in range (0 , 20):
	    if i % 2 == 0
		mx.nurbsCube()
		mx move (0 , i , 0)

    for i in range (0 , 20):
	   	mx.nurbsCube()
		mx.move (2 , i*2 , 0)

	    

	    
EX.1	    import maya.cmds as mx
	    if i % 2 == 0
		mx.nurbsCube()
		mx.move (0 , i , 0)	sphere
	nubscube
	    for i in range (0 , 20):
	    	if i % 2 == 1: 
	    	mx.Sphere ()
	    	mx.move (0 , i , 0) 

EX.2	    import maya.cmds as mx
	    if i % 2 == 0
		mx. nurbsCube()
		mx move (0 , i , 0)
	    else :
		mx.Sphere ()
	    	mx.move (0 , i , 0)


Function

import maya.cmds as mx
def createCube ()
	mx.nurbsCube()					# (0 , 0 , 0) start point
	mx .nurbsCube()
	mx.move (1 , 0 , 0)
	mx.nurbsCube()
	mx.move (2 , 0 , 0)

# End Function

def createSphere ():
	mx.Sphere (r =s)
	
createCube ()		# call function working
createSphere ()





EX.1	    import maya.cmds as mx
	    def createCone ():
		mx.Cone ()
		mx.Cone ()
		mx.move (1 , 0 , 0)
		mx.Cone ()
		mx.move (2 , 0 , 0)
		mx.Cone ()
		mx.move (3 , 0 , 0)
		mx.Cone ()
		mx. move (4 , 0 , 0)
	    createCone ()

EX.2	    import maya.cmds as mx
	    def createCone ():
		for i in range (1 , 101)
		mx.Cone ()
		mx.move (0 , i , 0)
	    createCone ()

EX.3	import maya.cmds as mx
	    def createConeParameter (myEndingRange):	       # myEnding = Parameter , Range = last point
		for i in range (1 , myEndingRange ):
			mx.Cone ()
			mx.move (0 , i , 0)
	    myEnd = input ()
	    createConeParameter (myEnd)

EX.4	import maya.cmds as mx
def createTorusParameter (myTemp):	
	for i in range (1 , myTemp):
		mx.Torus ()
			mx.move (10 , i , 0)
	
def createTorusParameter (myTemp):
	for i in range (1 , myTemp):
			mx.Cylinder ()
			mx.move (-5 , i , 0)
myEnd = input ()
createConeParameter (myEnd)
createTorusParameter (myEnd)

Random

EX.	import maya.cmds as mx
from random import*

	print random ()
	print radiant (1 , 10)
	def createRandomCubeOnTheGround () :	#def = start 
		for i in range (0 , 10) :
		mx.nurbsCube ()
		xRand = radiant (-5 , 5)
		zRand = radiant (-5 , 5)
		mx.move (xRand , zRand)
	
	createRandomCubeOnTheGround ()		#order



Uniform

# uniform is the one type of data

          print uniform (1 , 10)				: more detailed – 1 , 1.2 , 1.3 …
different
          print						: fix data – 1 , 2 , 3 …



Shuffle (myNumber)						: random’s function

MyNumber = [10 , 20 , 30 , 40 , 50 ,
60 , 70 , 80 , 90 , 100]
print (“Before ” + str (myNumber) )

print (“After ” + str (myNumber) )





Maya Python Basic


EX.	import maya.cmds as mx
	mx.file (f = True , new = True)			# f = force
							# c = create new maya work
							# save file
	mx.file (rn = ‘myfile 2.ma’)
	mx.file (f = True , type = ‘mayaAscii’ , save = True)
	mx.file (‘myfile 2.ma’ , open = True)		# if you don’t have file to open maybe got u
							errors



3rd Part
Datetime
import maya.cmds as mx
from datetime import datetime					: Fri Oct 19 09:19:30 2018
print (datetime.now().strftime("%c"))

import maya.cmds as mx
from datetime import datetime
#print (datetime.now().strftime("A%Y_%b_%d,ma"))		: A2018_Oct_19 show at title in
filename = "A"+datetime.now().strftime("%Y_%b_%d" )		maya
mx.file(rn = filename)
mx.file(f = True, type = 'mayaBinary',save = True)

Create object
import maya.cmds as mx
mx.nurbsPlane()
mx.nurbsPlane(n="myPlane1",w=4)
mx.nurbsPlane(n="myPlane2",w=4,lr=2)
mx.move(1,0,0)
mx.nurbsPlane(n="myPlane3",w=4,lr=3,u=2)
mx.move(2,0,0)
mx.nurbsPlane(n="myPlane4",w=4,lr=3,u=4)
mx.move(3,0,0)
mx.nurbsPlane(n="myPlane5",w=4,lr=3,u=4,v=4)
mx.move(4,0,0)
mx.nurbsPlane(n="myPlane6",w=4,lr=3,u=4,v=4,ax=[1,0,0])
mx.move(5,0,0)
mx.nurbsPlane(n="myPlane7",w=4,lr=3,u=4,v=4,ax=[0,1,0])
mx.move(6,0,0)
mx.nurbsPlane(n="myPlane8",w=4,lr=3,u=4,v=4,ax=[0,0,1])
mx.move(7,0,0)

ax = position of object (xyz)

EX. 	import maya.cmds as mx
def CreateCubeNurbsFromPlane():
mx.nurbsPlane(n="myPlane1",w=6,u=6,v=6)
mx.nurbsPlane(n="myPlane2",w=6,u=6,v=6)
mx.move(6,0,0)
mx.nurbsPlane(n="myPlane3",w=6,u=6,v=6,ax=[0,0,1])
mx.move(3,0,3)
mx.nurbsPlane(n="myPlane4",w=6,u=6,v=6,ax=[0,0,1])
mx.move(3,0,-3)
mx.nurbsPlane(n="myPlane5",w=6,u=6,v=6,ax=[0,1,0])
mx.move(3,3,0)
mx.nurbsPlane(n="myPlane6",w=6,u=6,v=6,ax=[0,1,0])
mx.move(3,-3,0)    
CreateCubeNurbsFromPlane()

filename = "Bell Cube"+datetime.now().strftime("%B%d%Y" )
mx.file(rn = filename)
mx.file(f = True, type = 'mayaAscii',save = True)

EX.	mx.file(f=1,new=1)
mx.nurbsCube(n='cube1',w=6,u=6,v=6)
mx.nurbsCube(n='cube2',w=6,u=6,v=6,hr=2,ax=[0,1,0])
mx.move(6,0,0)
mx.nurbsCube(n='cube3',w=6,u=6,v=6,lr=2)
mx.move(12,0,0)


r = rotation
s = size
p = position


mx.file(f=1,new=1)
mx.plane(n='myPlane1',p=[0,5,0])
mx.plane(n='myPlane2',p=[0,5,-2],s=4)
mx.plane(n='myPlane3',p=[0,5,-4],w=4,l=2)
mx.plane(n='myPlane4',p=[0,5,-2],s=4,r=[0,45,0])
mx.plane(n='myPlane5',p=[0,5,-2],s=4,r=[0,0,45])
mx.file(f=1,new=1)
def createPlane(): 
    for i in range(1,13):
        mx.plane(p=[0,5,0],s=4,r=[0,0,10*i])
createPlane()

EX.	mx.file(f=1,new=1)
def createPlane(): 
    for i in range(1,13):
        mx.plane(p=[0,5,0],s=4,r=[0,0,i])
createPlane()

ssw = startsweep
esw = endsweep
hr = heightRatio 


mx.file(f=1,new=1)
mx.cone(n='cone1',r=3)
mx.cone(n='coneDefault')
mx.move(0,0,4)
mx.cone(n='cone3',r=3,ssw=90)
mx.move(0,0,8)
mx.cone(n='cone4',r=3,ssw=180)
mx.move(0,0,12)
mx.cone(n='cone5',r=3,ssw=270)
mx.move(0,0,16)

mx.file(f=1,new=1)
mx.cone(n='cone1',r=3,ax=[0,1,0])
mx.cone(n='coneDefault',ax=[0,1,0])
mx.move(0,0,4)
mx.cone(n='cone3',r=3,ssw=90,ax=[0,1,0])
mx.move(0,0,8)
mx.cone(n='cone4',r=3,ssw=180,ax=[0,1,0])
mx.move(0,0,12)
mx.cone(n='cone5',r=3,ssw=270,ax=[0,1,0])
mx.move(0,0,16)

mx.cone(n='cone6',r=3,esw=90,ax=[0,1,0])
mx.move(6,0,10)


import maya.cmds as mx
def CreateCone():
    mx.file(f=1,new=1)
    for i in range(1,12):
        if(i%2==0):            #this is even number
            mx.cone(ssw=180,ax=[0,1,0])
        else:                 #this is odd number
            mx.cone(esw=180,ax=[0,1,0])
        mx.move(i*2,0,0)
CreateCone()


S =section áºè§·Ò§á¹ÇµÑé§
Span(nsp) = áºè§·Ò§á¹Ç¹Í¹



import maya.cmds as mx
def CreateCone():
    mx.file(f=1,new=1)
    for i in range(1,12):
        if(i%2==0):               				#this is even number
            mx.cone(ssw=180,ax=[0,1,0],s=5,spans=5)
        else:                 				#this is odd number
            mx.cone(esw=180,ax=[0,1,0],s=5,spans=5)
        mx.move(i*2,0,0)
CreateCone()

import maya.cmds as mx
def CreateCone():
    mx.file(f=1,new=1)
    for i in range(1,12):
        if(i%2==0):            #this is even number
            mx.cylinder(ssw=180,ax=[0,1,0],s=5,spans=5)
        else:                 #this is odd number
            mx.cylinder(esw=180,ax=[0,1,0],s=5,spans=5)
        mx.move(i*2,0,0)
CreateCone()
mx.file(f=1,new=1)
import maya.cmds as mx
def CreateCylinder():
    mx.sphere(r=2,ax=[0,1,0]) 
    mx.cylinder(ssw=180,r=1,hr=7,ax=[1,0,0])
    mx.move(-5,0,0)
    mx.cylinder(ssw=180,r=1,hr=7,ax=[1,0,0])
    mx.move(5,0,0)
    mx.cylinder(ssw=180,r=1,hr=7,ax=[0,0,1])
    mx.move(0,0,5)
    mx.cylinder(ssw=180,r=1,hr=7,ax=[0,0,1])
    mx.move(0,0,-5)
    mx.cylinder(ssw=0,r=1,hr=7,ax=[0,1,0])
    mx.move(0,5,0)
CreateCylinder()

mx.file(f=1,new=1)
mx.torus(n='torus1')
mx.torus(n='totus2',r=4,hr=0.05)
mx.torus(n='torus3',r=3,hr=0.1)
mx.torus(n='torus4',r=5,hr=0.001,ssw=180)
mx.torus(n='torus5',r=6,hr=0.5,msw=180)
mx.torus(n='torus6',r=6,hr=0.5,msw=90)
mx.move(6,0,0)
mx.torus(n='torus7',r=6,hr=0.5,msw=45)
mx.move(-6,0,0)

mx.file(f=1,new=1)
	def createTorus(): 
    for i in range(1,9):             
            mx.torus(n='totus1',r=i*1,hr=0.01)          
            mx.torus(n='totus2',r=i*1,hr=0.01,ax=[0,1,0])
            mx.move(0.5,0,0.5)
            mx.torus(n='totus3',r=i*1,hr=0.01,ax=[0,0,1])
            mx.move(0,0.5,0)
createTorus()     

4th Part
import maya.cmds as mx
mx.file(f=1,new=1)

mx.circle()
mx.circle(r=4)
mx.circle(r=5,sw=180)
mx.circle(r=2,sw=360,s=4)
mx.circle(r=3,sw=360,s=16)

NurbsSquare
EX.	import maya.cmds as mx
mx.file(f=1,new=1)

mx.nurbsSquare()
mx.nurbsSquare(sl1=4)
mx.move(2,0,0)
mx.nurbsSquare(sl2=4) 
mx.move(-2,0,0)
mx.nurbsSquare(sl1=4,sl2=6,sps=4)
mx.move(-4,0,0)
TextCurves

t = text
f = font
n = name

EX.	import maya.cmds as mx

mx.file(f=1,new=1)
mx.textCurves(f='Times-Roman' ,t='Maya')
mx.textCurves(f='Agency FB' ,t='Maya') 
mx.move(3,0,0)
mx.textCurves(f='Cordia New' ,t='·´ÊÍº')
mx.move(-3,0,0)
mx.textCurves(f='Céhinven Medium' ,t='Maya')
mx.move(-6,0,0)

POLYCONE

ax = axis
r = radius
n = name
h = height
sx = subdivisionsX(¤ÇÒÁÂÒÇ,á¹Ç¹Í¹)
sy = subdivisionsY (¤ÇÒÁÊÙ§,á¹ÇµÑé§)
sz = subdivisionsZ(¤ÇÒÁÅÖ¡,á¹Ç¹Í¹)

EX.	import maya.cmds as mx
mx.file(f=1,new=1)
mx.polyCone()
mx.polyCone(ax = (1,0,0),r=2,h=4)
mx.move(3,0,0)
mx.polyCone(ax = (-1,0,0),sx=3,sy=5,sz=6)
mx.move(-3,0,0)
mx.polyCone(ax = (0,0,1))
mx.move(0,0,3)
mx.polyCone(ax = (0,0,-1))
mx.move(0,0,-3)
mx.polyCone(ax = (1,0,1))
mx.move(3,0,3)
mx.polyCone(ax = (-1,0,-1))
mx.move(-3,0,-3)
mx.polyCone(ax = (1,0,-1))
mx.move(3,0,-3)
mx.polyCone(ax = (-1,0,1))
mx.move(-3,0,3)

PolyCube 
EX.	mx.file(f=1,new=1)
mx.polyCube()
mx.polyCube(d=4,sz=3)
mx.move(0,2,0)
mx.polyCube(w=4,sx=4)
mx.move(0,4,0)
mx.polyCube(h=4,sy=5)
mx.move(2,0,0)
PolyCylinder
EX.	mx.file(f=1,new=1)
mx.polyCylinder()
mx.polyCylinder(r=4)
mx.move(6,0,0)
mx.polyCylinder(h=4)
mx.move(-6,0,0)
mx.polyCylinder(h=4,sy=4)
mx.move(0,0,6) 
mx.polyCylinder(h=4,sx=4)
mx.move(0,0,-6)
mx.polyCylinder(h=4,sx=3,ax=(-1,0,0))
mx.move(6,0,-6)

EX.1	mx.file(f=1,new=1)
mx.polyCylinder(h=2,sx=3,ax=(0,0,0))
mx.move(0,1,0)
def createAll():
   		 for i in range (1,6):
        			mx.polyCylinder(sx=3+i)
       		 	mx.move(0,1,0+i*2) 
        			mx.polyCylinder(sx=3+i)
        			mx.move(0-i*2,1,0) 
      	  		mx.polyCylinder(sx=3+i)
       	 		mx.move(0,1,0-i*2)
        			mx.polyCylinder(sx=3+i)
      			mx.move(0+i*2,1,0)
createAll()

EX.2	mx.file(f=1,new=1)
mx.polyCylinder(h=4,sx=3,ax=(0,0,0))
mx.move(0,2,0)
mx.polyCylinder(h=4,sx=4)
mx.move(0,2,-2)
mx.polyCylinder(h=4,sx=4)
mx.move(0,2,2)
mx.polyCylinder(h=4,sx=4)
mx.move(2.5,2,0)
mx.polyCylinder(h=4,sx=4)
mx.move(-2.5,2,0)
mx.polyCylinder(h=4,sx=5)
mx.move(-5,2,0)
mx.polyCylinder(h=4,sx=6)
mx.move(-7,2,0)
mx.polyCylinder(h=4,sx=7)
mx.move(-9,2,0)
mx.polyCylinder(h=4,sx=8)
mx.move(-11,2,0)
mx.polyCylinder(h=4,sx=5)
mx.move(0,2,-4)
mx.polyCylinder(h=4,sx=6)
mx.move(0,2,-6)
mx.polyCylinder(h=4,sx=7)
mx.move(0,2,-8)
mx.polyCylinder(h=4,sx=8)
mx.move(0,2,-10)
mx.polyCylinder(h=4,sx=5)
mx.move(5,2,0)
mx.polyCylinder(h=4,sx=6)
mx.move(7,2,0)
mx.polyCylinder(h=4,sx=7)
mx.move(9,2,0)
mx.polyCylinder(h=4,sx=8)
mx.move(11,2,0)
mx.polyCylinder(h=4,sx=5)
mx.move(0,2,4)
mx.polyCylinder(h=4,sx=6)
mx.move(0,2,6)
mx.polyCylinder(h=4,sx=7)
mx.move(0,2,8)
mx.polyCylinder(h=4,sx=8)
mx.move(0,2,10)
PolyHelix
c = coils (¨Ó¹Ç¹)
d =direction        sa = subdivisionsAXIS(ÃÙ»ÃèÒ§)      sco = subdivisionsCoils

EX.	mx.file(f=True,new=True)
mx.polyHelix()

mx.polyHelix(c=10)
mx.move(3,0,0)

mx.polyHelix(c=10,h=8)
mx.move(6,0,0)

mx.polyHelix(c=10,h=8,r=0.1)
mx.move(-3,0,0)

mx.polyHelix(c=20,h=8,r=0.1)
mx.move(-6,0,0) 

mx.polyHelix(c=20,h=8,r=0.1,w=5)
mx.move(-10,0,0)

mx.polyHelix(c=20,h=8,r=0.1,w=5,sco=3)
mx.move(-16,0,0)

mx.polyHelix(c=20,h=8,r=0.1,w=5,sco=3,sa=3)
mx.move(-22,0,0)	

PolyPipe

t = thickness
sh = subdivisionsHeight
sc = subdivisionsCaps(¨Ó¹Ç¹ªèÍ§ã¹á¡¹)


EX.	mx.file(f=True,new=True)
mx.polyPipe()

mx.polyPipe(r=3)
mx.move(4,0,0)

mx.polyPipe(r=2,h=4)
mx.move(4,0,0)

mx.polyPipe(r=1.5,h=8,t=0.1)
mx.move(4,0,0)

mx.polyPipe(r=1.5,h=8,t=0.1,sa=4,sh=4,sc=4)
mx.move(9,0,0)



c = center
nr = normal
fp = first
r = radius


EX.	import maya.cmds as mx
mx.file(f=1,new=1)
mx.circle(n='c1')
#mx.circle(n='c2',first=[0,5,0],fc=False)
mx.circle(n='c3',nr=[1,0,0])
mx.circle(n='c4',nr=[0,1,0],sw=180,r=3)



5th Part
Polyplane

f = force


EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyPlane(n='plane1',w=5,h=5)
mx.polyPlane(n='plane2',w=5,h=5,ax=(0,1,0))
mx.polyPlane(n='plane2',w=5,h=5,ax=(1,0,0))



Make polyplane to cube
EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyPlane(n='plane1',w=5,h=5)
mx.polyPlane(n='plane2',w=5,h=5,ax=(-1,0,0))
mx.move(-2.5,2.5,0)
mx.polyPlane(n='plane3',w=5,h=5,ax=(1,0,0))
mx.move(2.5,2.5,0)
mx.polyPlane(n='plane4',w=5,h=5)
mx.move(0,5,0)
mx.polyPlane(n='plane5',w=5,h=5,ax=(0,0,1))
mx.move(0,2.5,2.5)
mx.polyPlane(n='plane6',w=5,h=5,ax=(0,0,-1))
mx.move(0,2.5,-2.5)
Polyprism

w = sideLenght
ns= number of sides
sh= subdivisionsHeight
sc= subdivisionsCap


EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyPrism(n='pp1',w=5) 
mx.polyPrism(n='pp2',w=5,l=10,ax=(1,0,0))
mx.rotate(0,90,0)
mx.polyPrism(n='pp3',w=5,l=10,ax=(1,0,0))


Make polyprism to roof of house
EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyPrism(n='pp2',w=5,l=10,ax=(-1,0,0))
mx.rotate(0,90,0)
mx.polyPrism(n='pp3',w=5,l=10,ax=(-1,0,0)) 
















EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyPrism(n='pp2',w=5,l=10,ax=(-1,0,0))
mx.rotate(0,90,0)
mx.move(0,5,0)
mx.polyPrism(n='pp3',w=5,l=10,ax=(-1,0,0))
mx.move(0,5,0)

mx.polyCube(h=4)
mx.move(0,2,0)

mx.polyPrism(n='pp4',w=5,l=10,ns=8,ax=(-1,0,0),sh=2,sc=5)

PolyPyramid


Don’t have a height in pyramid (can’t set height)
EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyPyramid(n='ppm1')
mx.polyPyramid(n='ppm2',ns=3,ax=(0,-1,0))
mx.polyPyramid(n='ppm3',ns=4,w=5,ax=(0,-1,0),sh=4)
mx.polyPyramid(n='ppm4',ns=5,w=5,ax=(0,-1,0),sh=4)
mx.polyPyramid(n='ppm5',ns=6,w=5,ax=(0,-1,0),sh=4)
PolySphere

EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polySphere(r=2) 
mx.polySphere(r=2,sx=3,sy=3)


PolyTorus

tw =twist


EX.	import maya.cmds as mx 
	
mx.file(f=1,new=1)
mx.polyTorus()
mx.polyTorus(r=4)
mx.polyTorus(r=6,sr=0.5)


Change sr
EX.	import maya.cmds as mx 
	
mx.file(f=1,new=1)
mx.polyTorus()
mx.polyTorus(r=4)
mx.polyTorus(r=6,sr=7 )
EX.1	import maya.cmds as mx 

mx.file(f=1,new=1)

mx.polyTorus()
mx.polyTorus(r=4)
mx.polyTorus(r=6,sr=0.5)
mx.polyTorus(r=5,sr=0.5,tw=60,sx=4,sy=6)

mx.polyTorus(r=2,sr=0.5,tw=60,sx=7,sy=6)
mx.move(0,12,0)
mx.polyTorus(r=2,sr=0.5,tw=60,sx=6,sy=6)
mx.move(0,10,0)
mx.polyTorus(r=2,sr=0.5,tw=60,sx=5,sy=6)
mx.move(0,8,0)
mx.polyTorus(r=2,sr=0.5,tw=60,sx=4,sy=6)
mx.move(0,6,0)
mx.polyTorus(r=2,sr=0.5,tw=60,sx=3,sy=6)
mx.move(0,4,0)

EX.2	import maya.cmds as mx 
mx.file(f=1,new=1)

mx.polyTorus()
mx.polyTorus(r=4)
mx.polyTorus(r=6,sr=0.5)
mx.polyTorus(r=5,sr=0.5,tw=60,sx=4,sy=6)


for i in range (3,8):
    mx.polyTorus(r=2,sr=0.5,tw=10*i,sx=i,sy=i)
    mx.move(0,i*1.5,0)

EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
for i in range(0,6):
    mx.polyTorus(r=3,sr=0.3)
    mx.move(10-i*4,0,-12)
    
    mx.polyTorus(r=3,sr=0.3)
    mx.rotate(90)
    mx.move(13-i*4,0,-12)
    
    mx.polyTorus(r=3,sr=0.3)
    mx.move(10-i*4,0,12) 
    
    mx.polyTorus(r=3,sr=0.3)
    mx.rotate(90)
    mx.move(13-i*4,0,12)
    
    mx.polyTorus(r=3,sr=0.3,sx=3)
    mx.move(-10,0,10-i*4)
    
    mx.polyTorus(r=3,sr=0.3,sx=3,ax=(-1,0,0))
    mx.move(-10,0,10-i*4)
    
    mx.polyTorus(r=3,sr=0.3,sx=4)
    mx.move(12,0,10-i*4)
    
    mx.polyTorus(r=3,sr=0.3,sx=4,ax=(-1,0,0))
    mx.move(12,0,10-i*4)
    
SETATTR( ) TRANSLATEX

r = rotate
t = translate
s = scale
v= visibility (hide)

EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyCube(w=8,h=5,d=7,sx=2,sy=2,sz=2,n='myCube')

print(mx.listAttr('myCube',keyable=True))
#print(mx.listAt tr('muCube',k=1))


When you want to move, size and rotate by use setAttr
EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyCube(w=8,h=5,d=7,sx=2,sy=2,sz=2,n='myCube')

print(mx.listAttr('myCube',keyable=True))
#print(mx.listAttr('muCube',k=1))
#mx.setAttr('myCube.tx',5)
#mx.setAttr('myCube.ty',5)
#mx.setAttr('myCube.tz',5)

mx.setAttr('myCube.t',5,5,5)

mx.setAttr('myCube.ry',45)

mx.setAttr('myCube.r',0,135,60)

mx.setAttr('myCube.sx',7)

mx.setAttr('myCube.s',1,4,7)

mx.setAttr('myCube.v',1)


EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
mx.polyCube(w=8,h=5,d=7,sx=2,sy=2,sz=2,n='myCube')

print(mx.listAttr('myCube',keyable=True))

myCubeX=mx.polyCube()
mx.setAttr(myCubeX[0]+'.t',0,5,0)
print(myCubeX) 

mx.setAttr(myCubeX[1]+'.w',4) mx.setAttr(myCubeX[1]+'.h',7)
mx.setAttr(myCubeX[1]+'.d',2)
mx.setAttr(myCubeX[1]+'.sw',5)

EX.	import maya.cmds as mx 

mx.file(f=1,new=1)
myC = mx.polyCube()
mx.setAttr(myC[0]+'.t',4,0,4)
mx.setAttr(myC[1]+'.w',6)
mx.setAttr(myC[1]+'.h',6)
mx.setAttr(myC[1]+'.d',6)
mx.setAttr(myC[1]+'.sw',4)
mx.setAttr(myC[1]+'.sh',4)
mx.setAttr(myC[1]+'.sd',4)
'''
print(mx.getAttr(myC[0]+'.tx'))
Temp = mx.getAttr(myC[0]+'.ty'))
'''
myCX = mx.polyCube()
mx.setAttr(myCX[0]+'.t',lock=0)
mx.setAttr(myCX[0]+'.s',lock=0)

mx.setAttr(myCX[0]+'.tz',k=1)

EX.	import maya.cmds as mx 

myCX2 = mx.polyCube()
mx.select(myCX2[0]+'.f[0]',
          myCX2[0]+'.f[2]',
          myCX2[0]+'.f[4]',
          myCX2[0]+'.f[6]',)
          
for i  in range(0,7,2):
    mx.select(myCX2[0]+'.f['+str(i)+']',add=1) 
    
myPlane=mx.polyPlane(w=8,h=8,sw=8,sh=8)
print(mx.polyEvaluate(f=1))

for i in range (0,mx.polyEvaluate(f=1),2):
    mx.select(myPlane[0]+'.f['+str(i)+']',add=1)
    
numberOfFace = mx.polyEvaluate(f=1)
numberOfEdge = mx.polyEvaluate(e=1)
numberOfVertex = mx.polyEvaluate(v=1)
    
EX.	mx.file(f=1,new=1)
myPlane = mx.polyPlane(w=8,h=8,sw=8,sh=8)
positionVertex = mx.xform('.vtx[40]',q=1,t=1,ws=1)
print(positionVertex[1])
mx.polyCube(n='myCube')
mx.setAttr('myCube.t',positionVertex[0],
                        			positionVertex[1],
                        			positionVertex[2])

EX.	mx.file(f=1,new=1)
myPlane = mx.polyPlane(w=8,h=8,sw=8,sy=8)
for i in range(0,mx.polyEvaluate(v=1),2):
   	 mx.select(myPlane[0]+'.vtx['+str(i)+']')
    
  	  positionVertex = mx.xform(q=1,t=1,ws=1)
    
   	 mx.polySphere(n='sp'+str(i),r=0.3)
    
    	mx.setAttr('sp'+str(i)+'.t',positionVertex[0],
                           		 positionVertex[1],
                            		 positionVertex[2])    
                                       
#myPlane[0]+'.vtx['+str(i)+']' => 'pPlane1.vtx[0]' 'pPlane1.vtx[1]'
#'sp'+str(i)      => "sp0 sp5 sp10 sp15"
#'sp'+str(i)+'.t' => "sp0.t sp5.t sp10.t sp15.t"                           
