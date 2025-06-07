FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    temp_c = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(temp_c)

def convert_to_fahrenheit(celcius):
    temp_f = celcius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(temp_f)

temp = int(input("Enter the temperature to convert: "))
c_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if c_f == "F":
    convert_to_celcius(temp)
elif c_f == "C":
    convert_to_fahrenheit(temp)
else:
    print("wrong entry")