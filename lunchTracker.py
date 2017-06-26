import numpy
import os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# data
restaurant = ["Chipotle", "Farm Burger", "Naan Stop"]
visited    = [0,0,0]
weekDay    = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekCount  = 1
restaurantLength = len(restaurant)
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
        elif (num > 0 and num < len(restaurant)+1 and visited[num-1] < 3 * weekCount):
            print "You chose %s on %s" % (restaurant[num-1], weekDay[(num-1) - (weekCount - 1) * 5])
            visited[num-1] += 1
        elif (num > 0 and num < len(restaurant)+1 and visited[num-1] >= 3 * weekCount):
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
        print "%s is the least visited" % sortedRestaurant[0]
        print "%s is the most visited" % sortedRestaurant[len(sortedRestaurant)-1]

    def listRestaurants():
        count = 0
        while count < 5:
            print "It is %s" % weekDay[count]
            pick()
            count = count + 1
        
    def printVisited():
        for x in range(len(restaurant)):
            print "%s has been visited %s times" % (restaurant[x], visited[x])

    def plot():
        global restaurant
        global restaurantLength
        global visited
        objects = []
        performance = []

        for x in restaurant:
            objects.append(x)
        for x in visited:
            performance.append(x)  

        y_pos = np.arange(len(objects))
        plt.barh(y_pos, performance, align='center', alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel('Usage')
        plt.title('Programming language usage')
        plt.show()
    
    def intro():
        global weekCount
        doList = raw_input("Do you want to list the restaurants? (y/n)")
        if (doList == 'y'):
            listRestaurants()
            weekCount += 1
            printVisited()
            doListAgain = raw_input("Do you want to list another week? (y/n) ")
            if (doListAgain == 'y'):
                listRestaurants()
                weekCount += 1
                printVisited()
        
        doManage = raw_input("Do you want to manage the list? (y/n)? ")
        os.system('clear')
        if (doManage == 'y'):
            addRestaurant()
            removeRestaurant()
            printVisited()
    
        doSort = raw_input("Do you want to sort the list by least to most visited? (y/n) ")
        os.system('clear')
        if (doSort == 'y'):
            sortByVisited()
    intro()
    plot()
    quit()

main()
