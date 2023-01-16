#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree   = ET.parse('books.xml')
#returns the root element
root   = tree.getroot()

# root = ET.fromstring(your_xml_as_string)

print('The root tag is: ', root.tag)
print('The number of children is: ', len(root))
print('The root has the following children: ')
for child in root:
    print(child.tag, child.attrib)

