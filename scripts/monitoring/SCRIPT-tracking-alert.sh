#!/bin/bash
# tracking-alert.sh
# Check the tracking html code of a website (200, 300, 400, 500...)
# if the code > 400, it means there is a problem and send an email
# Take only one argument [1] Website address
# ./tracking-alert.sh http://google.com

# Check the html code from IP
SERVERNAME=$1
echo $SERVERNAME
response=$(curl --write-out %{http_code} --silent --output /dev/null $SERVERNAME)

# Mail configuration
function fappend {
   echo "$2">>$1;
}
YYYYMMDD=`date +%Y-%m-%d`

TOEMAIL="gregoire@31ten.network, theo@31ten.network, pvci.btoc@groupepvcp.com";
SUBJECT="BtoC China - Warning / Website is down - $YYYYMMDD";
FROM="warning@puweiproperty.com"
TMP=`mktemp`

rm -r $TMP;
fappend $TMP "From: $FROM";
fappend $TMP "To: $TOEMAIL";
fappend $TMP "Subject: $SUBJECT";
fappend $TMP "";
fappend $TMP "";
fappend $TMP "";

# Compare the response html code if code > 400
if [ "$response" \> "400" ]; then
  echo "error"
  MSGBODY="You received a message code "$response" on "$SERVERNAME"";
  fappend $TMP "$MSGBODY";
  cat $TMP|/usr/sbin/sendmail -t -F "warning@puweiproperty.com" -f "$FROM";
else
  echo "tracking alert success"
fi
rm $TMP
echo "response code: "$response
