import os
import argparse
from shutil import copyfile

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, default='train_all', help='dataset path')
args = parser.parse_args()

all_path = args.input
train_save_path = 'train'
val_save_path = 'val'
if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)
if not os.path.isdir(val_save_path):
    os.mkdir(val_save_path)

dirnames = os.listdir(all_path)
for d in dirnames:
    src_dir = os.path.join(all_path, d)
    if os.path.isdir(src_dir):
        filenames = os.listdir(src_dir)
        for f in filenames:
            print(f)
            if not (f[-3:]=='jpg' or f[-3:]=='png') :
                continue
            src_path = os.path.join(src_dir, f)
            val_dst_path = os.path.join(val_save_path, d)
            train_dst_path = os.path.join(train_save_path, d)
            if not os.path.isdir(val_dst_path):
                os.mkdir(val_dst_path)
                os.mkdir(train_dst_path)
                dst_path = os.path.join(val_dst_path, f)  #first image is used as val image
                copyfile(src_path, dst_path)
            else:
                dst_path = os.path.join(train_dst_path, f)
                copyfile(src_path, dst_path)

