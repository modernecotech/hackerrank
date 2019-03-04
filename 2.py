year=1990 

if 1900 <= year <10**5:
    if year%100==0:
        if year%400==0:
            if year%4==0:
                return True
        return False
        
