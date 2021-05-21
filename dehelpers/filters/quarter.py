def like_quarter(xycell):
    if isinstance(xycell.value, str) and len(xycell.value) == 2 and str(xycell.value) in ['Q1', 'Q2', 'Q3', 'Q4']:
        return True
    else:
        return False
    
