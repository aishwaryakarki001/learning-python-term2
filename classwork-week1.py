class Person: #Creating a class name person
    # Initializing instance variables
    def __init__(self,name,sex,profession): 
        self.name = name
        self.sex= sex
        self.profession= profession
        #Distinguishing pronoun by gender
        self.pronoun = 'She' if sex == 'Female' or self.sex == 'female' else 'He'
    
    #Creating behavior-working function
    def working(self, company = ''):
        #Conditional statement for company name if available or not
        companyText = ' at '+ company if company != '' else ''
        #returning working behavior with the pronoun, profession and company name
        return (self.pronoun +' is working as a ' + self.profession + companyText)

    #Creating behavior-working function
    def study(self, hours):
        return (self.pronoun +' studies '+ str(hours) +' hours a day')

# Create instances of the Person class
person1= Person('Jessa','Female','Software Engineer')
# Printing information about person1 
print('Object 1 : '+person1.name)
print('State :' )
print('Name: '+ person1.name)
print('Sex: '+person1.sex)
print('Profession: '+person1.profession)
print('Behavior: ')
print(person1.working('ABC Company'))
print(person1.study(2))

# Create another instance of the Person class
person2= Person('Jon','Male','Doctor')
# Printing information about person2
print('Object 2 : '+person2.name)
print('State :' )
print('Name: '+ person2.name)
print('Sex: '+person2.sex)
print('Profession: '+person2.profession)
print('Behavior: ')
print(person2.working(''))
print(person2.study(5))