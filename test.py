import detect
import train_patch
import test_patch

#imgfile = "persons\person_001.jpg"
#detect.main("cfg/yolov2.cfg", "weights/yolo.weights", imgfile)

test_patch.main("saved_patches/patchperson1.png", "data")