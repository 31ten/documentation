#!/bin/bash
# daily-mail-checking
# Check in the mail.log from [****] server if each email has been sent correctly
# Otherwise send an email.
# take two arguments [1] file address [2] where to save the file
# ./daily-mail-checking user@ip-address:/where/the/file/is .


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
# Get Current date (Year, month, day)
YYYYMMDD=`date +%Y-%m-%d`

# Setup email contents
TOEMAIL="gregoire@31ten.network, theo@31ten.network, pvci.btoc@groupepvcp.com";
SUBJECT="BtoC China - Warning / CSV bridge was not sent - $YYYYMMDD";
FROM="warning@puweiproperty.com"
MSGBODY="Something happened on your server, an email has not been sent";
TMP=`mktemp`

rm -r $TMP;
fappend $TMP "From:" $FROM;
fappend $TMP "To: $TOEMAIL";
fappend $TMP "Subject: $SUBJECT";
fappend $TMP "";
fappend $TMP "";
fappend $TMP "";

#Read the file and check if there is an error
old_IFS=$IFS # IFS stands for "internal field separator". It is used by the shell to determine how to do word splitting. how to recognize word boundaries.
IFS=$'\n'

# get each line from the mail.log file
for line in $(cat mail.log)
do
  if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(stat\=Sent)+ ]]; then
    echo "Send ok"
    #echo $line
  elif [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(stat\=)+ ]]; then
    #echo $line
    echo "Error Alert mail send"
    fappend $TMP "$MSGBODY";
    cat $TMP|/usr/sbin/sendmail -t -F "warning@puweiproperty.com" -f "$FROM";
    break
  fi
done
rm $TMP
IFS=$old_IFS
$(rm mail.log)
