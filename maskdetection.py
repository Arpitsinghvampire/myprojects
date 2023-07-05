import os
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2 as cv
from sklearn.model_selection import train_test_split

from PIL import Image

with_mask=os.listdir('/Users/arpitsingh/Desktop/opencv projects/data/with_mask')


without_mask=os.listdir('/Users/arpitsingh/Desktop/opencv projects/data/without_mask')

print("the number of the masked images is ", len(with_mask))
print("the length of the unmasked images is ",len(without_mask))

#now we preprocess the image 
#we create the labels for the two class of the images
#0 for not wearing the mask 
#1 for wearing the mask

with_mask_labels=[1]*len(with_mask) #length of the list is 3725

without_mask_labels=[0]*len(without_mask) #contains all len(without_mask) values as 0

#now we combine the list
labels=with_mask_labels+without_mask_labels #the list will be concatenated



#image preprocessing

#first we resize the images
#convert the image to the numpy arrays
#this is for the masked data
with_mask_path='/Users/arpitsingh/Desktop/opencv projects/data/with_mask/'

data=[]
for image_file in with_mask:
    image=Image.open(with_mask_path+image_file) #this opens the image path and the image to be considered
    image=image.resize((128,128)) # we then resize the image to bring it to same size
    image=image.convert('RGBA') #some images are read as a black and white image image we convert it to a rgb image
    image=np.array(image) #we then convert it to a numpy array
    data.append(image) #we append the image  to the data

#no we do the same for the unmasked data

unmasked_path='/Users/arpitsingh/Desktop/opencv projects/data/without_mask/'
for img_files in without_mask:
    image1=Image.open(unmasked_path+img_files)
    #we again reshape the image
    image1=image1.resize((128,128))
    image1=image1.convert('RGB')
    image1=np.array(image1)
    data.append(image1)


#now we convert the image list and label list to a numoy array
x=np.array(data)
y=np.array(labels)


#now we train test split

x_train,y_train,x_test,y_test=train_test_split(x,y,test_size=0.2,random_state=2)


#now we scale down the image in the range 0 and 1
# so we divide it by 255

x_train_scaled=x_train/255
x_test_scaled=x_test/255

#now we build the convolution neural networks

import tensorflow as tf
from tensorflow import  keras

num_class=2

model=keras.Sequential()  #here we wstack all the layers

model.add(keras.layers.Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(128,128,3)))

#here 32 is the number of filters to be applied
#kernel size is 3,3 , activation function is relu and the image input is 128x128x3 , 3 because it contains three color channels 

model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))

model.add(keras.layers.Conv2D(64,kernel_size=(3,3),activation='relu'))  #64 filters will be applied
model.add(keras.layers.MaxPooling2D(pool_size=(2,2)))

model.add(keras.layers.Flatten()) #the data is converted to one dimension

model.add(keras.layers.Dense(128,activation='relu')) #dense layers also known as the fully connected layers
model.add(keras.layers.Dropout(0.5))  #some neurons are shut off to prevent the overfitting of the model

#we add another dense layer and introduce a dropout
model.add(keras.layers.Dense(64,activation='relu')) #dense layers also known as the fully connected layers
model.add(keras.layers.Dropout(0.5))  #some neurons are shut off to prevent the overfitting of the model

#now we scale down the data to the number of classes
model.add(keras.layers.Dense(num_class,activation='sigmoid'))
#the sigmoid activation function is generally used for binary class classification
#whereas the softmax function is used for multi class classification

#now we compile the programme
#here we set the loss and the optimizer function
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['acc'])

#now we train the neural network

history=model.fit(x_train_scaled,y_train,validation_split=0.1,epochs=5)

loss,accuracy=model.evaluate(x_test_scaled,y_test)

print("THE ACCURACY OF THE MODEL IS " ,accuracy)

h=history
#plot the loss value

plt.plot(h.history['loss'],label='train loss')
plt.plot(h.history['val_loss'],label='validation loss')
plt.legend()
plt.show()

#plot the accusracy value
plt.plot(h.history['acc'],label='train accuracy')
plt.plot(h.history['val_acc'],label='validation accuracy')
plt.legend()
plt.show()







