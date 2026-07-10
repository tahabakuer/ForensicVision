from pathlib import Path

import cv2

from core.video.video_loader import VideoLoader


OUTPUT = Path("output/frames")


def main():

    OUTPUT.mkdir(
        parents=True,
        exist_ok=True
    )

    video = VideoLoader(
        "input/video.mp4"
    )

    frames = video.get_frames_between(
        23,
        25
    )

    print(f"{len(frames)} frame bulundu.")

    for i, frame in enumerate(frames):

        filename = OUTPUT / f"frame_{i:04}.png"

        cv2.imwrite(
            str(filename),
            frame
        )

    print("Frame'ler kaydedildi.")

    video.release()


if __name__ == "__main__":

    main()