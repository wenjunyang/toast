import numpy as np
import pandas
from matplotlib.pylab import plt

train = pandas.read_csv('data/train.csv')

for index, row in train.iterrows():
    key = row['label']
    print 'it is:' + str(key)
    data = np.array(row[1:]).reshape((28, 28))
    plt.imshow(data, cmap=plt.get_cmap('gray'))
    plt.show()
    # raw_input('press enter to continue...')
