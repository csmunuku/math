#!/anaconda3/bin/python3
# usage: ./test_many_tables.py 7,8,9
import sys
import random

def test_tables(table_val):
    mylist = list(range(2, 20))
    table_list = table_val.split(',')
    random.shuffle(mylist)
    random.shuffle(table_list)
    for i, j in [(i,j) for i in mylist for j in table_list]:
        one=j
        two=i
        result=int(one)*int(two)
        print('{0:2} x {1:2} = \t | {2:2} x {3:2} = {4}'.format(one,two,one,two,result))

test_tables(sys.argv[1])
