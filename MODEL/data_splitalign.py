import os
from tqdm import tqdm

folder = "C:/Users/rogue/Downloads/GRID_LIP_160x80_TXT/GRID_LIP_160x80_TXT"
lip_folder = "lip"
align_folder = "GRID_align_txt"
source_align_folder = "C:/Users/rogue/GRID_LIP_160x80_TXT/GRID_align_txt"

if __name__ == '__main__':
    for _folder in tqdm(os.listdir(os.path.join(folder, lip_folder))):
        folder_path = f"{folder}/{lip_folder}/{_folder}"
        for _video_f in os.listdir(folder_path):
            _f_video_path = f"{folder_path}/{_video_f}"
            for mpg in os.listdir(_f_video_path):
                mpg_path = f"{_f_video_path}/{mpg}"
                for real_folder in os.listdir(mpg_path):
                    line = f"{mpg_path}/{real_folder}"
                    idx = line.find(_folder)
                    _line = line[idx:]
                    with open("C:/Users/rogue/LipNet-PyTorch/data/new_unseen_train.txt", 'a') as f:
                        f.write(_line + "\n")