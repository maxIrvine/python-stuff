def main():
    def letterSummary(word):
        dictionary = {}
        for x in word:
            if (x not in dictionary.keys()):
                dictionary[x] = 1
            elif (x in dictionary.keys()):
                dictionary[x] += 1
        print dictionary    

    letterSummary(raw_input("Desired word? "))
    
main()
