# 邮件发送脚本

#### 使用说明：

sd_email.py 

```
usage: sd_email.py [-h] [-s SUBJECT] -t TO [--images IMAGES]
                   [--attachs ATTACHS] [--sender SENDER] [--content CONTENT]
                   [-f FILE] [--password PASSWORD] [--mailhost MAILHOST]

optional arguments:
  -h, --help            show this help message and exit
  -s SUBJECT, --subject SUBJECT
                        mail subject
  -t TO, --to TO        receiver
  --images IMAGES       sended images
  --attachs ATTACHS     attachments
  --sender SENDER       sender
  --content CONTENT     mail content. If 'content' string exist and the '-f'
                        will be ignored.
  -f FILE, --file FILE  content file
  --password PASSWORD   sender password
  --mailhost MAILHOST   sender mail host
```

-s 邮件的主题,可谓空，默认值为’无‘

-t  邮件的接收者，可写多个用逗号分隔，必要值

--images 在邮件中插入图片，这是一种可以显示的状态，非必要值

--attachs 需要发送的附件，可以发送多个用逗号分隔开，非必要值

--sender 发送人邮件地址，可修改脚本默认值

--password 发送人邮件地址

--mailhost 发件主机地址

--content 发件正文，注意如果该值设置了 "-f"  参数将被忽略

-f 包含发件正文的文件，里面可以根据你想要的格式编写邮件的内容

```shell
#example：
python3 sd_email.py -s "email content" -t someone1@qq.com,someone2@qq.com --image xx.png --attachs xx.tar.gz,xxx.png --sender xx@163.com --content "happy birthday"
python3 sd_email.py -s "email content" -t someone1@qq.com,someone2@qq.com --image xx.png --attachs xx.tar.gz,xxx.png --sender xx@163.com -f birthday.txt
```



#### 关于发件箱密码你需要知道的事情：

由于大多数邮箱对于第三方登录的邮件需要一个第三方授权码，因此你可以去相应的邮件官方网站中获取你的发件箱授权码，并了解您的发件主机。



#### 修改文件中默认的发件地址，发件密码，发件主机

这样在以后的发件中就可以无需在输入这些参数了。

发件地址变量名：sender

发件邮箱密码变量名： passWord

发件邮箱主机变量名： mail_host



#### 测试文件：

python3 sd_email.py -s push_test -t 36******@qq.com --images test/L171128-A1.cnv.png --attachs test/test.tar.gz -f test/file.txt

#### 缺点：

还不能实现抄送功能

