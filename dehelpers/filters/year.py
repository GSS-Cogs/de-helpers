def like_year(xycell):
    if isinstance(xycell.value, (float, int)) and len(str(int(xycell.value))) == 4 and str(int(xycell.value)).startswith(('199', '200', '201', '202')) and int(xycell.value) < 2025:
        return True
    elif isinstance(xycell.value, str) and len(str(xycell.value)) == 4 and str(int(xycell.value)).startswith(('199', '200', '201', '202')) and int(xycell.value) < 2025:
        return True
    else:
        return False 
