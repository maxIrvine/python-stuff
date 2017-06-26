# string = raw_input("give me a string! ")
# print string.upper()

# print string[0].upper() + string[1: len(string)]

# print string[::-1]

# leet = {"a":4,"e":3,"g":6,"i":1,"o":0,"s":5,"t":7}
# arr = list(string)
# final = ""
# for x in arr:
#     print leet[x],

# array = ['a', 'e', 'i', 'o', 'u']
# arr = list(string)
# count = 0
# letter = 0
# for x in range(0, len(arr)):
#     if (arr[x] in array and arr[count+1] == arr[count] and letter < 4):
#         arr.insert(x, arr[x])
#         letter = letter + 1
#     count = count + 1
# print arr

# print ord('a')
# print ord('b')

def decrypt(word, shift):
    arr = list(word)
    # print arr
    asci = []
    final = []
    # print arr
    length = len(arr)
    for x in range(0,length):
        # print arr[x]
        if (ord(arr[x]) >= 97 and ord(arr[x]) <= 122):
            num = ord(arr[x])
            asci.append(num)
        else:
            asci.append(1)
        # print asci
        # print num
    for x in range(0, length):
        if (asci[x] != 1):
            if (asci[x] + shift > 122):
                asci[x] = asci[x] + shift - 26
            else:
                asci[x] = asci[x]+shift
        # print asci
    for x in range(0, length):
        if(asci[x] == 1):
            final.append(" ")
        else:
            letter = chr(asci[x])
            final.append(letter)
    print "Shift %s: %s " % (shift, ''.join(final))

decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 1)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 2)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 3)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 4)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 5)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 6)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 7)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 8)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 9)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 10)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 11)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 12)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 13)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 14)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 15)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 16)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 17)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 18)
decrypt("lbh zhfg hayrnea jung lbh unir yrnearq", 19)

def arrayCount(array):
    total = 0
    for x in array:
        total = total + x
    return total

arr = [3,4,5,6]
print "The array adds up to: %s" % arrayCount(arr)

def largestValue(var):
    largest = 0
    for x in var:
        if (x > largest):
            largest = x
    return largest
    
print "The largest value in the array is: %s" % (largestValue([3,4,7,19,2]))


# var = [3,4,-5,6,2,9,-8]
# factor = 2
# smallest = var[0]
# for x in var:
#     if (x < smallest):
#         smallest = x
# print smallest

# for x in var:
#     if (x%2==0):
#         print x
# pos = []
# for x in var:
#     if (x>0):
#         pos.append(x)
#         print pos

# factorList = []
# for x in var:
#     factorList.append(x*factor)
# print factorList
# list1 = [2,3,4]
# list2 = [3,4,6]
# list3 = []

# for x in range(0, len(list1)):
#     list3.append(list1[x] * list2[x])
# print list3

# list1 = [[1, 3], [2, 4], [3, 2]]
# list2 = [[5, 2], [1, 0], [4, 7]]
# list3 = [[],[], []]

# width = len(list1)
# height = 2

# for x in range(0, len(list1)):
#     for y in range(0, height):
#         list3[x].append(list1[x][y] + list2[x][y])
# print list3

# arr = ["hi", "my", "my", "name", "is", 22]
# dup = []
# for x in arr:
#     if (x in dup):
#         print ""
#     else:
#         dup.append(x)
# print dup



