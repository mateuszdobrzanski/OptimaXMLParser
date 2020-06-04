# Parser for:
# RMGastro

import xml.etree.ElementTree as ET
import csv, Functions
from pathlib import Path


def rm_gastro_parser(file):
    try:
        # read source file
        tree = ET.parse(file)
        root = tree.getroot()

        # starter param to check all of keys in xml
        length = 0

        # open and prepare output file
        home = str(Path.home())
        home = home.replace('\\', '\\\\')
        output_path = home + '\\Desktop\\rm_gastro_output.csv'
        with open(output_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(["Kod",
                             "Nazwa",
                             "JM",
                             "JmZ",
                             "Przelicznik_JmJmZ",
                             "Typ",
                             "NumerKatalogowy",
                             "SWW",
                             "Grupa",
                             "StanMin",
                             "StanMax",
                             "VAT",
                             "VATZak",
                             "VATFlaga",
                             "VatZakFlaga",
                             "EAN",
                             "Opis",
                             "OpakowanieKaucja",
                             "OdwrotneObciazenie",
                             "CenaZCzteremaMiejscami",
                             "Dostawca",
                             "Kod u dostawcy",
                             "Kod producenta",
                             "Cena zakupu",
                             "Waluta Cena zakupu",
                             "Cena hurtowa 1",
                             "Waluta Cena hurtowa 1",
                             "Cena hurtowa 2",
                             "Waluta Cena hurtowa 2",
                             "Cena hurtowa 3",
                             "Waluta Cena hurtowa 3",
                             "Cena detaliczna",
                             "Waluta Cena detaliczna"])
        
            for offer in root.findall('product'):
                product_item_code = Functions.if_node_exist(offer, 'itemcode')
                product_code = Functions.if_node_exist(offer, 'code')
                product_name = Functions.if_node_exist(offer, 'name')
                product_description = Functions.if_node_exist(offer, 'description')
                if product_description is None:
                    product_description = ""
                product_price = Functions.if_node_exist(offer, 'price')
                product_price = product_price.replace(".", ",")
                product_image = Functions.if_node_exist(offer, 'image')
                product_instruction = Functions.if_node_exist(offer, 'instruction')
                product_id = "RMG_" + product_item_code
        
                dict_child_name_and_value_xml = {}
                if Functions.if_node_exist(offer, 'property'):
                    for all_int in offer.iter('property'):
                        # print(all_int.text)
                        # print(all_int.attrib.get('name'))
                        dict_child_name_and_value_xml[all_int.attrib.get('name')] = all_int.text
                        # print(all_int[i][vector].text)
                else:
                    dict_child_name_and_value_xml['None'] = 'None'
        
                # print(dict_child_name_and_value_xml)
        
                description = "{} {}".format(product_description, Functions.clear_description_var(dict_child_name_and_value_xml))
        
                writer.writerow([product_id,
                                 product_name,
                                 "SZT",
                                 "",
                                 "",
                                 "UP",
                                 product_item_code,
                                 "",
                                 "RMGASTRO",
                                 "",
                                 "",
                                 "23,0",
                                 "23,0",
                                 "",
                                 "",
                                 "",
                                 description,
                                 "",
                                 "",
                                 "",
                                 "RMGASTRO",
                                 "",
                                 "",
                                 "",
                                 "",
                                 "",
                                 "",
                                 "",
                                 "",
                                 "",
                                 "",
                                 product_price,
                                 "PLN"])
        
                length += 1
        return length
    except:
        return "Wystąpił błąd pliku"