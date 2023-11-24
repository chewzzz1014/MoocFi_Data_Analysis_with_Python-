# sequences
# dont need to be same type
my_seq = [2, 100, "hello", 1.0]


# tuple
# fixed length, immutable, ordered
(3,)               # a singleton
(1,3)              # a pair
(1, "hello", 1.0); # a triple


# zip sequences
L1=[1,2,3]
L2=["first", "second", "third"]
print(zip(L1, L2))  # Note that zip does not return a list, like range
print(list(zip(L1, L2))) # [(1, 'first'), (2, 'second'), (3, 'third')]


# dictionary operations
d={"key1":"value1", "key2":"value2"}

# non-mutating
d.copy()
d.items()
d.keys()
d.values()
d.get(k[,x])

# mutating
d.clear()
d.update(d1)
d.setdefault(k[,x])
d.pop(k[,x])
d.popitem()


# set: dynamic, unordered, unique keys

# non-mutating set operations
s=set()
s1=set()
s.copy()
s.issubset(s1)
s.issuperset(s1)
s.union(s1)
s.intersection(s1)
s.difference(s1)
s.symmetric_difference(s1)

# set operations alternatives
s=set([1,2,7])
t=set([2,8,9])
print("Union:", s|t)
print("Intersection:", s&t)
print("Difference:", s-t)
print("Symmetric difference", s^t)

# mutating set methods
s.add(x)
s.clear()
s.discard()
s.pop()
s.remove(x)


