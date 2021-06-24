import os
import pandas as pd
import fnmatch

files = fnmatch.filter(os.listdir('.'), '406*')
combined_csv = pd.concat([pd.read_csv(f) for f in files[0:5]])
combined_csv.to_csv('combined_csv_light.csv', index=False)