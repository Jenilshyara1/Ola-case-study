class Employee:
    # Class variable
    office_name = 'XYZ Private Limited'

    # Constructor
    def __init__(self, employee_name, employee_ID):
        self.employee_name = employee_name 
        self.employee_ID = employee_ID
  
    def show(self):
        print(self.office_name)
        print(Employee.office_name)
        # print("Name:", self.employee_name)
        # print("ID:", self.employee_ID)
        # print("Office name:", Employee.office_name)
   
# create Object
e1= Employee('Ram', 'T0166')
e2= Employee('jENIL', '12312')
e1.show()
e2.show()
print("======================")
# Modify class variable
Employee.office_name = 'PQR Private Limited'
print('After')
e1.show()
e2.show()
