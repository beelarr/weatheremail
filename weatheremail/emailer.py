import weather
import sender
import get_emails
import get_schedule


def main():
    emails = get_emails.get_emails()
    schedule = get_schedule.get_schedule()
    forecast = weather.get_weather_forecast()
    sender.send_emails(emails, schedule, forecast)

main()
