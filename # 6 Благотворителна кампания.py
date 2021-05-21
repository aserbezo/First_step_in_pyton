# Първоначално прочитаме от конзолата броя на дните, в които тече кампанията и броя на сладкарите,
# които ще се включат. След това на отделни редове получаваме количеството на тортите, гофретите и палачинките,които ще бъдат приготвени от един сладкар за един ден.
# Трябва да се има предвид следния ценоразпис:
# Торта - 45 лв.
# Гофрета - 5.80 лв.
# Палачинка – 3.20 лв.
# 1/8 от крайната сума ще бъде използвана за покриване на разходите за продуктите по време на кампанията. Да се напише програма, която изчислява сумата, която е събрана в края на кампанията.

# От конзолата се четат 5 реда:
the_numbers_days_campaign_runs = int(input())
numbers_confectioners = int(input())
numbers_cakes = int(input())
number_waffles = int(input())
number_pancakes = int(input())
# Изчисляваме сумата, която се изкарва на ден за всеки един от продуктите, направени от 1 сладкар:
cakes = numbers_cakes * 45
waffles = number_waffles * 5.80
pancakes = number_pancakes * 3.20
# Обща сума за един ден
total_amount_for_one_day = (cakes + waffles +pancakes) * numbers_confectioners
# Сума събрана от цялата кампания
amount_collected_by_whole_company = total_amount_for_one_day * the_numbers_days_campaign_runs
# Сума след покриване на разходите
amount_after_covering_the_cost = amount_collected_by_whole_company - ( amount_collected_by_whole_company / 8)
print(amount_after_covering_the_cost)

# Да се отпечата на конзолата едно число:
# парите, които са събрани.

# Примерен вход и изход
# 23
# 8
# 14
# 30
# 16
# exit = 137687.2