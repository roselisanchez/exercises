#STUDENT BECOMES THE TEACHER: make a gradebook for all of your students.

#estudantes
adriane = {
  "name": "Adriane",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alicia = {
  "name": "Alicia",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
renata = {
  "name": "Renata",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

#funções
def average(numbers):
#calcula média
  total = sum(numbers)
  total = float(total)/ len(numbers)
  return total

def get_average(student):
#calcula as médias referentes a cada atividade
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return ((homework * 0.1) + (quizzes * 0.3) + (tests * 0.6))

def get_letter_grade(score):
#atribui letras como conceitos segundo a média obtida
  if score >= 90:
    return "A"
  elif score >= 80:
    return"B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  print score
  
def get_class_average(class_list):
#calcula a média da turma
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

#testando as funções
students = [adriane, alicia, renata]
print get_class_average(students)
print get_letter_grade(get_class_average(students))
