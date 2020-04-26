import smtplib, ssl, getpass
#skippy was here
print("""Before using this program be aware you will have to make some changes
to your gmail which will make it less secure.

It is recommended not to use a personal email to send emails.

To allow this program to interact with gmail go to the following link
https://myaccount.google.com/lesssecureapps
and toggle on, if link doesnt work then look for it in the settings.

When asked for password no text will be desplayed as you enter to ensure
privecy when running this app.

please use responsibly. I, the creator, take as much responibility for missuse
of this program as microsoft do, which is none.

be carful of who you spam.""")


run=True
while run:
    email=input('[enter your email]')
    password = getpass.getpass(prompt='password:',stream=None)
    logged_in=True
    while logged_in:
            
        spam=False
        from_file=False

        receiver_email=input('[enter receving email]')
        spam_YN=input('[do you wish to spam the email? y/n]').lower()
        spam_YN=spam_YN+' '
        if spam_YN[0]=='y':
            
            spam=True
            spam_file_YN=input('[do you want to send lines from a txt file y/n]').lower()
            if spam_file_YN[0]=='y':
                spam_file=input('[enter txt file name]')
                spam_file=spam_file+'.txt'
                want_header=input('[do you want a header for these emails y/n]').lower()
                if want_header[0]=='y':
                    subject=input('[enter subject now]')
                else:
                    subject=' '
                from_file=True
            else:
                spam_num=input('[enter how many times email is to be sent]')
        if from_file==False:
                
            subject=input('[type subject]')
            message_inp=input('[enter the main message]')
            message = """\
Subject: """+subject+"""

"""+message_inp+"""."""


            print(message)
            
        try:

            port = 465  # For SSL
            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                

                server.login(email, password)
                    
                if spam:
                    
                    if from_file:
                        file=open(spam_file,'r')
                        for line in file:
                                
                                message = """\
Subject: """+subject+"""

"""+line+"""."""

                                                    
                                server.sendmail(email,receiver_email,message)
                    else:
                        spam_count=0
                        for x in range(0,int(spam_num)):
                            spam_count+=1
                            server.sendmail(email,receiver_email,message)
                            print(spam_count,'/',spam_num)
                else:
                    
                    server.sendmail(email, receiver_email, message)
        except:
            print('make sure you enter your email and password correctly')
        
        logout_YN=input('[do you want to log out y/n]').lower()
        if logout_YN[0]=='y':
            logged_in=False

            
    kill=input('[do you want to end the program y/n]').lower()
    if kill[0]=='y':
        run=False            





