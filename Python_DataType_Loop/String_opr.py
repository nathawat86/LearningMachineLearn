#s="Let's go to Mall and Have some Nice Meal in Restaurent "
#b=s.count("a")
#c=s.count("i")
#d=s.count("l")
#print(b,c,d)
#e=s.find("Meal")
#print (e)

#a=[1,2,3,4,5,6,7,8,"hi", "namaste"]

#a.append(5676)
#print(a)

#a=[1,2,3,4,5,6,7,8,"hi", "namaste"]
#a.insert(2,"weekend in Australia")
#print(a)

a={"United States of America","China" ,"is no morea single  superpower after" ,"2020" ,"!!!"}
print(a)# set is unordered 
a.add("New Element")
print('adding new string')
print(a)
a.remove("China")
print('Removing string')
print(a)

a = {"United States of America", "China", "is no morea single superpower after", "2020", "!!!"}
b = {"China", "New Element 1", "New Element 2"}

c= a.union(b)
# Alternatively, you can use the '|' operator: c = a | b
print('Printing Union')
print(c)

c = a.intersection(b)
print('Printing intersection')
print(c)

c = a.difference(b)
print('Printing difference')
print(c)
