# employee_file = open('employees', 'a')
# employee_file.write('Billy - CEO')
# employee_file.close()

# you need to be careful with append because you may accidentally mess up your file
# append may be appended to where it already was

# employee_file = open('employees', 'a')
# employee_file.write('\nKelly - Customer Service')
# employee_file.close()

# if you want the information to append to a new line, you need to have \n

# WRITING ON FILES 'w' - will overwrite whatever's written in the file

employee_file = open('employees', 'w')
employee_file.write('Kelly - Customer Service')
employee_file.close()

# You can also generate new files ex. employees1
# MORE POWERFULLY, YOU CAN ALSO CREATE DIFFERENT TYPES OF FILES USING 'w'- ex. employee_file = open('index.html', 'w')