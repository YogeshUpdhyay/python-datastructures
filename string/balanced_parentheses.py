def ispar(string):
    _open = False
    count = 0
    parentheses = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    if string[0] in parentheses.values():
        return False

    i = 0
    opening_parenthese = None
    closing_parenthese = None
    temp = ''
    while i < len(string):
        if not _open:
            if parentheses.get(string[i], None):
                opening_parenthese = string[i]
                closing_parenthese = parentheses.get(string[i])
            else:
                return False
        else:
            if string[i] == opening_parenthese:
                count += 1

            if string[i] == closing_parenthese:
                if count > 0:
                    count -= 1

            temp += string[i]

if __name__ == '__main__':
    string = str(input().strip())
    print(ispar(string))