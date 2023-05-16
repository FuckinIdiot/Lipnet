gpu = '0'
random_seed = 0
data_type = 'unseen'
video_path = 'lip/'
train_list = f'data/new_{data_type}_train.txt'
val_list = f'data/new_{data_type}_train.txt'
anno_path = 'GRID_align_txt'
vid_padding = 75
txt_padding = 200
batch_size = 1
base_lr = 2e-5
num_workers = 2
max_epoch = 10000
display = 10
test_step = 1000
save_prefix = f'weights/LipNet_{data_type}'
is_optimize = True

