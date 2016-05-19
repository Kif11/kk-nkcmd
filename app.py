import subprocess as sp
from modules import yaml
from modules.pathlib import Path

test_image = 'tests/sample.tif'

class NukeCmd(object):

    def __init__(self):

        with open('conf.yml', 'r') as f:
            config = yaml.load(f)

        self.nuke_path = Path(config['nuke_launcher'])
        self.pwd = Path('/Users/kif/Desktop/nkcmd')

    def mov_from_seq(self, start_frame, end_frame):

        script_name = 'mov_from_seq'
        script_path = self.pwd / 'scripts' / Path(script_name + '.py')
        source = self.pwd / 'tests/jpgseq/SQ01_SH010.####.jpeg'
        dest = self.pwd / 'tests/SQ01_SH010.mov'

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
