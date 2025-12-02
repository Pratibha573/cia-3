from student import Student_details
def test_student_details():
 expected_output=(
    "Student Name:Alice\n"
    "Student ID:E1001\n"
    "Course:bca\n"
    "Year:2\n"
    "Fees:55000"
)
    assert student_details("Alice","E1001","bca",2,55000)==expected_output
