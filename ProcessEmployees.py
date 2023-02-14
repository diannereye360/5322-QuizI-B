'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

#open the file

cust_repr = open("employee_data.csv","r")

repr_infile = csv.reader(cust_repr, delimiter=",")

header = next(repr_infile)


#create an empty dictionary

repr_sal_up = {}

#use a loop to iterate through the csv file

tot_cur = 0.0
tot_new = 0.0
for r in repr_infile:
    #check if the employee fits the search criteria

    if r[9] == 'TS' and r[3] == 'Marketing':
        
        emp_name = r[1]+' '+r[2]
        cur_sal = int(r[5])
        tot_cur += cur_sal
        print(f'Employee Name: {emp_name} Current Salary: ${cur_sal:.2f}')

        up_sal = cur_sal + (cur_sal*.10)

        repr_sal_up[emp_name] = up_sal
        tot_new += up_sal
    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per image

for rep in repr_sal_up:
    print(f'Employee Name: {rep} New Salary: ${repr_sal_up[rep]:.2f}')


          

print()
print('=========================================')
print()

#print out the total difference between the old salary and the new salary as per image.
tot_inc = tot_new - tot_cur

print(f'Total Increase in Salary:${tot_inc:.2f}')

