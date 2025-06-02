"""The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28"""

#This kata was one of the first kata I solved the solution is absurdly long!

def century(year):
    num = str(year)
    if len(num) == 4:
        if 1 <= int(num[len(num)-2:len(num)]) <= 99:
            return int(num[len(num)-4:len(num)-2])+1
        else:
            return int(num[len(num)-4:len(num)-2])
            
    elif len(num) == 1:
        return 1
        
    elif len(num) == 3:
        if (1 <= int(num[len(num)-2:len(num)-1]) <= 99): #If the last 2 digits make a number between 1 and 99 (eg. 350, 457)
            if int(num[1]) == 0: #If the middle digit is 0
                new_century = num[0] + num[2]
                return int(new_century[0])+1
            elif 1 <= int(num[1]) <= 9:
                return int(num[0])+1
        elif int(num[1]) == 0 and int(num[2]) == 0: #If the last 2 digits in a year end in 0 (eg. 300, 400,)
            return int(num[0])
            
    elif len(num) == 2:
        l = []
        for character in num:
            l.append(character)
        l.insert(0,"0")
        new_year = "".join(l)
        if 1<= int(new_year[len(new_year)-2:len(new_year)-1]) <= 99:
            return int(new_year[len(new_year)-3:len(new_year)-2])+1
        else:
            return int(new_year[len(new_year)-3:len(new_year)-2])
