import sys
import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation


def remove_background_video(video_path):
    segmentor = SelfiSegmentation()
    cap = cv2.VideoCapture(video_path)
    split = video_path.split('.')
    outputPath = split[0] + '_output.' + split[-1]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(outputPath, fourcc, 30, (800, 600))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        imgOriginal = cv2.resize(frame, (800, 600))
        white = (255, 255, 255)
        imgBgRemoved = segmentor.removeBG(imgOriginal, white, cutThreshold=0.50)
        out.write(imgBgRemoved)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()



def remove_background_image(image_path):
    segmentor = SelfiSegmentation()
    imgOriginal = cv2.imread(image_path)
    imgOriginal = cv2.resize(imgOriginal, (800, 600))
    white = (255, 255, 255)
    imgBgRemoved = segmentor.removeBG(imgOriginal, white, cutThreshold=0.50)
    outputPath = image_path.split('.')[0] + '_output.jpg'
    cv2.imwrite(outputPath, imgBgRemoved)

def main():
    # read arguments from commandline
    args = sys.argv[1]
    file_type = args.split('.')[-1]
    if (file_type == 'jpeg' or file_type=='jpg' or file_type=='png'):
        remove_background_image(args)
    elif (file_type == 'mp4' or file_type == 'avi' or file_type == 'mov') :
        remove_background_video(args)

if __name__ == "__main__":
    main()