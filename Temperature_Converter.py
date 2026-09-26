# Conversion of temperature
unit = input("Convert into (C)elsius or (F)ahrenheit?:").upper()
if unit == "C":
    temp = float(input("Enter the temperature in Fahrenheit:"))
    temp = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {round(temp, 2)}\N{DEGREE SIGN}C")
elif  unit == "F":
    temp = float(input("Enter the temperature in Celsius:"))
    temp = temp * 9 / 5 + 32
    print(f"Temperature in Fahrenheit: {round(temp,2)}\N{DEGREE SIGN}F")
else:
    print(f"{unit} is invalid")