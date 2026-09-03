# create a list of squares from 1 to 10
# lst = []

# for i in range(1,11):
#     lst.append(i**2)

# print(lst)

x = [i**2 for i in range(1,11)]
print(x)

x=[i for i in range(1,11)]
print(x)

x = [i for i in range(1,11) if i%2==0]

