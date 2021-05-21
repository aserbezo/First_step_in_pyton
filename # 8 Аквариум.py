# Да се напише програма, която изчислява литрите вода, които са необходими за напълването на аквариума
# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

# От конзолата се четат 4 ри реда
length = float(input())
width = float(input())
height = float(input())
percent_occupied_by_volume = float(input())
# Изчисляваме обем на аквариум
volume_of_the_aquarium = length * width * height
# общо литри, които ще събере
volume_per_liter = volume_of_the_aquarium * 0.001
# процент
percent = percent_occupied_by_volume * 0.01
# литрите, които ще трябват
liters_you_will_need = volume_per_liter * (1-percent)
# Да се отпечата на конзолата едно число
print(liters_you_will_need)

#  Примерен вход
# 85
# 75
# 47
# 17
# Изход
# 248.68875
