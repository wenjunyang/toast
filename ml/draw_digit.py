__author__ = 'jiadong'

import pandas as pd
import numpy as np
from matplotlib.pylab import plt

data = pd.read_csv("train.csv")

dic = {}
for index, row in data.iterrows():
    key = row['label']
    dic.setdefault(key, []).append(row)


def extract_digit(n):
    img = pd.DataFrame(dic[n])
    mean = img.describe().loc['mean'].values
    return mean


def transfer(digit_pixel):
    img_matrix = np.zeros((28,28))
    for i in range(0,27):
        for j in range (0,27):
            index = i * 28 + j
            img_matrix[i][j] =digit_pixel[index+1]
    return img_matrix


def display(digit):
    mean = extract_digit(digit)
    img = transfer(mean)
    plt.imshow(img,cmap = plt.get_cmap('gray'))
    plt.axis('off')

# Display digit 9.
display(9)
plt.show()