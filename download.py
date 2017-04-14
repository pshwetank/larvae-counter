import urllib.request
import cv2
import numpy as np
import os

def store_raw_images():
  neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02909870'
  neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

  if not os.path.exists('neg'):
    os.makedirs('neg')
  pic_num = 1
  
  for i in neg_image_urls.split('\n'):
    try:
       print(i)
       urllib.request.urlretrieve(i, "neg/"+str(pic_num)+'.jpeg')
       img = cv2.imread("neg/"+str(pic_num)+'.jpeg', cv2.IMREAD_GRAYSCALE)
       resized_image = cv2.resize(img, (100,100))
       cv2.imwrite("neg/"+str(pic_num)+'.jpeg', resized_image)
       pic_num +=1
        
    except Exception as e:
       print(str(e))

store_raw_images()
