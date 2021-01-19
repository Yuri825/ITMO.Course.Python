#Create a list of randomly generated numbers between 1 and 100.  Based on the first list, generate a second that has 
#the word “High” or “Low” depending on whether the corresponding number in the first list is greater than or less than 50. 
# Generate a list of 100 names.  Generate two new lists.  One with the names where the first character begins with 
# a letter between “a” and “m” with the other lists containing the other names.
import random
import names
i = 0
lis = []
high = []
while(i < 100):
    a = random.randint(1, 100)
    lis.append(a)
    if a > 50:
        high.append(a)
    i+=1

print("Полный список\n" + str(lis))
print("\nСписок со значениями больше 50:")
print(*high, sep=', ')

list_befaure_M = []
list_after_M = []
j = 0
while (j < len(names.names)):
    if(names.names[j][0] <= "М"):
        list_befaure_M.append(names.names[j])
    else:
        list_after_M.append(names.names[j])
    j+=1

print("\nИмена от А до М:")
list_befaure_M.sort()
print(*list_befaure_M, sep=', ')
print("\nИмена от Н до Я")
list_after_M.sort()
print(*list_after_M, sep=', ')