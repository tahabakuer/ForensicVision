from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class AppConfig:
    input_video: Path = Path("input/video.mp4")

    output_dir: Path = Path("output")

    frame_output_dir: Path = Path("output/frames")

    best_frame_dir: Path = Path("output/best_frames")

    start_second: float = 23.0

    end_second: float = 25.0

    best_frame_count: int = 10