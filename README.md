# Hand Gesture Recognition

This repository contains code for hand gesture mouse control and hand gesture volume control using Python. The project leverages Mediapipe for hand tracking, OpenCV for computer vision tasks, and other helpful libraries such as Pycaw, Pyautogui, Comtypes, and NumPy.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Hand Gesture Mouse Control](#hand-gesture-mouse-control)
  - [Hand Gesture Volume Control](#hand-gesture-volume-control)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Installation
Note : Earlier python installation is required (Python 3.7 or higher).

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/hand-gesture-recognition.git
    cd hand-gesture-recognition
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Hand Gesture Mouse Control

1. Navigate to the `mouse_control` directory:
    ```bash
    cd mouse_control
    ```

2. Run the mouse control script:
    ```bash
    python mouse_control.py
    ```

3. Use your hand gestures to control the mouse. The script uses Mediapipe to track your hand and translates gestures into mouse movements and clicks.

### Hand Gesture Volume Control

1. Navigate to the `volume_control` directory:
    ```bash
    cd volume_control
    ```

2. Run the volume control script:
    ```bash
    python volume_control.py
    ```

3. Use your hand gestures to control the volume. The script uses Mediapipe to track your hand and Pycaw to control the system's audio volume.

## Requirements

- Mediapipe
- OpenCV
- Pycaw
- Pyautogui
- Comtypes
- NumPy

You can install all required libraries using the `requirements.txt` file.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request


## Acknowledgements

- [Mediapipe](https://github.com/google/mediapipe)
- [OpenCV](https://github.com/opencv/opencv)
- [Pycaw](https://github.com/AndreMiras/pycaw)
- [Pyautogui](https://github.com/asweigart/pyautogui)
- [Comtypes](https://github.com/enthought/comtypes)
- [NumPy](https://github.com/numpy/numpy)

---

Developed by Nirmal Choudhary(https://github.com/nirmalchoudhary9)
