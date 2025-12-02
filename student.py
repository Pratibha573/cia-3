def Student_details(name,student_id,course,year,fees):
   result=(
    f"Student Name:{name}\n"
    f"Student ID:{stud_id}\n"
    f"Course:{course}\n"
    f"Year:{year}\n"
    f"Fees:{fees}"
    )
   
   return result
if __name__=="__main__":
   #sample output(you can change)
   name="Alice"
   stud_id="E1001"
   course="bca"
   year=2
   fees=55000

   print(Student_details(name,stud_id,course,year,fees ))
