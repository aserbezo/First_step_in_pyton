# За рожденният ден на дъщеря си Людмила е решила да организира парти, на което да покани всичките ѝ съученици.
# За целта е решила да наеме развлекателна зала за деца, чийто наем ще получите като вход от конзолата.
# Напишете програма, с която да помогнете на Людмила да изчисли какъв бюджет ще ѝ бъде необходим,
# като имате следната информация за допълнителните неща, необходими за тържеството:
# Торта  – цената ѝ е 20% от наема на залата
# Напитки – цената им е 45% по-малко от тази на тортатa
# Аниматор – цената му е 1/3 от цената за наема на залата


# От конзолата се четe 1 ред:
# Наем за залата – цяло число
# Да се отпечата на конзолата какъв бюджет ще бъде необходим за организиране на тържеството.

rent_for_the_hall = float(input())
price_cakes = rent_for_the_hall * 0.2
price_drinks = price_cakes - (price_cakes * 0.45)
price_animator = rent_for_the_hall / 3
required_amoiunt = rent_for_the_hall + price_cakes + price_drinks + price_animator
print(required_amoiunt)

# Вход = 2250
# Изход = 3697.5
# Вход = 3720
# Изход = 6113.2




