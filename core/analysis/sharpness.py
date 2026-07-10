import cv2
import numpy as np


class SharpnessAnalyzer:
    """
    Calculates image sharpness using the variance
    of the Laplacian.
    """

    @staticmethod
    def score(frame: np.ndarray) -> float:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Laplacian(
            gray,
            cv2.CV_64F
        ).var()