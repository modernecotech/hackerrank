#string minion game

#number of possible words starting with vowels or consonants
#put them in a set to avoid duplicates
#compare the count of vowel and consonant 
#print out the number of the winner

def minion_game(string):
    consonants='AEIOU'
    kevin_consonants=0
    stuart_vowels=0
    for x in range(len(s)):
        if s[x] in consonants:
            kevin_consonants+=(len(s)-x)
        else:
            stuart_vowels+= (len(s)-x)
    if kevin_consonants > stuart_vowels:
        print("Kevin", kevin_consonants)
    elif kevin_consonants < stuart_vowels:
        print("Stuart", stuart_vowels)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)