# seismic2dreem
A python module to turn seismic output into dreem output

## Installation

```bash
pip install seismic2dreem
```

## Usage

```python
import seismic2dreem
seismic2dreem.run(
    seismic_folder_path = 'seismic_main_folder',  # path to the folder containing the seismic output
    dreem_output_dir = 'dreem_output_dir',        # path to the folder where the dreem output will be written
    beautify_json = True,                         # if True, the json files will be beautified. 10x slower and can generate bugs
    verbose = True)                              # if True, print the progress of the conversion
```

Output dreem files will be in the dreem_output_dir folder.

## License
[MIT](https://choosealicense.com/licenses/mit/)


## Authors

Yves Martin des Taillades
