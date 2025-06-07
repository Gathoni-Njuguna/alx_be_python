FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    temp_c = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temp_c}°C")

def convert_to_fahrenheit(celcius):
    temp_f = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{celcius}°C is {temp_f}°F")

temp = float(input("Enter the temperature to convert: "))
c_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if c_f == "F":
    convert_to_celcius(temp)
elif c_f == "C":
    convert_to_fahrenheit(temp)
else:
    print("Invalid entry. Please enter 'C' or 'F'.")