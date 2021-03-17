import pandas as pd
import os
import json
from pandas import json_normalize

for filename in os.listdir('./'):
    root, ext = os.path.splitext(filename)
    if ext == '.json':
        with open (filename) as f:
            data = [json.loads(line) for line in f]
        df = json_normalize(data)
        df.to_csv(root + '.csv', index=False)
