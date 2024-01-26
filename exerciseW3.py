'''
write a python program that takes from the user the employee's name, number of hours,
 pay rate and tax percent (??%) and calc. the gross pay and net pay (after deducting the tax amount),
  then prints the name, gross and net amounts using format function. Use input in a single line separated with
  ;
'''


#for regular expression
import re 

def main():
    #Get employee details from user input
    employeeDetail = getEmployeeDetail()
    grossAmt = employeeDetail['hours'] * employeeDetail['payRate']
    netAmt = grossAmt - (employeeDetail['taxRate']/ 100) * grossAmt

    #Output to be displayed
    print('Employee name:', employeeDetail['name'])
    print(f'Gross Pay: {grossAmt:.2f}')
    print(f'Net Pay: {netAmt:.2f}')


## Function to get employee details from user input
def getEmployeeDetail():
    while True:
        rawData = input("Enter employee details separated with ';' :").strip()

        #validation for the data whether it is inputted or not
        if rawData != '':

            employeeDetails = rawData.split(';')
            
            #Validation for checking if all the data is provided or not
            if not len(employeeDetails) == 4:
                print('Please enter all the details.')
            else:
                employeeName = employeeDetails[0]
               
               #Validation to check if any of the data is not provided
                if employeeName == '' or employeeDetails[1] == '' or employeeDetails[2] =='' or employeeDetails[3] == '':
                    print('Please enter all the details')
                else:

                    #Validation to check if the data for hour, payrate and taxrate provided is numeric or not
                    if not (is_numeric(employeeDetails[1]) and is_numeric( employeeDetails[2]) and is_numeric( employeeDetails[3])):
                        print('Enter hours, payrate, taxrate as numeric')
                    else:
                        workingHours = float(employeeDetails[1])
                        payRate = float(employeeDetails[2])
                        taxRate = float(employeeDetails[3])

                        #Validation to check if the user entered there full name or not
                        if " " in employeeName:
                            return {'name' : employeeName, 'hours' :workingHours, 'payRate': payRate,  'taxRate': taxRate}
                        else: 
                            print('Please enter the full name !')
        else: 
            print('Please provide the details !')

#Function to check the validation if the value is numeric or not
def is_numeric(n):
    pattern = r'^-?\d+(?:\.\d+)?$'
    if re.match(pattern, n):
        return True
    return False


main ()
