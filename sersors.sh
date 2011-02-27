a=`sensors -u | grep input | sed 's/temp1_input: //'`
b=1
cd /home/wliment/桌面/
 c=`ls | grep tem`

if [ -f $c ]
then
	rm $c
	touch $a.tem
else
	touch $a.tem
fi
while [ $b -eq 1 ]
do
	sleep 5 
	c=`ls | grep tem`
	rm $c
	a=`sensors -u | grep input | sed 's/temp1_input: //'`
	touch $a.tem
done
