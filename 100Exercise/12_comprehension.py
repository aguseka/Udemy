myrange = list(range(1,21))
mylist = []

''' This is my solution'''
for number in myrange:
    number = number * 10
    mylist.append(number)
print("this is my solution", mylist)


''' This is solution from the instructor'''

print( "this is from the instructor \n", [10 * x  for x in myrange])