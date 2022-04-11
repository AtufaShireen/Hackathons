import pandas as pd 
df = pd.read_csv(r"data\suicides.csv")
state  = {
    'A & N ISLANDS':'AN',
    'ANDHRA PRADESH':'AP',
    'ARUNACHAL PRADESH': 'AR',
    'ASSAM':'AS',
    'BIHAR': 'BR',
    'CHANDIGARH':'CH',
    'CHHATTISGARH': 'CT',
    'D & N HAVELI': 'DN',
    'DAMAN & DIU': 'DD',
    'DELHI (UT)':'DL',
    'GOA':'GA',
    'GUJARAT':'GJ',
    'HARYANA':'HR',
    'HIMACHAL PRADESH':'HP',
    'JAMMU & KASHMIR':'JK',
    'JHARKHAND':'JH',
     'KARNATAKA':'KA',
       'KERALA':'KL',
        'LAKSHADWEEP':'LD',
         'MADHYA PRADESH':'MP',
          'MAHARASHTRA':'MH',
       'MANIPUR':'MN',
        'MEGHALAYA':'ML',
         'MIZORAM':'MZ',
          'NAGALAND':'NL', 
          'ODISHA':'OR',
       'PUDUCHERRY':'PY',
        'PUNJAB':'PB', 
        'RAJASTHAN':'RJ',
         'SIKKIM':'SK',
          'TAMIL NADU':'TN',
       'TOTAL (STATES)':'TOTAL (STATES)',
        'TOTAL (UTs)':'TOTAL (UTs)',
         'TRIPURA':'TR',
          'UTTAR PRADESH':'UP',
       'UTTARAKHAND':'UT',
        'WEST BENGAL':'WB',
        'TOTAL (ALL INDIA)':'TOTAL (ALL INDIA)'
}

types_ = {
    'Hr. Secondary/Intermediate/Pre-Universit': 'pre-uni',
     'Middle': 'Middle',
     'Diploma':'Diploma',
     'Matriculate/Secondary':'Secondary',
     'No Education':'No Education',
      'Post Graduate and Above':'PG',
       'Primary':'Primary', 
     'Graduate':'Graduate',
     'Divorcee':'Divorcee',
     'Married':'Married',
     'Seperated':'Divorcee',
     'Widowed/Widower':'Divorcee',
     'Never Married':'Never Married' ,
    'By Consuming Insecticides':'Insecticides',
     'By Consuming Other Poison':'Poison',
       'By Drowning':'Drowning',
      'By Fire-Arms':'Fire-Arms'
      , 'By Fire/Self Immolation':'Fire Immolation',
       'By Hanging':'By Hanging',
      'By Jumping from (Building)':'Jump Building',
       'By Jumping from (Other sites)':'Jump Other sites',
       'By Jumping off Moving Vehicles/Trains':'Jump Moving Vehicles',
      'By Machine':'By Machine',
       'By Other means':'Other means',
      'By Other means (please specify)':'Other means',
       'By Over Alcoholism':'Over Alcoholism',
      'By Overdose of sleeping pills':'sleeping pills',
       'By Self Infliction of injury':'Self Infliction',
       'By coming under running vehicles/trains':'under running vehicles',
       'By touching electric wires':'electric wires',
     'Ideological Causes/Hero Worshipping':'Hero Worship',
     'Self-employed (Business activity)':'Business activity',
     'Illness (Aids/STD)':'illness',
     'Bankruptcy or Sudden change in Economic Status':'Economic Status change',
     'Suspected/Illicit Relation':'Illicit Relation',
     'Professional/Career Problem':'Professional problem'}

def convert_type(x):
    try:
        return types_[x]
    except:
        return x
df['new_state'] = df['State'].apply(lambda x: state[x])

df.drop('State',axis=1,inplace=True)
df['Type'] = df['Type'].apply(lambda x: convert_type(x))
df.to_csv("suicides_preprocessed.csv",index=False)