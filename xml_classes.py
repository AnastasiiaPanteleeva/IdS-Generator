# -*- coding: utf-8 -*-

from string import Formatter

  
#formatter for getting placeholder and set other value
#форматер для получения заполнителя и установки другого значения
class FormatXML:
    def __init__(self, template_string):
        #self.template = open(template_file).read()
        #template_string - шаблоны в виде строки
        self.template = template_string
        #выделяет из строки ключевые слова в фигурных скобках
        #индекс 1, потому что в виде tuple сохраняется что до/в/после вигурных скобок
        self.required_keys = [ele[1] for ele in Formatter().parse(self.template) if ele[1]]
        #print(self.required_keys)
        self.parameters = {}

    def set_value(self, key, value):
        self.parameters[key] = value

    def generate(self):
        #проверка есть ли вбиваемый ключ в ключевых словах шаблона
        if not all(k in self.parameters.keys() for k in self.required_keys):
            raise ValueError("Not enough keys.")
        #format заменяет в существующей строке первый указанный аргумент на второй
        # ** - распаковывают словарь
        return self.template.format(**self.parameters)

    def __str__(self):
        return str(self.generate())

    
#placeholderreplacement for different templates and parts of idsxml
class Entity:
    @staticmethod
    # 02_Entity.xml
    def set_entity_format(entity_string, entity_name, predefinedtype):
        entity_format = FormatXML(entity_string)
        entity_format.set_value("entity_name", entity_name)
        entity_format.set_value("predefinedtype", predefinedtype)
        return entity_format.generate()


class Classification:
    @staticmethod
    # 03_Classification.xml
    def set_classification_format(classification_string, classification_value, classification_system, classification_location="type"):
        classification_format = FormatXML(classification_string)
        classification_format.set_value("classification_location", classification_location)
        classification_format.set_value("classification_value", classification_value)
        classification_format.set_value("classification_system", classification_system)
        return classification_format.generate()


class Property:
    @staticmethod
    # 04_Property.xml
    def set_property_format(property_string, propertyset, property_name, property_value, property_location="type"):
        property_format = FormatXML(property_string)
        property_format.set_value("property_location", property_location)
        property_format.set_value("propertyset", propertyset)
        property_format.set_value("property_name", property_name)
        property_format.set_value("property_value", property_value)
        return property_format.generate()


class Material:
    @staticmethod
    # 05_Material.xml
    def set_material_format(material_string, material_value, material_location="type"):
        material_format = FormatXML(material_string)
        material_format.set_value("material_location", material_location)
        material_format.set_value("material_value", material_value)
        return material_format.generate()


class create_XML:
    @staticmethod
    #благодаря staticmethod возможен вызов функции без создания экземпляра
    # 01_Root.xml
    def get_xml(template_string, applicability, requirements, specification_name="binder"):
        formatter = FormatXML(template_string)
        formatter.set_value("specification_name", specification_name)
        formatter.set_value("applicability", applicability)
        formatter.set_value("requirements", requirements)
        return formatter.generate()


    
if __name__ == '__main__':
    
    template_string = '''
    <?xml version='1.0' encoding='UTF-8'?>
    <ids xmlns="http://standards.buildingsmart.org/IDS" xsi:schemaLocation="http://standards.buildingsmart.org/IDS http://standards.buildingsmart.org/IDS/ids.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <specification name="{specification_name}">
            <applicability>
                {applicability}
            </applicability>
            <requirements>
                {requirements}
            </requirements>
        </specification>
        <info/>
    </ids>
    '''
    xml = create_XML.get_xml(template_string, "","")
    print (xml)
    
    material_string = '''
                <material location={material_location}>
                    <value>
                        {material_value}
                    </value>
                </material> 
    '''
    material = Material.set_material_format(material_string,  "")
    print (material)    