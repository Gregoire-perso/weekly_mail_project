"""
@author: Grégoire Lefaure
@date: 2020-07-09 21:42
"""
#Global import
#Imports for email
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Import for database
import mysql.connector as db

#Local import
import creating_mail

def email_creation(recipient):
	#Email creation
	message = MIMEMultipart();
	message['From'] = "L'hebdo numérique";
	message['Subject'] = "L'hebdo numérique du {0}".format("09 07 2020");
	message['To'] = str(recipient);
	#msg = creating_mail.create_mail();
	msg = "coucou";
	message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'));
	text = message.as_string();

	return text

#Connection to MySQL database
conn = db.connect(host="localhost", user="weekly_mail", password="Mgfa23a.", database="weekly_mail");
cursor = conn.cursor();
cursor.execute("""SELECT email FROM Users""");
users_email = cursor.fetchall();

#Connection to the email
server = smtplib.SMTP('smtp.gmail.com', 587);
server.starttls();
server.login("lhebdonumerique@gmail.com", "vutmxzndseroyrpy");

for i in users_email:
	server.sendmail("lhebdonumerique@gmail.com", i, email_creation(i));

#Close connections
conn.close(); #Close database connection
server.quit(); #Close email connection
