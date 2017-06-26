options = {1: "Look up an entery", 2: "Set an entry", 3: "Delete an entry", 4: "List all entries", 5: "Quit"}
book = {}

def main():
    
    def look_up_entry(input):
        global book
        name = raw_input("What is the person's name? ").lower()
        print "%s\' phone number is %s" % (name, book[name])
    
    def set_entry(input):
        global book
        name = raw_input("What is the person's name? ").lower()
        number = raw_input("What is their phone number? ")
        book[name] = number
        print book  
    
    def delete_entry(input):
        global book
        name = raw_input("What is the person's name? ").lower()
        del book[name]
        print book
    
    def list_entries():
        global book
        print book
    
    def quit_program():
        print "Ok have a nice day!"
        quit()

    while True:
        print """Electronic Phone Book 
        =====================
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Quit """

        choice = raw_input("What do you want to do (1-5)? ")
        if (choice == '1'):
            look_up_entry(choice)
        elif (choice == '2'):
            set_entry(choice)
        elif (choice == '3'):
            delete_entry(choice)
        elif (choice == '4'):
            list_entries()
        elif (choice == '5'):
            quit_program()
        else:
            print "Input a number 1 through 5"

    
main()