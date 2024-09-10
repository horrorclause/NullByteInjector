#!/bin/env python3

'''
Null Byte Injection - Used to help obfuscate payloads/commands
'''

import sys
import base64

def injection(command):
    modifiedCommand = bytearray()
    for i in command:
        modifiedCommand.extend(i.encode('utf-8'))
        modifiedCommand.extend(b'\x00')
    return bytes(modifiedCommand)

def base64Encoding (encoded):
    return base64.b64encode(encoded).decode('utf-8')


if __name__ == "__main__":

    if len(sys.argv) >1:
        command = " ".join(sys.argv[1:])
        print(f"Command submitted: {command}")
        output = base64Encoding(injection(command))
        print(f"Modified Command: {output}")

    else:
        print('Script usage is "python3 nullbyte.py <command>"')
        
