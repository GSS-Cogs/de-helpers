def like_year_quarter(xycell): 
    if isinstance(xycell.value, (float, int)) and len(str(int(xycell.value))) == 4 and str(xycell.value).startswith(('199', '200', '201', '202')) and int(xycell.value) < 2025:
        return True
    elif isinstance(xycell.value, str) and len(str(xycell.value)) == 4 and str(xycell.value).startswith(('199', '200', '201', '202')) and (xycell.value).isnumeric() and int(xycell.value) < 2025:
        return True
    elif isinstance(xycell.value, str) and len(str(xycell.value)) > 6 and " " in str(xycell.value) and len(str(xycell.value).replace(" ", "")) == 6 and str(xycell.value)[:4].isnumeric() and str(xycell.value).startswith(('199', '200', '201', '202')) and int(str(xycell.value)[:4]) < 2025 and str(xycell.value)[-2:] in ['Q1', 'Q2', 'Q3', 'Q4']:
        return True
    elif isinstance(xycell.value, str) and " " not in str(xycell.value) and len(str(xycell.value)) == 6 and str(xycell.value)[:4].isnumeric() and str(xycell.value).startswith(('199', '200', '201', '202')) and int(str(xycell.value)[:4]) < 2025 and str(xycell.value)[-2:] in ['Q1', 'Q2', 'Q3', 'Q4']:
        return True
    else:
        return False 
    