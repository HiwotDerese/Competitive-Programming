import textwrap

def wrap(string, max_width):
    wrapped = string[0]
    width = 1
    for i in range(1, len(string)):
        if i % max_width == 0:
            wrapped += '\n' + string[i]
        else:
            wrapped += string[i]
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)