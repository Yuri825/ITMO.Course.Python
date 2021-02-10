from tkinter import*

#root = Tk()

#root.geometry('300x250')
#root.mainloop()
#canvas = Canvas(root, height=300, width=300)
#canvas.pack()
#frame = Frame(root, bg='red')
#frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)


#ЗАДАНИЕ 2

#Основной класс
class Pizza:
   # name = ''
   # dough = ''
   # souse = ''
    #filling = ''
   # price = 0.0
#конструктор
    def __init__ (self, name, dough, souse, filling, price):
        self.name = name
        self.dough = dough
        self.souse = souse
        self.filling = filling
        self.price = price


#класс наследник
class pizzaPepperoni (Pizza):
    fil = {'cheese': 12, 'sosage': 14}

#класс наследник
class pizzaBarbeku (Pizza):
    fil = {'meat': 15, 'souse': 5}
    
#класс наследник
class pizzaDaryMoria (Pizza):
    fil = {'креветки': 20, 'мидии': 25}

#переменная для выбора вида пиццы (вывод меню)
choose = int(input('сделайте заказ:\nпицца пепперони - 1\nпицца барбекю - 2\nпицца дары моря - 3\n'))

#переменная для выбора вида теста
d = int(input('Выберите тесто: \nТонкое тесто - 1\nПышное тесто - 2 \n'))

#выбор теста
if d == 1:
    your_dough = 'тонкое тесто'
elif d == 2:
    your_dough = 'пышное тесто'
else:
    print('вы не туда нажали')

#переменная для выбора вида сыра
s = int(input('Выберите соус: \nСырный - 1\nСметанный - 2\n'))

#выбор сыра
if s == 1:
    your_souse = 'cырный'
elif s == 2:
    your_souse = 'сметанный'

#переменная для выбора начинки
f = int(input('выберите начинку:\nколбаса - 1\nветчина - 2\n'))

#выбор начинки
if f == 1:
    your_filling = 'колбаса'
elif f == 2:
    your_filling = 'ветчина'


#экземпляры класса Pizza. Сразу задаем цену по умолчанию
p = pizzaPepperoni('Пепперони', your_dough, your_souse, your_filling, 300.0)
b = pizzaBarbeku('Барбекю', your_dough, your_souse, your_filling, 400.0)
dm = pizzaDaryMoria('Дары моря', your_dough, your_souse, your_filling, 500.0)

#если выбрана пицца Пепперони
if choose == 1:
    print('Вы выбрали:\n' + 
          'Вид пиццы: ' + p.name)
    addCheese = int(input('Добавить больше сыра ?\nда - 1\nнет - 2\n'))
    if addCheese == 1:
        p.price = p.price + p.fil['cheese']
    addSosage = int(input('Добавить больше колбасы?\nда - 1\nнет - 2\n'))
    if addSosage == 1:
        p.price = p.price + p.fil['sosage']

    print('Ваш заказ:\n' + 
          'Вид пиццы: ' + p.name + 
          '\nтесто: ' + p.dough + 
          '\nсоус: ' + p.souse + 
          '\nначинка: ' + p.filling + 
          '\nцена заказа: ' + str(p.price))

#если выбрана пицца Барбекю
if choose == 2:
     print('Вы выбрали:\n' + 
          'Вид пиццы: ' + b.name)
     addMeat = int(input('Добавить больше мяса?\nда - 1\nнет - 2\n'))
     if addMeat == 1:
        b.price = b.price + b.fil['meat']
     addGarlicSouse = int(input('Добавить чесночный соус?\nда - 1\nнет - 2\n'))
     if addGarlicSouse == 1:
         b.price = b.price + b.fil['souse']
     print('Ваш заказ:\n' + 
          'Вид пиццы: ' + b.name + 
          '\nтесто: ' + b.dough + 
          '\nсоус: ' + b.souse + 
          '\nначинка: ' + b.filling + 
          '\nцена заказа: ' + str(b.price))

#если выбрана пицца Дары моря
if choose == 3:
    print('Вы выбрали:\n' + 
          'Вид пиццы: ' + dm.name)
    addShrimp = int(input('Добавить больше креветок?\nда - 1\nнет - 2\n'))
    if addShrimp == 1:
        dm.price = dm.price + dm.fil['креветки']
    addMussels = int(input('Добавить больше мидий?\nда - 1\nнет - 2\n'))
    if addMussels == 1:
        dm.price = dm.price + dm.fil['sosage']
    print('Ваш заказ:\n' + 
          'Вид пиццы: ' + dm.name + 
          '\nтесто: ' + dm.dough + 
          '\nсоус: ' + dm.souse + 
          '\nначинка: ' + dm.filling + 
          '\nцена заказа: ' + str(dm.price))
          

