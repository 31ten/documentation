#!/bin/bash
# daily-mail-checking
# take two arguments [1] file address [2] where to save the file
# Make sure to download mail.log and check an error occured
# Download the mail.log file to our server
scp $1 $2

# Get Month and Day
MONTHS=(MONTHS Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec)
CURRENTMONTH=$(date +%m)
CURRENTDAY=$(date +%d)

# Mail configuration
function fappend {
   echo "$2">>$1;
}
YYYYMMDD=`date +%Y%m%d`

TOEMAIL="greg@31ten.network, theo@31ten.network";
SUBJECT="Admin send error from mail.log - $YYYYMMDD";
MSGBODY="Something happened on your server, an email has not been sent";
TMP=`mktemp`

rm -rf $TMP;
fappend $TMP "To: $TOEMAIL";
fappend $TMP "Subject: $SUBJECT";
fappend $TMP "";
fappend $TMP "$MSGBODY";
fappend $TMP "";
fappend $TMP "";


#Read the file and check if there is an error
old_IFS=$IFS
IFS=$'\n'
for line in $(cat mail.log)
do
  if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(stat\=Sent)+ ]]; then
    echo "Send ok"
    #echo $line
  elif [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(stat\=)+ ]]; then
    #echo $line
    echo "Error Alert mail send"
    cat $TMP|/usr/sbin/sendmail -t;
    break
  fi
done
rm $TMP
IFS=$old_IFS
$(rm mail.log)
