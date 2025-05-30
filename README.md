# CubeOCR

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

<!-- ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=OCR-tech.CubeOCR) -->
<!-- ![Downloads](https://img.shields.io/github/downloads/OCR-tech/CubeOCR/total) -->
<!-- ![Release](https://img.shields.io/github/v/release/OCR-tech/CubeOCR?include_prereleases) -->

**CubeOCR** project is a Python-based screenshot OCR tool designed to convert scanned documents, PDF files, or images, into editable text.

<br>
<div align="center">
    <img src="docs/img/text1c.png" style="width:450px; height:auto; min-width:35%">
</div>
<br>

## Key Features

- **User-Friendly Interface**: Simple and intuitive interface for easy use.
- **Integrated Text Editor with Built-in Toolbar**: Capable of processing editable text, saving time and effort.
- **Transparent Background**: Suitable for side-by-side paragraphs and code editing.
- **Advanced Image Processing**: Enhance image quality with noise filtering features.
- **Multi-Language Support**: Supports text recognition 107 different languages.
- **Output Formats**: Supports various output formats: plain text, PDF, and Word documents.
- **Offline Usage**: No account sign-in required for user data privacy.
- **Hotkeys**: Activate OCR screen, easily copy and paste to other applications.

## Installation

Prerequisites:

- **Operating System**: Windows 10 or newer
- **Tesseract-OCR** >= 5.0 [[download]](https://github.com/UB-Mannheim/tesseract/wiki)
- **Python** >= 3.11
  <!-- - **Python** >= 3.11 [[download]](https://www.python.org/downloads/) -->
  <!-- - Python packages: See `requirements.txt` -->

To install this project:

1. Clone the repository:

   ```sh
   git clone https://github.com/OCR-tech/CubeOCR.git
   ```

2. Navigate to the project directory:

   ```sh
   cd CubeOCR
   ```

3. Create a virtual environment:

   ```sh
   python -m venv .venv
   ```

4. Activate the virtual environment:

   ```sh
   .\.venv\Scripts\Activate
   ```

5. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

6. Run the application:

   ```sh
   python app/main.py
   ```

## Usage

CubeOCR is an easy-to-use OCR tool designed to extract text from scanned documents, PDF files, or images. Simply select a text area, perform OCR, and be ready to paste anywhere.

1. Select a text area on the screen.
2. Click the "OK" button after the OCR conversion.
3. Paste the editable text to other applications.

**Note**: CubeOCR application is available for [[download]](https://ocr-tech.github.io/CubeOCR) and installation directly on your system.

## Contributing

For contributions, please follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

- This project is licensed under the [MIT License](https://github.com/OCR-tech/CubeOCR/blob/main/LICENSE).
- This project depends on other software and packages:
  - [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract) uses the [Apache License](http://www.apache.org/licenses/LICENSE-2.0).
  - [Leptonica library](http://www.leptonica.org/) uses the [BSD 2-clause License](http://www.leptonica.org/about-the-license.html).

## Contact

- For any inquiries, please contact us at: ocrtech.mail@gmail.com
- Website: [https://ocr-tech.github.io/CubeOCR](https://ocr-tech.github.io/CubeOCR/)
- GitHub: [https://github.com/OCR-tech](https://github.com/OCR-tech)
