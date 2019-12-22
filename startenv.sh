#!/bin/bash

setup_jack () {
    # Get list of available devices
    # internal=`jack_control dpd device | grep "ALC3266 Analog (duplex)" | cut -d\' -f 2`
    roland=`cat /proc/asound/cards | grep "UA22"`
    # If roland is not here
    if [ -z "$roland" ]; then
        echo "Setting internal soundcard"
        jack_control dps device hw:PCH,0
    else
        echo "Setting Roland soundcard"
        jack_control dps device  hw:UA22,0
    fi
}

# Status
status=`jack_control status | tail -1`

if [ $status == 'stopped' ]
then
    setup_jack
    jack_control start
elif [ $status == 'started' ]
then
    jack_control stop
    setup_jack
    jack_control start
fi

echo "FoxDot.start;" > start.sc
sclang start.sc
rm start.sc
