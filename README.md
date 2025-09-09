
# Number Counter-YouTube Shorts Stream

**Realtime number counter with visual display and text-to-speech audio for YouTube Shorts live streams.**

---

## 📌 Overview

NumberCounter-YTStream is a Python-based tool that generates real-time number counters with visual formatting and text-to-speech narration. It's designed for YouTube Shorts creators, streamers, and educators who want to display and audibly announce numbers in a dynamic and engaging way.

---

## 🎯 Features

* **Real-time number display**: Shows numbers with comma formatting and optional background image.
* **Text-to-speech narration**: Converts numbers into words and reads them aloud using TTS technology.
* **Customizable fonts and styles**: Supports custom fonts and sizes for both numbers and text.
* **Easy integration**: Outputs frames compatible with OBS Studio for seamless streaming.

---

## ⚙️ Requirements

* Python 3.8+
* Required libraries:

  * `opencv-python`
  * `numpy`
  * `Pillow`
  * `num2words`
  * `kokoro` (for TTS functionality)

  Install dependencies using:

  ```bash
  pip install -r requirements.txt
  ```

---

## 🚀 Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/NeuralFalconYT/NumberCounter-YTStream.git
   cd NumberCounter-YTStream
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python obs.py
   ```

   This will start the number counter, displaying the current number and announcing it aloud.

---

## 🎥 OBS Studio Setup

To stream your counter to YouTube:

1. Open **OBS Studio**.
2. **Add a new source**:

   * Choose **Window Capture** → Select `[python.exe]` window showing the counter image.
   * **⚠️ Warning:** Do **not minimize** the Python window, otherwise OBS will not capture it.
   * Add **Audio Input Capture** → Choose `Stereo Mix (Realtek(R) Audio)` to capture system audio and Set volume to -35.
3. Grab your **YouTube Stream API key** and start the stream.
4. The OBS scene will now show your live number counter with TTS audio directly on your YouTube Shorts live stream.

---

## 🧪 Testing

To test the number counter and TTS functionality:

* **Visual Test**: Run `test_image.py` to generate a sample image with the number displayed.
* **TTS Test**: Run `test_tts.py` to test the text-to-speech output.


## Demo


https://github.com/user-attachments/assets/b418fd7a-0a1b-4915-9f11-f074018d86d7



