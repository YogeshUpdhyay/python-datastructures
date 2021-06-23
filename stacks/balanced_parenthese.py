
open_list = ['(', '[', '{']
close_list = [')', ']', '}']

def is_balanced(string):
    stack = list()
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and stack[-1] == open_list[pos]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
        
if __name__ == '__main__':
    string = str(input().strip())
    print(is_balanced(string))