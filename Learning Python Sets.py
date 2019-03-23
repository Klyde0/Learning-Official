cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.union(art_courses))

# Sets dont care about Order in a list
# They are useful for removing duplicate values because Sets remove duplicates
# Also used to test for whether a value is in a set - do it more efficiently = membership test

print('Math' in cs_courses)