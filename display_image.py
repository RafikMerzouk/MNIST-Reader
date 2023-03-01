import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ImageDisplay :
    def __init__(self, df) :
        self.df = df
        self.images = None
        self.labels = None
        self.load_images()

    def load_images(self) :
        self.labels = self.df.iloc[:, 0].values

        self.images = self.df.iloc[:, 1:].values
        # self.images = self.images.astype('float32') / 255.0
        # self.images = self.images.reshape((self.images.shape[0], 784))

    def display_image(self, ax, index):
        image = self.images[index][0]
        image = np.reshape(image, (28, 28))
        
        ax.imshow(image, cmap='gray')