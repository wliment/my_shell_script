#! /usr/bin/expect
set timeout 60
spawn /usr/bin/ssh -D 1988  -g wliment@174.121.161.226
        expect {
		    "password:" {
			        send "gomesomapa\r"
				 }
		 }
    interact {
	        timeout 60 { send " "}
		    }
