import sys
import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation

def remove_background_video(video_path, color, size):
    segmentor = SelfiSegmentation()
    cap = cv2.VideoCapture(video_path)
    split = video_path.split('.')
    outputPath = split[0] + '_output.' + split[-1]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(outputPath, fourcc, 30, size)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        imgOriginal = cv2.resize(frame, size)
        imgBgRemoved = segmentor.removeBG(imgOriginal, color, cutThreshold=0.50)
        out.write(imgBgRemoved)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()

def read_args(len):
    color = (255, 255, 255)
    frame = (800, 600)
    if (len == 3):
        color = sys.argv[2]
    elif (len == 4):
        color = sys.argv[2]
        frame = sys.argv[3]
    return color, frame


def remove_background_image(image_path, color, size):
    segmentor = SelfiSegmentation()
    imgOriginal = cv2.imread(image_path)
    imgOriginal = cv2.resize(imgOriginal, size)
    imgBgRemoved = segmentor.removeBG(imgOriginal, color, cutThreshold=0.50)
    outputPath = image_path.split('.')[0] + '_output.jpg'
    cv2.imwrite(outputPath, imgBgRemoved)

def main():
    # read arguments from commandline
    args = sys.argv
    file_type = args[1].split('.')[-1]
    color, size = read_args(len(args))

    if (file_type == 'jpeg' or file_type=='jpg' or file_type=='png'):
        remove_background_image(args, color, size)
    elif (file_type == 'mp4' or file_type == 'avi' or file_type == 'mov') :
        remove_background_video(args, color, size)
    else:
        print("Invalid file type. Please provide a valid image or video file.")
        sys.exit(1)

if __name__ == "__main__":
    main()