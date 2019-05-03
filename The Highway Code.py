import easygui as eg

# functions


def mainMenu():  # produces main menu
    title = "Main Menu"
    msg = "Do you wish to begin the test?"
    choices = ["Begin", "Quit"]
    main_menu = eg.buttonbox(title=title, msg=msg, choices=choices)  # produces a buttonbox using variables above

    return main_menu  # returns "Begin" or "Quit"


def questions():  # produces questions
    points = 0  # stores the points

    incorrect = []  # stores missed answers in array

    for i in range(0, 5):  # for loop iterates 5 times for each question
        # questions & filenames etc. stored as 2D array, which is defined by a number using a dictionary

        content = {0: [["Which of these warns of falling rocks?", 2],
                      ["AheadOnly.gif", "FallingRocks.gif", "SteepHill.gif"]],

                   1: [["Which of these means ‘No stopping’?", 1],
                      ["NoStopping.gif", "NoOvertaking.gif", "AheadOnly.gif"]],

                   2: [["Which of these means there are strong side winds?", 1],
                      ["Sidewinds.gif", "TurnLeft.gif", "NoEntry.gif"]],

                   3: [["Which of these means no motor vehicles allowed?", 1],
                      ["NoMotorVehicles.gif", "CycleRoute.gif", "NoVehiclesOverThisHeight.gif"]],

                   4: [["Which of these means no through road?", 1],
                      ["NoThroughRoad.gif", "OpeningBridgeAhead.gif", "UnevenRoads.gif"]]
                  }

        title = "Question {q}".format(q=i+1)
        # produces buttonbox using the variable title, and the content dictionary
        question = eg.buttonbox(title=title, msg=content[i][0][0], image=content[i][1], choices =[])

        answer = content[i][0][1] - 1
        answer_msg = str(content[i][1][answer])  # gets correct answer from dictionary

        if question == answer_msg:  # if answer is correct, buttonbox informs user
            points += 1

            title = "Correct!"
            msg1 = "Correct."

            choices = ["Continue"]
            eg.buttonbox(title=title, msg=msg1, image=answer_msg, choices=choices)

        else:  # if not correct, buttonbox informs user
            title = "Incorrect!"
            msg1 = "Incorrect, this was the correct answer:"

            choices = ["Continue"]
            eg.buttonbox(title=title, msg=msg1, image=answer_msg, choices=choices)

            incorrect.append(answer_msg)  # appends answer to list of missed answers

    return [str(points), incorrect]  # casts points as a string, and stores the incorrect array and points as a 2D array

# logic


if mainMenu() == "Begin":  # if mainMenu function returns begin, questions function is called
    points = questions()

    if len(points[1]) is not 0:  # if there are missed answers, message is modified
        msg = "You got {p} points. Here are the answers you missed:".format(p=points[0])

    else:  # if there are no missed answers, message includes the points only
        msg = "You got {p} points.".format(p=points[0])

    title = "Results"
    image = points[1]  # sets missed answers to a variable
    choices = ["Quit"]

    eg.buttonbox(title=title, msg=msg, image=image, choices=choices)  # produces buttonbox using variables above

else:  # if mainMenu function returns quit, python quits program
    quit()