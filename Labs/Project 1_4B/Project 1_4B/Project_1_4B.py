#Project:  Load the …\data\orderdata_sample.csv file.  
#Use the “Quantity”, “Price” and “Freight” columns to generate a new “Total” column (e.g. Quantity * Price + Freight).  
#Save all the data to a new file.
import csv
with open ("orderdata_sample.csv",  newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    with open ("new_orderdata_sample.csv", 'w', newline='') as csvfile:
        for row in reader:
            a = float (row['Quantity']) * float (row['Price']) + float (row['Freight'])
            print(row['Quantity'], row['Price'], row['Freight'], str(a))
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow([row['Quantity'], row['Price'], row['Freight'], a])
