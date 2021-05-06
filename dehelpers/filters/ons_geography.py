# def like_ons_geography(xycell):
#     try:
#         if isinstance(xycell.value, str) and xycell.value.isalnum() == True and xycell.value.isupper() == 
def like_ons_geography(xycell):
    if isinstance(xycell.value, str) and xycell.value.isalnum() == True and xycell.value.isupper() == True and len(xycell.value) == 9:
        return True
    else:
        return False

   
