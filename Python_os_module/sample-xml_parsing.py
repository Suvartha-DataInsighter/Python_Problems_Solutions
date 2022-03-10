
import xml.etree.ElementTree as ET
 
# Passing the path of the xml document to parsing items
tree = ET.parse('sample.xml')
 
# getting the parent tag of the xml document
root = tree.getroot()
 
# printing the root (parent) tag of the xml document
print(root)
 
# printing the attributes of the tag from parent 
for item in root:
    print(item.attrib)


