# Null Byte Injector


This is a simple script that will iterate through your command and inject a nullbyte behind every character and then base64 encoding the command, hoping it helps with command obfuscation.

## Usage

```cmd
python3 nullByte.py {Your Command Here}
```

![Example Command Submitted](image.png)

You can decode the Base64 with [CyberChef](https://gchq.github.io/CyberChef/) and see the null bytes:

![Decoded](image-1.png)