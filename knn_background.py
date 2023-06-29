#THE WORKING OF KNN IN A SIMPLE CODE
#HERE YOU SHOULD TAKE THE VALUE OF K AS AN ODD NUMBER
#this code is for the binary classsification
import math
import matplotlib.pyplot as plt
def euclidean_distance(x,y,z,w):
    return math.sqrt((x-y)**2+(z-w)**2)
def nearest_number(distance,train_coordinates,n):  #here n denotes the number of coordinates to be checked
    m=distance
    i=0
    checked=[]
    while  i<n:
        l=m.index(min(m))
        checked.append(train_coordinates[l])
        del(distance[l])
        del(train_coordinates[l])
        i=i+1
    return checked



import random
#now i generate around 3000 random coordinates in the range(0-200) and a binary class classification
train_coordinates=[]

for j in range(3000):
    sample=[]
    x_coordinate=random.randint(0,3000)
    y_coordinate=random.randint(0,3000)
    pos_class=[0,1,2]   #------------------------->change this for increasing the number of classes
    class1=random.choice(pos_class)  #this alloctes the class to the sample

    sample.append(x_coordinate)
    sample.append(y_coordinate)
    sample.append(class1)
    train_coordinates.append(sample)   #this creates a superset of all the sample spaces

#now we generate the test cases where i generate the random x  and y coordinates

#i choose to make a test sample of around 20
test_sample=[]
for j in range(20):
    test=[]
    x=random.randint(0,3000)
    y=random.randint(0,3000)
    test.append(x)
    test.append(y)
    test_sample.append(test)
test_sample_class=[]   #this will store the classes of the test cases
neighbours=int(input("ENTER THE NUMBER OF NEIGHBOURS FOR CHECKING :: "))  #take the number to be considered while taking the distance

#now i generate the distance of each element in the test sample to the train coordinates
all_distances=[]  #this shows all the distances
for i in range(len(test_sample)):
    distance_between_sample=[]
    for j in range(len(train_coordinates)):
        m=train_coordinates[j]
        z=test_sample[i]
        z2=train_coordinates[j]
        m=euclidean_distance(z[0],z2[0],z[1],z2[1])
        distance_between_sample.append(m)
    #now i know the distances of the test sample with all the coordinates

    s=nearest_number(distance_between_sample,train_coordinates,neighbours)
    #this returns the coordinates which are nearest to the test coordinate
    class_coordinate=[]
    for i in range(len(s)):
        m4=s[i]
        class_coordinate.append(m4[2])
    if class_coordinate.count(0)>class_coordinate.count(1):
        test_sample_class.append(0)
    else:
        test_sample_class.append(1)
print(test_sample_class)  #this will print the list along with the classes to which it belongs

#this part is for plotting the graph
x_final_class0=[]
x_final_class1=[]
y_final_class0=[]
y_final_class1=[]
for i in range(len(train_coordinates)):
    z=train_coordinates[i]
    if z[2]==0:
        x_final_class0.append(z[0])
        y_final_class0.append(z[1])
    else:
        x_final_class1.append(z[0])
        y_final_class1.append(z[1])
x_test=[]
y_test=[]  
for i in range(len(test_sample)):
    m3=test_sample[i]
    x_test.append(m3[0])
    y_test.append(m3[1])
    
plt.scatter(x_final_class0,y_final_class0,color='red',label='CLASS 0 ELEMENTS')
plt.scatter(x_final_class1,y_final_class1,color='blue',label='CLASS 1 ELEMENTS')
plt.scatter(x_test,y_test,color='black',label='TEST CASES')
plt.legend(loc='best')
plt.xlabel('X COORDINATE')
plt.ylabel('Y COORDINATE')
plt.show()










