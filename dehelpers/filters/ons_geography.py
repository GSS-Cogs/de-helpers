def like_ons_geography(xycell):  
    if isinstance(xycell.value, str) and xycell.value[0].isalpha() and xycell.value[0].isupper() and xycell.value[1:].isnumeric() and len(str(xycell.value)) == 9:
        return True
    else:
        return False
    