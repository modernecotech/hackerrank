#sorting string
if __name__ == '__main__':
    n=str(input())
    n=(n[:1000]) #string limit of 1000 characters
    
#All sorted lowercase letters are ahead of uppercase letters.
#All sorted uppercase letters are ahead of digits.
#All sorted odd digits are ahead of sorted even digits.
print(*sorted(n,key=lambda c:(c.isdigit(), c.isupper(), c in '02468', c)), sep='')

#upper case first, then even digits, then odd digits then lower case letters
print(*sorted(n,key=lambda c:(c.islower(), c.isdigit(), c in '13579', c)), sep='')

