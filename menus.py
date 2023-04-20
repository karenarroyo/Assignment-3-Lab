from student import Student
from teacher import Teacher
from grade import Grade
from load import Load

students = []
teacher = []

def addStudents():
    while True:
        print()
        print('T- add Teacher')
        print('S- add Students')
        print()
        add = input('What do you want to add?')
        add = add.upper()
        print()
        if add == 'S':
            id = input('Enter id: ')
            lastName = input('Enter last name: ')
            firstName = input('Enter first name: ')
            middleName = input('Enter middle name: ')
            type = input('Enter type: ')
            course = input('Enter Course: ')
            year = input('Enter year: ')
            section = input('Enter section: ')
            print('----------------------------')
            filipino = input('Grade filipino: ')
            math = input('Grade math: ')
            science = input('Grade science: ')
            english = input('Grade english: ')

            stud = Grade(filipino, math, science, english)
            stud.id = id
            stud.last_name = lastName
            stud.first_name = firstName
            stud.middle_name = middleName
            stud.type = type
            stud.course = course
            stud.year = year
            stud.section = section

            students.append(stud)
        elif add == 'T':
            id = input('Enter ID: ')
            lastname = input('Enter lastname: ')
            firstname = input('Enter Firstname: ')
            middlename = input('Enter Middlename: ')
            type = input('Enter Type: ')
            print('-------------------------------------')
            department = input('Enter department')
            position = input('Enter position')
            subject = input('Enter subject:')
            tchr = Load(subject)
            tchr.department = department
            tchr.position = position
            tchr.id = id
            tchr.lastname = lastname
            tchr.firstname = firstname
            tchr.middlename = middlename
            tchr.type = type
            teacher.append(tchr)
            ans = input('Enter another? [y/n]: ')
        else:
            menu ( )
            print()
            ans = input('Enter another? [y/n] : ')
            ans = ans.lower()
        if (ans != 'y'):
         break

    menu()

def deleteRecord():
            print('T = Delete from Teacher')
            print('S = Delete from student')
            print('DT = Delete Teachers')
            print('DS = Delete Students')
            print('Z = Delete All')
            delete = input('What do you want to delete?')
            delete = delete.upper()

            if delete == 'S':
                i = int(input('Enter index:'))
                students.remove(i)

            elif delete == 'T':
                i = int(input('Enter index: '))
                teacher.remove(i)
            elif delete == 'DT':
                i = int(input('Enter index: '))
                teacher.remove(i)
            elif delete == 'Z':
                i = int(input('Enter index: '))
                students.remove(i)
                teacher.remove(i)
            else:
                 deleteRecord()

            menu()


def searchRecord():
            print('T = Search Teacher')
            print('S = Search from student')
            print()
            search = input('Type do you want to search: ')
            search = search.upper()
            if search == 'S':
                i = int(input('Enter index: '))
                print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')
            elif search == 'T':
                i = int(input('Enter index:'))
                print(f'{i}\t {teacher[i].Type()} \t {teacher[i].getName()} | {teacher[i].getID()}' | {
                    teacher[i].getDept()} | {teacher[i].getPosition()})
            else:
                searchRecord()

                menu()

def displayRecords():
                print()
                print()
                print('T = Display from Teacher')
                print('S = Display from student')
                print('A = Display All')
                print()

                display = input('What do you want to display?')
                display = display.upper()

                if display == 'S':
                    print()
                    print('---------------------------------------------------------------------------------')
                    i = 0
                    for s in students:
                        print(f'{i}\t {students[i].Type()} \t {students[i].getName()} \t | {students[i].getID()} \t | {students[i].YrCourseSec()}')
                    i += 1
                    print('--------------------------------------------------------------------------------------')
                elif display == 'T':
                    print()
                    print('---------------------------------------------------------------------------------------------------------------------------------')
                    i = 0
                    for t in teacher:
                        print(
                            f'{i}\t {t[i].Type()} \t {t[i].getName()} \t | {t[i].getID()} \t | {t[i].YrCourseSec()}')
                    i += 1
                    menu()
                elif display == 'A':
                    print()
                    print(
                        '---------------------------------------------------------------------------------------------------------------------------------')
                    i = 0
                    for s in students:
                        print(f'{i}\t {students[i].Type()} \t {students[i].getName()} \t | {students[i].getID()} \t | {students[i].YrCourseSec()}')
                    i += 1
                    for t in teacher:
                        print(
                            f'{i}\t {t[i].Type()} \t {t[i].getName()} \t | {t[i].getID()} \t | {t[i].YrCourseSec()}')

                    else :
                        displayRecords()
def menu():
    print()
    print()
    print('::Menu::')
    print('D - delete record        S - search record')
    print('A - add record           M - display all')
    print()
    choice = input('Enter a function: ')
    if (choice == 'D'):
        deleteRecord()
    elif (choice == 'A'):
        addStudents()
    elif(choice == 'S'):
        searchRecord()
    elif (choice == 'M'):
        displayRecords()

    print()

menu()