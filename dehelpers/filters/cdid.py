def like_cdid(xycell):
    if isinstance(xycell.value, str) and xycell.value.isalnum() and xycell.value.isupper() and len(xycell.value) == 4:
        return True
    else:
        return False
    
   