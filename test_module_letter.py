


courses = ['History', 'Math', 'Physics', 'Compsci']

def find_index(list, target_index):
    for i, value in enumerate(list):
        if value == target_index:
            return i
    return -1

    print(find_index(courses, 'Math'))
#


# fruit = [['bananna',"apple",'grape'],['ham',"sammy",'canada'],['fdas', 'tim', 'Learning 1']]
# for i in fruit:
#         print (i[1])