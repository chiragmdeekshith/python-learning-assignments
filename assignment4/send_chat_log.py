import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymysql


def send_mail(chat_log, to):
    print("Send mail function called")
    from_address = "email@gmail.com"
    to_addresses = to

    to_addresses_string = ""
    for address in to_addresses:
        if to_addresses_string == "":
            to_addresses_string = address
        else:
            to_addresses_string = to_addresses_string + "," + address

    message = MIMEMultipart()
    message["From"] = from_address
    message["To"] = to_addresses_string
    message["Subject"] = "CHAT_LOG"

    message_body = "Hello. Please find the chat log below.\n\n" + chat_log + "\n\n End of log. Don't reply to this."
    message.attach(MIMEText(message_body, "plain"))

    smtp_session = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_session.starttls()
    smtp_session.login(from_address, "pass")
    smtp_session.sendmail(from_address, to_addresses, message.as_string())
    smtp_session.quit()


def get_log_from_database():
    database = pymysql.connect("localhost", "root", "toor", "python")
    cursor = database.cursor()
    query = "SELECT * FROM chat_log"
    cursor.execute(query)
    results = cursor.fetchall()

    chat_log = ""
    emails = []

    for row in results:
        time = row[0]
        email = row[1]
        message = row[2]

        chat = time + " -- " + email + " : " + message
        chat_log = chat_log + chat + "\n"
        emails.append(email)

    database.close()
    return chat_log, emails


def main():
    chat_log, to = get_log_from_database()
    send_mail(chat_log, to)


main()
