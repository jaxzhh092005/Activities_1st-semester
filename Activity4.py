# Fahrenheit to Celsius conversion and rounding

f = eval(input("Enter the Fahrenheit to convert:"))
c = (f - 32) * 5 / 9

print(f"\n{f} degree Fahrenheit converted to Celsius is {round(c, 2)}")

cel = eval(input("\nEnter the Celsius:"))
fah = (cel * 9 / 5) + 32

print(f"\n{cel} degree Celsius converted to Fahrenheit is {round(fah, 2)}")
