
def wordsInString(string):
    wordCount = len(string.split())
    return wordCount

def main():
     userString = input("Please enter a sentance: ")
     print(wordsInString(userString))

if __name__ == '__main__':
    main()