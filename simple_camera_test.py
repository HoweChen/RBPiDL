import cv2


def real_time_video():
    window_name = 'Test'
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyWindow(window_name)
    cap.release()


if __name__ == '__main__':
    real_time_video()
