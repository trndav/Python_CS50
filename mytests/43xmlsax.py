# https://www.youtube.com/watch?v=R2bhO0kZZnQ
# SAX and DOM libraries to read XML markup
# DOM for large files and read/edit, SAX for smaller and only read

import xml.sax

# handler = 
# parser = 

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("-----PERSON------")
            print("ID: {}".format(attrs['id']))

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content
    
    def endElement(self, name):
        if self.current == "name":
            print(f"Name is {self.name}")
        elif self.current == "age":
            print(f"Age is {self.age}")
        elif self.current == "weight":
            print(f"Weight is {self.weight}")
        elif self.current == "height":
            print(f"Height is {self.height}")
        self.current = ""


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("group.xml")