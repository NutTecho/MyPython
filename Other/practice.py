a = [1,2,3,4,5,6,7,8,9]
c = [1,2,3,4]
d = ["a","b","c","d"]
b = list(filter(lambda x : x%2 ==0 , a))
e = list(map(lambda q , j : str(q) + j  ,c ,d))
f = [{a2 : a1 } for a1 , a2 in zip(c,d)]
print(b)
print(e)
print(f)
print(list(f[0].keys()))
# g = [ i%2 == 0 for i in f]
# print(g)