# TODO Найдите количество книг, которое можно разместить на дискете
Book = 1.44
x = (4 * 25 * 50 * 100)
y = x / (1024 ** 2)
z = int(Book / y)
print("Количество книг, помещающихся на дискету:", z)
