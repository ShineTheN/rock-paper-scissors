"""Các hằng số để dễ điều chỉnh game."""
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / 'models/hand_landmarker.task'
COUNTDOWN = 3.0
STABLE_TIME = 0.5
MAX_FRAME_GAP = 0.25  # Gián đoạn lâu: bắt đầu giữ tay lại từ đầu.
TARGET_SCORE = 5
CURL_RATIO = 0.9    # Tỉ lệ đầu ngón/PIP so với cổ tay <= giá trị này: co hẳn.
OPEN_RATIO = 1.25   # >= giá trị này: duỗi hẳn.
EXTEND_THRESHOLD = 0.5  # Điểm duỗi > giá trị này: tính là ngón duỗi.
MOVES = ('ROCK', 'PAPER', 'SCISSORS')