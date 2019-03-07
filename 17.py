#python alphabet rangoli

def print_rangoli(n):
    import string

#N=int(input())

    while n not in range(1,27,1):
        print("please enter a number between 1 and 26")
        n=int(input())
        

#size 2 width is 3 and height is 3
#size 3 the width is 9 height is 5, tabs in middle 4
#size 5 the width is 17 height is 9, tabs in middle 8

#the height is ((N-1)*2)+1
#the width is ((N*2)-1)+((N-1)*2)

#put all letters of the alphabet into a list
    letters=list(string.ascii_lowercase)

    rangoli=[]

    for i in range (n):
        s="-".join(letters[i:n])
        rangoli.append((s[::-1]+s[1:]).center(4*n-3,"-"))
    print('\n'.join(rangoli[:0:-1]+rangoli))

if __name__ == '__main__':
    n=int(input())
    print_rangoli(n)