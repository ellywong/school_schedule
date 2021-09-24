from school_schedule.student import Student
def test_student_class_name_is_correct():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  # assert
  assert student.name == "Trenisha"

def test_student_class_course_list_type_is_list():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

  # assert
  assert type(student.classes) == list

def test_student_year_string_type_is_string():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

  # assert
  assert type(student.grade) == str

def test_class_number_is_four():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

  # assert
  assert len(student.classes) == 4

def test_add_class_append_class_to_classes_list():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

  Student.add_class(student, "Science")

    # assert
  assert student.classes == ["Calculus", "Choir", "Photography", "AP History", "Science"]
