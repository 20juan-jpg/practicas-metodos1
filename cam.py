import cv2,time
cam = cv2.VideoCapture(0)

try:
	n = 0
	while True:
		n = n+1
		ret,frame = cam.read()
		img_name = "%s.png"%(n)
		cv2.imwrite(img_name, frame)


		print "foto capturada "
		time.sleep(10)

except KeyboardInterrupt:
    cam.release()
    print"detenido"
