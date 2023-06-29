# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:30:32 2023

@author: Asus
"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd
  

addressList = pd.read_excel(r'D:\_HomePro\2023_05_27_FuzzySearchForThailandAddress\MasterData\Thailand_Province_District_SubDistrict_List.xlsx')
address4Check = pd.read_excel(r'D:\_HomePro\2023_05_27_FuzzySearchForThailandAddress\AddressListForChecking.xlsx')

mat1 = []
mat2 = []

address4Check['match1'] = ''
address4Check['match1_score'] = ''
address4Check['match2'] = ''
address4Check['match2_score'] = ''


for i, row in address4Check.iterrows():
    province = row['Province']
    district = row['District']

    compareAddressList = addressList['TambonThaiShort'][(addressList['ProvinceThai'] == province) & (addressList['DistrictThaiShort'] == district)].tolist()

    checkAddress = row['SubDistrict']

    matches = process.extract(checkAddress, compareAddressList, limit=2)
    #mat2 = {'match1': matches[0][0], 'match1_score': matches[0][1], 'match2': matches[1][0], 'match2_score': matches[1][1]}
    #mat1.append(mat2)
    address4Check.loc[i, 'match1'] = matches[0][0]
    address4Check.loc[i, 'match1_score'] = matches[0][1]
    address4Check.loc[i, 'match2'] = matches[1][0]
    address4Check.loc[i, 'match2_score'] = matches[1][1]
    
    
    
#address4Check['match1'] = pd.DataFrame([mat1])['0']
#address4Check['match2'] = pd.DataFrame([mat1])['1']


address4Check.to_excel(r'D:\_HomePro\2023_05_27_FuzzySearchForThailandAddress\AddressListForChecking_Result.xlsx', index=False)

""""
dict1 = {'name': ["aparna", "pankaj", 
                  "sudhir", "Geeku"]}
  
dict2 = {'name': ["aparn", "arup", "Pankaj",
                  "sudhir c", "Geek", "abc"]}
  
# converting to pandas dataframes
dframe1 = pd.DataFrame(dict1)
dframe2 = pd.DataFrame(dict2)
  
# empty lists for storing the
# matches later
mat1 = []
mat2 = []
  
# printing the pandas dataframes
#dframe1.show()
#dframe2.show()


list1 = dframe1['name'].tolist()
list2 = dframe2['name'].tolist()

# taking the threshold as 80
threshold = 80


# iterating through list1 to extract 
# it's closest match from list2
for i in list1:
    mat1.append(process.extract(i, list2, limit=2))
dframe1['matches'] = mat1
  
print(dframe1)
"""