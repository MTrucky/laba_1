my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Получаем индексы начала и конца для каждого фильма
start_terminator =  0
end_terminator = my_favorite_movies.find(',')

start_pjatij_element = end_terminator +  1
end_pjatij_element = my_favorite_movies.find(',', start_pjatij_element)

start_avatar = end_pjatij_element +  1
end_avatar = my_favorite_movies.find(',', start_avatar)

start_chuzhiye = end_avatar +  1
end_chuzhiye = my_favorite_movies.find(',', start_chuzhiye)

start_nazad_v_budushee = end_chuzhiye +  1
end_nazad_v_budushee = len(my_favorite_movies)

# Извлекаем названия фильмов с помощью срезов
first_movie = my_favorite_movies[start_terminator:end_terminator]
last_movie = my_favorite_movies[start_nazad_v_budushee:end_nazad_v_budushee]
second_movie = my_favorite_movies[start_pjatij_element:end_pjatij_element]
second_from_last_movie = my_favorite_movies[start_chuzhiye:end_chuzhiye]

# Выводим результаты
print(first_movie)
print(last_movie)
print(second_movie)
print(second_from_last_movie)
