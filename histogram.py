def main():
    def letterSummary(word):
        dictionary = {}
        for x in word:
            if (x not in dictionary.keys()):
                dictionary[x] = 1
            elif (x in dictionary.keys()):
                dictionary[x] += 1
        print dictionary    

    letterSummary(raw_input("Desired word to count? "))
    
    def wordSummary(sentence):
        sentence = sentence.lower()
        sentenceList = sentence.split(" ")
        print sentenceList
        dictionary = {}
        for x in sentenceList:
            if (x not in dictionary.keys()):
                dictionary[x] = 1
            elif (x in dictionary.keys()):
                dictionary[x] += 1
        print dictionary
    
    wordSummary(raw_input("Desired sentence to count? "))
main()
