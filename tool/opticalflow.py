# coding: utf-8

import numpy as np
import cv2
import time
import matplotlib.pyplot as plt
import scipy.misc
import os,sys
from PIL import Image
def ToImg(raw_flow,bound):
	'''
	this function scale the input pixels to 0-255 with bi-bound

	:param raw_flow: input raw pixel value (not in 0-255)
	:param bound: upper and lower bound (-bound, bound)
	:return: pixel value scale from 0 to 255
	'''
	flow=raw_flow
	flow[flow>bound]=bound
	flow[flow<-bound]=-bound
	flow-=-bound
	flow*=(255/float(2*bound))
	ppicture= Image.fromarray(flow)
	return ppicture

def flow2img(flow, BGR=True):
	x, y = flow[..., 0], flow[..., 1]
	hsv = np.zeros((flow.shape[0], flow.shape[1], 3), dtype = np.uint8)
	ma, an = cv2.cartToPolar(x, y, angleInDegrees=True)
	hsv[..., 0] = (an / 2).astype(np.uint8)
	hsv[..., 1] = (cv2.normalize(ma, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)).astype(np.uint8)
	hsv[..., 2] = 255
	if BGR:
		img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	else:
		img = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
	return img

startT = time.clock()
im1 = cv2.imread("/home/wuwei/datasets/jpegs_256_1_2/v_ApplyEyeMakeup_g01_c01/frame000006.jpg")
im2 = cv2.imread("/home/wuwei/datasets/jpegs_256_1_2/v_ApplyEyeMakeup_g01_c01/frame000007.jpg")
gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# methods = ["Farneback_x","Farneback_y", "SpareToDense PyrLK", "Dual TV-L1",
# 	"DIS Flow", "Simple Flow", "PCA Flow",
# 	"Deep Flow"]
methods=["Farneback_x","Farneback_y","flowSTD_x","flowSTD_y","flowDTVL1_x","flowDTVL1_y","flowSF_x","flowSF_y"]
flows = list()
####dense flow
##paper:Two-Frame Motion Estimation Based on PolynomialExpansion
flowFB = cv2.calcOpticalFlowFarneback(gray1, gray2, None, 0.6, 3, 25, 7, 5, 1.2, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
#flows.append(flow2img(flowFB, False))
flowFB_x=ToImg(flowFB[...,0],15)
flows.append(flowFB_x)
flowFB_y=ToImg(flowFB[...,1],15)
flows.append(flowFB_y)

flowSTD = cv2.optflow.calcOpticalFlowSparseToDense(gray1, gray2, grid_step=5, sigma=0.5)
#flows.append(flow2img(flowSTD, False))
flowSTD_x=ToImg(flowSTD[...,0],15)
flows.append(flowSTD_x)
flowSTD_y=ToImg(flowSTD[...,1],15)
flows.append(flowSTD_y)

dtvl1 = cv2.createOptFlow_DualTVL1()
flowDTVL1 = dtvl1.calc(gray1, gray2, None)
#flows.append(flow2img(flowDTVL1, False))
flowDTVL1_x=ToImg(flowDTVL1[...,0],15)
flows.append(flowDTVL1_x)
flowDTVL1_y=ToImg(flowDTVL1[...,1],15)
flows.append(flowDTVL1_y)
# dis = cv2.optflow.createOptFlow_DIS()
# flowDIS = dis.calc(gray1, gray2, None)
# flows.append(flow2img(flowDIS, False))

##dense flow
##SimpleFlow: A Non-iterative, Sublinear Optical FlowAlgorithm 2012
flowSF = cv2.optflow.calcOpticalFlowSF(im1, im2, 3, 5, 5)
# flows.append(flow2img(flowSF, False)
flowSF_x=ToImg(flowSF[...,0],15)
flows.append(flowSF_x)
flowSF_y=ToImg(flowSF[...,1],15)
flows.append(flowSF_y)
# pcaF = cv2.optflow.createOptFlow_PCAFlow()
# flowPCA = pcaF.calc(gray1, gray2, None)
# flows.append(flow2img(flowPCA, False))

startT = time.clock()
deepF = cv2.optflow.createOptFlow_DeepFlow()
flowDeep = deepF.calc(gray1, gray2, None)
flows.append(flow2img(flowDeep, False))
endT = time.clock()

print(endT - startT, "s")
cv2.optflow.writeOpticalFlow("dp.flo", flowDeep)

fig, axes = plt.subplots((len(flows) + 2) // 4, 4)
for i in range(axes.size):
	ax = axes.item(i)
	if (i < len(flows)):
		ax.imshow(flows[i])
		ax.set_title(methods[i])
	ax.axis("off")

plt.show()
