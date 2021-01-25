#Project:  Load the …\data\orderdata_sample.csv file.  
#Use the “Quantity”, “Price” and “Freight” columns to generate a new “Total” column (e.g. Quantity * Price + Freight).  
#Save all the data to a new file.
import csv
#открываем для чтения
with open ("orderdata_sample.csv",  newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    #открываем для записи заголовка
    with open("new_orderdata_sample.csv", 'w', newline='') as file:
        columns = ['Quantity', 'Price', 'Freight', 'Total']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        #открываем для дозаписи остальных строк
    with open ("new_orderdata_sample.csv", 'a', newline='') as csvfile:
        for row in reader:
            a = float (row['Quantity']) * float (row['Price']) + float (row['Freight'])
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([row['Quantity'], row['Price'], row['Freight'], a])
            #хочу вывести результат на экран
with open("new_orderdata_sample.csv", 'r', newline='') as csvfile_1:
    reader_1 = csv.DictReader(csvfile_1, delimiter=',')
    for row in reader_1:
        print('Quantity: ' + row['Quantity'] + '\t', 'Price: ' + row['Price'] + '\t', 'Freight: ' + \
            row['Freight'] + '\t', 'Total: ' + row['Total'])
