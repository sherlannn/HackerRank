from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    for x in range(0, len(string)-k+1, k):
        print(''.join(OrderedDict.fromkeys(string[x:x + k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)