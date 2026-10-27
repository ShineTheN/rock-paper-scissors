"""Logic độc lập camera: dễ đọc và kiểm thử bằng thời gian giả."""
import random
from rps.settings import COUNTDOWN, STABLE_TIME, MAX_FRAME_GAP, TARGET_SCORE, MOVES


def winner(player, computer):
    """1: người thắng; 0: hòa; -1: máy thắng."""
    if player not in MOVES or computer not in MOVES:
        raise ValueError('Invalid move')
    if player == computer:
        return 0
    return 1 if (player, computer) in (
        ('ROCK', 'SCISSORS'), ('SCISSORS', 'PAPER'), ('PAPER', 'ROCK')
    ) else -1


class Game:
    def __init__(self, choose=random.choice):
        self.choose = choose  # Có thể thay máy chọn ngẫu nhiên bằng lựa chọn cố định trong test.
        self.player_score = self.computer_score = 0
        self.phase = 'READY'
        self.player = self.computer = self.result = None
        self.candidate = None
        self.since = self.last_frame = None
        self.started = 0

    def start(self, now):
        if self.phase not in ('READY', 'RESULT'):
            return
        self.phase = 'COUNTDOWN'
        self.started = now
        self.player = self.result = self.candidate = None
        self.since = self.last_frame = None
        # Máy chọn TRƯỚC khi người chơi ra tay; giao diện giấu đến lúc khóa.
        self.computer = self.choose(MOVES)

    def update(self, move, now):
        if self.phase == 'COUNTDOWN':
            if now - self.started < COUNTDOWN:
                return
            self.phase = 'CAPTURE'
        if self.phase != 'CAPTURE':
            return  # Kết quả đã khóa: không cộng điểm thêm.
        gap = self.last_frame is not None and now - self.last_frame > MAX_FRAME_GAP
        self.last_frame = now
        if move not in MOVES:
            self.candidate = self.since = None
            return
        if gap or move != self.candidate:
            self.candidate, self.since = move, now
        if now - self.since < STABLE_TIME:
            return
        self.player = move
        self.result = winner(move, self.computer)
        self.player_score += self.result == 1
        self.computer_score += self.result == -1
        self.phase = 'FINISHED' if max(self.player_score, self.computer_score) >= TARGET_SCORE else 'RESULT'
