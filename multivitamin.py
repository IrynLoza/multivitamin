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
    
    return



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ YOU ARE STAR! ALL TESTS PASSED!\n')