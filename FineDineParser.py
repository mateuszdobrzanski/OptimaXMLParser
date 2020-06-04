# Parser for:
# Hendi
# Fine Dine
# Grafen

import xml.etree.ElementTree as ET
import csv
from pathlib import Path
import Functions

# prepared dictionary to replace some chars in text
dictionary = {
    "<![CDATA[<ul><li>":"",
    "</li><li>":" ",
    "</li></ul>]]>":" ",
    "<ul><li>":"",
    "</li></ul>":"",
    "<p><br></p><p><br></p>":"",
    "</p><p><br><b></b></p>":"",
    "<p> - ":"",
    "– ":" ",
    "<br>- ":"",
    "<br>":"",
    "   ":" ",
    "</p><p>-":"",
    "<br></p><p>-":"",
    '\n':"",
    '<br class="aloha-end-br"></p>':"",
    '<p>	- ':"",
    '<p></p>':"",
    '  ':" ",
    '- {':"",
    '<p>-</p> ':"",
    '<p>- ':"",
    '</p><p>':"",
    '<span style="color: rgb(90, 90, 90);">':"",
    '<span>':"",
    '<p>-</p>':"",
    '<p><span style="color: black;">':"",
    '<p><strong>':"",
    '<p>x</p>':"",
    '<p>Pozycjonowanie Hendi24.pl</span></p>':"",
    '<span style="color: rgb(74, 74, 74);">':"",
    '<p>.</p> ':"",
    '</span>':"",
    '<p>':"",
    '</p>':"",
}


def fine_dine_parser(file):
    try:
        # read source file
        tree = ET.parse(file)
        root = tree.getroot()

        # starter param to check all of keys in xml
        length = 0

        # open and prepare output file
        home = str(Path.home())
        home = home.replace('\\', '\\\\')
        output_path = home + '\\Desktop\\fine_dine_output.csv'
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

            # find all offers in xml and get values
            for offer in root.findall('offer'):
                # prepare vector and second key-value dict (res variable) with child values in xml
                # from <pom name='key'>value</>
                vector = 0
                dict_child_name_and_value_xml = {}

                for child in offer:
                    dict_child_name_and_value_xml[Functions.clear_none(child.attrib.get('name'), 'None')] = root[length][
                        vector].text
                    vector += 1

                # nazwa
                product_name = offer.find('name').text
                # Kod u dostawcy
                product_producer_code = offer.find('id').text

                # producent
                product_producer = offer.find('producer').text
                # ean
                ean = offer.find('ean')
                product_ean = ''
                if ean is None:
                    product_ean = ''
                else:
                    product_ean = str(offer.find('ean').text)
                    product_ean = Functions.clear_none(product_ean, ' ')
                    if product_ean == '-':
                        product_ean = ''

                # Nr katalogowy
                product_code = dict_child_name_and_value_xml.get('productCode')

                # Kod
                product_id = "H_" + product_code

                # Cena netto
                product_price = Functions.get_value_from_dict(dict_child_name_and_value_xml, 'basePrice')
                product_price = product_price.replace(".", ",")

                Functions.clear_list(dict_child_name_and_value_xml)

                # wymiary
                product_size = str(dict_child_name_and_value_xml)

                # description
                temp_product_description = Functions.clear_none(root[length][2].text, '- {')
                product_description = Functions.replace_all(temp_product_description, dictionary) + " " + product_size
                temp_product_description = product_description.lstrip(' ')
                product_description = Functions.remove_prefix(temp_product_description, '- ')
                product_description = product_description.replace('{', '')
                product_description = product_description.replace('}', '')
                product_description = product_description.replace("'", '')

                # alternative_id = 'H_' + product_name[:60]
                # alternative_id = alternative_id.replace(" ", "_")

                # save values to file
                writer.writerow([product_id,
                                 product_name,
                                 "SZT",
                                 "",
                                 "",
                                 "UP",
                                 product_code,
                                 "",
                                 "FINEDINE",
                                 "",
                                 "",
                                 "23,0",
                                 "23,0",
                                 "",
                                 "",
                                 product_ean,
                                 product_description,
                                 "",
                                 "",
                                 "",
                                 product_producer,
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
