#strings split into segments, remove indistinct characters and print
#out answer on newlines


def merge_the_tools(string, k):
    part_length=(len(string)/k)
    for i in zip(*[iter(string)]*k):
        result=dict()
        print(''.join([result.setdefault(c,c,c) for c in i if c not in result]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)