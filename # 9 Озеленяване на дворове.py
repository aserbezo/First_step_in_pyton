# Озеленяване на дворове
# Божидара разполага с няколко къщи на Черноморието и желае да озелени дворовете на някои от тях, като по този начин създаде уютна обстановка и комфорт на гостите си. За целта е наела фирма.
# Напишете програма, която изчислява необходимите средства, които Божидара ще трябва да заплати на фирмата изпълнител на проекта. Цената на един кв. м. е 7.61лв със ДДС. Тъй като нейният двор е доста голям, фирмата изпълнител предлага 18% отстъпка от крайната цена.
# Вход
#От конзолата се прочита само един ред:
# Кв. метри, които ще бъдат озеленени – реално число.
#Изход
#"The final price is: {крайна цена на услугата} lv."
#"The discount is: {отстъпка} lv."
# 550
# The final price is:  3432.11 lv.
# The discount is: 753.39 lv.



landscaping = float(input())

price_per_square_meter = 7.61 * landscaping

discount_price = 0.18

discount = discount_price * price_per_square_meter

end_price = price_per_square_meter - discount

print(f"The final price is: {end_price} lv.")

print(f"The discount is: {discount} lv.")
