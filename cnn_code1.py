#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.layers import Convolution2D


# In[2]:


from keras.layers import MaxPooling2D


# In[3]:


from keras.layers import Flatten


# In[4]:


from keras.layers import Dense


# In[5]:


from keras.models import Sequential


# In[6]:


model = Sequential()


# In[7]:


model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(64, 64, 3)
                       ))


# In[8]:


model.summary()


# In[9]:


model.add(MaxPooling2D(pool_size=(2, 2)))


# In[10]:


model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                       ))


# In[11]:


model.add(MaxPooling2D(pool_size=(2, 2)))


# In[12]:


model.summary()


# In[13]:


model.add(Flatten())


# In[14]:


model.summary()


# In[15]:


model.add(Dense(units=128, activation='relu'))


# In[16]:


model.summary()


# In[17]:


model.add(Dense(units=1, activation='sigmoid'))


# In[18]:


model.summary()


# In[19]:



model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[20]:


from keras_preprocessing.image import ImageDataGenerator


# In[21]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        'cnn_dataset/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        'cnn_dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
model.fit(
        training_set,
        steps_per_epoch=10,
        epochs=epochs,
        validation_data=test_set,
        validation_steps=800)


# In[22]:


accuracy=out.history['accuracy'][-1] *100


# In[ ]:


print("Accuracy for the model is : " , accuracy ,"%")


# In[ ]:


f= open("/mlops-ws/accuracy.txt","w+")
f.write(str(accuracy))
f.close()

f= open("epoch.txt","w+")
f.write(str(epochs))
f.close()

