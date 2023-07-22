import json
consumer_data={"consumer_name":"Ram","eb_reading":[1100,1200,1350,1650,2050]}
def calculate_electricity_bill(consumer_data):
    bills=consumer_data['eb_reading']
    lst=[]
    for i in range(0,len(bills)-1):
        dictionary_view={}
        estimate=bills[i+1]-bills[i] 
        if estimate<100:
            bill_amount=0
        elif estimate>=100 and estimate<200:
            bill_amount=2*estimate
        elif estimate>200 and estimate<500:
            bill_amount=5*estimate
        elif estimate>500 and estimate<1000:
            bill_amount=10*estimate
        elif estimate>1000:
            bill_amount=14*estimate
        dictionary_view['month']=i+1  
        dictionary_view['units_consumed']=estimate 
        dictionary_view['billAmount']=bill_amount  
        # print(dictionary_view)
        lst.append(dictionary_view)
    #     str_lst=str(lst)
    # print(type(str_lst))
    return lst
e_lst=calculate_electricity_bill(consumer_data)
str_lst=str(e_lst)
# print(type(str_lst))
my_file=open("/home/abi/Documents/jsons.txt",'w')
# my_file.close(s)
user_choice=input("Enter your choice :")
formats=user_choice.upper()
if formats=="DICT":
    print(e_lst)
elif formats=="JSON":
    jsons=json.dumps(str_lst)
    print(jsons)

   
