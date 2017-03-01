import smtplib

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