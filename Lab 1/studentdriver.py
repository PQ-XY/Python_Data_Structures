from random import randint
from student import Student

def main(numScores = 3):
    """Tests Student class."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Juan", "Bill", "Stacy", "Maria", "Charley")
    for name in names:
        s = Student(name, numScores)
        for index in range(numScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    # Print the contents
    print("The list of students:")
    for s in students:
        print(s)
        
if __name__ == "__main__":
    main()