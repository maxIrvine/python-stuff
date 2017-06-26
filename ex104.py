# for num in range(1,11): 
#     print num

# start = int(raw_input("What number do you want to start at? "))
# end = int(raw_input("What number do you want to end at? "))
# for num in range(start, end+1):
#     print num

# for num in range(1, 11):
#     if (num%2 != 0):
#         print num

# want = True;
# coin = 0;
# while want:
#     another = raw_input("Do you want another? ")
#     if (another == "yes"):
#         coin = coin + 1
#         print "You have " + str(coin) 
#         want = True
#     else:
#         want = False

# for num in range (1, 6):
#     print "*" * 5

# num = int(raw_input("How many * do you want? "))
# for number in range(1, num+1):
#     print "*" * num

# height = int(raw_input("What do you want the height to be? "))
# width = int(raw_input("What do you want the width to be? "))
# print "*" * width
# for y in range (1, height-1):
#     print "*" + (" " * (width-2)) + "*"
# print "*" * width


# num = 8
# for j in range (0, num):
#         print " " * ((num-j)/2) + ("* " * j) + " " * ((num-j-1)/2)

# num = int(raw_input("Please enter number! "))
# for num in range(1, num+1):
#     equal = num * num
#     print "%d x %d = %d" % (num, num, equal)

# message = raw_input("Enter a message! ")
# length = len(message)
# print "*" * (length+2)
# print "*" + message + "*"
# print "*" * (length+2)

# for num in range(1, 100):
#     print num*(num+1)/2

# number = int(raw_input("Give a number! "))
# for num in range(1,11):
#     if (number % num == 0):
#         print "The number is divisable by %s" % num


import time 

num = int(raw_input("What number do you want to start at? "))
if (num >= 200):
    num = 25
while (num>=0):
    print num
    time.sleep(1)
    num = num - 1
print "BLAST OFF!"