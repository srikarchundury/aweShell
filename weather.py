import pyowm
owm = pyowm.OWM('81553685bbd49eaa92bea218e44a87d0')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London,GB')  
w = observation.weather
print('Wind ',w.get_wind())
print('temperature ',w.get_temperature('celsius')) 
print('Humidity ',w.get_humidity())
print("Clouds ",w.get_clouds())
print("Rain Volume ",w.get_rain())
print("Detailed Weather status ",w.get_detailed_status())