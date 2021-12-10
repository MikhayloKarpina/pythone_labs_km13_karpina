import csv

filename = "sonic_youth.csv"

with open("sonic_youth.csv", "w", newline="") as csvfile:
    fieldnames = ["Song","Year"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Song" : "Songs",
                     "Year" : "Years"})
    writer.writerow({"Song" : "Diamod Sea",
                     "Year" : 1995})
    writer.writerow({"Song" : "Titanium Expose",
                     "Year" : 1990})
    writer.writerow({"Song" : "Confusion Is Next",
                     "Year" : 1983})
    writer.writerow({"Song" : "Death Valley 69",
                     "Year" : 1985})
    writer.writerow({"Song" : "Sunday",
                     "Year" : 1998})
    writer.writerow({"Song" : "100%",
                     "Year" : 1992})
    writer.writerow({"Song" : "Do You Believe In Rapture?",
                     "Year" : 2006})

with open("sonic_youth.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    print(f"\n{filename}")
    print("------------------------------")
    for row in reader:
        print(row["Song"], " - ", row["Year"])

#Second option for the task

""" import csv

filename = "sonic_youth.csv"

songs = [
    ["Song","Years"],
    ["Diamond Sea",1995],
    ["Titanium Expose",1990],
    ["Confusion Is Next",1983],
    ["Death Valley 69",1985],
    ["Sunday",1998],
    ["100%",1992],
    ["Do You Believe In Rapture?",2006]
]

with open(filename,"w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(songs)

print(f"\n{filename}")
with open(filename, "r", newline="") as file:
    reader = csv.reader(file)
    print("------------------------------")
    for row in reader:
        print(row[0]," - ", row[1])  """