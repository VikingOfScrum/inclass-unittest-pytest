def palindrome(string):
    isPali = string == string[::-1]
    return isPali

def main():
   userString = input("Please enter a word: ")
   print(palindrome(userString))


if __name__ == '__main__':
    main()