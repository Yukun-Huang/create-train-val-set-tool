import os
import os.path as osp
from shutil import copyfile
import argparse
import json

dataset_dict = {
    'caviar'    :   'caviar',
    'mlr_cuhk03':   'MLR_cuhk03',
    'mlr_viper' :   'MLR_viper',
}

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='mlr_viper', help="dataset name")
args = parser.parse_args()

# You only need to change this line to your dataset download path
root = '/home/kevinh/dataset/reid/resolution'
data_root = os.path.join(root, dataset_dict[args.dataset])


def read_image_list():
    with open(os.path.join(data_root, 'meta.json'), 'r') as f:
        meta = json.load(f)
    with open(os.path.join(data_root, 'split.json'), 'r') as f:
        split = json.load(f)

    return meta, split


if __name__ == '__main__':

    meta, split = read_image_list()
    save_path = osp.join(data_root, 'pytorch')

    for id in split['trainval']:
        for cam_list in meta['identities'][id]:
            for src_path in cam_list:
                src_path = os.path.join(data_root, src_path)
                dst_path = os.path.join(save_path, 'train', "%04d" % id)
                if not os.path.isdir(dst_path):
                    os.makedirs(dst_path)
                cam_id = src_path.split('/')[-2].split('_')[-1]
                filename = src_path.split('/')[-1].split('_')
                filename = filename[0] + '_c{}_'.format(cam_id) + filename[1]
                copyfile(src_path, osp.join(dst_path, filename))
                print(filename)

    for id in split['trainval']:
        for cam_list in meta['identities'][id]:
            for src_path in cam_list:
                src_path = os.path.join(data_root, src_path)
                dst_path = os.path.join(save_path, 'val', "%04d" % id)
                if not os.path.isdir(dst_path):
                    os.makedirs(dst_path)
                cam_id = src_path.split('/')[-2].split('_')[-1]
                filename = src_path.split('/')[-1].split('_')
                filename = filename[0] + '_c{}_'.format(cam_id) + filename[1]
                copyfile(src_path, osp.join(dst_path, filename))
                print(filename)

    for id in split['test_gallery']:
        for cam_list in meta['identities'][id]:
            for src_path in cam_list:
                src_path = os.path.join(data_root, src_path)
                dst_path = os.path.join(save_path, 'gallery', "%04d" % id)
                if not os.path.isdir(dst_path):
                    os.makedirs(dst_path)
                cam_id = src_path.split('/')[-2].split('_')[-1]
                filename = src_path.split('/')[-1].split('_')
                filename = filename[0] + '_c{}_'.format(cam_id) + filename[1]
                copyfile(src_path, osp.join(dst_path, filename))
                print(filename)

    for id in split['test_probe']:
        for cam_list in meta['identities'][id]:
            for src_path in cam_list:
                src_path = os.path.join(data_root, src_path)
                dst_path = os.path.join(save_path, 'query', "%04d" % id)
                if not os.path.isdir(dst_path):
                    os.makedirs(dst_path)
                cam_id = src_path.split('/')[-2].split('_')[-1]
                filename = src_path.split('/')[-1].split('_')
                filename = filename[0] + '_c{}_'.format(cam_id) + filename[1]
                copyfile(src_path, osp.join(dst_path, filename))
                print(filename)
