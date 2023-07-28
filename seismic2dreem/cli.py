from .main import run
import click

@click.command()
@click.argument('seismic_dir', required=True, nargs=-1, type=click.Path(exists=True))
@click.option('--output', '-o', help='Output directory for the DREEM-formatted files', default='.', type=click.Path(exists=True))
@click.option('--beautify/--no-beautify', default=True, help='Beautify JSON output')
@click.option('--verbose/--no-verbose', default=True, help='Print warnings')
def cli(seismic_dir, output, beautify, verbose):
    """seismic2dreem converts SEISMIC data to DREEM format.

    SEISMIC_DIR is the name of the SEISMIC input directory.
    
    """
    run(seismic_dir, output, beautify, verbose)
    