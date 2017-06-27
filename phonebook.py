import pickle

#global variable data
options = {1: "Look up an entery", 2: "Set an entry", 3: "Delete an entry", 4: "List current entries", 5: "Save entries", 6: "Load saved entries", 7: "Quit"}
book = {}
file_name = "phonebook_data.pickle"

#main function
def main():
    
    def look_up_entry(input):
        global book
        name = raw_input("What is the person's name? ").lower()
        print "%s\' phone number is %s" % (name, book[name])
    
    def set_entry(input):
        global book
        name = raw_input("What is the person's name? ").lower()
        number = raw_input("What is their phone number? ")
        email = raw_input("What is their email address? ")
        website = raw_input("What is their website URL? ")
        book[name] = number, email, website
    
    def delete_entry(input):
        global book
        name = raw_input("What is the person's name? ").lower()
        del book[name]
    
    def list_entries():
        global book
        print "Current unsaved entries are: %s" % book

    def load_saved_entries():
        global file_name
        file_open = open(file_name, "rb")
        book = pickle.load(file_open)
        file_open.close()
        print "The saved entries are: %s" % book

    def save_entries():
        global book
        global file_name
        file_open = open(file_name, "wb")
        pickle.dump(book, file_open)
        print book
        file_open.close()
        print "Contacts Saved"


    def quit_program():
        print "Ok have a nice day!"
        quit()

    while True:
        print """Electronic Phone Book 
        =====================
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List current entries
        5. Save entries
        6. Load saved entries
        7. Quit """

        choice = raw_input("What do you want to do (1-7)? ")
        if (choice == '1'):
            look_up_entry(choice)
        elif (choice == '2'):
            set_entry(choice)
        elif (choice == '3'):
            delete_entry(choice)
        elif (choice == '4'):
            list_entries()
        elif (choice == '5'):
            save_entries()
        elif (choice == '6'):
            load_saved_entries()
        elif (choice == '7'):
            quit_program()
        else:
            print "Input a number 1 through 5"

    
main()