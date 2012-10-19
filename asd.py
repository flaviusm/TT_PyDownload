'''
Created on Sep 9, 2012

@author: UndergroundJesus
'''
import Tkinter
from Tkinter import *
master = Tk()
import urllib2
import os
url="http://rd.software.yahoo.com/msgr/11/msgr11us.exe"
url2="ftp://ftp.mozilla.org/pub/mozilla.org/firefox/releases/6.0/win32/en-US/Firefox%20Setup%206.0.exe"
url3="http://download.nullsoft.com/winamp/client/winamp563_full_emusic-7plus_all.exe"
url4="http://downloads.malavida.net/en/file-3d2c01966f495a63c77a89280b3dd43c-qpDv38iQ6c7iz9Tw4Kbgxs_T293PxqfS8dg/vlc-windows-malavida.exe"
url5="http://downloads.malavida.net/en/file-0fdf527e1836c74c71c5ad3294fcf886-qpDs3t7T15Lr1NPd3PDmktDT0dXhzt3Op9jdyA/skype-windows-malavida.exe"
def var_states():
    print("Yahoo Messenger: %d,\nMozilla Firefox: %d, \nWinamp, \nVLC Media Player, \nSkype" % (var1.get(), var2.get(), var3.get(), var4.get(), var5.get()))
    
 
def downinstall():
    if var1.get()==1:
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
        
    if var2.get()==1:
        file_name = url2.split('/')[-1]
        u = urllib2.urlopen(url2)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
        
    if var3.get()==1:
        file_name = url3.split('/')[-1]
        u = urllib2.urlopen(url3)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
        
    if var4.get()==1:
        file_name = url4.split('/')[-1]
        u = urllib2.urlopen(url4)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
    
    if var5.get()==1:
        file_name = url5.split('/')[-1]
        u = urllib2.urlopen(url5)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
     
Label(master, text="Your programs:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Yahoo Messenger", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Mozilla Firefox", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Winamp", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="VLC Medya Player", variable=var4).grid(row=4, sticky=W)
var5 = IntVar()
Checkbutton(master, text="Skype", variable=var5).grid(row=5, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=6, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=7, sticky=W, pady=4)
Button(master, text='Download', command=downinstall).grid(row=8, sticky=W, pady=4)
mainloop()