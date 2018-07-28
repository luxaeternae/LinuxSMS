import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '{username}', '{your password}' )

##Define Service Providers

def company(raw_input):
    if raw_input == "verizon":
      return 'vtext.com'
    elif raw_input == "sprint":
      return 'messaging.sprintpcs.com'
    elif raw_input == "at&t":
      return 'txt.att.net'
    elif raw_input == "t-mobile":
      return 'tmomail.net'
    else:
      return "Provider invalid or unsupported. Contact app developer for assistance."
  
#Create a file to store Contacts

print "Welcome to LinuxChat v 1.1"

print "Send a Text"
print "Read my inbox"
print "Add a contact"
print "list my contacts"
choice = raw_input("Select one of the above by typing it here:").lower()


if choice == "send a text":
    number = raw_input("Phone Number/Contact:")
    provide = raw_input("Provider:").lower()
    text = raw_input("Message:")
    server.sendmail ( '%s@%s' % (number, company(provide)), '%s@%s' % (number, company(provide)), '%s' % (text))
    print "Your message was sent!"
    
elif choice == "read my inbox":
    import webbrowser
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                    
elif choice == "add a contact":
    print "Okay"
 
elif choice == "list my contacts":
    f = open('contacts.txt')
    lines = f.readlines()
