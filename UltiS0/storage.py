"""this file help to definde and save usable and redeay used pattern.abs
"""
import pickle
import numpy as np
import copy
import math

def Separator(data, MinBars=8, MaxBars=480, Period=15):
    """separate data into patterns
        data:
           open close high low volume
    """
    pattern_len = 8    
    gap=2
    result_len=4
    start_index = {}
    pattern_repeats = {}
    length = len(data[0])
    if length < MaxBars*3/2:
        ll = 2*length/3/MinBars
        MaxBars = 2**int(math.log(ll, 2))*MinBars
    while pattern_len < MaxBars:
        pattern_index = str(pattern_len)+'_'+str(gap)+'_'+str(result_len)
        start_index[pattern_index] = [ii for ii in range(0, length-(pattern_len+result_len), gap)]
        pattern_repeats[pattern_index] = 1
        if len(start_index[pattern_index])<=0:
            break
        pattern_len = pattern_len*2
        result_len = int(pattern_len/2)
        if gap <= 10:
            gap = gap + 1
        pass

    mirror_data = np.array(data)
    maxd = max(mirror_data[2])
    mind = min(mirror_data[3])
    mirror_data = (maxd+mind*2) - mirror_data
    return {
        'data': copy.copy(data),
        'mirror_data': mirror_data,
        'start_index': start_index,  
        #'pattern_repeats': pattern_repeats,
        'des': str(MinBars) +'_'+str(MaxBars)+'_'+str(Period)
    }    

def WriteRaw(data, name):
    path = './raw/'+name+'.pickle'
    with open(path, 'wb') as f:
        pickle.dump(data, f)
def WritePrimary(data, des):
    path = './primary/'+data['des']+des+'.pickle'
    with open(path, 'wb') as f:
        pickle.dump(data, f)
def WriteMature(mature_data, pattern_repeats):
    mature_path = './mature/'+'mature_data'+'.pickle'
    repeats_path = './mature/'+'pattern_repeats'+'.pickle'
    with open(mature_path, 'wb') as f:
        pickle.dump(mature_data, f)
    with open(repeats_path, 'wb') as f:
        pickle.dump(pattern_repeats, f)

def loadRawData():
    import os
    datas={}
    dirName = './raw'
    for name in os.listdir():         
        with open(os.path.join(dirName, name), 'rb') as f:
            datas[name] = pickle.load(f)
    return datas

def loadPrimaryData():
    with open('./primary/primary_data.pickle', 'rb') as f:
        return pickle.load(f)

def loadMatureData():
    with open('./mature/mature_data.pickle','rb') as f:
        mature_data = pickle.load(f)
        with open('./mature/pattern_repeats.pickle','rb') as ff:
            pattern_repeats = pickle.load(ff)
            return mature_data, pattern_repeats
    


def main():
    import random
    tem = [random.random() for i in range(1000)]
    Separator(tem)
    pass

if __name__ == '__main__':
    main()
