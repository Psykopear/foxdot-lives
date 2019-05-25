#!/bin/bash

setup_jack () {
    # Get list of available devices
    internal=`jack_control dpd device | grep "ALC3266 Analog (duplex)" | cut -d\' -f 2`
    roland=`jack_control dpd device | grep "UA-22" | cut -d\' -f 2`
    # If roland is not here
    if [ -z "$roland" ]; then
        jack_control dps device $internal
    else
        jack_control dps device $roland
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
