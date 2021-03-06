#!/anaconda3/bin/python3
import sys
import random

def usage():
    print("Provide a number that you want to test the multiples")
    print("Example:")
    print('{} {}'.format(__file__, "9"))

def test_tables(table_val):
    mylist = list(range(2, 20))
    random.shuffle(mylist)
    for i in mylist:
        one=table_val
        two=i
        result=int(one)*int(two)
        print('{0:2} x {1:2} = \t | {2:2} x {3:2} = {4}'.format(one,two,one,two,result))

if len(sys.argv) == 2 and sys.argv[1].isdigit():
   test_tables(sys.argv[1])
else:
   usage()
