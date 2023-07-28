import sys, os
sys.path.append(os.path.abspath('..'))
from seismic2dreem import run
from io import StringIO
import contextlib

def test_end2end():
    # capture the output
    with contextlib.redirect_stdout(StringIO()) as f:
        run(
            seismic_folder_path='/Users/ymdt/src/seismic2dreem/test_files/dragui_rerun', 
            dreem_output_dir='/Users/ymdt/src/seismic2dreem/test_files', 
            beautify_json=False,
            verbose=True)
        
        f = f.getvalue()
        
        assert "WARNING: invalid literal for int() with base 10: 'b' for Dragui_1_S6_L001/ENSG00000138161.14/full" in f, f
        assert "saved Dragui_1_S6_L001.json to" in f, f
        assert "saved Dragui_1_S6_L001.json to" in f, f
        assert f.count('\n') == 3, f
