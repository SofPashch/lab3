import csv

#запис у файл
print("1 group")
f1 = "FirstGroup.txt"
fd = open(f1, "w")
fd.write("St1 - 5\n")
fd.write("St2 - 8\n")
fd.write("St3 - 10\n")
fd.write("St4 - 9\n")
fd.close()

#дозапис у файл
fd = open(f1, "a")
fd.write("St5 - 7\n")
fd.close()

#читання файлу
fd = open(f1, "r")
reader = csv.reader(fd, delimiter = "\t")
for str in reader:
    print(str)
fd.close()

#запис у файл
print("2 group")
f2 = "SecondGroup.txt"
fd = open(f2, "w")
fd.write("St1 - 6\n")
fd.write("St2 - 4\n")
fd.write("St3 - 11\n")
fd.write("St4 - 12")
fd.close()

#читання файлу
fd = open(f2, "r")
reader = csv.reader(fd, delimiter="\t") 
for str in reader: 
 print(str) 
fd.close()
