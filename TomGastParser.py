# Parser for:
# tom gast


import xml.etree.ElementTree as ET
import csv
from pathlib import Path


def tom_gast_parser(file):
    try:
        # read source file
        tree = ET.parse(file)
        root = tree.getroot()

        # starter param to check all of keys in xml
        length = 0

        # open and prepare output file
        home = str(Path.home())
        home = home.replace('\\', '\\\\')
        output_path = home + '\\Desktop\\tom_gast_output.csv'
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

            for offer in root.findall('Produkt'):
                # nazwa
                product_name = offer.find('NAZWA').text
                # Kod u dostawcy
                product_producer_code = offer.find('Indeks').text

                # producent
                # product_producer = offer.find('NAZWA').text

                # ean
                product_ean = ""

                # Nr katalogowy
                # product_code = ""

                # Kod
                product_id = "T_" + product_producer_code

                # Cena netto
                product_price = offer.find('BRUTTO').text
                product_price = product_price[:-2]
                product_price = product_price.replace('.', ',')

                # wymiary
                product_size = ""

                # description
                product_description = offer.find('ZDJECIE').text

                # vat
                product_vat = int(offer.find('VAT').text)

                # save values to file
                writer.writerow([product_id,
                                 product_name,
                                 "SZT",
                                 "",
                                 "",
                                 "UP",
                                 product_producer_code,
                                 "",
                                 "TOMGAST",
                                 "",
                                 "",
                                 product_vat,
                                 product_vat,
                                 "",
                                 "",
                                 product_ean,
                                 product_description,
                                 "",
                                 "",
                                 "",
                                 "TOMGAST",
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
