#!/anaconda3/bin/python3
import sys
def table(table_val):
    for i in range(1,21):
        print('{} x {} = {}'.format(table_val, i, int(table_val)*i))

table(sys.argv[1])
