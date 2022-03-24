#In your Week 1 folder, create a file called payroll.py
#In the file payroll.py create a class to store an employee.  This class must have the following data elements defined

    #week 1 assignment

class Employee:

	def __init__(self, firstname, lastname, employeeid,hourlypay):
		self.firstname = firstname
		self.lastname = lastname
		self.employeeid = employeeid
		self.hourlypay = hourlypay
	
def getFirstName(self):
	    return self.firstname
    
def setFirstName(self,firstName):
         self.firstName= firstName
		
def setLastName(self, last):
        self.lastname=last
	
def getLastName(self):
	    return self.lastname	    
        
def setID(self, id):
        self.employeeid= id   
         
def getID(self):
        return self.employeeid

def setHourlyPay(self, pay):
        self.hourlypay=pay    
        
def getHourlyPay(self):
        return self.hourlypay    
        
def pay (self,hoursWorked):
        if hoursWorked <= 40.0:
            return self.hourlypay * hoursWorked
         
        else:
            weeklyPay =self.hourlypay *40
            weeklyPay += (self.hourlypay*1.5)*(hoursWorked-40)
            return weeklyPay
        
id = int(input("Please enter your employee ID:"))
fName=input("Please enter your employee's First Name:")  
lName=input("Please enter your employee's Lasst Name:")
pay=input("Please enter your employee's Hourly Pay Rate:")
newEmployee= Employee ("fName, lName, id,pay")
hours= float(input("HOw many hours did"+newEmployee.getFirstNAme()+"work this week?"))
print("{0} {1}'s paycheck amount is ${2:2f}".format(newEmployee.getFirstName(),newEmployee.getLastName(),newEmployee.pay(hours)))




#Your class must also have a method called “pay” that has the following:
#Accepts the total hours worked by the employee during the week as a parameter.  This value will be float. (ie: 40.0, 35.5, 44.25).
#If the hours are equal to or less than 40 hours, pay the employee their hourly rate times the number of hours worked.
#If the hours are greater than 40 hours, pay the employee their hourly rate for the first 40 hours and then pay them 1.5 times their hourly rate for the additional hours.  
#The method must return their pay amount as a float.
#Prompt the user to enter necessary information to create an employee.
#Prompt the user to enter the hours worked for the week for the employee
#Print the employee’s name along with their total pay for the week.
 


