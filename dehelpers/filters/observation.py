def like_observations(xycell): 
    try:
        float(xycell.value)
        return True
    except:
        return False 
   
