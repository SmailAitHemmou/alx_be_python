  # Temperature Conversion Tool :

temperature = float(input("Enter the temperature to convert: "))
c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def celsius_to_fahrenheit():
    if c_or_f.lower() == 'c':
        CELSIUS_TO_FAHRENHEIT_FACTOR = ( temperature * 9/5) + 32
        print(f"{temperature}°C is {CELSIUS_TO_FAHRENHEIT_FACTOR}°F")
        return
    elif c_or_f.lower() == 'f':
        FAHRENHEIT_TO_CELSIUS_FACTOR = (temperature - 32) * 5/9
        print(f"{temperature}°F is {FAHRENHEIT_TO_CELSIUS_FACTOR}°C")
        return
    else:
        print("Invalid temperature. Please enter a numeric value.")
celsius_to_fahrenheit()
