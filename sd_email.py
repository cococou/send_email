#!/usr/bin/env python3
import smtplib 
from email import encoders 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email.mime.image import MIMEImage
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
import argparse

sender = '你的发件箱地址'
passWord = '你的发件箱密码'
mail_host = '发件主机'

def get_par():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--subject",help="mail subject",default="无")
    parser.add_argument("-t","--to",help="receiver",required=True)
    parser.add_argument("--images",help="sended images",default=None)
    parser.add_argument("--attachs",help="attachments",default=None)
    parser.add_argument("--sender",help="sender",default=sender)
    #parser.add_argument("-c","--copy",help="copy to",default=None)
    parser.add_argument("--content",help="mail content. If 'content' string exist and the '-f' will be ignored.",default=None)
    parser.add_argument("-f",'--file',help="content file",dest='FILE')
    parser.add_argument("--password",help="sender password",default=passWord)
    parser.add_argument("--mailhost",help="sender mail host",default=mail_host)
    args = parser.parse_args()
    #print(args)
    return args

def parse_send_header():
    from email.parser import Parser
    headers = Parser().parsestr('From: <user@example.com>\n'
        'To: <someone_else@example.com>\n'
        'Subject: Test message\n'
        '\n'
        'Body would go here\n')
    print('To: %s' % headers['to'])
    print('From: %s' % headers['from'])
    print('Subject: %s' % headers['subject'])

def pic_fuc(image):
    with open(image,'rb') as fp:
        img = fp.read()
    return img

def get_content(par):
    msg_content = par.content
    if not msg_content:
        f = open(par.FILE,'rb')
        msg_content = f.read()
        f.close()
    return msg_content

def main():
    par = get_par()
    msg = MIMEMultipart()
    msg['Subject'] = par.subject
    msg['From'] = par.sender
    msg['To'] = par.to
    #if par.copy:
    #    msg['Cc'] = par.copy
    
    #add content
    msg_content = get_content(par)
    msg.attach(MIMEText(msg_content,'plain','utf-8'))

    #add picture
    if par.images:
        images = par.images.split(',')
        for image in images:
            img = pic_fuc(image)
            msg.attach(MIMEImage(img))

    #add attachment
    if par.attachs:
        attachs = par.attachs.split(',')
        for attach in attachs:
            att = MIMEText(open(attach,'rb').read(),'base64','utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="{f}"'.format(f=attach)
            msg.attach(att)

    #send email
    receviers = par.to.split(',')
    for recevier in receviers:
        try:    
            #QQsmtp服务器的端口号为465或587    
            s = smtplib.SMTP_SSL(par.mailhost, 465)   
            s.set_debuglevel(1)    
            s.login(par.sender,par.password)
            #给receivers列表中的联系人逐个发送邮件    
            s.sendmail(par.sender,recevier,msg.as_string())
            print ("All emails have been sent over!")
        except smtplib.SMTPException as e:    
            print ("Falied,%s",e)

if __name__ == "__main__":
    main()
