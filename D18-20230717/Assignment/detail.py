row1_details=[{"name":"Abinaya","place":"Vattavilai",
            "hobbies":["watching series","embroidry","mobile gaming"],
            "SSLC":{"tamil":86,"english":73,"maths":98,"science":66,"social":69}},
    {"name":"Ajeedha","place":"Kannangulam",
    "hobbies":["Aari work","gardening","reading books"],
    "SSLC":{"tamil":89,"english":90,"maths":79,"science":74,"social":90}},
    {"name":"Abinesh","place":"Vattavilai",
    "hobbies":["Cricket","football","vollyball"],
    "SSLC":{"tamil":89,"english":70,"maths":91,"science":70,"social":81}},
    {"name":"Dhanush","place":"Peruvilai",
    "hobbies":["Cricket","football","vollyball"],
    "SSLC":{"tamil":78,"english":94,"maths":86,"science":93,"social":85}},
    {"name":"Sri Ram","place":"Krishnan kovil",
    "hobbies":["cricket","chess","carrom"],
    "SSLC":{"tamil":86,"english":79,"maths":82,"science":80,"social":98}}]

for row1_detail in row1_details:
    marks=row1_detail['SSLC']
    total=0
    for mark in marks.values():
        total+=mark
    prcntg=total/len(marks)
    if prcntg>90 or 75<prcntg<80 and marks['maths']>=98:
        print(f"name : {row1_detail['name']}, total : {total}, percentage : {prcntg}, you are eligible for maths biology")
    elif 80<prcntg<=90 or 70<prcntg<75 and marks['maths']>=98:
        print(f"name : {row1_detail['name']}, total : {total}, percentage : {prcntg}, you are eligible for maths computer")
        