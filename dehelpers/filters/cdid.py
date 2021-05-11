def like_cdid(xycell):
    if isinstance(xycell.value, str) and xycell.value.isalnum() == True and xycell.value.isupper() == True and len(xycell.value) == 4:
        return True
    else:
        return False
    
   