#!/bin/sh

if [ "x-x" = x"$1" ]; then
    EXIT="; exit"; shift;
fi

DIR="$( cd "$( dirname "$0" )" && pwd )"
COMMAND="java -jar $DIR/selenium-server-standalone-2.13.0.jar"
echo "$COMMAND $EXIT"

osascript 2>/dev/null <<EOF
    tell application "Terminal"
        activate
        do script with command "$COMMAND $EXIT"
    end tell
EOF









