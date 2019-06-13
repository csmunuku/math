#!/anaconda3/bin/python3
# ./multiples.py <some_number>
import sys

def multiples(number):
    one=list(range(2, 21))
    two=list(range(2, 21))
    for i in one:
        for j in two:
          result=i*j
          if result > int(number):
             break
          elif int(number) == result:
             print('{} x {} = {}'.format(i,j,result))

def usage():
    print("Provide a number below 401 for which you want multiples")
    print("Example:")
    print('{} {}'.format(__file__, "144"))

if len(sys.argv) == 2 and sys.argv[1].isdigit():
   multiples(sys.argv[1])
else:
   usage()
