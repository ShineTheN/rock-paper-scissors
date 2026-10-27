"""Chỉ lấy landmarks từ MediaPipe; không quyết định thắng/thua."""
import cv2
import mediapipe as mp
from rps.settings import MODEL_PATH


class HandTracker:
    def __init__(self):
        if not MODEL_PATH.is_file():
            raise FileNotFoundError(f'Missing model: {MODEL_PATH}')
        options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(model_asset_path=str(MODEL_PATH)),
            running_mode=mp.tasks.vision.RunningMode.VIDEO,
            num_hands=2,  # Phát hiện 2 tay để yêu cầu chỉ đưa 1 tay vào khung hình.
        )
        self.detector = mp.tasks.vision.HandLandmarker.create_from_options(options)
        self.timestamp = -1

    def read(self, frame, now):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        self.timestamp = max(self.timestamp + 1, int(now * 1000))
        result = self.detector.detect_for_video(image, self.timestamp)
        if len(result.hand_landmarks) != 1:
            return [], []
        points = [(p.x, p.y, p.z) for p in result.hand_world_landmarks[0]]
        return points, result.hand_landmarks[0]

    def close(self):
        self.detector.close()
