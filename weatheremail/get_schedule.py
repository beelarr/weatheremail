def get_schedule():
    try:
        schedule_file = open('/Users/bryonlarrance/weatheremail/weatheremail/inputs/schedule.txt', 'r')
        schedule = schedule_file.read()

    except FileNotFoundError as err:
        print(err)

    return schedule