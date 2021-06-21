def reverse_string(string):
    return string[::-1]

if __name__ == '__main__':
    string = str(input().strip())
    output = reverse_string(string)
    print(output)