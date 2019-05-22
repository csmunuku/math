#!/anaconda3/bin/python3
def table(table_val):
    for i in range(1,11):
        print('{} x {} = {}'.format(table_val, i, int(table_val)*i), end="\t")
        print('{} x {} = {}'.format(table_val, i+10, int(table_val)*(i+10)))
    print()

for i in range(1,21):
    table(i)
