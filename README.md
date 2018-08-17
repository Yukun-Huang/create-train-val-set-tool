# create-train-val-set-tool
Split image samples ( pytorch's ImageFolder format ) to train set and val set.

## description
Input the path to the image set， this script will create a train set and val set.
Images in the original set should be arranged in this way:

        path-to-imageset/dog/xxx.png
        path-to-imageset/dog/xxy.png
        path-to-imageset/dog/xxz.png

        path-to-imageset/cat/123.png
        path-to-imageset/cat/nsdf3.png
        path-to-imageset/cat/asd932_.png

Exactly the same as pytorch's ImageFolder format.
For each class, the first image chosed as a val sample, the others are train samples.

## usage
python3 create_train_and_val_set.py -i path-to-imageset/
