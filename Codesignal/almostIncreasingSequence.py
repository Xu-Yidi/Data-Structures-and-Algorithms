def almostIncreasingSequence(sequence):
    times = 0
    index = []
    for i in range(0, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            times+=1
            index.append(i)
    sequence1 = sequence.copy()       
    
    if times>1:
        return False
    else:
        if remove_index(sequence, index[0]) is False and remove_index(sequence1, index[0]+1) is False:
            return False
        else:
            return True
       
def remove_index(sequence,index):
    del sequence[index]
    for i in range(0, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return False
    return True
