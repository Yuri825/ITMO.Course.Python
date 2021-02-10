import csv
def funcReadByDate (FILENAME):
    try:
        d = str(input('введите дату\n'))
        with open(FILENAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row['Date'])
                if row['Date'] == d:
                    print(row['Category'] + '\t' + row['Product'] + '\t' + row['Price'] + "\t" + row['Quantity'] + '\t' + row['Date'])
    except IOError as err:
        print(err)

def funcWrite (FILENAME):
    d = str(input("введите дату\n"))
    c = str(input("введите категорию товара\n"))
    p = str(input("введите товар\n"))
    pr = float(input("введите цену\n"))
    q = float(input("введите количество\n"))
    bar = {'Category': c, 'Product': p, 'Price': pr, 'Quantity': q, 'Date': d}
    columns = ["Category", "Product", "Price", "Quantity", "Date"]
    try:
        with open(FILENAME, 'a+', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(bar)
    except IOError as err:
        print(err)

def funcReadAll (FILENAME):
     with open(FILENAME, 'r', newline='') as file:
         reader = csv.reader(file)
         print('\n')
         for row in reader:
             print(row[0] + '\t' + row[1] + '\t'  + row[2] + '\t'  + row[3] + '\t'  + row[4])
         print('\n')

def funcReadByCategory (FILENAME):
      try:
        d = str(input('категорию товара\n'))
        with open(FILENAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Category'] == d:
                    print(row['Category'] + '\t' + row['Product'] + '\t' + row['Price'] + "\t" + row['Quantity'] + '\t' + row['Date'])
      except IOError as err:
          print(err)

def funcDelAll (FILENAME):
       try:
            with open(FILENAME, 'w', newline="") as file:
                columns = ['Category', 'Product', 'Price', 'Quantity', 'Date']
                writer = csv.DictWriter(file, fieldnames=columns)
                writer.writeheader()
       except IOError as err:
                print(err)

def funcSortByPrice (FILENAME):
    lis = []
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lis.append(row['Price'])
    print(lis)
    lis.sort()
    print(lis)


while True:

    step = int(input("Для добавления данных нажмите\t 1\nДля вывода всех данных нажмите\t 2\nДля поиска по дате нажмите\t 3\nДля поиска по категории продукта введите 4\nДля очистки файла введите 5\nДля сортировки по цене нажмите 6\nДля выхода из программы нажмите 7\n"))

    if step == 1:
        funcWrite("MyBase.csv")
    elif step == 2:
        funcReadAll("MyBase.csv")
    elif step == 3:
        funcReadByDate("MyBase.csv")
    elif step == 4:
        funcReadByCategory("MyBase.csv")
    elif step == 5:
        funcDelAll("MyBase.csv")
    elif step == 6:
        funcSortByPrice("MyBase.csv")
    elif step == 7:
        break
    else:
        print('Вы ввели некорректное число')