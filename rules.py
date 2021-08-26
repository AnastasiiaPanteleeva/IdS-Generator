# -*- coding: utf-8 -*-

def value_restriction (value):
    
    
    if "enumeration" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_list.remove("enumeration")
        value_ids = ['''				<value>''',
                     '''					<xs:restriction base="xs:string">''']
        for v in value_list:
            value_ids.append('''						<xs:enumeration value="{}"/>'''.format(v))
        value_ids.append('''					</xs:restriction>''')
        value_ids.append('''				</value>''')
        value_str = "\n".join(value_ids)

    
    elif "pattern" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_list.remove("pattern")
        value_ids = ['''				<value>''',
                     '''					<xs:restriction base="xs:string">''']
        
        if "[" in value:
            value_ids.append('''						<xs:pattern value="{}"/>'''.format(" ".join(value_list)))
            
        else:
            value_list_new = []
            for i in value_list:
                value_list_new.append(i + ".*")
            value_ids.append('''						<xs:pattern value="^({})"/>'''.format("|".join(value_list_new)))
       
        
       
        value_ids.append('''					</xs:restriction>''')
        value_ids.append('''				</value>''')
        value_str = "\n".join(value_ids)
        
    
    elif "min" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_ids = ['''				<value>''',
                     '''					<xs:restriction base="xs:integer">''']
        if "min" in value_list:
            value_ids.append('''						<xs:minInclusive value="{}"/>'''.format(value_list[value_list.index("min")+1]))
        if "max" in value_list:
            value_ids.append('''						<xs:maxInclusive value="{}"/>'''.format(value_list[value_list.index("max")+1]))
        value_ids.append('''					</xs:restriction>''')
        value_ids.append('''				</value>''')
        value_str = "\n".join(value_ids)
    
    
    elif "length" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_list.remove("length")
        value_ids = ['''				<value>''',
                     '''					<xs:restriction base="xs:string">''']
        value_ids.append('''						<xs:length value="{}"/>'''.format(" ".join(value_list)))
        value_ids.append('''					</xs:restriction>''')
        value_ids.append('''				</value>''')
        value_str = "\n".join(value_ids)
        
        
    else:
        value_ids = ['''				<value>''']
        value_ids.append('''					<simpleValue>{}</simpleValue>'''.format(value))
        value_ids.append('''				</value>''')
        value_str = "\n".join(value_ids)
        
        
    return value_str


def restriction (value):
    
    
    if "enumeration" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_list.remove("enumeration")
        value_ids = ['''					<xs:restriction base="xs:string">''']
        for v in value_list:
            value_ids.append('''						<xs:enumeration value="{}"/>'''.format(v))
        value_ids.append('''					</xs:restriction>''')
        value_str = "\n".join(value_ids)

    
    elif "pattern" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_list.remove("pattern")
        value_ids = ['''					<xs:restriction base="xs:string">''']
        
        if "[" in value:
            value_ids.append('''						<xs:pattern value="{}"/>'''.format(" ".join(value_list)))
            
        else:
            value_list_new = []
            for i in value_list:
                value_list_new.append(i + ".*")
            value_ids.append('''						<xs:pattern value="^({})"/>'''.format("|".join(value_list_new)))
       
        
       
        value_ids.append('''					</xs:restriction>''')
        value_str = "\n".join(value_ids)
        
    
    elif "min" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_ids = ['''					<xs:restriction base="xs:integer">''']
        if "min" in value_list:
            value_ids.append('''						<xs:minInclusive value="{}"/>'''.format(value_list[value_list.index("min")+1]))
        if "max" in value_list:
            value_ids.append('''						<xs:maxInclusive value="{}"/>'''.format(value_list[value_list.index("max")+1]))
        value_ids.append('''					</xs:restriction>''')
        value_str = "\n".join(value_ids)
    
    
    elif "length" in value:
        value_list = value.replace(',','').replace(':','').split()
        value_list.remove("length")
        value_ids = ['''					<xs:restriction base="xs:string">''']
        value_ids.append('''						<xs:length value="{}"/>'''.format(" ".join(value_list)))
        value_ids.append('''					</xs:restriction>''')
        value_str = "\n".join(value_ids)
        
        
    else:
        value_str = '''					<simpleValue>{}</simpleValue>'''.format(value)
        
        
    return value_str



class Entity:
    # 02_Entity.xml
    def __init__ (self):
        self.entity_name = None
        self.predefinedtype = '''					<simpleValue>whatever</simpleValue>'''
        
    def set_entity_name (self, entity_name):
        self.entity_name = restriction(entity_name)
    
    def set_predefinedtype (self, predefinedtype):
        self.predefinedtype = restriction(predefinedtype)
        
    
class Classification:
    # 03_Classification.xml
    def __init__ (self):
        self.classification_location = "type"
        self.classification_value = None
        self.classification_system = None
        
    def set_classification_location (self, classification_location):
        self.classification_location = classification_location
        
    def set_classification_value (self, classification_value):
        self.classification_value = value_restriction(classification_value)
        
    def set_classification_system (self, classification_system):
        self.classification_system = restriction(classification_system)
    

class Property:
    # 04_Property.xml
    def __init__ (self):
        self.property_location = "type"
        self.propertyset = None
        self.property_name = None
        self.property_value = None
        
    def set_property_location (self, property_location):
        self.property_location = property_location
        
    def set_propertyset (self, propertyset):
        self.propertyset = restriction(propertyset)
        
    def set_property_name (self, property_name):
        self.property_name = restriction(property_name)
        
    def set_property_value (self, property_value):
        self.property_value = value_restriction(property_value)
    

class Material:
    # 05_Material.xml
    def __init__ (self):
        self.material_location = "type"
        self.material_value = None
        
    def set_material_location (self, material_location):
        self.material_location = material_location
        
    def set_material_value (self, material_value):
        self.material_value = value_restriction(material_value)
    
    
class Root:
    # 01_Root.xml
    def __init__ (self):
        self.specification_name = "test"
        self.applicability = []
        self.requirements = []
        
    def set_specification_name (self, specification_name):
        self.specification_name = specification_name
        
    def add_applicability (self, applicability):
        self.applicability.append(applicability)
        
    def add_requirements (self, requirements):
        self.requirements.append(requirements)
    

if __name__ == '__main__':

    template_string = "min: 0, max: 120"
    value_restriction(template_string)
