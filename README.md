# 💪 Bicep Curl Counter with OpenCV + MediaPipe

Track your workouts in real-time with this **AI-powered bicep curl counter**! Using your webcam, this Python app detects your movements, counts reps for **both arms**, and gives you instant visual feedback — all thanks to the power of [MediaPipe](https://mediapipe.dev/) and [OpenCV](https://opencv.org/).

---

## 🚀 Features

- 🎥 **Live Pose Tracking**  
  Real-time body landmark detection via webcam.

- 🔄 **Dual-Arm Rep Counter**  
  Tracks and counts left and right arm curls **independently**.

- 📊 **Visual Feedback Overlay**  
  Displays elbow angles, current rep stage (⬆️ up / ⬇️ down), and total reps per arm — right on the video feed.

- 🔁 **Easy Reset**  
  Press `r` to restart your rep counts anytime.

---

## ⚙️ Requirements

- Python 3.7 or above  
- [OpenCV](https://pypi.org/project/opencv-python/)  
- [MediaPipe](https://pypi.org/project/mediapipe/)  
- [NumPy](https://pypi.org/project/numpy/)

---

## 🛠️ Installation

Install the required packages via pip:

```bash
pip install opencv-python mediapipe numpy
```

---

## ▶️ How to Use

1. Save the script (e.g., `bicep_curl_counter.py`).
2. Run the program:

   ```bash
   python bicep_curl_counter.py
   ```

3. Grant webcam access when prompted.
4. Perform your bicep curls in front of the camera.
5. Watch your **rep count and stage updates live**!
6. Press:
   - `q` to quit
   - `r` to reset the counters

---

## 🧠 How It Works

- Uses **MediaPipe Pose** to detect key landmarks: **shoulder**, **elbow**, and **wrist**.
- Calculates the **angle at your elbow** using vector math.
- Classifies the motion as **"up"** or **"down"** based on angle thresholds (e.g., < 30° = up, > 160° = down).
- When a full range of motion is detected, it **counts one repetition**.
- Everything is visualized live with overlays using **OpenCV**.

---

## 🎮 Controls

| Key | Action                |
|-----|-----------------------|
| `q` | Quit the application  |
| `r` | Reset repetition count |

---

## 📝 Code Highlights

- `calculate_angle(a, b, c)`  
  → Computes the joint angle at point `b` given three 2D/3D coordinates.

- **Main Loop**  
  → Captures webcam frames, applies pose estimation, updates rep counts, and renders visuals in real time.

---

## 📌 Tips

- Use in a **well-lit area** for best tracking.
- Position your body clearly in front of the camera.
- Can be adapted for other exercises (e.g., squats, shoulder press) with minor modifications.

---

## 📚 References

- [MediaPipe Pose Documentation](https://google.github.io/mediapipe/solutions/pose.html)  
- [OpenCV Docs](https://docs.opencv.org/)

---

**Author**: JulesDimanche  
**License**: MIT  
**Project Type**: Computer Vision, Fitness AI, Python
