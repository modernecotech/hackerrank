#capitalisation of first names in python
def solve(s):
    s=input()

    #while S.len() is not in range(1,1000,1):
    #    print("please make sure that the name is between 1 to 1000 characters")
    #    S=str(input())

    for _ in s[:].split():
        s=s.replace(_,_.capitalize())
    string1=s
    return(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
