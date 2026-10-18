import os
import pickle
class StudentReportCard():
    def __init__(self):
        print("***** STUDENT REPORT CARD SYSTEM *****\n")
        self.name=""
        self.roll_no=0
        self.marks=[]
        self.total=0
        self.percentage=0.0
        self.grade=""
    def input_detail(self):
        self.name=input("Enter student's name:")
        self.roll_no=int(input("Enter roll number:"))
        print()
        print("Enter marks for 3 subjects (out of 100):")
        self.marks=[]
        for i in range(1,4):
            m=float(input(f'Subject {i} marks:'))
            self.marks.append(m)
    def calculate_result(self):
        self.total=sum(self.marks)
        self.percentage=((self.total)/len(self.marks))
        if self.percentage>=85:
            self.grade='A+'
        elif self.percentage>=70:
            self.grade='A'
        elif self.percentage >= 50:
            self.grade = "B"
        elif self.percentage >= 35:
            self.grade = "C"
        else:
            self.grade = "Fail"
    def display_report(self):
        print('='*30)
        print('   OFFICIAL REPORT CARD    ')
        print('='*30)
        print("Student Name:",self.name)
        print("Student Roll_no:",self.roll_no)
        print("-"*30)
        for i,j in enumerate(self.marks,1):
            print(f' Subject {i} :{j}')
        print("-"*30)
        print("Total Marks :",self.total,'/300')
        print("Percentage  :",self.percentage,"%")
        print("Grade       :",self.grade)
        print("="*30 + "\n")
        obj=open("Student_Details.dat","ab+")
        students_details={
            "Name":self.name,
            "Roll_no":self.roll_no,
            "Marks": self.marks,
            "Total": self.total,
            "Percentage": self.percentage,
            "Grade": self.grade
            }
        pickle.dump(students_details,obj)
        obj.close()
        print("Dictionary created successfully:")
        
def main():
    student=StudentReportCard()
    while True:
        print("1. Enter Student Details & Marks")
        print("2. Calculate Result")
        print("3. Show Report Card")
        print("4. Exit")
        print("5. Search Student Details")
        
        choice = int(input("\nEnter your choice (1-5): "))
        if(choice==1):
            student.input_detail()
        elif(choice==2):
            student.calculate_result()
            print("\nResult calculated successfully!\n")
        elif(choice==3):
            student.display_report()
        elif(choice==4):
            print("Exiting program. Good bye!")
            quit()
        elif(choice==5):
            print("****** All STUDENT DETAILS ******\n")
            pre_std=input("Enter previous student name:")
            if not os.path.exists("Student_Details.dat"):
                print("No previous customer records found.")
                continue
            found = False
            with open("Student_Details.dat", "rb") as obj:
                while True:
                    try:
                        students_details = pickle.load(obj)
                        
                        if students_details['Name'].lower().strip() == pre_std.lower().strip():
                            print("\n--- Student Found! ---")
                            print(f"Name       : {students_details['Name']}")
                            print(f"Roll No    : {students_details['Roll_no']}")
                            print(f"Marks      : {students_details['Marks']}")
                            print(f"Total Marks: {students_details['Total']}/300")
                            print(f"Percentage : {students_details['Percentage']}")
                            print(f"Grade      : {students_details['Grade']}\n")
                            found = True
                            break
                    except EOFError:
                        break
                        
            if not found:
                print("Student Not Found\n")
        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")
main()
            
                  
                                            
        

            
        
            
    
        
        
        
        
