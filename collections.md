El módulo collections nos brinda un conjunto de objetos primitivos que nos permiten extender el comportamiento de las built-in collections que poseé Python y nos otorga estructuras de datos adicionales. Por ejemplo, si queremos extender el comportamiento de un diccionario, podemos extender la clase UserDict; para el caso de una lista, extendemos UserList; y para el caso de strings, utilizamos UserString.

1. `namedtuple()` factory function for creating tuple subclasses with named fields
2. `deque` list-like container with fast appends and pops on either end
3. `ChainMap` dict-like class for creating a single view of multiple mappings
4. `Counter` dict subclass for counting hashable objects
5. `OrderedDict` dict subclass that remembers the order entries were added
6. `defaultdict` dict subclass that calls a factory function to supply missing values
7. `UserDict` wrapper around dictionary objects for easier dict subclassing
8. `UserList` wrapper around list objects for easier list subclassing
9. `UserString` wrapper around string objects for easier string subclassing


##### Counter
```python
from collections import Counter

list = [1,2,3,4,1,2,6,7,3,8,1]
Counter(list)
Counter({1: 3, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1})

list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt[1])
# Output:
3
```
Counter tiene tres funciones adicionales.

```python
Elements
Most_common([n])
Subtract([interable-or-mapping])
elements()


cnt = Counter({1:3,2:4})
print(list(cnt.elements()))
# Output:
[1, 1, 1, 2, 2, 2, 2]
most_common()


list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt.most_common())
# Output:
[(1, 3), (2, 2), (3, 2), (4, 1), (6, 1), (7, 1), (8, 1)]
subtract


cnt = Counter({1:3,2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)
# Output:
Counter({1: 2, 2: 2})
defaultdict

Crear diccionarios con el constructor defaultdict()


from collections import defaultdict

nums = defaultdict(int)
nums['one'] = 1
# -
print(nums)
# Output:
defaultdict(<class 'int'>, {'one': 1, 'two': 2})
# -
print(nums['two'])
# Output:
2

count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print(count)
# Output:
defaultdict(<class 'int'>, {'Mike': 5, 'Britney': 1, 'John': 3, 'Smith': 2, 'Anna': 2})
OrderedDict

Ordenar diccionario(s)


from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
# Output:
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

for key, value in od.items():
    print(key, value)
# Output
a 1
b 2
c 3
```

deque

```python
from collections import deque

list = ["a","b","c"]
deq = deque(list)
print(deq)
# Output
deque(['a', 'b', 'c'])

deq.append("d")
deq.appendleft("e")
print(deq)deque
# Output
deque(['e', 'a', 'b', 'c', 'd'])

deq.pop()
deq.popleft()
print(deq)
# Output
deque(['a', 'b', 'c'])

list = ["a","b","c"]
deq = deque(list)
print(deq)
print(deq.clear())
# Output
deque(['a', 'b', 'c'])
None

list = ["a","b","c"]
deq = deque(list)
print(deq.count("a"))
# Output
1
```
ChainMap

```python

from collections import ChainMap

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)
# Output
[{'b': 2, 'a': 1}, {'c': 3, 'b': 4}]

dict2['c'] = 5
print(chain_map.maps)
# Output
[{'a': 1, 'b': 2}, {'c': 5, 'b': 4}]

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print (list(chain_map.keys()))
print (list(chain_map.values()))
# Output
['b', 'a', 'c']
[2, 1, 3]

dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)
# Output
ChainMap({'f': 6, 'e': 5}, {'a': 1, 'b': 2}, {'b': 4, 'c': 3})
namedtuple()


from collections import namedtuple

Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1)
print(s1.fname)
# Output
Jhon
Student(fname='John', lname='Clarke', age='13')
Creando namedtuple usando una lista


s2 = Student._make(['Adam','joe','18'])
print(s2)
# Output
Student(fname='Adam', lname='joe', age='18')
Creando una nueva instancia usando una instancia existente


s2 = s1._asdict()
print(s2)
# Output
OrderedDict([('fname', 'John'), ('lname', 'Clarke'), ('age', '13')])
Cambiando valores con la funcion _replace()


s2 = s1._replace(age='14')
print(s1)
print(s2)
# Output
Student(fname='John', lname='Clarke', age='13')
Student(fname='John', lname='Clarke', age='14')