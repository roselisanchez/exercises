#TAKING A VACATION

def hotel_cost(nights):
  #$140 por noite
  return 140 * nights

def plane_ride_cost(city):
  #calcular valor da passagem ida-volta
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
  	return 222
  elif city == "Los Angeles":
  	return 475

def rental_car_cost(days):
  #aluguel do carro $40 por dia
  car_cost = 40 * days
  if days >= 7:
    car_cost -= 50
  elif days >= 3:
    car_cost -= 20
  return car_cost

def trip_cost(city, days, spending_money):
  #custo total da viagem
  #spending_money para comidas, presentes, etc.
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
