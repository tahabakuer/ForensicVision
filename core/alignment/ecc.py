import cv2

from core.video.frame import Frame


class ECCAligner:

    def align(
        self,
        reference: Frame,
        target: Frame,
    ) -> Frame:

        reference_gray = cv2.cvtColor(
            reference.image,
            cv2.COLOR_BGR2GRAY,
        )

        target_gray = cv2.cvtColor(
            target.image,
            cv2.COLOR_BGR2GRAY,
        )

        warp = cv2.Mat.eye(2, 3, cv2.CV_32F)