import random

my_random_number = random.randint(1,10)
secret_number = 5
count = 5
guess = int(raw_input("Guess a number between 1 and 10."))
while (my_random_number != guess):
    
    if (guess < my_random_number):
        print "%s is to low " % guess
        print "You have %s guess's left" % (count)
        count = count - 1
        print "You have %s guess's left" % (count)
    else:
        print "%s is to high " % guess
        count = count - 1
        print "You have %s guess's left" % (count)
    guess = int(raw_input("Guess a number between 1 and 10."))
    
print "Yay you got it! "

again = raw_input("Do you want to play again? ")
while (againw): 
    my_random_number = random.randint(1,10)
    secret_number = 5
    count = 5
    guess = int(raw_input("Guess a number between 1 and 10."))
    while (my_random_number != guess):
        
        if (guess < my_random_number):
            print "%s is to low " % guess
            print "You have %s guess's left" % (count)
            count = count - 1
            print "You have %s guess's left" % (count)
        else:
            print "%s is to high " % guess
            count = count - 1
            print "You have %s guess's left" % (count)
        guess = int(raw_input("Guess a number between 1 and 10."))
        
    print "Yay you got it! "