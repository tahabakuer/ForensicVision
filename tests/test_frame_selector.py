from core.analysis.frame_selector import FrameSelector
from core.video.frame import Frame
import numpy as np


def test_select_best():

    frames = []

    for i in range(20):

        frame = Frame(
            image=np.zeros((10, 10, 3), dtype=np.uint8),
            index=i,
            timestamp=float(i),
        )

        frame.quality = float(i)

        frames.append(frame)

    best = FrameSelector().select_best(
        frames,
        count=5,
    )

    assert len(best) == 5
    assert best[0].quality == 19.0