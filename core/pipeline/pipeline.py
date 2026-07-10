from pathlib import Path

from core.video.video_loader import VideoLoader
from core.video.frame_extractor import FrameExtractor


class Pipeline:

    def __init__(self):

        self.output = Path("output/frames")

    def run(
        self,
        video_path: str,
        start: float,
        end: float
    ):

        video = VideoLoader(video_path)

        extractor = FrameExtractor(video)

        frames = extractor.extract_between(
            start,
            end
        )

        print(f"{len(frames)} frame bulundu.")

        extractor.save_frames(
            frames,
            self.output
        )

        video.release()