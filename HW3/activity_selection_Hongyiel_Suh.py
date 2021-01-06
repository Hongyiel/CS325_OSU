# OSU 325
# HONGYIEL SUH
def getSelection(activities):
    # getSelection function will running algoritim
    selectedActivity = []
    # define selectedActivity
    activities = sorted(activities, key=lambda a: a['start'])
    # first element in activities to append
    activityTime = max([x['last'] for x in activities])
    # find the largest of last time
    while activities:
        act_selected = activities.pop()
        # adding smaller or equal array when previous finished time's array is samll in selectedActivity
        if act_selected['last'] <= activityTime:
            selectedActivity.append({
            'index': act_selected['index'],
            'start': act_selected['start']
            })
            # get append on the selectedActivity
            activityTime = act_selected['start']
            # setting activityTime
    return selectedActivity

#######################OPENING act file to read function########################
with open("act.txt", "r") as file_open:
    lines = file_open.read().splitlines()
    # settingActivity is used to store different sets of activity from file
    settingActivity = []
    activities = []
    # activities is array to store all the activities in one set
    # read line by line
    while lines:
        line = lines.pop(-1)
        # lines.pop(-1) will give the last of the list array (11,12,16)
        line = [int(num) for num in line.split(" ")]
        # splits line in " "
        if len(line) == 1 or not lines:
            if len(activities):
                settingActivity.append(activities)
                    # capsuling all arrays
                    # the biggest different between activities and settingActivity is that
                    # the settingActivity's array format will show below the array formats
                            # [[{'index': 11, 'start': 12, 'last': 16},
                            # {'index': 10, 'start': 2, 'last': 14},
                            # {'index': 9, 'start': 8, 'last': 12}, ...]]
                # storing all activities array
        else:
            # SETTING index (for number)
            # setting starting point of the line
            # setting last point of the line
            activities.append({
                'index': line[0],
                'start': line[1],
                'last': line[2]
            })
            # The activities's array format will show below the array formats
            # [{'index': 11, 'start': 12, 'last': 16},
            # {'index': 10, 'start': 2, 'last': 14},
            # {'index': 9, 'start': 8, 'last': 12}, ...]
            # listed example [{index: 1, start: 1, last: 4} ... ]

    i = 1
    # init i for avoid belowing error
    # Traceback (most recent call last):
    # File "hong.py", line 63, in <module>
    # i = i + 1

    for s in settingActivity:
        act_selected = getSelection(s)
        # sorting array's result
        act_selected = sorted(act_selected, key=lambda a: a['start'], reverse=False)
        # sorting array's result in start time
        print("Number of activities selected = " + str(len(act_selected)))
        print("Activities:" + (" ".join([str(x['index']) for x in act_selected])))
        print("")
        i = i + 1

# Citation
#https://www.programiz.com/python-programming/methods/list/append
#https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
#https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
#https://www.studytonight.com/data-structures/activity-selection-problem
