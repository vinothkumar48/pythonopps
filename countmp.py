gender=[]
close=False
print('''if type is enough please type "stop"''')
while(close==False):
    gen=input("enter your gender ").lower()
    gender.append(gen)
    if gen=="stop":
        close=True   
print("Total Male Student is",gender.count("male"))
print("Total Female Student is",gender.count("female"))




