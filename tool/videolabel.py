import cv2
import os
import shutil
from tqdm import tqdm


## 按小写字母d是保存为非暴力视频文件夹
## 按小写字母a是保存为暴力视频文件夹
## 其他按键不保存该视频片段


def label():
    video_path="/media/daves/Seagate/datasets/ourdatas/no3"
    dst_fight_path="/media/daves/Seagate/datasets/ourdatas/test"
    dst_no_path=""
    for video_name in tqdm(os.listdir(video_path)):
        abs_video_path=os.path.join(video_path,video_name)
        cap = cv2.VideoCapture(abs_video_path)
        ret, frame = cap.read()
        while ret :
            gray=cv2.resize(frame,(480,270)) ##to gray
            cv2.imshow(video_name, gray)
            cv2.waitKey(5)
            ret,frame = cap.read()   ##ret =True or false
        keycode=cv2.waitKey(0)
        if keycode==100:
            shutil.copyfile(abs_video_path,os.path.join(dst_fight_path,video_name))
        elif keycode==97:
            shutil.copyfile(abs_video_path, os.path.join(dst_no_path, video_name))
        else:
            pass
        cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    label()
