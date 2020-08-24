import cv2
path = r"frame_at_6.jpg"
img = cv2.imread(path)
img[:, :, :] =