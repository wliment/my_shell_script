#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xmpp

login = 'wliment.bak@gmail.com' #发送者的gmail帐号     ***** @gmail.com
pwd      = 'ZHENGTAO5655327' #密码
target = 'wliment@gmail.com' #接收者的帐号

cl = xmpp.Client('gmail.com',debug=[])
cl.connect( server=('talk.google.com',5222) )
cl.auth(login,pwd, 'Script')
cl.sendInitPresence()
cl.send( xmpp.Message( target ,"Hello World as xmpp" ) )

cl.disconnect()

