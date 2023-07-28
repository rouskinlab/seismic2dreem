# seismic2dreem
A python module to turn seismic output into dreem output

## Installation

```bash
pip install seismic2dreem
```

## Usage

### Python

```python
import seismic2dreem
seismic2dreem.run(
    seismic_folder_path = 'seismic_main_folder',  # path to the folder containing the seismic output. Can be a list of folders.
    dreem_output_dir = 'dreem_output_dir',        # path to the folder where the dreem output will be written
    beautify_json = True,                         # if True, the json files will be beautified. 10x slower and can generate bugs
    verbose = True)                              # if True, print the progress of the conversion
```

### Command line

```bash
seismic2dreem seismic_main_folder another_seismic_main_folder -o dreem_output_dir --beautify_json --verbose
```

## License
[MIT](https://choosealicense.com/licenses/mit/)


## Author

Yves Martin des Taillades
