import schedule
import time

from send_email import send_email


def job():
    print("Sending Email...")
    send_email()


schedule.every().day.at("10:00").do(job)

print("Scheduler Started...")


while True:
    schedule.run_pending()
    time.sleep(1)
