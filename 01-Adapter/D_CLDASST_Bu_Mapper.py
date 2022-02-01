import pandas as pd
import os
import platform

current_path = os.getcwd()
bu_df = pd.read_csv(current_path + '\\ad_dump\\AD_Extract.csv')

bu_df.drop('User Name', axis=1, inplace=True)
number_list = ['USR_' + str(num) for num in range(1, len(bu_df)+1)]

bu_df.insert(0, "USR_ID", number_list)
bu_df.rename(columns={'Display Name': 'USR_NM'}, inplace=True)
bu_df.rename(columns={'Department': 'USR_BUS_UNT'}, inplace=True)
bu_df['USR_STAT'] = ""
bu_df['USR_LOC'] = ""
bu_df['USR_SUB'] = ""
bu_df['USR_CAT'] = ""
bu_df['USR_SAS_SKL'] = ""
bu_df['USR_SAS_AGE'] = ""
bu_df['USR_NON_SAS_SKL'] = ""
bu_df['USR_NON_SAS_AGE'] = ""

if platform.system() == 'Windows':
    if not os.path.isdir("..\\00-Data Model"):
        os.makedirs("..\\00-Data Model")
    bu_df.to_csv('..\\00-Data Model\\D_CLDASST_Bu_Mapper_Output.csv', index=False)
