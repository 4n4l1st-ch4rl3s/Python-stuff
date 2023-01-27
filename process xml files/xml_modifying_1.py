import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag,':', sub_child.text)

#remove unneccessary prints
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    # print('\n')
    print(child.tag, child.attrib)
        
    for sub_child in child:   
        print(sub_child.tag,':', sub_child.text)