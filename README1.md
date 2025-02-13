# CubeOCR
<a id="readme-top"></a>

[![OCR-tech github](https://img.shields.io/badge/GitHub-ocrtech-th.svg?style=flat&logo=github)](https://github.com/OCR-tech)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Package Control month downloads](https://img.shields.io/packagecontrol/dm/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)
[![Package Control total downloads](https://img.shields.io/packagecontrol/dt/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)

**CubeOCR** is a tool designed to extract text from images and scanned documents.
- Simple & easy-to-use OCR tool for extracting any text on screen
- Integrated built-in text editor with transparent background
- Advanced image processing with noise filtering features
- Suitable for side-by-side paragraphs and code editing
- Offline use for confidential & sensitive personal data
- Support more than 107 different languages

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

**CubeOCR** project is a Python-based screenshot OCR tool designed to extract text from images and scanned documents. Simply select the text area, perform OCR, and be ready to paste it anywhere.

### Features:
- Fast and accurate text recognition
- Instant and side-by-side integrated text editor
- Transparent background feature for built-in toolbar
- Easily copy & paste to other applications
- Activate OCR screen with hotkeys

## Installation

### Prerequisites:
- Visual Studio Code (1.96.4 or newer) - Download [Visual Studio Code](https://code.visualstudio.com/)
- Tesseract-OCR (5.5.0 or newer) - Download [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- Python (3.11 or newer)
- Python packages: `numpy`, `opencv-python`, `pynput`, `pyautogui`, `PyQt5`, `qtpy`, `pytesseract`, `pywin32`, `openpyxl`, `pandas`

### Steps to Install:
1. Clone this repository:
    ```sh
    git clone https://github.com/OCR-tech/CubeOCR
    ```
2. Go into the project directory:
    ```sh
    cd CubeOCR
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the project:
    ```sh
    python main.py
    ```

### Screenshots:

<div align="center">
  <a href="https://github.com/OCR-tech/CubeOCR/blob/main/image/screen1.gif">
    <img src="image/screen1.gif" alt="screen">
  </a>  
</div>

<div align="center">
  <a href="https://github.com/OCR-tech/CubeOCR/blob/main/image/screen2.gif">
    <img src="image/screen2.gif" alt="screen">
  </a>  
</div>

<p align="center"> <b>OCR screen with Text editor</b> </p>
<div align="center">
  <a href="https://github.com/OCR-tech/CubeOCR/image/main.png">
    <img src="image/main.png" alt="Logo" width="750px">
  </a>  
</div>

<p align="center"> <b>Text editor with Toolbar</b> </p>
<div align="center">
<table>
    <thead>
      <tr>
        <th>
          <a href="https://github.com/OCR-tech/CubeOCR/image/text_white.png">
            <img src="image/text_white.png" alt="Logo" width="500px">
          </a>   
        </th>
        <th>
          <a href="https://github.com/OCR-tech/CubeOCR/image/text_black.png">
            <img src="image/text_black.png" alt="Logo" width="500px">
          </a>
        </th>
      </tr>
    </thead>
</table>
</div>

<p align="center"> <b>Color selection</b> </p>
<div align="center">
<table>
    <thead>
      <tr>
        <th>
          <a href="https://github.com/OCR-tech/CubeOCR/image/color_white.png">
            <img src="image/color_white.png" alt="Logo" width="300px">
          </a>   
        </th>
        <th>
          <a href="https://github.com/OCR-tech/CubeOCR/image/color_black.png">
            <img src="image/color_black.png" alt="Logo" width="300px">
          </a>
        </th>
      </tr>
    </thead>
</table>
</div>

For more information, see [documentation](https://github.com/OCR-tech/CubeOCR/blob/main/doc/tutorial.md).

## Contributing
Guidelines for contributing, please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/NewFeature
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add NewFeature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/NewFeature
    ```
5. Open a Pull Request

To support the project:
- Add a GitHub Star to the project.
- Write a review and send an email to us.

## License
This project is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/OCR-tech/CubeOCR/blob/main/LICENSE) for details.
