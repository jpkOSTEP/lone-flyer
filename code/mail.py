import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

#only gmail account will work
fromEmail = 'sendermail@gmail.com (sender mail)'


fromEmailPassword = 'email_password'


toEmail = 'receivermail@gmail.com (receiver email)'

def sendEmail(image):
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Security Update'
	msgRoot['From'] = fromEmail
	msgRoot['To'] = toEmail
	msgRoot.preamble = 'Raspberry pi security camera update'

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('Smart security cam found object')
	msgAlternative.attach(msgText)

	msgText = MIMEText('<img src="cid:image1">', 'html')
	msgAlternative.attach(msgText)

	msgImage = MIMEImage(image)
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()
	smtp.login(fromEmail, fromEmailPassword)
	smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
	smtp.quit()
