#!/bin/bash
# form-mail-checking
# take two arguments [1] file address [2] where to save the file [3] Number form
# [3] 0 is contact-us, 1 is recall
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
YYYYMMDD=`date +%Y-%m-%d`

TOEMAIL="greg@31ten.network, theo@31ten.network, pvci.btoc@groupepvcp.com";
SUBJECT="BtoC China - Warning / A form did not work - $YYYYMMDD";
FROM="warning@puweiproperty.com"
MSGBODY="Test filling form at http://www.puwei-property.com/contact-us failed";
TMP=`mktemp`

rm -r $TMP;
fappend $TMP "From:" $FROM;
fappend $TMP "To: $TOEMAIL";
fappend $TMP "Subject: $SUBJECT";
fappend $TMP "$MSGBODY";
fappend $TMP "";
fappend $TMP "";

#Read the file and check if there is an error
old_IFS=$IFS
IFS=$'\n'
for line in $(cat mail.log)
do
  if [ "$3" -eq "0" ]; then
    if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(to\=gregoire@31ten.network,31ten.test@gmail.com)+(.)*(stat\=)+ ]]; then
      if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(to\=gregoire@31ten.network,31ten.test@gmail.com)+(.)*(stat\=Sent)+ ]]; then
          echo "Send ok"
          echo $line
      else
          cat $TMP|/usr/sbin/sendmail -t -F "warning@puweiproperty.com" -f "$FROM";
          break
      fi
    fi
  elif [ "$3" -eq "1" ]; then
    if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(to\=gregoire@31ten.network,31ten.test+recall@gmail.com)+(.)*(stat\=)+ ]]; then
      if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(to\=gregoire@31ten.network,31ten.test+recall@gmail.com)+(.)*(stat\=Sent)+ ]]; then
          echo "Send ok"
          echo $line
      else
          cat $TMP|/usr/sbin/sendmail -t -F "warning@puweiproperty.com" -f "$FROM";
          break
      fi
    fi
  elif [ "$3" -eq "2"]; then
    if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(to\=gregoire@31ten.network,31ten.test+contact@gmail.com)+(.)*(stat\=)+ ]]; then
      if [[ $line =~ (${MONTHS[$CURRENTMONTH]} $CURRENTDAY)+(.)*(to\=gregoire@31ten.network,31ten.test+contact@gmail.com)+(.)*(stat\=Sent)+ ]]; then
          echo "Send ok"
          echo $line
      else
          cat $TMP|/usr/sbin/sendmail -t -F "warning@puweiproperty.com" -f "$FROM";
          break
      fi
    fi
  fi
done
rm $TMP
IFS=$old_IFS
$(rm mail.log)
