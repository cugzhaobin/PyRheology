import numpy as np
import h5py, yaml
import sys, os

def load_rock(h5file):
    with h5py.File(h5file, 'r') as h5:
        print(h5.keys())
        return h5

def main(cfgfile):
    if os.path.isfile(cfgfile) != True:
        sys.exit()
    
    with open(cfgfile, 'r') as fid:
        lines = fid.read()
        cfg   = yaml.load(lines, Loader=yaml.FullLoader)
        general = cfg['general_dict']
        print(general)


    h5 = load_rock('rock.h5')

     
    


main('structure_cfg.yaml')

#if __name__ == '__main__':
#   if len(sys.argv) != 2:
#       sys.exit()

#   cfgfile = sys.argv[1]
#   main(cfgfile)
