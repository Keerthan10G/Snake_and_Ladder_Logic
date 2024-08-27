import numpy
import time 
class Game: # class is used due to multiplayers 
  def __init__(self,i1,j1,k1,l1,m1,dict1,lad,list1):  #Construct is used beacause of get value for classs function
      self.i1=i1
      self.j1=j1
      self.k1=k1
      self.l1=l1
      self.m1=m1
      self.dict1=dict1
      self.lad=lad
      self.list1=list1
      
      
  def p1(self):
     enter=input("\nplayer 1 choice ")
     if enter=="1":
         a1=numpy.random.choice([1,2,3,4,5,6])
         time.sleep(3)
         print("dice value",a1) 
        
         if self.i1 in self.lad: # this is for increase of ladder and for this not specified list
             self.i1=self.i1+self.lad[self.i1] # used lad dict
             i=self.i1
             print("ladder",self.i1)
         elif self.i1 in self.list1:# but here we used special list1
             self.i1=self.i1-self.dict1[self.i1]#this is for snake
             i=self.i1
             print("Snake Bited")
         else:
             self.i1=self.i1+a1 # normal old to new position
             i=self.i1   
         print("player now in",self.i1)
         return i # we can use i1 also
         
  def p2(self):
    enter=input("\nplayer 2 choice ")
    if enter=="2":
        a2=numpy.random.choice([1,2,3,4,5,6])
        time.sleep(3)
        print("dice value",a2)
         
        if self.j1 in self.lad:
             self.j1=self.j1+self.lad[self.j1]
             j=self.j1
             print("ladder",self.j1)
        elif self.j1 in self.list1:
             self.j1=self.j1-self.dict1[self.j1]
             j=self.j1
             print("Snake Bited")
        else:
             self.j1=self.j1+a2
             j=self.j1
        print("player now in",self.j1)
        return j
        
  def p3(self):
     enter=input("\nplayer 3 choice ")
     if enter=="3":
         a3=numpy.random.choice([1,2,3,4,5,6])
         time.sleep(3)
         print("dice value",a3)
        
         if self.k1 in self.lad:
             self.k1=self.k1+self.lad[self.k1]
             k=self.k1
             print("ladder",self.k1)
         elif self.k1 in self.list1:
             self.k1=self.k1-self.dict1[self.k1]
             k=self.k1
             print("Snake Bited")
         else:
             self.k1=self.k1+a3
             k=self.k1
         print("player now in",self.k1)
         return k
        
  def p4(self):
     enter=input("\nplayer 4 choice ")
     if enter=="4":
         a4=numpy.random.choice([1,2,3,4,5,6])
         time.sleep(3)
         print("dice value",a4)
        
         if self.l1 in self.lad:
             self.l1=self.l1+self.lad[self.l1]
             l=self.l1
             print("ladder",self.l1)
         elif self.l1 in self.list1:
             self.l1=self.l1-self.dict1[self.l1]
             l=self.l1
             print("Snake Bited")
         else:
             self.l1=self.l1+a4
             l=self.l1
         print("player now in",self.l1)
         return l

  def c1(self):
     #enter=input("\nplayer 4 choice ")
     #if enter=="4":
         a5=numpy.random.choice([1,2,3,4,5,6])
         print("\ncomputer")
         time.sleep(3)
         print("dice value",a5)
        
         if self.m1 in self.lad:
             self.m1=self.m1+self.lad[self.m1]
             m=self.m1
             print("ladder",self.m1)
         elif self.m1 in self.list1:
             self.m1=self.m1-self.dict1[self.m1]
             m=self.m1
             print("Snake Bited")
         else:
             self.m1=self.m1+a5
             m=self.m1
         print("player now in",self.m1)
         return m 
         

i1=0
j1=0
k1=0
l1=0
m1=0
dict1={15:1,10:6,6:3,11:8}
lad={3:4,12:8,17:1}
list1=[6,10,15,11]
print("Snake and Ladder Game")
print("*** Rules of Game ***")
print("PLAYERS1 PRESS 1  PLAYERS2 PRESS 2 players3 press 3 players4 press 4")
print("If Snake Bites Then you will be taken Few Steps backward")
print("If Ladder gets Then you will be taken Few Steps forward")
ob=Game(i1,j1,k1,l1,m1,dict1,lad,list1)
ch=int(input("No of players"))
if ch==1:
    print("\n***computer vs you***")
    while True:
        i=ob.p1()
        if i>20:
             print("player 1 is winner")
             print("***Exit***")
             break
        m=ob.c1()
        if m>20:
            print("computer is winner")
            print("***Exit***")
            break


if ch==2:
    while True:
        i=ob.p1()
        
        if i==20 or i>20:
             print("**player 1 is winner**")
             break
        j=ob.p2()
        if j==20 or j>20:
             print("**player 2 is winner**")
             break
if ch==3:
   while True:
        i=ob.p1()
        if i>20:
             print("**player 1 is winner**")
             break
        j=ob.p2()
        if j>20:
             print("**player 2 is winner**")
             break
        j=ob.p3()
        if k>20:
             print("**player 3 is winner**")
             break
if ch==4:
   while True:
        i=ob.p1()
        if i>20:
             print("**player 1 is winner**")
             break
        j=ob.p2()
        if j>20:
             print("**player 2 is winner**")
             break
        k=ob.p3()
        if k>20:
             print("**player 3 is winner**")
             break
        l=ob.p4()
        if l>20:
             print("**player 4 is winner**")
             break


'''a=4
b=20
if a>10 and a!=10:
    print("ds")


i=0
j=0
i1=0
j1=0
print( (i!=20 and i>20) or (j>20 and i!=20))

dict1={15:1,10:6,6:3,11:8}

print(10-dict1[15])'''
