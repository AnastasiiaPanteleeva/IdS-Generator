# -*- coding: utf-8 -*-

import xml_classes
import rules
import xml.etree.ElementTree as ET


#open adding template files to written rule classes
class_to_template_file = {
    rules.Entity: "02_Entity.xml",
    rules.Classification: "03_Classification.xml",
    rules.Property:"04_Property.xml",
    rules.Material: "05_Material.xml",
    rules.Root: "01_Root.xml"
}


def get_template_file(class_type, template_root):
    #template_root где находятся шаблоны, class_type - тип класса (ключ)
    return template_root + '\\' + class_to_template_file[class_type]


def get_formatted_string(template_root, rule):
    # rule - созданный экземпляр класса
    format_string = open(get_template_file(rule.__class__, template_root), 'r').read()

    if (isinstance(rule, rules.Entity)):
        return xml_classes.Entity.set_entity_format(format_string, rule.entity_name, rule.predefinedtype)
    
    elif (isinstance(rule, rules.Classification)):
        return xml_classes.Classification.set_classification_format(format_string, rule.classification_value, rule.classification_system, rule.classification_location)
    
    elif (isinstance(rule, rules.Property)):
        return xml_classes.Property.set_property_format(format_string, rule.propertyset, rule.property_name, rule.property_value, rule.property_location)
    
    elif (isinstance(rule, rules.Material)):
        return xml_classes.Material.set_material_format(format_string, rule.material_value, rule.material_location)
    
    elif (isinstance(rule, rules.Root)):
        applicability = [get_formatted_string(template_root, x) for x in rule.applicability]
        requirements = [get_formatted_string(template_root, x) for x in rule.requirements]
        return xml_classes.create_XML.get_xml(format_string, "\n".join(applicability), "\n".join(requirements), rule.specification_name)
        

def generate(template_root, rule):
    final_string = get_formatted_string(template_root, rule)
    return ET.fromstring(final_string)

if __name__ == '__main__':
    
    template_string = '''
    <classification>
        <value>{classification_value}</value>
        <system>{classification_system}</system>
    </classification>
    '''
    ids = ET.fromstring(template_string)
    tree = ET.ElementTree(ids)
    tree.write("Test.xml", method='xml', encoding = "UTF-8", xml_declaration = True)
