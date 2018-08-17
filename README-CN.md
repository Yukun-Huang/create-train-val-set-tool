# create-train-val-set-tool

## 描述
将一个以pytorch ImageFolder格式存储的样本集划分为训练集和验证集。
对于每个类别，选择第一张图像作为验证集，其余的作为训练集。

pytorch ImageFolder格式示例如下：

        path-to-imageset/dog/xxx.png
        path-to-imageset/dog/xxy.png
        path-to-imageset/dog/xxz.png

        path-to-imageset/cat/123.png
        path-to-imageset/cat/nsdf3.png
        path-to-imageset/cat/asd932_.png

## 用法
python3 create_train_and_val_set.py -i path-to-imageset/
