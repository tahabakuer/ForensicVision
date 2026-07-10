from core.video.frame import Frame


class ReferenceFrameSelector:
    """
    Selects the highest-quality frame to be used as
    the alignment reference.
    """

    def select(self, frames: list[Frame]) -> Frame:

        if not frames:
            raise ValueError("Frame listesi boş.")

        return max(
            frames,
            key=lambda frame: frame.quality,
        )