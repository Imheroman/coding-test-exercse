a_tuple = 10, 20, 30, 40, 50
print(a_tuple)
a, b, *c = a_tuple
print("a:", a)
print("b:", b)
print("c:", c)




books = {"the reason of travel": 1, "the three of women": 2}
print("The books are:", list(books.keys()))
print(books["the three of women"])

