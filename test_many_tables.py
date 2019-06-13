#!/anaconda3/bin/python3
# usage: ./test_many_tables.py 7,8,9
import sys
import random

def test_tables(table_val):
    mylist = list(range(2, 20))
    table_list = table_val.split(',')
    for x in range(1,101):
       one=random.choice(table_list)
       two=random.choice(mylist)
       result=int(one)*int(two)
#       print('{0:2} x {1:2} = \t | {2:2} x {3:2} = {4}'.format(one,two,one,two,result))
       print('{0:2} x {1:2} = '.format(one,two))

def usage():
    print("Provide a comma seperated list of numbers for which you want multiples")
    print("Example:")
    print('{} {}'.format(__file__, "7,8,9"))

if len(sys.argv) == 2:
   test_tables(sys.argv[1])
else:
   usage()
