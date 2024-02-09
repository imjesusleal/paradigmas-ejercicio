class KeyStringError(Exception):
    pass
        
def check_dic(dict, key):
    if isinstance(key, str):
        del dict[key]
        raise KeyStringError("No se aceptan las llaves de tipo string")
    return dict[key]

try:
    dicc = {"a":1, "b":2}
    check_dic(dicc, "a")
except KeyStringError as err:
    print(err)