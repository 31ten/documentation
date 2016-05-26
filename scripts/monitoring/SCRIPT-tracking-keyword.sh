#!/bin/bash
# tracking-keyword.sh
# Download the page's contents and check if the keywords exist
# Otherwise send an email.
# Take two argument [1] Website Address [2] Keyword
# ./tracking-keyword http://google.com google

# Mail configuration
function fappend {
   echo "$2">>$1;
}
YYYYMMDD=`date +%Y-%m-%d`

#TOEMAIL="gregoire@31ten.network, theo@31ten.network";
TOEMAIL="sofiane@31ten.network"
SUBJECT="BtoC China - Warning / Website is down - $YYYYMMDD";
FROM="warning@puweiproperty.com"
TMP=`mktemp`

rm -r $TMP;
fappend $TMP "From: $FROM";
fappend $TMP "To: $TOEMAIL";
fappend $TMP "Subject: $SUBJECT";
fappend $TMP "";
fappend $TMP "$MSGBODY";
fappend $TMP "";
fappend $TMP "";

# Get website address and keyword to check
WEBSITE=$1
KEYWORD=$2
toggle=0

# Check if word exist after getting page's contents
content=$(wget $WEBSITE -q -O -)
for word in $content; do
  if [[ $word =~ $KEYWORD ]]; then
    toggle=1
    break
  fi
done
if [ "$toggle" -ne "1" ]; then
  MSGBODY="Keyword ["$KEYWORD"]"$content" not found inside the page";
  fappend $TMP "$MSGBODY";
  cat $TMP|/usr/sbin/sendmail -t -F "warning@puweiproperty.com" -f "$FROM";
fi
rm $TMP
