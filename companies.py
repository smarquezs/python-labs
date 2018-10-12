import pandas as pd
import re

all_companies = pd.read_csv('~/all_companies.csv', sep='\t')

pattern = r'(INC|INC.|Inc|LLC|LLC.|LTD|LTD.|LTd.|Ltd|Ltd.|S\.A\.S?C?|S\.L|S\.L\.|S\.L\.L\.|\sSA|SA,|SL|ltd|Co\.|Ltda|Ltda\.|SRL|Co.,|CO\.)'

filter = all_companies.name.str.contains(pattern, na=False)
filtered_companies = all_companies[filter]
replace = lambda x: re.sub(pattern, r'', x)
filtered_companies['clean_name'] = filtered_companies.name.apply(replace)
filtered_companies['clean_name'] = filtered_companies.clean_name.apply(lambda x: re.sub(r'[,\.]*', r'', x))
filtered_companies['clean_name'] = filtered_companies.clean_name.apply(lambda x: re.sub(r'\s+[aA&]+\s*$', r'', x))
filtered_companies['clean_name'] = filtered_companies.clean_name.apply(lambda x: x.strip())

for index, row in filtered_companies.iterrows():
    company_id   = row['id']
    company_name = row['name']
    clean_name   = row['clean_name']
    print('{} {} {}'.format(company_id, company_name, clean_name))

filtered_companies.to_csv('~/companies_remove_type_proposal.csv')
