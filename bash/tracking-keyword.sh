#!/bin/bash
# Take two argument [1] Website Address [2] Keyword
# Mail configuration
function fappend {
   echo "$2">>$1;
}
YYYYMMDD=`date +%Y%m%d`

TOEMAIL="greg@31ten.network, theo@31ten.network";
SUBJECT="Missing keyword detected - $YYYYMMDD";
TMP=`mktemp`

rm -rf $TMP;
fappend $TMP "To: $TOEMAIL";
fappend $TMP "Subject: $SUBJECT";
fappend $TMP "";
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
  MSGBODY="Keyword ["$KEYWORD"] not found inside the page";
  fappend $TMP "$MSGBODY";
  cat $TMP|/usr/sbin/sendmail -t;
fi
rm $TMP
