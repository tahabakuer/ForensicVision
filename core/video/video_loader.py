from pathlib import Path

import cv2


class VideoLoader:

    def __init__(self, video_path: str):

        self.path = Path(video_path)

        if not self.path.exists():
            raise FileNotFoundError(self.path)

        self.cap = cv2.VideoCapture(str(self.path))

        if not self.cap.isOpened():
            raise RuntimeError("Video açılamadı.")

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        self.frame_count = int(
            self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        self.width = int(
            self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

        self.height = int(
            self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        self.duration = self.frame_count / self.fps

    def info(self):

        return {
            "fps": self.fps,
            "frames": self.frame_count,
            "width": self.width,
            "height": self.height,
            "duration": self.duration
        }

    def release(self):

        self.cap.release()