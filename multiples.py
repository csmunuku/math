#!/anaconda3/bin/python3
# ./multiples.py <some_number>
import sys

def multiples(number):
    one=list(range(2, 21))
    two=list(range(2, 21))
    for i in one:
#        print('i is - {}'.format(i))
        for j in two:
#          print('j is - {}'.format(i))
          result=i*j
#          print('result is - {}'.format(result))
          if result > int(number):
#             print("breaking here")
             break
          elif int(number) == result:
#             print("Matched here")
             print('{} x {} = {}'.format(i,j,result))

multiples(sys.argv[1])
