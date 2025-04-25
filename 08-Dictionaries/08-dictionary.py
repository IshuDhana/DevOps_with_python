my_dict = {'name':"Dev", 'Language':"python", 'version':'3.2.13'}
print(my_dict['version'])


#modify the dictionary name
my_dict['name'] = 'DevOps'
print(my_dict['name'])


#deletion 
del my_dict['Language']
print(my_dict)

if 'version' in my_dict:
    print("version name is updated")

for key,value in my_dict.items():
    print(key,value)



