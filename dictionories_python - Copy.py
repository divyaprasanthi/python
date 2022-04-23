student_dict={
    'name'   :'python',
    'roll_no':345,
    'CGPA'    :69,
    'subjects':['maths','physics','chemistry'],
    'native_place':'india'
}
print(type(student_dict))
print(student_dict["name"])
print(student_dict["subjects"])
print(student_dict["subjects"][-1])
print(student_dict["CGPA"])
print(student_dict.get('company'))
print(student_dict.get('company','company key does not exit'))
print(student_dict.get('company',-1))
print(student_dict)
