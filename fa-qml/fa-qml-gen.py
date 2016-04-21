#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import re
import httplib
import os


qml_file_name = "Loader.qml"
version = ""

### get font awesome cheatsheet from http://fontawesome.io/cheatsheet/
html_file_name = "cheatsheet.html"
http_client = None
html_file = open(html_file_name, "w")
try:
    http_client = httplib.HTTPConnection('fontawesome.io')
    http_client.request('GET', '/cheatsheet/')
    response = http_client.getresponse()
    if response.status != 200:
        print "ERROR: can not GET http://fontawesome.io/cheatsheet/ please check your connection..."
        exit()

    html_source = response.read()
    html_file.write(html_source)
    
except Exception, e:
    print e
    exit()
finally:
    if http_client:
        http_client.close()
    html_file.close()


### read html and parse icons table
infile = open(html_file_name, "r")
outfile = open(qml_file_name, "w")
dict = {}

# read
try:
    while True:
        inline = infile.readline()
        if not inline:
            print "EOF"
            break
        if 'page-header' in inline:
            pattern = re.compile(r'.*Every Font Awesome (.*) Icon.*')
            match = pattern.match(inline)
            if match:
                version = match.group(1)
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
                
except Exception, e:
    print e
    exit()
finally:
    infile.close()
    os.remove(html_file_name)

items = dict.items()
items.sort()

# write FontAwesome.qml
try:
    # modify this line if you are using other version of QtQuick
    outfile.write("import QtQuick 1.1\n\n")
    outfile.write("FontLoader {\n")
    # modify this line if you are using other version of Font Awesome
    outfile.write("    // Font Awesome {0}\n".format(version))
    
    for fa_name, fa_unicode in items:
        # for QtQuick 2.0, you can add a 'readonly' flag
        outline = "    property string {0}: \"\\u{1}\"\n".format(fa_name, fa_unicode)
        outfile.write(outline)
    
    outfile.write("}\n")
    
except Exception, e:
    print e
    exit()
finally:
    outfile.close()
    print "DONE"

exit()