#How to keep a gullible person busy
while True:
    print("Do you know want to know how to keep a gullible person busy? Y/N ")
    response = input("> ")
    if response.lower()=='n' or response.lower()=='no':
        break
    if response.lower()=='y' or response.lower()=='yes':
        continue
    print(f'{response} is not a valid yes/no answer.')