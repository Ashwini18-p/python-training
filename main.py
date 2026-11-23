#for reading - csv module

import csv
with open("training.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#for writing - csv module
import csv
with open("training.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Salary"])
    data = [
        [101, "Aswini", 25000],
        [102, "likky", 30000],
        [103, "teju", 28000]
    ]
    writer.writerows(data)


    import csv
with open("training.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#using append
import csv
with open("training.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([104, "darshik", 30000])
    import csv
with open("training.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#in table the first row is completely header if we want only the values we will use next
    import csv
with open("training.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

#dict write the csv returns the format in list if we want dict we will use dictwriter()
import csv
with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["ID", "Name", "Salary"]
    )
    writer.writeheader()
    writer.writerow({
        "ID": 101,
        "Name": "Aswini",
        "Salary": 25000
    })
    writer.writerow({
        "ID": 102,
        "Name": "Likky",
        "Salary": 30000
    })
    writer.writerow({
        "ID": 103,
        "Name": "Teju",
        "Salary": 28000
    })