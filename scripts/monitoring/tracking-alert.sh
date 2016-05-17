#!/bin/bash
# Get the tracking html code of a website (200, 300, 400, 500...)
# Take only one argument [1] Website address
# Check the html code from IP
SERVERNAME=$1
echo $SERVERNAME
response=$(curl --write-out %{http_code} --silent --output /dev/null $SERVERNAME)

# Mail configuration
function fappend {
   echo "$2">>$1;
}
YYYYMMDD=`date +%Y%m%d`

TOEMAIL="greg@31ten.network, theo@31ten.network";
TMP=`mktemp`

rm -rf $TMP;
fappend $TMP "To: $TOEMAIL";
fappend $TMP "Subject: $SUBJECT";
fappend $TMP "";
fappend $TMP "";
fappend $TMP "";

# Compare the response html code
if [ "$response" \> "400" ]; then
  echo "error"
  SUBJECT="[Error "$response"] - $YYYYMMDD"
  MSGBODY="You received a message code "$response" on your server";
  fappend $TMP "Subject: $SUBJECT";
  fappend $TMP "$MSGBODY";
else
  echo "tracking alert success"
fi
rm $TMP
echo "response code: "$response
