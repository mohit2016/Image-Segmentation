import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import time
import os

def extract_image(image,n):


    img = "./static/" + image
    img = plt.imread(img)
    
    
    scale_percent = 50 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


#     img =cv2.resize(img, (500,330))

    img_reshape = img.reshape((-1,3))


    from sklearn.cluster import KMeans
    n_clusters = n
    kmeans = KMeans(n_clusters)
    kmeans.fit(img_reshape)

    centers = kmeans.cluster_centers_
    centers = np.round(centers)



    extracted_img = np.zeros((img.shape[0]*img.shape[1],3), dtype="int")

    for i in range(extracted_img.shape[0]):
        extracted_img[i] = centers[kmeans.labels_[i]]

    extracted_img = extracted_img.reshape((img.shape[0],img.shape[1],3))
    
    
    plt.imsave("static/extracted_images/extracted_"+str(n)+image, extracted_img/255.)
    
    
