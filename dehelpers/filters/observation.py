from gssutils import *
# from databaker.framework import *
import re
regex = re.compile(r'([0-9]+)')

def like_observations(tab):
    '''
    Observation filter
    This is the valid code for geting the observations
    '''

    def observation_year(xycell): 
        if isinstance(xycell.value, (float, int)) == True:
            return True
        else:
            return False 

    def years(xycell): 
        if isinstance(xycell.value, (float, int)) == True and len(str(int(xycell.value))) == 4 and str(int(xycell.value)).startswith(('199', '20')) and int(xycell.value) < 2025:
            return True
        else:
            return False 

    obs_year = tab.filter(observation_year)
    if len(obs_year) <= 1:
        raise TypeError("Observation data from source data must be of type <float> or <int>")
        
    year = tab.filter(years)

    if len(year) <= 1:
        observations = obs_year
    
    elif len(year) > 1:
        year_actual = []
        for cell in list(year):
            if regex.split(xypath.contrib.excel.excel_location(cell))[1] == regex.split(xypath.contrib.excel.excel_location(list(year)[0]))[1] or regex.split(xypath.contrib.excel.excel_location(cell))[0] == regex.split(xypath.contrib.excel.excel_location(list(year)[0]))[0]:
                year_actual.append(cell)
        
        if len(year_actual) > 1:
            zipped_year = list(zip(year_actual, year_actual[1:]))
            year_set = []
            for i, j in zipped_year:
                if regex.split(xypath.contrib.excel.excel_location(j))[1] == regex.split(xypath.contrib.excel.excel_location(i))[1] and int(j.value) - int(i.value) == 1:
                    year_set.append((i, j))
                elif regex.split(xypath.contrib.excel.excel_location(j))[0] == regex.split(xypath.contrib.excel.excel_location(i))[0] and int(j.value) - int(i.value) == 1:
                    year_set.append((i, j))
                else:
                    continue

            if len(year_set) >= len(zipped_year)/3:
                year_first_ref = xypath.contrib.excel.excel_location(year_actual[0])
                year_second_ref = xypath.contrib.excel.excel_location(year_actual[1])
                if regex.split(year_first_ref)[1] == regex.split(year_second_ref)[1]:
                    period = tab.excel_ref(year_first_ref).expand(RIGHT).is_not_blank()
                elif regex.split(year_first_ref)[0] == regex.split(year_second_ref)[0]:
                    period = tab.excel_ref(year_first_ref).expand(DOWN).is_not_blank()
                observations =  obs_year - period
            else:
                observations =  obs_year
        else:
            observations =  obs_year
    return observations

