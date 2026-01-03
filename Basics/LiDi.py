info = [{"name" : "Krish", "English" : 89, "Maths" : 99, "science" : 88},
        {"name" : "Arinjay", "English" : 80, "Maths" : 78, "science" : 80},
        {"name" : "Kevin", "English" : 99, "Maths" : 65, "science" : 82},
        {"name" : "Pranjal", "English" : 78, "Maths" : 84, "science" : 78},
        {"name" : "Tushar", "English" : 64, "Maths" : 89, "science" : 85},
        ]

for i in info:
    avg = (i["English"] + i["Maths"] + i["science"]) / 3
    print(i["name"] + " " , avg)