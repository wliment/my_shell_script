#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
import gtk
import urllib
import urllib2
from sgmllib import SGMLParser

class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.is_it = False
        self.answer = []
    
    def start_div(self,attrs):
        id = [v for k,v in attrs if k=='id']
        if 'result_box' in id:
            self.is_it = True
    
    def end_div(self):
        self.is_it = False
    
    def handle_data(self,text):
        if self.is_it:
            self.answer.append(text)

class GT():
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def getText(self, widget):
        buf = widget.get_buffer()
        b,e = buf.get_bounds()
        return buf.get_text(b,e)

    def setText(self, widget, text=''):
        buf = widget.get_buffer()
        buf.set_text(text)
        widget.set_buffer(buf)
            
    def transIt_from_zh_to_en(self, widget, data=None):
        url = 'http://translate.google.cn/translate_t'
        lan_in = 'zh-CN'
        lan_out = 'en'

        be_trans_text = self.getText(self.textview_out)

        values = {'hl':'zh-CN','ie':'UTF-8','text':be_trans_text, \
                'langpair':"%s|%s" % (lan_in, lan_out)}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        req.add_header('User-Agent', "Mozilla/4.0 (compatible; MSIE 6.0; \
                Windows NT 5.1;SV1; .NET CLR 2.0.50727)")
        response = urllib2.urlopen(req)
        return_html = response.read() #-----------------
        response.close() 
        
        uu = URLLister()
        uu.feed(return_html)
        u2 = uu.answer[0]
        self.setText(self.textview_in, u2)
        del uu

    def transIt_from_en_to_zh(self, widget, data=None):
        url = 'http://translate.google.cn/translate_t'
        lan_in = 'en'
        lan_out = 'zh-CN'
        be_trans_text = self.getText(self.textview_out)

        values = {'hl':'zh-CN','ie':'UTF-8','text':be_trans_text,\
                'langpair':"%s|%s" % (lan_in, lan_out)}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        req.add_header('User-Agent', "Mozilla/5.0 (Windows; U; \
                Windows NT 5.0; zh-CN; rv:1.7.5) \
                Gecko/20041224 Firefox/1.0")
        response = urllib2.urlopen(req)
        return_html = response.read()
        response.close()
        
        uuu = URLLister()
        uuu.feed(return_html)
        uu2 = uuu.answer[0]
        self.setText(self.textview_in, uu2)

    def __init__(self):
        # window ---------------------------------------
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_default_size(300, 200)
        self.window.set_border_width(5)
        # VBox ----------------------------------------
        self.vbox = gtk.VBox(False, 2)
        self.window.add(self.vbox)
        # 3 Hbox---------------------------------------
        self.hbox1 = gtk.HBox(False, 2)
        self.vbox.pack_start(self.hbox1, True, True, 2)

        self.hbox2 = gtk.HBox(False, 2)
        self.vbox.pack_start(self.hbox2, True, True, 2)

        self.hbox3 = gtk.HBox(False, 2)     
        self.vbox.pack_start(self.hbox3, True, True, 2)
        # 2 Button -----------------------------------------------
        self.button_zh2en = gtk.Button("中译英")
        self.button_zh2en.connect("clicked", self.transIt_from_zh_to_en)
        self.hbox3.pack_start(self.button_zh2en, True, True, 0)
        self.button_en2zh = gtk.Button("英译中")
        self.button_en2zh.connect("clicked", self.transIt_from_en_to_zh)
        self.hbox3.pack_start(self.button_en2zh, True, True, 0)
        
        self.label_out = gtk.Label("原文：")
        self.hbox1.pack_start(self.label_out, True, True, 0)
        
        self.label_in = gtk.Label("译文：")
        self.hbox2.pack_start(self.label_in, True, True, 0)
        
        self.textview_out = gtk.TextView(buffer=None)
        self.textview_out.set_wrap_mode(1)#自动换行
        self.textview_out.set_size_request(250, 50)
        self.hbox1.pack_start(self.textview_out, True, True, 0)
        
        self.textview_in = gtk.TextView(buffer=None)
        self.textview_in.set_wrap_mode(1)#自动换行
        self.textview_in.set_size_request(250, 50)
        self.hbox2.pack_start(self.textview_in, True, True, 0)

        self.textview_in.show()
        self.textview_out.show()
        self.label_in.show()
        self.label_out.show()
        self.button_zh2en.show()
        self.button_en2zh.show()
        self.hbox1.show()
        self.hbox2.show()
        self.hbox3.show()
        self.vbox.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == '__main__':
    gt = GT()
    gt.main()
 
