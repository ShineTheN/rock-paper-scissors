"""OpenCV dùng chữ không dấu để tránh lỗi font mặc định."""
import math
import cv2
from rps.settings import COUNTDOWN, STABLE_TIME, TARGET_SCORE


def draw(frame, landmarks, game, move, count, now):
    height, width = frame.shape[:2]
    for p in landmarks:
        cv2.circle(frame, (int(p.x * width), int(p.y * height)), 4, (80, 255, 120), -1)
    # Panel cố định, không phụ thuộc độ phân giải webcam.
    frame = cv2.resize(frame, (960, 720))
    cv2.rectangle(frame, (0, 0), (960, 230), (25, 28, 38), -1)
    lines = [f'ROCK PAPER SCISSORS | First to {TARGET_SCORE}',
             f'YOU {game.player_score} : {game.computer_score} CPU',
             f'Detected: {move or "UNKNOWN / NO SINGLE HAND"} | Fingers: {count}/4']
    if game.phase == 'COUNTDOWN':
        lines.append(f'Ready... {max(1, math.ceil(COUNTDOWN - (now - game.started)))}')
    elif game.phase == 'CAPTURE':
        held = 0 if game.since is None else now - game.since
        lines.append(f'HOLD ONE GESTURE: {min(100, int(held / STABLE_TIME * 100))}%')
    elif game.phase in ('RESULT', 'FINISHED'):
        label = {1: 'YOU WIN', 0: 'DRAW', -1: 'CPU WINS'}[game.result]
        lines.append(f'LOCKED: {game.player} vs {game.computer} | {label}')
    else:
        lines.append('Press SPACE to start')
    if game.phase == 'FINISHED':
        champion = 'YOU' if game.player_score >= TARGET_SCORE else 'CPU'
        lines.append(f'MATCH WINNER: {champion} | R: new match')
    else:
        lines.append('SPACE: next round | R: reset | Q / ESC: quit')
    for i, text in enumerate(lines):
        cv2.putText(frame, text, (20, 35 + 40*i), cv2.FONT_HERSHEY_SIMPLEX,
                    0.65, (240, 245, 255), 2, cv2.LINE_AA)
    return frame
