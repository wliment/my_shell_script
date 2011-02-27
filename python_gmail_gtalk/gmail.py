#!/usr/bin/python
#coding:utf-8 
from email.mime.text import MIMEText
import smtplib 

class Gamil (object ):
    def __init__ (self ,account,password):
        """ 
        Gamil("wliment","xxxx") 
        """ 
        self.account="%s@gmail.com" % account
        self.password=password

    def send (self,to,title,content):
        """ 
        send('zsp007@gmail.com,zsp747@gmail.com") 
        """ 
        server = smtplib.SMTP('smtp.gmail.com' )
        server.docmd("EHLO server" )
        server.starttls()
        server.login(self.account,self.password)

        msg = MIMEText(content)
        msg['Content-Type' ]='text/plain; charset="utf-8"' 
        msg['Subject' ] = title
        msg['From' ] = self.account
        msg['To' ] = to
        server.sendmail(self.account, to ,msg.as_string())
        server.close()

if __name__=="__main__" :
    gmail=Gamil("wliment","ZHENGTAO5655327")
    gmail.send("wliment@gmail.com,wliment@gmail.com" ,"[video_status]你好,测试一下" ,"好好学习,天天向上" )
