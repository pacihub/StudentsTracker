# studentstracker

program is implemented entirely with OOP.

A Student class is defined that keeps track of all created students.

The class implements the following methods, class variables and properties:

* An instance called 'name'

* A property called 'grade' that returns the student's grade. Trying to set the grade raises a ValueError if the grade is 
not a number between 0 and 100.

* A static method called calculate_average_grade(students) that accepts a list of Student objects and returns the average grade for those students. If there 
no students in the list, it returns -1.

* A class variable called all_students that stores all of the student objects that have been created in a list.

* A class method named get_average_grade() which returns the average grade of all students

* A class method get_best_student() which returns the student object with the best grade out of all the currently created students.
If there are no students created this method returns None.
It is assumed that there will always be one student with the best grade, except in the case where there are no students created.

Example of the behavior of Student class:

=> Student.get_average_grade()

-1

=> student1 = Student("Antoine", 75)

=> student1.name

"Antoine"

=> student1.grade

75

=> student1.grade = 150

Traceback (most recent call last):
  
  File "<stdin>", line 1, in <module>
  
ValueError: Not a valid grade.
  
 => student1 == Student.get_best_student()
  
  True
  
