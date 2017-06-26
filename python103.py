day = int(raw_input("Day (0-6)? "))
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print week[day]
if (day == 0 or day == 6):
    print "Sleep in"
else:
    print "Go to work"

celsius = int(raw_input("Enter a temperature in celsius: "))
fahrenheit = (celsius*1.8) + 32
print fahrenheit 


# bill = float(raw_input("Total bill amount? "))
# service = raw_input("Level of service? ")
# split = float(raw_input("Split how many ways? "))
# if (service == "good"):
#     print "Tip Amount: $%f" % (bill*1.2)
#     print "Amount per person: $%f" % (bill/split)
# elif (service == "fair"):
#     print "Tip Amount: $%f" % (bill*1.15)
#     print "Amount per person: $%f" % (bill/split)
# else:
#     print "Tip Amount: $%f" % (bill*1.1)
#     print "Amount per person: $%f" % (bill/split)

def tiper(bill, service, split):
    if (service == "good"):
        print "Tip Amount: $%f" % (bill*1.2)
    elif (service == "fair"):
        print "Tip Amount: $%f" % (bill*1.15)
    else:
        print "Tip Amount: $%f" % (bill*1.1)

    print "Amount per person: $%f" % (bill/split)

tiper(float(raw_input("Total bill amount? ")), raw_input("Level of service? "), float(raw_input("Split how many ways? ")))
