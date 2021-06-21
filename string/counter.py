from collections import Counter

def count_chars(string):
    return dict(Counter(string))

if __name__ == '__main__':
    string = str(input().strip())
    print(count_chars(string))