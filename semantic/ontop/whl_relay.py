import pandas as pd

# Load the CSV files
relay_whs_df = pd.read_csv('RELAY_WHS.csv')
#who_life_exp_df = pd.read_csv('/mnt/data/who_life_exp.csv')

# Rename columns for relay_whs
relay_whs_df.rename(columns={
    'GEO_NAME_SHORT': 'Country',
    'AMOUNT_N': 'Value'
}, inplace=True)

# Create a combined indicator column
relay_whs_df['Indicator'] = relay_whs_df.apply(lambda row: f"{row['IND_NAME']} ({row['DIM_SEX']})", axis=1)

# Save the modified CSVs
relay_whs_df[['Country', 'Indicator', 'Value']].to_csv('relay_whs_modified.csv', index=False)