import numpy as np
import pandas as pd

translation_arrays = {
    "Called": 'cov',
    "Subbed": 'sub_N',
    "Subbed-A": 'sub_A',
    "Subbed-C": 'sub_C',
    "Subbed-G": 'sub_G',
    "Subbed-T": 'sub_T',
    "Deleted": 'del',
    "Inserted": 'ins',
}

def seismic_csv_to_dreem_json(csv_path:str):
    i = pd.read_csv(csv_path)
    d = {}
    for k, v in translation_arrays.items():
        d[v] = np.array(i[k], dtype=np.int64).tolist()
    d['sequence'] = ''.join(i['Base'].tolist())
    d['min_cov'] = min(d['cov'])
    d['info'] = (i['Mutated'] + i['Matched']).tolist()
    d['sub_rate'] = (np.array(d['sub_N']) / np.array(d['info'])).tolist()
    return d

