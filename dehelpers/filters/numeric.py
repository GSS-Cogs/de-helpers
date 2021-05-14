def is_numeric(xycell): 
    try:
        float(xycell.value)
        return True
    except:
        return False 
   