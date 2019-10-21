import numpy as np
import cv2

inAreas=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]

def xValue(gray,row,col):
    list=[]
    for i in range(8):
        list.append(abs(gray[row+inAreas[i][0]][col+inAreas[i][1]]-gray[row][col]))

    list.append(0)
    new_list=sorted(list)
    return new_list[4]

class ALMD:
    def __init__(self):
        self.map=np.array([[8.0,4.0,2.0],[16.0,0.0,1.0],[32.0,64.0,128.0]])
        # self.map=np.array([[8,4,2],[16,0,1],[32,64,128]])

    def calculate(self,gray_before,gray_next,height,width):
        upper_pattern = np.zeros((height, width),dtype=np.float64)
        lower_pattern = np.zeros((height, width),dtype=np.float64)
        gray_before = np.pad(np.float64(gray_before),1,mode='edge')
        gray_next = np.pad(np.float64(gray_next),1,mode='edge')

        # gray_before = expandPicture(gray_before, height, width)
        # gray_next = expandPicture(gray_next, height, width)

        for row in range(1,height+1):
            for col in range(1,width+1):

                before=gray_before[row - 1:row + 2,col-1:col+2] - gray_before[row][col]
                next=gray_next[row - 1:row + 2,col-1:col+2] - gray_next[row][col]
                # xb=np.median(np.fabs(before))
                # xn=np.median(np.fabs(next))
                xn = xValue(gray_before, row, col)
                xb = xValue(gray_next, row, col)
                x_mean=(xn+xb)/2.0

                upper = np.multiply((before >= x_mean) ^ (next >= x_mean), self.map)
                upper_value = np.sum(upper)
                upper_pattern[row - 1][col - 1] = upper_value

                lower = np.multiply((before<=x_mean)^(next<=x_mean),self.map)
                lower_value=np.sum(lower)
                lower_pattern[row - 1][col - 1] = lower_value

        return (upper_pattern,lower_pattern)
