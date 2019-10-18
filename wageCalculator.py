#part 1 Calculates a woman's wage based on a man's wage and the gender wage gap

def convertWageMtoW():
   wageGap = 0

#prompts the user to input a country name and a wage amount   

   country = input("Enter the name of a country: ")
   mWage = input("Enter a wage amount: ")

#depending on each country, the wage gap is different for each one, so we used if statements so that depending on what country the user inputs, the wageGap variable adjusts accordingly so it will equal what the actual wage gap in that country is 
   if country.lower() == "united states":
        wageGap = 0.182
   if country.lower() == "korea":
        wageGap = 0.346
   if country.lower() == "luxembourg":
        wageGap = 0.034
#ratio would be 1 minus whatever the wageGap is for the inputted country. this is then multiplied by mWage to give the user the final answer

#mWage is converted to a float, because ratio is a float as well and they must match for the program to work; without it, an error message will pop up

   ratio = 1-wageGap
   product = float (mWage) * ratio
   return product

#this prints the final answer to the user, so that they can find out how much they would make in another country based on their wage

print (convertWageMtoW())

#code from the first part of the assignment
# Test Case 1
#print (convertWageMtoW(100))
# Test Case 2
#print (convertWageMtoW(76.2))
# Test Case 3
#print (convertWageMtoW(0))
# Test Case 4
#print (convertWageMtoW(98.45))
# Test Case 5
#print (convertWageMtoW(0.68))


