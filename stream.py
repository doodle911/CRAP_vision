import cv2
import os
import time
import numpy as np
import pyvirtualcam
from pyvirtualcam import PixelFormat

from cropBoard import ExtractAndStraightenFromImage  # Adjusted module name

# Set default camera ID and FPS
CAMERA_ID = 0
FPS_OUT = 20

def main():
    # Start the video capture
    vid = cv2.VideoCapture(CAMERA_ID)

    if not vid.isOpened():
        raise RuntimeError('Could not open video source')

    # Query final capture device values (may be different from preferred settings).
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f'Webcam capture started ({width}x{height} @ {vid.get(cv2.CAP_PROP_FPS)}fps)')

    with pyvirtualcam.Camera(width, height, FPS_OUT, fmt=PixelFormat.BGR) as cam:
        print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')

        rotated = False  # Rotation state

        try:
            while True:
                ret, frame = vid.read()
                if not ret:
                    print("Failed to grab frame")
                    break

                # Apply the image processing function
                boardImg = ExtractAndStraightenFromImage(frame)

                key = cv2.waitKey(1) & 0xFF

                if key == ord('r'):
                    rotated = not rotated  # Toggle rotation state

                if rotated:
                    width = height
                    height = width
                    boardImg = cv2.rotate(boardImg, cv2.ROTATE_180)
                    
                # Display the processed frame
                cv2.imshow("Processed Frame", boardImg)
                cv2.imshow('Original Frame', frame)

                # Send to virtual cam
                cam.send(boardImg)
                cam.sleep_until_next_frame()

                if key == ord('q'):  # Quit if 'q' is pressed
                    break
        finally:
            vid.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



