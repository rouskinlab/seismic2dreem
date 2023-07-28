from os.path import join, exists
import json
from .dump import dump_json
from .path import SeismicPath
from .translation import seismic_csv_to_dreem_json


def run(seismic_folder_path:str, dreem_output_dir:str, beautify_json:bool=True, verbose:bool=True):
    """A function to convert a seismic folder to a dreem json output.
    
    Arguments:
        seismic_folder_path {str} -- The path to the seismic folder
        dreem_output_dir {str} -- The path to the output directory
        beautify_json {bool} -- Whether to beautify the json output (default: True). Deactivate for faster processing and less possible errors.
        verbose {bool} -- Whether to print warnings (default: True)
        
    Returns:
        None
    """
    
    if type(seismic_folder_path) == str:
        seismic_folder_path = [seismic_folder_path]
            
    for this_seismic_folder_path in seismic_folder_path:
        seismic_path = SeismicPath(this_seismic_folder_path)
            
        for sample in seismic_path.list_samples():
            out = {'sample': sample}
            for construct in seismic_path.list_constructs(sample):
                out[construct] = {}
                for section in seismic_path.list_sections(sample, construct):
                    out[construct][section] = {}
                    try:
                        out[construct][section] = seismic_csv_to_dreem_json(seismic_path.get_csv_path(sample, construct, section))
                    except FileNotFoundError:
                        if verbose:
                            print(f"WARNING: no csv found for {sample}/{construct}/{section}")
                    except ValueError as e:
                        if verbose:
                            print(f"WARNING: {e} for {sample}/{construct}/{section}")
                    except Exception as e:
                        if verbose:
                            print(f"WARNING: {e} for {sample}/{construct}/{section}")
                
            # clean up empty constructs
            for construct in seismic_path.list_constructs(sample):
                if len(out[construct]) == 1:
                    if len(out[construct][list(out[construct].keys())[0]]) == 0:
                        del out[construct]
                        
            # Save to file
            path = join(dreem_output_dir, sample + ".json")
            
            # warning if file already exists
            if exists(path):
                print(f"WARNING: {path} already exists")
            
            if beautify_json:
                dump_json(out, path)
            else:
                with open(path, 'w') as f:
                    json.dump(out, f)
            if verbose:
                print(f"saved {sample}.json to {seismic_path.get_sample_path(sample)}")