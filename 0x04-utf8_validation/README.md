# 0x04 UTF-8 Validation

1[](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/Encodings--Number-Systems_Watermarked.906d62e907dc.jpg)

## Resources

- [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](youtube.com/watch?v=MijmeoH9LT4)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 14.04 LTS` using `python3 (version 3.4.3)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

> Write a method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: def validUTF8(data)
- Return: True if data is a valid UTF-8 encoding, else return False
> A character in UTF-8 can be 1 to 4 bytes long
> The data set can contain multiple characters
> The data will be represented by a list of integers
> Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

```bash
sammy@ubuntu-trusty-64:~$ python3 utf_test.py
True
True
False
```
