from pathlib import Path

import cv2

from core.video.video_loader import VideoLoader


class FrameExtractor:

    def __init__(self, video: VideoLoader):

        self.video = video

    def extract_between(
        self,
        start_second: float,
        end_second: float,
    ):

        return self.video.get_frames_between(
            start_second,
            end_second
        )

    def save_frames(
        self,
        frames,
        output_dir: Path
    ):

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        for i, frame in enumerate(frames):

            filename = output_dir / f"frame_{i:04}.png"

            cv2.imwrite(
                str(filename),
                frame
            )