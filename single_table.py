#!/anaconda3/bin/python3
import sys
def table(table_val):
    for i in range(1,21):
        print('{} x {} = {}'.format(table_val, i, int(table_val)*i))

def usage():
    print("Provide a number for which you want multiples")
    print("Example:")
    print('{} {}'.format(__file__, "9"))

if len(sys.argv) == 2 and sys.argv[1].isdigit():
   table(sys.argv[1])
else:
   usage()
