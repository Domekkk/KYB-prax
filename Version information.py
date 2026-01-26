#!/bin/python

#with open("example.cimg","wb") as file:
#       file.write(b"((m6E"\x23)
        
with open ("example.cimg","wb") as file:
        header_magic=b"(m6E"
        version=(225).to_bytes(1, "little")
        file.write(header_magic+version)
