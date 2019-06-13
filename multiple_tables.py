#!/anaconda3/bin/python3
# usage: ./multiple_tables.py 7,8,9
import sys

def usage():
    print("Provide a comma seperated list of numbers for which you want multiples")
    print("Example:")
    print('{} {}'.format(__file__, "7,8,9"))

def table(table_val):
    mylist = list(range(2, 21))
    table_list = table_val.split(',')
    for i, j in [(i,j) for i in table_list for j in mylist]:
        result=int(i)*int(j)
        print('{} x {} = {}'.format(i, j, result))

if len(sys.argv) == 2:
   table(sys.argv[1])
else:
   usage()
