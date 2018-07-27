import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '{username}', '{your password}' )

def company(raw_input):
    if raw_input == "Verizon":
      return 'vtext.com'
    elif raw_input == "Sprint":
      return 'messaging.sprintpcs.com'
    elif raw_input == "AT&T":
      return 'txt.att.net'
    elif raw_input == "T-mobile":
      return 'tmomail.net'
    else:
      return "Provider invalid or unsupported. Contact app developer for assistance."

print "Welcome to LinuxChat v 1.1"

number = raw_input("Phone Number/Contact:")
provide = raw_input("Provider:")
text = raw_input("Message:")

server.sendmail ( '%s@%s' % (number, company(provide)), '%s@%s' % (number, company(provide)), '%s' % (text))

print "Your message was sent!"'
