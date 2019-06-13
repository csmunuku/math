#!/anaconda3/bin/python3
import sys

def usage():
    print("Provide a comma seperated list of numbers for which you want multiples")
    print("Example:")
    print('{} {}'.format(__file__, "7,8,9"))

def table(table_val):
    for i in range(1,11):
        print('{} x {} = {}'.format(table_val, i, int(table_val)*i), end="\t")
        print('{} x {} = {}'.format(table_val, i+10, int(table_val)*(i+10)))
    print('#' * 30)

if len(sys.argv) == 2:
   for num in sys.argv[1].split(','):
     table(num)
else:
   usage()

