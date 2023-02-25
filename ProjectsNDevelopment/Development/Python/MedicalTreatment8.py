class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num + 24000 * self.smoker - 125000
    print("{Patient}'s estimated insurance costs is {estimated} dollars.".format(Patient=self.name,estimated=estimated_cost))
  
  def update_age(self, new_age):
    self.age = new_age
    print('{Patient} is now {page} year old.'.format(Patient=self.name, page=new_age))
    self.estimated_insurance_cost()

  def update_num_children(self,new_num_children):
    self.num = new_num_children
    if self.num == 1:
      print('{Patient} has {num} child'.format(Patient=self.name, num=self.num))
    else:
      print('{Patient} has {num} children'.format(Patient=self.name, num=self.num))

  def patient_profile(self):
    patient_information = {}
    patient_information["name"] = self.name
    patient_information["age"] = self.age
    patient_information["sex"] = self.sex
    patient_information["bmi"] = self.bmi
    patient_information["num"] = self.num
    patient_information["smoker"] = self.smoker
    return patient_information

  def update_bmi(self,new_bmi):
    self.bmi = new_bmi
    print('{Patient} has new {bmi} bmi'.format(Patient=self.name, bmi=self.bmi))

  def update_smoking_status(self,smoking):
    self.smoker = smoking
    print('{Patient} has {that} started smoking'.format(Patient=self.name, that=self.smoker))

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0) 
patient1.estimated_insurance_cost()
patient1.update_age(26)
patient1.update_num_children(3)
patient1.estimated_insurance_cost()
print(patient1.patient_profile())
patient1.update_bmi(25.1)
patient1.estimated_insurance_cost()
patient1.update_smoking_status(1)
patient1.estimated_insurance_cost()