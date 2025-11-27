count_bytes = 1.44*1024*1024

pages = 100
string_on_page = 50
digit_on_string = 25

bytes_in_digit = 4
count_digit = digit_on_string * string_on_page * pages
count_bytes_in_book = count_digit * bytes_in_digit


count_book = count_bytes//count_bytes_in_book
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(count_book))
