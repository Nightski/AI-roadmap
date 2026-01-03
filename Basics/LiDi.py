info = [{"name" : "Krish", "English" : 89, "Maths" : 99, "science" : 88},
        {"name" : "Arinjay", "English" : 80, "Maths" : 78, "science" : 80},
        {"name" : "Kevin", "English" : 99, "Maths" : 65, "science" : 82},
        {"name" : "Pranjal", "English" : 78, "Maths" : 84, "science" : 78},
        {"name" : "Tushar", "English" : 64, "Maths" : 89, "science" : 85},
        ]
print("Individual Average")
for i in info:
    avg = (i["English"] + i["Maths"] + i["science"]) / 3
    print(i["name"] + " " , avg)
print()

eng, mt, sc = 0,0,0
for i in info:
    eng += i["English"]
    mt += i["Maths"]
    sc += i["science"]
print("Class Average")
print("Science: ",sc/5)
print("English: ",eng/5)
print("Maths: ",mt/5)

top_e = max(info, key=lambda x : x["English"])
top_m = max(info, key=lambda x:x["Maths"])
top_s = max(info, key=lambda x:x["science"])
print()
print("Toppers of each subject:")
print("Maths: ",top_m["name"], ", Marks: ",top_m["Maths"])
print("Science: ",top_s["name"], ", Marks: ",top_s["science"])
print("English: ",top_e["name"], ", Marks: ",top_e["English"])