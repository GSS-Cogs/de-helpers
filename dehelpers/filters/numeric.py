def like_float(xycell): 
    try:
        float(xycell.value)
        return True
    except:
        return False 
   
