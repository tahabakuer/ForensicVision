from pathlib import Path

import cv2

from core.video.frame import Frame
from core.video.video_loader import VideoLoader


class FrameExtractor:

    def __init__(self, video: VideoLoader):
        self.video = video

    def extract_between(
        self,
        start_second: float,
        end_second: float,
    ) -> list[Frame]:

        start_frame = int(start_second * self.video.fps)
        end_frame = int(end_second * self.video.fps)

        self.video.cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            start_frame,
        )

        frames = []

        current = start_frame

        while current <= end_frame:

            success, image = self.video.cap.read()

            if not success:
                break

            timestamp = current / self.video.fps

            frames.append(
                Frame(
                    image=image,
                    index=current,
                    timestamp=timestamp,
                )
            )

            current += 1

        return frames

    def save_frames(
        self,
        frames: list[Frame],
        output_dir: Path,
    ):

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        for frame in frames:

            filename = output_dir / f"frame_{frame.index:05}.png"

            cv2.imwrite(
                str(filename),
                frame.image,
            )