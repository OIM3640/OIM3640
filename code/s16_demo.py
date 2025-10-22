s = ['python', 'javascript', 'c', 'c++']
s[2] = 'c#'
s
name = 'tauria'
name[0] = 'T'
d = {'name': 'TSLA', 'price': 350, 'shares': 200}
d['shares'] -= 100
d
d['name'] = 'MSFT'
d
d = {'name': 'TSLA', 'name': 'MSFT', 'price': 200}
d
d = {'name': 'TSLA', 'brand': 'TSLA', 'price': 200}
d
stock_1 = {'name': 'TSLA', 'price': 200}
stock_2 = {'name': 'MSFT', 'price': 300}
stock_1 = {'name': 'TSLA', 'price': 200}
stock_2 = {'name': 'MSFT', 'price': 300}
# what data structure to use to store multiple stocks
stocks= [stock_1, stock_2]
stocks
stocks[0]['name']
stocks[0]['price']
stocks[0]['price'] += 50
stocks
person = {'name': 'Guido', 'age': 70 }
'Guido' in person
'name' in person
'age' in person
person = {'name': 'Guido', 'age': 70 }
'Guido' in person.values()
'name' in person.keys()
for k in person.keys():
    print(k)
person['age']
person['country']
persons = [
{'name': 'tauria', 'age': 21},
{'name': 'Guido', 'age': 70},
{'name': 'Zhi'}
]
for person in persons:
    print(person['age'])
persons
for p in persons:
    print(p['age'])
    continue
persons
for p in persons:
    if 'age' in p:
        print(p['age'])
for p in persons:
    if 'age' in p:
        print(p['age'])
    else:
        print('N/A')
persons
for p in persons:
    age = p.get('age', 'N/A')
    print(age)
person
i  = 100
for i in range(4):
    print(i)
i
person = {'name': 'Guido', 'age': 70 }
print('Guido' in person)
person
# add new data to dict
person['city'] = 'Belmont'
person
numbers = [10, 22, 2025]
# how to add new number to the list
numbers[3] = 3
numbers.append(3)
numbers
numbers
numbers.insert(1, 100)
numbers
numbers.extend(200)
numbers
numbers.append(.5)
numbers
sorted(numbers)
numbers
numbers.extend([200])
numbers
numbers.extend('200')
numbers
list('200')
numbers
numbers.append('nidhi')
numbers
numbers.extend([5324, 65, 865, 85432])
numbers
numbers
sorted(numbers)
numbers = numbers[:5]
numbers
numbers
sorted(numbers)
numbers
numbers[0] = 1000
numbers
name
name[0] = 'T'
d
stock
persons[0]
numbers
2 ** 38