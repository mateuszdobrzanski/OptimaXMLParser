# Replace chars from dictionary, dic is bellow
def replace_all(text, dic):
    for x, y in dic.items():
        text = text.replace(x, y)
    return text


# replace none to other value
def clear_none(text, val):
    if text is None:
        text = val
    return text


# clear list with bellow tags
def clear_list(in_list):
    del in_list['None']


# remove some text at beginning
def remove_prefix(text, prefix):
    return text[len(prefix):] if text.startswith(prefix) else text


def get_value_from_dict(my_dict, val):
    if val in my_dict:
        return my_dict.get(val)
    else:
        return ''
    

# clear list with bellow tags
def clear_list_tom_gast(in_list):
    del in_list['None']
    del in_list['productId']
    del in_list['basePrice']
    del in_list['tillStockLasts']
    del in_list['largeSize']
    del in_list['productCode']
    del in_list['categoryId']
    if 'symbol' in in_list:
        del in_list['symbol']
    if '-' in in_list:
        del in_list['-']


def if_node_exist(child, parameter):
    node = child.find(parameter)
    if node is not None:
        return node.text
    else:
        return 'None'


def change_none_to_text(text):
    if text is not None:
        return text
    else:
        return "None"


def clear_description_var(dictionary):
    string = str(dictionary)
    string = string.replace("{", "")
    string = string.replace("}", "")
    string = string.replace("'", "")
    string = string.replace("(szt#)", "szt.")
    string = string.replace("None", "")

    return string