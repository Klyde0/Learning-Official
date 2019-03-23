# Often times in Python, you will want to read Python files outside of your current file
# ex. txt file, html file, etc.for
# use open() - relative, absolute path to file, or just file name if its in the same directory
# "r" = just read file
# "w" = write on the file (change existing information
# "a" = append (add) new information to the file
# "r+" = read and write on the file (basically gives you all the power over the file



employee_file = open('employees', 'r')
for employee in employee_file.readlines():
    print(employee)


# generally its a good idea to check if a file is readable = file.readable()
# .readline() - gives us the first line
# .readlines() - gives us all the lines in an array
employee_file.close()

# typically you want to close files after you open them so you are no longer able to access it
