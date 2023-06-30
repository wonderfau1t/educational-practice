
distance = float(input('Сколько километров хотите проехать на автомобиле? '))
consumption = float(input('Сколько литров топлива расходует автомобиль на 100 километров? '))
fuel = float(input('Сколько литров топлива в вашем баке? '))

# Сколько топлива уходит на 1км пути
fuel_per_km = round(consumption / 100, 2)

if fuel >= fuel_per_km * distance:
    print('Вам хватит бензина в баке для преодоления желаемого расстояния')
else:
    print(f'К сожалению вам не хватит топлива, заправьте бак еще на {fuel_per_km * distance - fuel}л')
