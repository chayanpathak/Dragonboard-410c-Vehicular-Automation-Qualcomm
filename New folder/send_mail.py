def send_mail():
    import smtplib
    fromaddr = 'suhascholleti4@gmail.com'
    toaddrs  = 'chayanpathak2011@gmail.com'
    msg = "\r\n".join([
        "From: suhascholleti4@gmail.com",
        "To: chayanpathak2011@gmail.com",
        "Subject: Emergency car crash infomation",
        "",
        "My name is john doe. My car has crashed, my blood group is A+.\nEmergency Contact Name:xyz.\nPhone number:9552438038.\nHouse Location:No. 658, 1st main road,Washington."
    ])
    username = 'suhascholleti4@gmail.com'
    password = '12345678qwerty'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

send_mail()

