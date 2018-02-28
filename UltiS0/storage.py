"""this file help to definde and save usable and redeay used pattern.abs
"""
import pickle
import numpy as np
import copy

"""
#just for mature data
pattern_repeats[pattern_index] = {
    id_x: {fluermethod : '', fluerparameter: '', reperats: >=2},
    id_x: {fluermethod : '', fluerparameter: '', reperats: >=2},
    }
"""

def Separator(data, MinBars=8, MaxBars=480, Period=15):
    """separate data into patterns
        data:
           open close high low volume
    """
    pattern_len = 8    
    gap=2
    result=4
    start_index = {}
    pattern_repeats = {}
    while pattern_len < MaxBars:
        pattern_index = str(pattern_len)+'_'+str(gap)+'_'+str(result)
        start_index[pattern_index] = [ii for ii in range(0, len(data)-(pattern_len+result), gap)]
        pattern_repeats[pattern_index] = 1
        if len(start_index[pattern_index])<=0:
            break
        pattern_len = pattern_len*2
        result = int(pattern_len/2)
        if gap <= 10:
            gap = gap + 1
        pass

    mirror_data = np.array(data)
    maxd = max(mirror_data[2])
    mind = min(mirror_data[3])
    mirror_data = (maxd+mind*2) - mirror_data
    return {
        'data': copy.copy(data),
        'mirror_data': mirror_data
        'start_index': start_index,
        'pattern_repeats': pattern_repeats,
        'des': str(MinBars) +'_'+str(MaxBars)+'_'+str(Period)
    }    
    pass

def WriteRaw(data, des):
    path = './raw/'+data['des']+des+'.pickle'
    with open(path, 'wb') as f:
        pickle.dump(data, f)
def WritePrimary(data, des):
    path = './primary/'+data['des']+des+'.pickle'
    with open(path, 'wb') as f:
        pickle.dump(data, f)
def WriteMature(data, des):
    path = './mature/'+data['des']+des+'.pickle'
    with open(path, 'wb') as f:
        pickle.dump(data, f)

def loadData(dirName):
    """return [{the pickle}, ...]
    """
    import os
    datas=[]
    for name in os.listdir(dirName):         
        with open(os.path.join(dirName, name), 'rb') as f:
            datas.append(pickle.load(f))
    return datas

def main():
    import random
    tem = [random.random() for i in range(1000)]
    Separator(tem)
    pass

if __name__ == '__main__':
    main()