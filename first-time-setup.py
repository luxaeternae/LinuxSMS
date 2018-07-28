print "Welcome to the first time setup of your linux SMS application."
print ""

var1 = str(raw_input("What is your linux username?"))
var2 = raw_input("What is your gmail email account? e.g xxx@gmail.com")
var3 = raw_input("What is your gmail password?")

print "Thank you."
print "This application will only work on Linux systems."
print "This is free experimental software. It will not harm your system, but is not guarenteed to work."
print "This application is only compatible with gmail email servers. Please make sure POP/IMAP is enabled. (Tutorial in README.md)"
print "Please have the gmail that you use for this be your default (inbox/0) inbox, or else inbox will not work and will redirect you to the wrong email."

f = open("setupvars.txt", "w")
f.write("pathuser = /home/%s/project/project-1A02-12094/contacts") % (var1)
f.write("emaill = %s") % (var2)
f.write("password = %s") %s (var3)
f.close()
