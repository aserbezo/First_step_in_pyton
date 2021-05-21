# Мария решава да мине на диета и отива до  близкия пазар, за да купи ягоди, банани, портокали и малини.
# Да се напише програма, която пресмята колко пари са  ѝ необходими за да плати сметката.
# като знаете,че:
# цената на  малините е на половина по-ниска от тази на ягодите;
# цената на портокалите е с 40% по-ниска от цената на малините;
# цената на бананите е с 80% по-ниска от цената на малините.

# от конзолата се четат 5 реда:

price_strawberries_in_BGN =  float(input())
amounts_of_bananas_in_kilograms = float(input())
amounts_of_oranges_in_kilograms = float(input())
amounts_of_raspberries_in_kilograms = float(input())
amounts_of_strawberries_in_kilograms = float(input())
# Цена на малините, портокалите и бананите за килограм
price_raspberries = price_strawberries_in_BGN / 2
price_orages = price_raspberries - (0.4 * price_raspberries)
price_bananas = price_raspberries - (0.8 * price_raspberries)
# Сума на малините ,портокалите , бананите и ягодите умножени по цената
sum_raspberries = amounts_of_raspberries_in_kilograms * price_raspberries
sum_oranges = amounts_of_oranges_in_kilograms * price_orages
sum_bananas = amounts_of_bananas_in_kilograms * price_bananas
sum_strawberry = amounts_of_strawberries_in_kilograms * price_strawberries_in_BGN
# Обща сума като съберем сбора от сумите на ягодите, портокалите , малините и бананите
toal_sum = sum_raspberries + sum_strawberry + sum_bananas + sum_oranges
print(toal_sum)

# Да се отпечата на конзолата едно число:
# парите, които са необходими на Мария.

# Примерен Вход и изход
# 57.5
# 10
# 3.4
# 6.5
# 1.7

# 400.775




