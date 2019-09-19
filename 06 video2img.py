#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-09-19 09:05:06
# @Author  : xchaoinfo (github.com/xchaoinfo)

import os
import cv2


def video2img(videoFile, outFolder="img_from_video"):
    if not os.path.exists(outFolder):
        os.mkdir(outFolder)

    vc = cv2.VideoCapture(videoFile)
    num = 0
    while True:
        flag, data = vc.read()
        if not flag:
            break
        imgFileName = os.path.join(outFolder, "%s-%s.jpg" % (videoFile, num))
        cv2.imwrite(imgFileName, data)
        num += 1


if __name__ == '__main__':
    videoFile = "demo.mp4"
    outFolder = "img_from_video"
    video2img(videoFile, outFolder)


