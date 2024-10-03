
    
BOEING_747_SPEED = 576  
distance = float(input("Distance to destination (miles): "))
wind_speed = float(input("Wind speed (mph, positive for tailwind, negative for headwind): "))
adjusted_speed = BOEING_747_SPEED + wind_speed

   
flight_time = distance / adjusted_speed

    
print(f"Estimated flight time: {flight_time:.2f} hours")


