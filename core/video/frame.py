from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class Frame:
    """
    Represents a single frame extracted from a video.
    """

    image: np.ndarray

    index: int

    timestamp: float

    sharpness: float = 0.0

    brightness: float = 0.0

    contrast: float = 0.0

    quality: float = 0.0