__all__ = ['print_path']

import os
from pathlib import Path


# path_ = "c:/Users/ykarabekov/Desktop/gb/python/7/test/"

# os.chdir(path_)

def print_path():
    print(Path.cwd())   
    dir_list = os.listdir()
    for obj in dir_list:
        print(f'{os.path.isdir(obj) = }', end='\t')
        print(f'{os.path.isfile(obj) = }', end='\t')
        print(f'{os.path.islink(obj) = }', end='\t')
        print(f'{obj = }')
        
        
if __name__ == "__main__":
    print_path()
    
    # p = Path(Path().cwd())
    # for obj in p.iterdir():
    #     print(f'{obj.is_dir() = }', end='\t')
    #     print(f'{obj.is_file() = }', end='\t')
    #     print(f'{obj.is_symlink() = }', end='\t')
    #     print(f'{obj = }')
    
    