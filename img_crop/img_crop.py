import cv2
import glob


def main():
    imgs = glob.glob(r'your_dir\*.png')

    for i, img in enumerate(imgs):
        img_org = cv2.imread(img)
        img_crop = img_org[318:919, 358:1559, :]
        cv2.imwrite("img_crop" + str(i + 1) + ".png", img_crop)


if __name__ == '__main__':
    main()
