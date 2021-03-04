#Furkan Kerim Yildirim
#28138
GradeList = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F', 'S', 'U']
AllLessonLib = {}
def main():
    firstInput = prevInput()
    if checkInput(firstInput):
        firstEdit = editInput(firstInput)
    else:
        return
    
    if firstEdit:
        secondInput = nextInput()
    else:
        return

    if checkInput(secondInput):
        secondEdit = editInput2(secondInput)
    else:
        return

    if secondEdit:
        checkLesson()

    else:
        return


def prevInput():
    prevInput = input('Please enter the courses you have taken previously with letter grades: ')
    return prevInput

def nextInput():
    nextInput = input('Please enter the courses you have taken this semester with letter grades: ')
    return nextInput

def checkLesson():
    checkInput = input('Please enter the course you want to check: ')
    return getGrade(checkInput)
    
def checkInput(data):
    charIndex=0
    if data[-1] != ':':
        for char in data:
            if char == ':':
                testChar = data[charIndex+1].upper()
                #print(testChar)
                if testChar == ':' or testChar == ';' or testChar == None or testChar not in GradeList:
                    print('Invalid input')
                    return False
                else:
                    pass
            charIndex += 1
        return True
    else:
        print('Invalid input')
        return False
    
    
def editInput(data):
    dataList = data.split(';')
    if '' not in dataList:
        for lesson in dataList:
            lessonInfo = lesson.split(':')
            lessonInfo[1] = lessonInfo[1].upper()
            AllLessonLib[lessonInfo[0]] = lessonInfo[1]
        return AllLessonLib
    else:
        print('Invalid input')
        return False

def editInput2(data):
    dataList = data.split(';')
    if '' not in dataList:
        for lesson in dataList:
            lessonInfo = lesson.split(':')
            lessonInfo[1] = lessonInfo[1].upper()
            if lessonInfo[1] == 'F':
                if lessonInfo[0] not in AllLessonLib:       
                    AllLessonLib[lessonInfo[0]] = 'U'
                else:
                    if AllLessonLib[lessonInfo[0]] == 'U':
                        AllLessonLib[lessonInfo[0]] = 'U'
                    else:
                        AllLessonLib[lessonInfo[0]] = 'F'
            else:
                AllLessonLib[lessonInfo[0]] = lessonInfo[1]
        return AllLessonLib
    else:
        print('Invalid input')
        return False
    
def getGrade(data):
    if data in AllLessonLib:
        if AllLessonLib[data] != 'F' and AllLessonLib[data] != 'S' and AllLessonLib[data] != 'U':
            return print('You can choose between S and {} for {}.'.format(AllLessonLib[data],data))
        else:
            return print('Your grade for {} is {}.'.format(data,AllLessonLib[data]))
    else:
        return print("You didn't take {} this semester.".format(data))


if __name__ == "__main__":
    main()

