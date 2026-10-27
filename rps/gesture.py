"""Thuật toán tự viết, không dùng bộ nhận dạng cử chỉ có sẵn.

Mỗi ngón (trỏ, giữa, áp út, út) được đo bằng tỉ lệ khoảng cách:
    đầu ngón -> cổ tay  /  khớp PIP -> cổ tay
Ngón duỗi thì đầu ngón xa cổ tay hơn khớp PIP (tỉ lệ > 1), ngón co thì đầu ngón
cuộn về phía lòng bàn tay (tỉ lệ < 1). Tỉ lệ này không phụ thuộc kích thước tay,
hướng xoay, lật gương và hầu như không phụ thuộc mặt tay (lòng hay mu bàn tay),
vì chỉ dùng tọa độ x, y, không dùng độ sâu z vốn nhiễu.
"""
from math import hypot
from rps.settings import CURL_RATIO, OPEN_RATIO, EXTEND_THRESHOLD


def distance(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def finger_score(wrist, pip, tip):
    """Điểm duỗi 0..1 (0 = co hẳn, 1 = duỗi hẳn)."""
    base = distance(wrist, pip)
    if base < 1e-9:
        return 0.0  # Điểm trùng nhau không được coi là duỗi.
    ratio = distance(wrist, tip) / base
    score = (ratio - CURL_RATIO) / (OPEN_RATIO - CURL_RATIO)
    return max(0.0, min(1.0, score))


def classify(points):
    """Trả về (cử chỉ, số ngón duỗi). Chỉ đếm 4 ngón, bỏ ngón cái."""
    if len(points) != 21:
        return None, 0
    wrist = points[0]
    fingers = [finger_score(wrist, points[base + 1], points[base + 3]) > EXTEND_THRESHOLD
               for base in (5, 9, 13, 17)]  # Trỏ, giữa, áp út, út.
    count = sum(fingers)
    if count == 0:
        return 'ROCK', count
    if count == 4:
        return 'PAPER', count
    if fingers == [True, True, False, False]:
        return 'SCISSORS', count
    return None, count  # Không phải cứ 2 ngón bất kỳ là kéo.