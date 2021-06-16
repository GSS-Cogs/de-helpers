        
def is_numeric(xycell):
    """
    Given an xycell return True if the .value attribute of the cell is numeric
    """
    try:
        float(xycell.value)
        return True
    except:
        return False 


def like_cdid(xycell):
    """
    Given an xycell return True if the .value attribute of the cell _appears_ to be a CDID code, a CDID code is
    an upper cased alpha numeric code of length four. 
    """
    if isinstance(xycell.value, str) and xycell.value.isalnum() == True and xycell.value.isupper() == True and len(xycell.value) == 4:
        return True
    else:
        return False


def like_ons_geography(xycell):
    """
    Given an xycell return True if the .value attribute of the cell _appears_ to be an ONS geography code, an
    ONS geography code is a 9 digit code consisting of a single uppercase letter followed by 8 numbers.
    """
    if isinstance(xycell.value, str) and xycell.value[0].isalpha() and xycell.value[0].isupper() and xycell.value[1:].isnumeric() and len(str(xycell.value)) == 9:
        return True
    else:
        return False

