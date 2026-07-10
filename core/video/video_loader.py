from pathlib import Path

import cv2


class VideoLoader:

    def __init__(self, video_path: str):

        self.path = Path(video_path)

        if not self.path.exists():
            raise FileNotFoundError(
                f"Video bulunamadı:\n{self.path.resolve()}"
            )

        self.cap = cv2.VideoCapture(str(self.path))

        if not self.cap.isOpened():
            raise RuntimeError("Video açılamadı.")

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.duration = self.frame_count / self.fps

    def info(self):

        return {
            "fps": self.fps,
            "frames": self.frame_count,
            "width": self.width,
            "height": self.height,
            "duration": self.duration,
        }

    def get_frame_at(self, second: float):

        frame_number = int(second * self.fps)

        if frame_number >= self.frame_count:
            return None

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def get_frames_between(self, start_second: float, end_second: float):

        start_frame = int(start_second * self.fps)
        end_frame = int(end_second * self.fps)

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        frames = []

        while self.cap.get(cv2.CAP_PROP_POS_FRAMES) <= end_frame:

            success, frame = self.cap.read()

            if not success:
                break

            frames.append(frame)

        return frames

    def release(self):

        self.cap.release()