# Author RTS 12/9/21

def grade (choice):
    if choice < 60:
        print("F")
    elif choice <= 64:
        return("D")
    elif choice <= 69:
        return("D+")
    elif choice <= 72:
        return("C-")
    elif choice <= 76:
        return("C")
    elif choice <= 79:
        return("C+")
    elif choice <= 82:
        return("B-")
    elif choice <= 86:
        return("B")
    elif choice <= 89:
        return("B+")
    elif choice <= 92:
        return("A-")
    elif choice <= 100:
        return("A")

choice = input("Enter your Grade: ")
grade(int(choice))

print(grade)
