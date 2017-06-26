import operator 

def main():
    dictionarySmall = {}
    dictionaryBig = {}

    def top(tally):
        sorted_tally = sorted(tally.items(), key=operator.itemgetter(1))
        print sorted_tally

    def letterSummary(word):
        global dictionarySmall
        dictionary = {}
        for x in word:
            if (x not in dictionary.keys()):
                dictionary[x] = 1
            elif (x in dictionary.keys()):
                dictionary[x] += 1
        dictionarySmall = dictionary
        print dictionary    

    letterSummary(raw_input("Desired word to count? "))
    top(dictionarySmall)
    
    def wordSummary(sentence):
        global dictionaryBig
        sentence = sentence.lower()
        sentenceList = sentence.split(" ")
        print sentenceList
        dictionary = {}
        for x in sentenceList:
            if (x not in dictionary.keys()):
                dictionary[x] = 1
            elif (x in dictionary.keys()):
                dictionary[x] += 1
        dictionaryBig = dictionary
        print "Top = %s" % dictionary

    wordSummary(raw_input("Desired sentence to count? "))
    top(dictionaryBig)
main()
