# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент. Използвайте следната формула:
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
# Вход
# От конзолата се четат 3 реда:
# Депозирана сума – реално число;
# Срок на депозита(в месеци) – цяло число;
# Годишен лихвен процент – реално число;

deposit_amount = float(input())
term_deposit_in_mounts = int(input())
annual_interest_rate = float(input())

# изчисляваме натрупаната лихва: 200 * 5.7% = 11.4лв.
calcilation_of_accured_interest = deposit_amount * (annual_interest_rate / 100)
# изчисляваме лихвата за 1 месец: 11.4лв./12 месеца = 0.95лв
calcilation_of_interes_rate_for_one_month = calcilation_of_accured_interest / 12
# общата сума е 200лв депозит + (3 (срок на депозита) * 0.95 лв)
total_sum = deposit_amount + term_deposit_in_mounts * calcilation_of_interes_rate_for_one_month
print(total_sum)




# Вход / Изход
#200
#3
#5.7
# 202.85