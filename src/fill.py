def fill(coll, value, begin, end):
    return [value if i >=begin and i<end else coll[i] for i in range(len(coll))]

print(fill([1,2,3,4,5], 0, 2, 4))