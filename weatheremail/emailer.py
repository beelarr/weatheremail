import weather
import sender
import get_emails
import get_schedule


def main():
    emails = get_emails.get_emails()
    print(emails)

    schedule = get_schedule.get_schedule()
    print(schedule)

    forecast = weather.get_weather_forecast()
    print(forecast)

    sender.send_emails(emails, schedule, forecast)

main()
