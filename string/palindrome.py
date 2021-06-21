
def palindrome(string):
    return True if string == string[::-1] else False

if __name__ == '__main__':
    string = str(input().strip())
    print(palindrome(string))