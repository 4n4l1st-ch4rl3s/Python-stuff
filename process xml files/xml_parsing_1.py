#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree   = ET.parse('books.xml')
#returns the root element
root   = tree.getroot()

# root = ET.fromstring(your_xml_as_string)

#Show the root element
print('The root tag is: ', root.tag)
#Show the number of elements in the root
print('The number of children is: ', len(root))
print('The root has the following children: ')
#Ireterates between the children of the root and shows their contents
for child in root:
    #prints out the child and its attributes
    print(child.tag, child.attrib)

print('\n')
print('\n')

print('My books: \n')
#iterates over the elements of the root and and stores it the the variable books
for book in root:
    print(book.attrib, '\n')# dispalys the attributes
    print('Title: ', book.attrib['title'])
    print('Author: ', book[0].text)
    print('Year: ', book[1].text, '\n')

# Display the author only
for author in root.iter('author'):
    print(author.text)
    print('\n')

#get book titles using findall
for book in root.findall('book'):
    print(book.get('title'))
    print('\n')

#Using find only returns one line
print(root.find('book').get('title'))

