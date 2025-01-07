choice = input("Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F) ").upper()
temperature = float(input("Enter the temperature: "))

if choice == "C":
    converted = (temperature * 9 / 5) + 32
    print(f"{temperature:.0f}°C is equal to {converted:.0f}°F")
elif choice == "F":
    converted = (temperature - 32) * 5 / 9
    print(f"{temperature}°F is equal to {converted}°C")
else:
    print("Invalid choice")

"""
Breaking down :.2f:
: This is the start of the format specifier in an f-string.
.2: The number 2 indicates the number of decimal places we want to display. 
f: The f means that we are working with a floating-point number (a number with decimals). 
"""
