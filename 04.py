my_family = ['отец', 'мать', 'брат']

my_family_height = [
    ['отец',  180],
    ['мать',  165],
    ['брат',  190]
]

father_height = next((height for name, height in my_family_height if name == 'отец'), None)

if father_height:
    print(f"Рост отца - {father_height} см")
else:
    print("Информация о росте отца отсутствует.")

# Подсчет общего роста семьи
total_height = sum(height for _, height in my_family_height)
print(f"Общий рост моей семьи - {total_height} см")
