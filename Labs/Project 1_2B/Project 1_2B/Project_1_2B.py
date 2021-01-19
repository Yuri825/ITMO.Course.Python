#You will create three lists that each contain ten values.  One will contain product names, another product 
#costs and the third a three-digit employee code.  Your task will be to merge all three lists into a single navigable array

import module
#task = input("Введите id продукта")
#print("Наименование продукта: " + module.names[module.code.index(task)])
#print("Стоимость продукта: " + str(module.costs[module.code.index(task)]))
#print(shared_array_list)

shared_array = zip(module.code, module.names, module.costs)
shared_array_list = list(shared_array)
inp = input("Введите код продукта от 001 до 010\n")
num = 0
while num < len(shared_array_list):
    if shared_array_list[num][0] == inp:
        print("Наименование продукта: " + shared_array_list[num][1] + "\n" + "Стоимость продукта: " + \
            str(shared_array_list[num][2]))
    num+=1 