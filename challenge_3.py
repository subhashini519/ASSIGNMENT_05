class Student:
    def __init__(self):
        # Private properties
        self.__name = ""
        self.__rollNumber = ""

    # Getter and setter methods for 'name'
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    # Getter and setter methods for 'rollNumber'
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

# Sample usage
student = Student()

# Set name and rollNumber using setter methods
student.setName("John")
student.setRollNumber("12345")

# Get and print the values using getter methods
print("Name:", student.getName())
print("Roll Number:", student.getRollNumber())
