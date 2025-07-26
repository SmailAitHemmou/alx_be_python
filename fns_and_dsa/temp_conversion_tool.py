  # Temperature Conversion Tool :

temp = float(input("Enter the temperature to convert: "))
c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def celsius_to_fahrenheit():
    if c_or_f.lower() == 'c':
        celsius = ( temp * 9/5) + 32
        print(f"{temp}°C is {celsius}°F")
        return
    elif c_or_f.lower() == 'f':
        fahrenheit = (temp - 32) * 5/9
        print(f"{temp}°F is {fahrenheit}°C")
        return
    else:
        print("Invalid temperature. Please enter a numeric value.")
celsius_to_fahrenheit()
