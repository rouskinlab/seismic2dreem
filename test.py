import sys, os
sys.path.append(os.path.abspath('..'))
from seismic2dreem import run
from io import StringIO
import contextlib

def test_end2end():
    # capture the output
    with contextlib.redirect_stdout(StringIO()) as f:
        run(
            seismic_dir='test_files', 
            output='test_output', 
            ow=True,
            beautify=True,
            verbose=True)
        
        f = f.getvalue()
        
        assert "WARNING: invalid literal for int() with base 10: 'b' for Dragui_1_S6_L001/ENSG00000138161.14/full" in f, f
        assert "saved 1-5_3_S4_L001.json to" in f, f
        assert "saved 1-5_4_S6_L001.json to" in f, f
        assert f.count('\n') == 3, f
