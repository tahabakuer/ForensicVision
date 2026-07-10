from core.video.frame import Frame


class FrameSelector:

    def select_best(
        self,
        frames: list[Frame],
        count: int = 10,
    ) -> list[Frame]:

        return sorted(
            frames,
            key=lambda f: f.quality,
            reverse=True,
        )[:count]