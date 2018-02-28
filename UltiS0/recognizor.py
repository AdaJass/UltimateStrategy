import storage
import numpy as np

GRID_HEIGHT = 1000
Primary_Data = storage.loadData('./primary')
Mature_Data = storage.loadData('./mature')

def rescale(data):
    """make data at the same grid scale
    """
    maxd = max(data)
    mind = min(data)
    g=maxd - mind
    s=GRID_HEIGHT/g
    f = lambda x: GRID_HEIGHT*(x-mind)/(maxd-mind)
    scale_data = [f(i) for i in data]
    return scale_data
    pass

#similarity description
def smooth_and_distance(data1, data2, treshold):

    pass
#similarity description
def data_compress(data1, data2, treshold):

    pass

def main():
    #read and tidy the comming data

    #compare with the matrue, if true, increase the repeats and use the result

    ##compare with the primary, if true, move to the mature

    ###insert into primary if possible.

    #update the data to pickle
    pass

if __name__ == '__main__':
    main()


