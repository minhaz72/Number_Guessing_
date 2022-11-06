# let's create tik tak toe more efficinetly : 
import random 
x= random.randint(0,1)
y=  int(input('enter a number between 1 and 0 : '))
a = [[x, y , x ] , 
     [y,  x ,y],
     [x , y  , x ]]
if x==  y : 
    print( 'win : ' , a )
else :
    print('you lose : ' , a )
    