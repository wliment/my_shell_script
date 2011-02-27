#! /usr/bin/expect
set timeout 60
spawn /usr/bin/ssh -D 1988  -g u084632289@202.201.224.3
        expect {
		    "password:" {
			        send "wlimentwukong\r"
				 }
		 }
    interact {
	        timeout 60 { send " "}
		    }
