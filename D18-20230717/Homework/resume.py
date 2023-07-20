my_resume={"Name":"Abinaya",
    "E-mail":"rsabinaya2002@gmail.com",
    "Mobile-no":9344729839,
    "Soft Skills":["communication skill","problem solving","typing"],
    "Hard Skills":["python"],
    "Education Qualification":[{"course":"sslc",
                              "institute":"Evans Matric Hr.Sec School",
                              "percentage":94,
                              "passed out year":2018},
                            {"course":"HSC",
                            "institute":"Evans Matric Hr.Sec School",
                            "percentage":87,
                            "passed out year":2020},
                            {"course":"B.Sc Computer Science",
                            "institute":"WCC",
                            "percentage":85,
                            "passed out year":2023}],
    "Projects":{"title":"Snack Ordering App","lang":"kotlin"},
    "Experience":[{"company name":"WIPRO","role":"Developer","years":1},
                {"company name":"TCS","role":"Developer","years":2},
                {"company name":"Infosys","role":"Developer","years":2.5}],
    "Hobbies":["watching series","hand embroidry","mobile gaming"],
    "Personal Details":{"Father's name":"Rajan",
                        "Father's Occupation":"late",
                        "Languages Known":["Tamil","English"],
                        "DOB":"15-03-2002",
                        "Gender":"Female",
                        "Marital Status":"Single",
                        "Address":{"Door no":"62A/6",
                                "Street Name":"Amman Kovil backstreet",
                                "Place":"Vattavilai",
                                "PO":"Edalakudy",
                                "City":"Nagercoil",
                                "District":"Kannyakumari",
                                "Pin code":629002}},
    "Declaration":" I hereby declare that the above mentioned information is true."}
title="RESUME"
print(title.center(95))
for key,details in my_resume.items():
    if type(details)==str or type(details)==int:
        print(f"{key}\t:\t{details}")
    elif type(details)==list:
        print(f"{key}\t:")
        for lst in details:
            # print(lst)
            if type(lst)==str:
                print(f"\t\t{lst}")
            elif type(lst)==dict:
                for key,detail in lst.items():
                    print(f"\t{key}:{detail}")
    elif type(details)==dict:
        print(f"{key}\t:")
        for key,dicts in details.items():
            # print(f"\t{key}\t:{dicts}")
            if type(dicts)==dict:
                print(f"\t{key}\t:")
                for key,dic in dicts.items():
                    print(f"\t\t{key}\t:{dic}")
            if type(dicts)==str:
                print(f"\t\t{key}\t:\t{dicts}")
            if type(dicts)==list:
                
                

            