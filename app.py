import subprocess as sp
from modules import yaml
from modules.pathlib import Path

test_image = 'tests/sample.tif'

class NukeCmd(object):

    def __init__(self):

        self.module_dir = Path(__file__).parent

        config_file = self.module_dir / 'conf.yml'

        with open(str(config_file), 'r') as f:
            config = yaml.load(f)

        self.nuke_path = Path(config['nuke_launcher'])

    def mov_from_seq(self, source, dest, start_frame, end_frame):

        script_name = 'mov_from_seq'
        script_path = self.module_dir / 'scripts' / Path(script_name + '.py')
        # source = self.module_dir / 'tests/jpgseq/SQ01_SH010.####.jpeg'
        # dest = self.module_dir / 'tests/SQ01_SH010.mov'

        cmd = [
            str(self.nuke_path), '-t',
            str(script_path),
            str(source),
            str(dest),
            str(start_frame),
            str(end_frame)
        ]
        sp.Popen(cmd)

def main():
    nkcmd = NukeCmd()
    nkcmd.mov_from_seq(0, 10)

if __name__ == '__main__':
    main()
