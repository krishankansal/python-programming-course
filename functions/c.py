def login(**kwargs):
    print(kwargs)
    print("Total Arguments:", len(kwargs))
    print(kwargs["b"])

login(a=1, b=2, c=3,d=4,e=5)  # Output: {'a': 1, 'b': 2, 'c': 3}


