from pathlib import Path

from core.video.video_loader import VideoLoader
from core.video.frame_extractor import FrameExtractor


OUTPUT = Path("output/frames")


def main():

    video = VideoLoader("input/video.mp4")

    extractor = FrameExtractor(video)

    frames = extractor.extract_between(
        23,
        25
    )

    print(f"{len(frames)} frame bulundu.")

    extractor.save_frames(
        frames,
        OUTPUT
    )

    video.release()


if __name__ == "__main__":
    main()