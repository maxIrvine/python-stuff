import numpy

# data
restaurant = ["Chipotle", "Farm Burger", "Naan Stop"]
visited    = [0, 0, 0]
weekDay    = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print restaurant

def main():
    global restaurant
    global visited
    # prompt user to pick one
    def pick():
        num = int(raw_input("Please pick (0 - quit,1,2,or 3) "))
        interpolate(num)

    # interpolate user response
    def interpolate(num):
        if (num == 0):
            quit()
        elif (num > 0 and num < len(restaurant)+1 and visited[num-1] < 3):
            print "You chose %s" % restaurant[num-1]
            visited[num-1] += 1
        elif (num > 0 and num < len(restaurant)+1 and visited[num-1] >= 3):
            print "You've visited this restaurant 3 times already! Please pick a new one"
            pick()
        else:
            print "Please enter a valid restaurant!"
    
    def addRestaurant():
        shouldAdd = True
        while shouldAdd == True:
            add = raw_input("Would you like to add a restaurant (y/n)? ")
            if (add == 'y'):
                name = raw_input("What is the name of the restaurant? ")
                restaurant.append(name)
                visited.append(0)
                print restaurant
            else:
                shouldAdd = False
                print "Ok."
        

    def removeRestaurant():
        shouldRemove = True
        while shouldRemove == True:
            remove = raw_input("Would you like to remove a restaurant (y/n)? ")
            if (remove == 'y'):
                name = raw_input("What is the name of the restaurant? ")
                index = restaurant.index(name)
                restaurant.pop(index)
                visited.pop(index)
                print restaurant
            else:
                shouldRemove = False
                print "Ok goodbye"

    def sortByVisited():
        global restaurant
        global visited
        restaurant = numpy.array(restaurant)
        visited = numpy.array(visited)
        inds = visited.argsort()
        sortedRestaurant = restaurant[inds] 
        print sortedRestaurant

    count = 0
    while count < 5:
        print "It is %s" % weekDay[count]
        pick()
        count = count + 1
    
    def printVisited():
        for x in range(len(restaurant)):
            print "%s has been visited %s times" % (restaurant[x], visited[x])
    
    printVisited()
    addRestaurant()
    removeRestaurant()
    printVisited()
    sortByVisited()

main()
