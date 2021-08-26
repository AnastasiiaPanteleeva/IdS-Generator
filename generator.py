# -*- coding: utf-8 -*-


import csv
import xml.etree.ElementTree as ET
import pathlib
import os
import datetime


#self-written modules
import rules
import xml_laden


def entity_write (name, predefinedtype):
    Root = rules.Root()
    Entity = rules.Entity()           
    Entity.set_entity_name(name)
    if predefinedtype != "":
        Entity.set_predefinedtype (predefinedtype)
    Root.add_applicability(Entity)
    Root.add_requirements(Entity)
    return Root


def classification_write (Root, value, system, location, applicability=True):
    if value != "":
        Classification = rules.Classification()
        Classification.set_classification_value(value)
        Classification.set_classification_system(system)
        if location != "":
            Classification.set_classification_location(location)
        if applicability:
            Root.add_applicability(Classification)
        else:
            Root.add_requirements(Classification)
    return Root


def property_write (Root, propertyset, name, value, location, applicability=True):
    if propertyset != "":
        Property = rules.Property()
        Property.set_propertyset(propertyset)
        Property.set_property_name(name)
        Property.set_property_value(value)
        if location != "":
            Property.set_property_location(location) 
        if applicability:
            Root.add_applicability(Property)
        else:
            Root.add_requirements(Property)
    return Root

    
def material_write (Root, value, location, applicability=True):
    if  value != "":
        Material = rules.Material()
        Material.set_material_value(value)
        if location != "":
            Material.set_material_location(location) 
        if applicability:
            Root.add_applicability(Material)
        else:
            Root.add_requirements(Material)
    return Root


def ids_generate (csv_path):
    Path = pathlib.Path(__file__).parent.absolute()
    time = str(datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S"))
    rules_name = csv_path.split("\\")
    folder = "{}\\Ids_{}_{}".format(Path, rules_name[-1], time)
    os.mkdir(folder)

    with open(csv_path) as checkfile:
        reader = csv.DictReader(checkfile,delimiter=";")
     
        row_nummer = [""]
        
        for row in reader:
            if row["entity_name"] != "":
                Root = entity_write(row["entity_name"],row["predefinedtype"])
                classification_write (Root, row["ap_classification_value"], row["ap_classification_system"], row["ap_classification_location"])
                property_write (Root, row["ap_propertyset"], row["ap_property_name"], row["ap_property_value"], row["ap_property_location"])
                material_write (Root, row["ap_material_value"], row["ap_material_location"])
                classification_write (Root, row["classification_value"], row["classification_system"], row["classification_location"], False)
                property_write (Root, row["propertyset"], row["property_name"], row["property_value"], row["property_location"], False)
                material_write (Root, row["material_value"], row["material_location"], False)

              
                row_nummer.append("")
                ids_name = str(len(row_nummer)) + "_" + row["entity_name"] + ".xml"
  
                
                ids = xml_laden.generate('{}\\templates'.format(Path), Root)
                tree = ET.ElementTree(ids)
                tree.write(folder + "\\" + ids_name, method='xml', encoding = "UTF-8", xml_declaration = True)

    
if __name__ == '__main__':
    
    Path = pathlib.Path(__file__).parent.absolute()
    csv_path = '{}\\ifc_check.csv'.format(Path)
#    csv_path = '{}\\er_A1.csv'.format(Path)
    ids_generate (csv_path)
    

    
    
'''
#specifies the location of the current file. If the model is in the same folder,
#then this is convenient
Path = pathlib.Path(__file__).parent.absolute()
time = str(datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S"))
folder = "{}\\Ids_{}".format(Path, time)
os.mkdir(folder)


with open('{}\\ifc_check.csv'.format(Path)) as checkfile:
    reader = csv.DictReader(checkfile,delimiter=";")
 
    
    row_nummer = [""]
    for row in reader:
        if row["entity_name"] != "":
            Root = rules.Root()
            Entity = rules.Entity()           
            Entity.set_entity_name(row["entity_name"])
            if row["predefinedtype"] != "":
                Entity.set_predefinedtype (row["predefinedtype"])
            Root.add_applicability(Entity)
            Root.add_requirements(Entity)


            if row["ap_classification_value"] != "":
                Classification = rules.Classification()
                Classification.set_classification_value(row["ap_classification_value"])
                Classification.set_classification_system(row["ap_classification_system"])
                if row["ap_classification_location"] != "":
                    Classification.set_classification_location(row["ap_classification_location"])    
                Root.add_applicability(Classification)
                
                
            if row["ap_propertyset"] != "":
                Property = rules.Property()
                Property.set_propertyset(row["ap_propertyset"])
                Property.set_property_name(row["ap_property_name"])
                Property.set_property_value(row["ap_property_value"])
                if row["ap_property_location"] != "":
                    Property.set_property_location(row["ap_property_location"]) 
                Root.add_applicability(Property)


            if row["ap_material_value"] != "":
                Material = rules.Material()
                Material.set_material_value(row["ap_material_value"])
                if row["ap_material_location"] != "":
                    Material.set_material_location(row["ap_material_location"]) 
                Root.add_applicability(Material)
              
                
            if row["classification_value"] != "":
                Classification = rules.Classification()
                Classification.set_classification_value(row["classification_value"])
                Classification.set_classification_system(row["classification_system"])
                if row["classification_location"] != "":
                    Classification.set_classification_location(row["classification_location"])    
                Root.add_requirements(Classification)


            if row["propertyset"] != "":
                Property = rules.Property()
                Property.set_propertyset(row["propertyset"])
                Property.set_property_name(row["property_name"])
                Property.set_property_value(row["property_value"])
                if row["property_location"] != "":
                    Property.set_property_location(row["property_location"]) 
                Root.add_requirements(Property)


            if row["material_value"] != "":
                Material = rules.Material()
                Material.set_material_value(row["material_value"])
                if row["material_location"] != "":
                    Material.set_material_location(row["material_location"]) 
                Root.add_requirements(Material)

                
            row_nummer.append("")
            ids_name = str(len(row_nummer)) + "_" + row["entity_name"] + ".xml"
  
                
            ids = xml_laden.generate('{}\\templates'.format(Path), Root)
            tree = ET.ElementTree(ids)
            tree.write(folder + "\\" + ids_name, method='xml', encoding = "UTF-8", xml_declaration = True)
'''
                
            
            
            
            