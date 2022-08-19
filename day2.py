#your life in weeks
age = input("what is your current age?")

year =90-int(age)
month = year *12
day = year *365

print(f"your have {year} years, {month} months and {day}days left ")



#tip calculator
print("welcome to tip calculator:")

bill =input("what is the total bill? $")

tip= input("what percentage tip would you like to give(10/12/15)")

split= input("how many people to split the bill?")

a= float(bill)
b= int(tip)
c= int(split)
percentage = a* (1+ (b/100))

divide =round( percentage/c ,2)

print(f"Each person should pay ${divide} ")
