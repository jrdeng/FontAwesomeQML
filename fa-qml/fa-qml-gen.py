#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import re

if len(sys.argv) != 2:
    print "Usage:", sys.argv[0], "fa-cheatsheet.html"
    exit()

infile = open(sys.argv[1], "r")
outfile = open("Loader.qml", "w")
dict = {}

# read
try:
    while True:
        inline = infile.readline()
        if not inline:
            print "EOF"
            break
        if 'fa fa-fw' in inline:
            # get unicode of fa icon
            pattern = re.compile(r'.*<i class="fa fa-fw".*>&#x(.*)</i>$')
            match = pattern.match(inline)
            if match:
                fa_unicode = match.group(1)
                # fa name is in next line
                inline = infile.readline()
                fa_name = inline.strip().replace("-", "_")

                # save in dict
                dict[fa_name] = fa_unicode
finally:
    infile.close()

items = dict.items()
items.sort()

# write FontAwesome.qml
try:
    # modify this line if you are using other version of QtQuick
    outfile.write("import QtQuick 1.1\n\n")
    outfile.write("FontLoader {\n")
    # modify this line if you are using other version of Font Awesome
    outfile.write("    // Font Awesome 4.6.1\n")
    
    for fa_name, fa_unicode in items:
        # for QtQuick 2.0, you can add a 'readonly' flag
        outline = "    property string {0}: \"\\u{1}\"\n".format(fa_name, fa_unicode)
        outfile.write(outline)
    
    outfile.write("}\n")
finally:
    outfile.close()
    print "DONE"

exit()