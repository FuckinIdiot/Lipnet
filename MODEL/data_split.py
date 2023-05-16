import os
import shutil
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
                    name = os.path.basename(line)
                    align_file = f"{source_align_folder}/{_folder}/align/{name}.align"
                    os.makedirs(f"{folder}/{align_folder}/{_folder}/align", exist_ok=True)
                    dest_file = f"{folder}/{align_folder}/{_folder}/align/{name}.align"
                    shutil.copy(align_file, dest_file)
