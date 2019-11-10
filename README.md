#### Violence_Detection
## 这是一个暴力算法的项目
### tool文件介绍
这里提供了几个py文件，主要作用为
+ opticalflow.py 提供了opencv中计算光流的几种方式
+ split_video_to_50f.py 提供了将拍摄的数据集进行裁剪成为50帧为一个小视频
+ videolabel.py 提供了给视频片段进行打上标签的一个小工具
+ split_train_test_val.py 提供了划分训练测试验证集的程序
### method文件介绍
这里提供一些小算法
+ chose_key_pic.py 是用于选择关键帧的算法，后续会上传
+ almd.py是复现论文中human action recognition using adaptive local motion descriptor in Sparks.的方法，计算almd运动图像特征。
### ourdatasets文件介绍
这是是我们拍摄的数据集（我们称之为 real violence datasets，RV datastes），现在只提供了划分的训练集和测试集以及验证集的结果，后续会通过某种方式公开。


#### 最终视频展示
 [![Watch the video](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](https://www.bilibili.com/video/av66943237/)
