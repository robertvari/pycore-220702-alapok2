add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
divide_numbers = lambda a, b: a/b


name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]
# print(sorted(name_list))
# print(sorted(name_list, key=lambda name: name.split()[-1]))


movie_list = {
    1: {"name": "The Princess", "rating": 63},
    2: {"name": "Spider-Man: No Way Home", "rating": 81},
    3: {"name": "Morbius", "rating": 64},
    4: {"name": "The Northman", "rating": 72},
}

result = sorted(movie_list, reverse=True, key=lambda movie_id: movie_list[movie_id]["rating"])
for i in result:
    print(f"Title: {movie_list[i]['name']} Rating: {movie_list[i]['rating']}")