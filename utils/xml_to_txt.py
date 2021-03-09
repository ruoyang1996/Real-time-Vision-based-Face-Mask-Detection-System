# -*- coding: utf-8 -*-
# @Author  : argus
# @File    : make_train_val_test_set.py
# @Software: PyCharm

import os
import random


def _main():
    xmlfilepath = "/home/haolin/2DDETECTION/YOLOv4-Ruoyang/dataset/val/Annotations/"
    total_xml = os.listdir(xmlfilepath)

    num = len(total_xml)
    list = range(num)

    ftrainval = open(
        "/home/haolin/2DDETECTION/YOLOv4-Ruoyang/dataset/val/val.txt",
        "w",
    )

    for i in list:
        name = total_xml[i][:-4] + "\n"
        ftrainval.write(name)

    print('finish!')
    ftrainval.close()


if __name__ == "__main__":
    _main()
