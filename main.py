# Author: Dymea Schippers dxs5940@psu.edu

def getGradePoint(grade):
  gradepoint = 0.0
  if grade == "A":
    gradepoint = 4.0
  elif grade == "A-":
    gradepoint = 3.67
  elif grade == "B+":
    gradepoint = 3.33
  elif grade == "B":
    gradepoint = 3.0
  elif grade == "B-":
    gradepoint = 2.67
  elif grade == "C+":
    gradepoint = 2.33
  elif grade == "C":
    gradepoint = 2.0
  elif grade == "D":
    gradepoint = 1.0
  else:
    gradepoint = 0.0
  return gradepoint

def run():
  GPA_total = 0.0
  credit_total = 0.0

  for i in range(1,4):
    grade = input(f"Enter your course {i} letter grade: ")
    gradepoint = getGradePoint(grade)
    credit = float(input(f"Enter your course {i} credit: "))
    print(f"Grade point for course {i} is: {gradepoint}")
    GPA = gradepoint * credit
    GPA_total += GPA
    credit_total += credit
  GPA = GPA_total / credit_total
  print(f"Your GPA is: {GPA}.")

if __name__ == "__main__":
  run()