# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names=["Maria","Rohan","Valentina"]
insurance_cost=[4150.0,5320.0,35210.0]
insurance_data=list(zip(names,insurance_cost))
estimated_insurance_data=[]
estimated_insurance_data.append(("Maria",maria_insurance_cost))
estimated_insurance_data.append(("Rohan",rohan_insurance_cost))
estimated_insurance_data.append(("Valentina",valentina_insurance_cost))
print("Here is the actual insurance cost data "+str(insurance_data))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))
insurance_cost_difference = []
insurance_cost_difference.append(("Maria",abs(maria_insurance_cost-insurance_data[0][1])))

insurance_cost_difference.append(("Rohan",abs(rohan_insurance_cost-insurance_data[1][1])))

insurance_cost_difference.append(("Valentina",abs(valentina_insurance_cost-insurance_data[2][1])))
print(insurance_cost_difference)

akira_insurance_cost = estimate_insurance_cost(name = "Akira", age=19, sex=1,bmi=27.1,num_of_children=0,smoker=0)

insurance_data.append(("Akira",2930.0))
estimated_insurance_data.append(("Akira",akira_insurance_cost))
print(insurance_data)
print(estimated_insurance_data)
insurance_cost_difference.append(("Akira",abs(akira_insurance_cost - insurance_data[3][1])))
print(insurance_cost_difference)
