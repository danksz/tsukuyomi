To view kaitai struct data:

$ cd sd-parser/kaitai-struct
$ ksv Lunii.img lunii-global.ksy

To use the python parser you need to convert the kaitai struct into python 
library first:

$ cd sd-parser
$ kaitai-struct-compiler --target python kaitai-struct/lunii-global.ksy

And then execute the script:
$ ./sd-lunii-parser.py Lunii.img
