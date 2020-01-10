import pyowm
from colorama import Fore, Back

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
print( Back.GREEN)
print( Fore.BLACK)

place = input("Change your city: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]

print( Back.CYAN )
print( Fore.BLACK)
print(" In the city " + place + " now " + w.get_detailed_status())

print( Back.BLUE )
print( Fore.BLACK)
print( "Temperature now " + str(temp) )

if temp < 10:
    print( "The coldest" )
elif temp < 20:
    print( "Very cold" )
else:
    print( "Normally" )