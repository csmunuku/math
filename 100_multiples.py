#!/anaconda3/bin/python3
import sys

def multiples(number):
    one=list(range(2, 101))
    two=list(range(2, 101))
    for i in one:
        for j in two:
          result=i*j
          if result > int(number):
             break
          elif int(number) == result:
             print('{} x {} = {}'.format(i,j,result))

if len(sys.argv) == 2 and sys.argv[1].isdigit():
   multiples(sys.argv[1])
else:
   print("Provide a number less than 10000 as argument to the script")
