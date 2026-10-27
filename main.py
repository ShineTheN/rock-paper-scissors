"""Chạy: python main.py --camera 0"""
import argparse
import time
import cv2
from rps.game import Game
from rps.gesture import classify
from rps.hand import HandTracker
from rps.view import draw


def main():
    parser = argparse.ArgumentParser(description='MediaPipe Rock Paper Scissors')
    parser.add_argument('--camera', type=int, default=0)
    args = parser.parse_args()
    camera = cv2.VideoCapture(args.camera)
    tracker = None
    try:
        if not camera.isOpened():
            raise RuntimeError('Cannot open camera. Try --camera 1 or check camera permissions.')
        tracker = HandTracker()
        game = Game()
        while True:
            ok, frame = camera.read()
            if not ok:
                raise RuntimeError('Camera disconnected or frame unavailable.')
            frame = cv2.flip(frame, 1)  # Hiển thị như gương.
            points, landmarks = tracker.read(frame, time.monotonic())
            now = time.monotonic()
            move, count = classify(points)
            game.update(move, now)
            cv2.imshow('Rock Paper Scissors', draw(frame, landmarks, game, move, count, now))
            key = cv2.waitKey(1) & 0xFF
            if key in (27, ord('q')) or cv2.getWindowProperty('Rock Paper Scissors', cv2.WND_PROP_VISIBLE) < 1:
                break
            if key == ord('r'):
                game = Game()
            elif key == 32:
                game.start(now)
    finally:
        camera.release()
        if tracker is not None:
            tracker.close()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
