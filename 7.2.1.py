from sense_hat import SenseHat
sense = SenseHat()
temperature = sense.get_temperature()
humidity = sense.get_humidity()
print("Temperature: ", temperature, " Humidity: ", humidity)

# no all these decimal places are not meaningful. The data is represented by 16 bits, giving a resolution of 65536.
# by the data sheet the least significant bit of temperature represents 0.016 C. and for humidity represents 0.004rH
# this means 3 decimal places will fully capture the full sensitivity of both temperature and humidity
