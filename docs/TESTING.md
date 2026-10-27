# Manual tests

| # |  | Kết quả mong đợi | Đạt |
|---|---|---|---|
| 1 | Mở game | Hiện cửa sổ webcam, tỉ số `0 : 0`, dòng `Press SPACE to start` | ✅ |
| 2 | Đưa một tay vào, nắm tay lại (búa) | `Detected: ROCK`, `Fingers: 0/4` | ✅ |
| 3 | Xòe cả bàn tay (bao) | `Detected: PAPER`, `Fingers: 4/4` | ✅ |
| 4 | Giơ ngón trỏ và giữa (kéo) | `Detected: SCISSORS`, `Fingers: 2/4` | ✅ |
| 5 | Giơ cử chỉ khác (1 ngón, 3 ngón, trỏ + áp út) | `UNKNOWN`, không khóa cử chỉ | ✅ |
| 6 | Lật tay, mu bàn tay hướng về camera | Vẫn nhận đúng như test 2, 3, 4 | ✅ |
| 7 | Đưa cả hai tay vào khung hình, sau đó rút bớt một tay | Hai tay: `UNKNOWN / NO SINGLE HAND`, không khóa; còn một tay thì nhận lại bình thường | ✅ |
| 8 | Bấm SPACE, giữ sẵn một cử chỉ từ trước countdown | Hiện `Ready... 3, 2, 1`; hết countdown không khóa ngay, phải giữ đủ 0,5 giây | ✅ |
| 9 | Bấm SPACE giữa lúc đang đếm ngược hoặc đang giữ tay | Không bỏ qua lượt đang chơi | ✅ |
| 10 | Giữ một cử chỉ ổn định sau countdown | `HOLD ONE GESTURE` tăng tới 100%, hiện `LOCKED: ... vs ...` và kết quả; điểm chỉ cộng một lần, đổi tay sau đó không đổi kết quả | ✅ |
| 11 | Trong lúc giữ, đổi cử chỉ hoặc rút tay ra | `HOLD ONE GESTURE` về 0%, bắt đầu giữ lại từ đầu | ✅ |
| 12 | Chơi tới khi có bên đạt 5 điểm, sau đó bấm SPACE, R, rồi Q hoặc Esc | Hiện `MATCH WINNER`; SPACE không mở lượt mới; R xóa điểm về `0 : 0`; Q/Esc đóng cửa sổ và thoát; hòa không cộng điểm | ✅ |

## Kết quả chạy thử

- 12/12 manual tests pass.
- Chạy thực tế trên Windows với webcam laptop: MediaPipe nhận được bàn tay, game nhận diện được búa, bao, kéo, kể cả khi lật tay (mu bàn tay hướng về camera).