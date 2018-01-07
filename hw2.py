
myList = [i for i in range(7)]
print(myList)
# first reversing, then ignoring:
reversed1 = myList[::-1][2:]
print(reversed1)
# first ignoring, then reversing:
reversed2 = myList[2:][::-1]
print (reversed2)

if(reversed1[2] == 7):
    print("Boom")
else:
    print("The number is={0}".format(reversed1[2]))