def route_cost(distance, fuel_efficiency,fuel_price):
    if( 0<distance<=100 )and fuel_efficiency>0 and fuel_price>0:
        cost = ((distance/fuel_efficiency)*fuel_price)+5
        return round(cost,2)
    elif distance>100 and fuel_efficiency>0 and fuel_price>0:
      cost=(((distance/fuel_efficiency)*fuel_price)+5)*1.10
      return round(cost,2)
    else:
      return "error"

a = float(input("enter distance  : "))
b = float(input("enter fuel efficiency : "))
c = float(input("enter fuel price : "))
print(route_cost(a,b,c))
