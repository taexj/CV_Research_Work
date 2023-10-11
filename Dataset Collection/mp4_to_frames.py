#!/usr/bin/env python
# coding: utf-8

# In[10]:


# import open cv
import cv2
import os

# change directory to where video is present then run command
video_path = "example.mp4"
video = cv2.VideoCapture(video_path)

success = True
count = 1
image_id = 1


output_path = "out_image"

while success:
    success , frame = video.read()
    
    if success == True:
        
        
        # for every 5th frame from video
    
        
        if count%5 == 0:
            # specify the output path and file name
            # i used count as a file name
            # you can use any
            name = str(image_id)+".jpg"
            image_id += 1
            
            # save the image
            cv2.imwrite(os.path.join(output_path , name), frame)
            #cv2.imwrite(name,frame)
        
        count += 1
    else:
        break

print("Total Extracted Frames :",image_id)   


# In[5]:


pwd


# In[6]:


cd D:\ML_research

