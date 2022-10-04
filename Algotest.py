def search(arr, x): #linear search algorithm
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return ('This does not exist')

def dictKey(countries, key): #using the dictionary data structure
    if key in countries:
        print('This is ', countries[key])
    else:
        print('This country doesnot exist')

countries = {
    "1-784":"Saint Vincent and the Grenadines",
     "255": "Tanzania", 
     "679": "Fiji", 
     "380": "Ukraine", 
     "93": "Afghanistan", 
     "1-242":"Bahamas"} #creating a hashatable data structure

mumble_data = ['A96447', 'A94160', 'A95681', 'A94169', 'A94161', 'S21B23/016', 'S21B23/034', 'S21B23/007','J22B23/032','S21B23/008',countries,
'Katukunda Rochelle', 'Najjoba Tracy', 'Muganga Charles', 'Nkata Joshua Luyombya', 'Mukisa Isaiah'] #mumble_data array containing a dictionary

mylist = sorted(mumble_data) #sorting the array using the sorted() func
print (mylist)

key = '7' #using the key to look through the dictionary 
dictKey(countries, key)

print(search(mylist,'A94160')) #searching through the array for the A94160 item

key = '380' #checking for country code with code 380
dictKey(countries, key)
print(search(mylist,'Doe'))

