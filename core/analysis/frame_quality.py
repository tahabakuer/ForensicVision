from __future__ import annotations

import cv2

from core.video.frame import Frame


class FrameQualityAnalyzer:
    """
    Calculates quality metrics for a frame.
    """

    def analyze(self, frame: Frame) -> Frame:

        gray = cv2.cvtColor(
            frame.image,
            cv2.COLOR_BGR2GRAY,
        )

        frame.sharpness = float(
            cv2.Laplacian(
                gray,
                cv2.CV_64F,
            ).var()
        )

        frame.brightness = float(
            gray.mean()
        )

        frame.contrast = float(
            gray.std()
        )

        frame.quality = (
            frame.sharpness * 0.65 +
            frame.contrast * 0.25 +
            frame.brightness * 0.10
        )

        return frame