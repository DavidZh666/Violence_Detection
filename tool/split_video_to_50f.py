import cv2

#将拍摄的视频片段随机裁剪成50帧一段，用于训练模型

def save_video(path,n):
  #path是视频地址，n定义的起始文件名称 
	cap = cv2.VideoCapture(path)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter("output_"+str(n)+'.avi', fourcc, 15.0, (1920, 1080))
		# out=cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
	i = 0
	number=n+1
	while (cap.isOpened):
		if i==50:
			i=0
			fourcc = cv2.VideoWriter_fourcc(*'XVID')
			out = cv2.VideoWriter("/media/daves/Seagate/datasets/ourdatas/Train3/fight/video/output_"+str(number)+'.avi', fourcc, 24.0, (1920, 1080))
			number += 1

		ret, frame = cap.read()
		i+=1
		if ret == True:
			frame = cv2.resize(frame,(1920, 1080))  ##flip image
			out.write(frame)
			# cv2.imshow('frame', frame)
			if cv2.waitKey(1) & 0xff == ord('q'):
				break
		else:
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()

if __name__=="__main__":
	save_video('/media/daves/Seagate/datasets/ourdatas/Train3/fight/1.mp4',4000)
	save_video('/media/daves/Seagate/datasets/ourdatas/Train3/fight/2.mp4',4240)
	save_video('/media/daves/Seagate/datasets/ourdatas/Train3/fight/3.mp4',4027)
	save_video('/media/daves/Seagate/datasets/ourdatas/Train3/fight/4.mp4',4070)
	save_video('/media/daves/Seagate/datasets/ourdatas/Train3/fight/5.mp4', 4110)
	save_video('/media/daves/Seagate/datasets/ourdatas/Train3/fight/6.mp4', 4150)
	save_video('/media/daves/Seagate/datasets/ourdatas/Train3/fight/7.mp4', 4200)


