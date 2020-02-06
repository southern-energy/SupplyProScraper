#!/bin/sh
FILE=$1
UNIQUE='-={GR}=-'
#
if [ -z "$FILE" ]; then
        exit;
fi;
#
for LINE in `sed "s/ /$UNIQUE/g" $FILE`; do
        LINE=`echo $LINE | sed "s/$UNIQUE/ /g"`;
        echo $LINE;
done;