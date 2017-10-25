#!/usr/bin/env python3
import sys
import json
import struct
import subprocess

speakConfigFile = open('./speak.cfg', 'r')
speakConfig = speakConfigFile.read()


# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode('utf-8')
    message = message.replace("'", "\\'")
    return json.loads(message)

while True:
    receivedMessage = getMessage()
    cmd=speakConfig.format(receivedMessage)
    subprocess.call( cmd, shell=True )
