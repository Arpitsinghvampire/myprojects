#THIS CODE IMPLEMENTS THE LINEAR REGRESSION MODEL FROM SCRATCH
#FIRST I WILL GENERATE A RANDOM POINTS OR THE TRAIN CASE

import random
def mean_squared_error(m,b,train_cases):
    x3=0
    for i in range(len(train_cases)):
        z=train_cases[i]
        y_pred=m*z[0]+b
        x3=x3+(y_pred-z[1])**2
    return x3/len(train_cases)
#mean_squared_error=1/n E(y-(mx+b))**2  

#we need to minimize the error function for that we will use the gradient descent method
#gradient with respect to m is -2/n E(y-(mx+b))*x   , here E is the sum of i=0 to i=n
#gradient with respect to b is -2/n E(y-(mx+b))
def gradient_descent(m,b,l,train_cases):   #here l is the learning rate
    sum1=0 #this calculates sum with respect to m
    sum2=0 #this calculates sum with respect to b
    for i in range(len(train_cases)):
        z=train_cases[i]
        sum1=sum1+((m*z[0]+b)-z[1])*z[0]
        sum2=sum2+((m*z[0]+b)-z[1])
    grad_m=2*sum1/len(train_cases)
    grad_b=2*sum2/len(train_cases)
    print(grad_m)
    print(grad_b)
    m=m-l*grad_m
    b=b-l*grad_b
    return m,b


train_cases=[]
#here i will generate a random train sample of 20 coordinates
for i in range(20):
    x_coordinate=random.randint(0,100)
    y_coordinate=random.randint(0,100)
    train=[]
    train.append(x_coordinate)
    train.append(y_coordinate)
    train_cases.append(train)
print(train_cases)   #this prints the train coordinate

#the linear regression model fits a line to the model , this line always passes through the mean of the x and y coordinate
#here we first consider a min sqaured errror and start with a random value of m and b and then use gradient descent 
#to tweak the values of m and b
#lets start be a random value of m and b  
m=random.randint(0,10)
b=random.randint(0,10)
l=0.001 #this is the learning rate

y_coordinates=[]
x_coordinates=[]
for i in range(100):
    print("---------------------------------------------------------------------")
    print("THE ITERATION NUMBER IS ",i+1)
    z=mean_squared_error(m,b,train_cases)
    print(z)   #this calculates the error 

    #now we will update the values of m and b
    

    
    print("THE VALUE OF M IS "+ str(float(m)) +" AND THE VALUE OF B IS "+ str(float(b)))
    x1,y1=gradient_descent(m,b,l,train_cases)
    m=x1
    b=y1
    print("-----------------------------------------------------------------------")

import matplotlib.pyplot as plt
x_coordinates=[]
y_coordinates=[]
line_coordinate=[]
for i in range(len(train_cases)):
    z1=train_cases[i]
    x_coordinates.append(z1[0])
    y_coordinates.append(z1[1])
    line_coordinate.append(m*z1[0]+b)
plt.scatter(x_coordinates,y_coordinates,color='red')
plt.scatter(x_coordinates,line_coordinate,color='blue')


plt.xlabel("X LABEL")
plt.ylabel("Y LABEL")
plt.show()







