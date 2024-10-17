# dictionary = {Key : Value}
# key is a unique value

a = {1 : 'hi'}
b = {'t':[1, 2, 3]}

#add
a = {1: 'a'}
a[2] = 'b'
a #{1: 'a', 2: 'b'}

a = {1 : 'a'}
a[2] = 'b'
a["name"] = "May"
a[3] = [1, 2, 3]
a

#del
del a[1]
a


###

grade = {'pey': 10, 'julliet': 99}
grade['pey']
grade['julliet']

a = {1:'a', 2:'b'}
a[1] # 'a'
a[2] # 'b'

a = {'a': 1, 'b':2}
a['a']
a['b']

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
dic["name"]
dic["phone"]
dic["birth"]
dic.keys() #dict_keys(['name', 'phone', 'birth'])

# key must be a unique value
a = {1:'a', 1:'b'}
a # {1:'a'}

# A list cannot be used as a key, but a tuple can be used as a key.
# For the value, any type of data can be used, whether mutable or immutable.

for k in dic.keys():
    print(k)

list(dic.keys())

dic.values()
# dict_values(['pey', '010-9999-1234', '1118'])

dic.items()
# dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

dic.clear()
dic
#{}

# If you try to retrieve a value using a key that does not exist in the dictionary, 
# the a['nokey'] method will raise an error, whereas the a.get('nokey') method will return None.
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
dic.get('name')
dic['name']
dic.get('phone')
dic['phone']

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
'name' in a
'email' in a
