#K means algorithm is an unsupervised algorithm , this is based o formation of clusters
#this algorithm basically puts the points in the clusters on the basis of the distance of the medians from the point

#first we will generate random points
import random
import math
def euclidean_distance(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
test_sample=[]
for  i in range(300):
    sample=[]
    x_coordinate=random.randint(0,3000) #the range of x coordinate is 0 to 2999
    y_coordinate=random.randint(0,3000)
    #since this is an unsupervised algorithm the data is not available which tells us about which class it belongs to
    sample.append(x_coordinate)
    sample.append(y_coordinate)
    test_sample.append(sample)
#now our train data has been computed
#we perform the k means algorithm until and unless our median stops changing

#here we need to choose how many clusters are there 
#here i choose a random point to start as the center
# we choose the point the point randomly
m=int(input("ENTER THE NUMBER OF CLUSTERS :: "))
median_coordinate=[]
for i in range(m):
    median=[]
    x_coordinate=random.randint(0,3000)
    y_coordinate=random.randint(0,3000)
    median.append(x_coordinate)
    median.append(y_coordinate)
    median_coordinate.append(median)

print(median_coordinate) #this gives the immediate coordinate of the medians
#here we choose the euclidean distance, we can also choose the minkowski distance or the manhattan distance
cluster_points=[]
for i in range(m):
    l=[]
    cluster_points.append(l)

for i in range(len(test_sample)):
    distance_between_medians=[]
    z=test_sample[i]
    for j in range(len(median_coordinate)):
        s=median_coordinate[j]
        m3=test_sample[i]                             #this part is for finding the distance
        k=euclidean_distance(m3,s)
        distance_between_medians.append(k)
            
    print("-------------------------------------------")
    print("the iteration number is ",i+1)
    print(distance_between_medians)
    z3=median_coordinate
    k3=distance_between_medians.index(min(distance_between_medians))  #this finds the minimum distance with the median
#the minimum distance between the median and the coordinate would mean that the point belongs to that cluster
    belongs_to=cluster_points[k3]  #the coordinate is then appended to the cluster
    
    belongs_to.append(z)
    print(belongs_to)
    l2=median_coordinate[k3]   #this contains the original cluster median point coordinate
    print(median_coordinate)
    
    sum=0
    sum1=0
    #after including the point , the cluster median is again recalculated
    for i in  range(len(belongs_to)):  
        s=belongs_to[i]
        sum=sum+s[0]
        sum1=sum1+s[1]
    #now we calculate the median
    l2[0]=(sum+l2[0])//(len(belongs_to)+1)   #this is the new median point for x ccordinate
    l2[1]=(sum+l2[1])//(len(belongs_to)+1)  #this is new median for the y coordinate
    z4=median_coordinate
    print(median_coordinate)  #this prints the new median coordinate
    print("--------------------------------------------")
     #if the median coordinate does not change its coordinate then we should break out from the process
for i in range(len(cluster_points)):
    print("the cluster "+ str(i+1) + " has  the elements")
    print(cluster_points[i])
    print("*********************************************")









