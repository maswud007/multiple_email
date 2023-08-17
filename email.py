import smtplib as sb

object = sb.SMTP('smtp.gmail.com',587)
object.ehlo()
object.starttls()
object.login('abdullahalmaswudewu@gmail.com','pass')
subject = "Testing python to send multiple email"
body = "I love you tuptup"
message = "subject:{}\n\n{}".format(subject,body)
sending_address = ["farzana51-008@diu.edu.bd"]
object.sendmail('abdullahalmaswudewu@gmail.com',sending_address,message)
print("email sent successfully.")
object.quit()
