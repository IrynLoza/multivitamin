"""Rick is really fond of fruit juices, but he is bored of their traditional flavours. 
Therefore, he has decided to mix as many of them as possible to obtain something 
entirely new as a result.
What is the maximum number of flavours that Rick can mix:
>>> count_multivitamin([10, 2, 1, 1], [10, 3, 2, 2])
2
>>> count_multivitamin([1, 2, 3, 4], [3, 6, 4, 4])
3
>>> count_multivitamin([2,3], [3, 4])
1
>>> count_multivitamin([1, 2, 3, 4], [0, -2, -1, -5])
0
"""

def count_multivitamin(juice, capacity):
    """Return maximum number of juice flavours can mix"""
    sum_sets = {
        1: juice
    }

    #Add data to hashmap
    for i in range(len(juice)):
        summ = juice[i]
        y = i+1
        count = 1
        while y < len(juice):
            summ+= juice[y]
            y+= 1
            count+= 1
            if count not in sum_sets:
                sum_sets[count] = []
                sum_sets[count].append(summ) 
            else:  
                sum_sets[count].append(summ)            
        count = 0    

    #Sort capacity
    for i in range(len(capacity)):
        for y in range(i+1, len(capacity)):
            if capacity[i] < capacity[y]:
                capacity[i], capacity[y] = capacity[y], capacity[i]           

    result = 0
    #Iterate through hasm map
    for key in sum_sets:
        for i in range(len(sum_sets[key])):
            if sum_sets[key][i] <= capacity[i]:
                if result < key:
                    result = key
    
    return result



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ YOU ARE STAR! ALL TESTS PASSED!\n')