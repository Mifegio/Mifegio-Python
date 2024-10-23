# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
bites = 4
symb = 25
lines = 50
pages = 100
book = (bites
        * symb
        * lines
        * pages)
mbites = (book
          / (1024 ** 2))
count = int(volume / mbites)
print("Количество книг, помещающихся на дискету:", count)
