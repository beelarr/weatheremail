import requests

def get_emails():
    emails = {}

    try:
        email_file = open('/Users/bryonlarrance/PycharmProjects/emailer/weather_emailer/emails.txt', 'r')
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    try:
        schedule_file = open('/Users/bryonlarrance/PycharmProjects/emailer/weather_emailer/schedule.txt', 'r')
        schedule = schedule_file.read()

    except FileNotFoundError as err:
        print(err)

    return schedule

def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Orlando&units=imperial&appid=b24b9adf867c14467552d2e7f7c37caa'
    weather_request = requests.get(url)
    weather_json = weather_request.json()



    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast


def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    get_weather_forecast()

main()
