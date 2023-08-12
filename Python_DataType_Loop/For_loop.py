numbers = [0, 1, 2, 3, 4, 5]
for i in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    if i==4:
        break
    print(i)       # the numbers will be printed line by line, from 0 to 5

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(i,language[i])


    

