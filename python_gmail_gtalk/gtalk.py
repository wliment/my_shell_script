#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xmpp

login = 'wliment.bak@gmail.com' #�����ߵ�gmail�ʺ�     ***** @gmail.com
pwd      = 'ZHENGTAO5655327' #����
target = 'wliment@gmail.com' #�����ߵ��ʺ�

cl = xmpp.Client('gmail.com',debug=[])
cl.connect( server=('talk.google.com',5222) )
cl.auth(login,pwd, 'Script')
cl.sendInitPresence()
cl.send( xmpp.Message( target ,"Hello World as xmpp" ) )

cl.disconnect()

