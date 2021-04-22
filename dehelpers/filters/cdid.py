# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

def cdid_filter(xycell):
    if str(xycell.value).isalnum() == True and str(xycell.value).isupper() == True and len(xycell.value) == 4:
        return True
    else:
        return False
