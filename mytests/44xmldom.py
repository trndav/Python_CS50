# https://www.youtube.com/watch?v=R2bhO0kZZnQ
# SAX and DOM libraries to read XML markup
# DOM for large files and read/edit, SAX for smaller and only read

import xml.dom.minidom

domtree = xml.dom.minidom.parse('group.xml')
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print("----PERSON---")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))

    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

# change values and save in xml file
# persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
# persons[0].setAttribute('id', '100')
# persons[1].getElementsByTagName('age')[0].childNodes[0].nodeValue = "13"
# domtree.writexml(open('group2.xml', 'w'))

# Add new elements to XML file
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')
name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Jack Star'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('22'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('77'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('185'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)
domtree.writexml(open('group.xml', 'w'))