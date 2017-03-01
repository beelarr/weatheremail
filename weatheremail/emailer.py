import requests
import smtplib


def get_emails():
    emails = {}

    try:
        email_file = open('/Users/bryonlarrance/weatheremail/weatheremail/inputs/emails.txt', 'r')
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():
    try:
        schedule_file = open('/Users/bryonlarrance/weatheremail/weatheremail/inputs/schedule.txt', 'r')
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

    forecast = 'The forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast

def send_emails(emails, schedule, forecast):
    server = smtplib.SMTP('smtp.gmail.com', '587')

    server.starttls()
    from_email = 'blarrance@gmail.com'
    password = input("What's your password?")
    server.login(from_email, password)

    #Sending to entire list
    for to_email, name in emails.items():
        message = 'Subject: Todays Forecast!\n'
        message += 'Hi ' + name + '!\n\n\n'
        message += forecast + '\n\n\n'
        message += schedule + '\n\n\n'
        message += 'Have a great day!' + '\n\n Bryon'
        server.sendmail(from_email, to_email, message)
    server.quit()



def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    forecast = get_weather_forecast()
    print(forecast)

    send_emails(emails, schedule, forecast)

main()
