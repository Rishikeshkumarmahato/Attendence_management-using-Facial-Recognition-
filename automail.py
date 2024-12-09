import yagmail
import os
import datetime
date=datetime.date.today().strftime("%B %d, %Y")
path='Attendance'
os.chdir(path)
files=sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest=files[-1]
filename=newest
sub="Attendance Report for " + str(date)
#mail information
yag=yagmail.SMTP (user = "SenderEmailAddress@domain.com", password="Password of that Account should be inserted here")
#sent the mail
yag.send(
    to="Receiver email adress",
    subject=sub, #email subject
    contents="None", #email body
    attachments=filename # file attached
)
print("Email Sent!")