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
    f = lambda x: GRID_HEIGHT*(x- mind)/(maxd-mind)
    scale_data = [f(i) for i in data]
    return scale_data
    pass

def is_same_source(data1, data2):
    
    pass
#similarity description
def smooth_and_distance(data1, data2, treshold):

    pass
#similarity description
def data_compress(data1, data2, treshold):

    pass

def idx_maker(s):
    return s

def main(data, MinBars=8, MaxBars=480, Period=15):
    #read and tidy the comming data
    incomedata = storage.Separator(data)
    for pattern, start_list in enumerate(incomedata['start_index']):  #for the unlike length of pattern
        compare_primary = Primary_Data['start_index'][pattern]
        compare_mature = Mature_Data['start_index'][pattern]
        name = pattern.split('_')
        pattern_len = int(name[0])
        gap = int(name[1])
        result_len = int(name[2])

        for index in start_list: #for the same length of pattern in differ palce
            data1 = incomedata['data'][index: index+pattern_len]
            data1_result = incomedata['data'][index+pattern_len: index+pattern_len+result_len]
            passover = False
            for mature_index in compare_mature: #every of them compare to the any of mature_data: original and mirror data
                data2 = Mature_Data['data'][mature_index: mature_index+pattern_len]
                data2_result = Mature_Data['data'][mature_index+pattern_len: mature_index+pattern_len+result_len]
                m_data2 = Mature_Data['mirror_data'][mature_index: mature_index+pattern_len]
                m_data2_result = Mature_Data['mirror_data'][mature_index+pattern_len: mature_index+pattern_len+result_len]
                # here make the compare....
                if is_same_source(data1, data2):
                    passover = True
                    break
                # for para in parameters:
                #     smooth_and_distance(data1, data2, para)
                temresult = smooth_and_distance(data1, data2, 90)
                if temresult[0]:
                    if Pattern_Repeats[pattern].get(idx_maker(temresult[1])):
                        #record the infomation to pattern_repeats in storage
                        pass
                    else:
                        Pattern_Repeats[pattern][idx_maker(temresult[1])]={}
                        pass
                    passover = True
                    break
                
                temresult = data_compress(data1, data2, 90)
                if temresult[0]:
                    if Pattern_Repeats[pattern].get(idx_maker(temresult[1])):
                        #record the infomation to pattern_repeats in storage
                        pass
                    else:
                        Pattern_Repeats[pattern][idx_maker(temresult[1])]={}
                        pass
                    passover = True
                    break
                

            if passover:
                passover = False
                continue
            ##########################################################################
            for primary_index in compare_primary: 
                data3 = Primary_Data['data'][primary_index: primary_index+pattern_len]
                data3_result = Primary_Data['data'][primary_index+pattern_len: primary_index+pattern_len+result_len]
                m_data3 = Primary_Data['mirror_data'][primary_index: primary_index+pattern_len]
                m_data3_result = Primary_Data['mirror_data'][primary_index+pattern_len: primary_index+pattern_len+result_len]
                # here make the comparation....
                if is_same_source(data1, data3):
                    break
                # for para in parameters:
                #     smooth_and_distance(data1, data2, para)
                temresult = smooth_and_distance(data1, data3, 90)
                if temresult[0]:
                    if Pattern_Repeats[pattern].get(idx_maker(temresult[1])):
                        #record the infomation to pattern_repeats in storage
                        #delete from primary and add to mature
                        pass
                    else:
                        Pattern_Repeats[pattern][idx_maker(temresult[1])]={}
                        pass
                    break
                
                temresult = data_compress(data1, data3, 90)
                if temresult[0]:
                    if Pattern_Repeats[pattern].get(idx_maker(temresult[1])):
                        #record the infomation to pattern_repeats in storage
                        #delete from primary and add to mature
                        pass
                    else:
                        Pattern_Repeats[pattern][idx_maker(temresult[1])]={}
                        pass
                    break        

    pass

if __name__ == '__main__':
    main()


