import operator 

dictionarySmall = {}
dictionaryBig = {}

def main():

    def top(data):
        length = len(data)
        tupleVersion = sorted(data.items(), key=lambda x:x[1])
        listVersion = list(tupleVersion)
        if length > 3:
            for x in range (0, length-3):
                listVersion.pop(x)
        print listVersion

    def letterSummary(word):
        global dictionarySmall
        word = word.lower()
        wordList = list(word)
        # print wordList
        dictionary = {}
        for x in wordList:
            if (x not in dictionary.keys()):
                dictionary[x] = 1
            elif (x in dictionary.keys()):
                dictionary[x] += 1
        dictionarySmall = dictionary
        print "Top = %s" % dictionary    

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