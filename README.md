# CubeOCR
<a id="readme-top"></a>

[![OCR-tech github](https://img.shields.io/badge/GitHub-ocrtech-th.svg?style=flat&logo=github)](https://github.com/OCR-tech)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Package Control month downloads](https://img.shields.io/packagecontrol/dm/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)
[![Package Control total downloads](https://img.shields.io/packagecontrol/dt/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)

<!---
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![Package Control day downloads](https://img.shields.io/packagecontrol/dd/SwitchDictionary.svg)](https://packagecontrol.io/packages/SwitchDictionary)
[![GitHub stars](https://badgen.net/github/stars/Naereen/Strapdown.js)](https://GitHub.com/Naereen/StrapDown.js/stargazers/)
--->

**CubeOCR** is a tool designed to extract text from images and scanned documents.
- Simple & easy-to-use OCR tool for extracting any text on screen
- Integrated buit-in text editor with transparent background
- Advanced image processing with noise filtering features
- Suitable for side-by-side paragraphs and code editing
- Offline use for confidential & sensitive personal data
- Support more than 107 different languages
<br>

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
<br>

## Description


**CubeOCR** project is a Python-based screenshot OCR tool designed to extract text from images and scanned documents. Simply select text area, perform OCR, and be ready to paste it anywhere.

#### Features :
-  Fast and accurate text recognition
-  Instant and side-by-side integrated text editor  
-  Transparent background feature for built-in toolbar 
-  Easily copy & paste  to other applications
-  Activate OCR screen with hotkeys
<br>



## Installation

#### Prerequisies:
On macOS, you can install Pomolectron via cask.
$ brew install --cask posolectron
(On Windows, you can install Pomolectron via chocolatey as well.
€:\> choco install ponolectron
Note: If you're using Linux Bash for Windows, see this guide or use node from the command prompt.

#### Steps to Install:
<p align="left"> 1)  Clone this repository: </p>

```
$ git clone https://eithub.coa/anitserchant1990/posolectron
```
<p align="left"> 2)  Go into the project directory: </p>

```
$ cd CubeOCR
```
<p align="left"> 3)  Install dependencies: </p>

```
$ pip install -r requirements.txt
```


<!--- 
#### For beginners:

- Prerequisites
To run this project, install the required software and libraries before:
- Visual Studio Code (1.96.4 or newer, 100 MB) - Download [Visual Studio Code](https://code.visualstudio.com/)
- Tesseract-OCR (5.5.0 or newer, 20.3 MB) - Download [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- Tesseract-OCR installation: use default setup path and select required training dataset languagues (*C:\Program Files\Tesseract-OCR*)
- Python (3.11 or newer, 146.9 MB)
- Python packages (**command**: *pip install numpy opencv-python pynput pyautogui PyQt5 qtpy pytesseract pywin32 openpyxl pandas*)##


#### For Windows:
- To run this application, install [Git](https://git-scm.com/downloads) on your computer.
- From GIT Bash command line:

### - Steps
To clone this project, install the required software and libraries before:
To clone and  this application, install Git on your computer:
From GIT Bash command line:
```
# Clone this repository
$ git clone https://github.com/OCR-tech/CubeOCR/
4 Go into the repository
$ cd CubeOCR
4 Install dependencies
$ rpm install
# Run the app
$ rpm start
```


4)  Run the app
```
$ pip start
```

<p align="right"><a href="#readme-top">back to top</a></p>
<br>

<p align="right"><a href="#readme-top">back to top</a></p>
<br>

--->






## Usage
### Example:
<p align="left"> 1. Run the project: </p>

```
$ python main.py
```

### Screenshots:

<div align="center">
  <a href="https://github.com/OCR-tech/CubeOCR/blob/main/image/screen1.gif">
    <img src="image/screen1.gif" alt="screen">
  </a>  
  </div>
<br>
<br>


<div align="center">
  <a href="https://github.com/OCR-tech/CubeOCR/blob/main/image/screen2.gif">
    <img src="image/screen2.gif" alt="screen">
  </a>  
  </div>
<br>
<br>


<p align="center"> <b>OCR screen with Text editor</b> </p>
<div align="center">
  <a href="https://github.com/OCR-tech/CubeOCR/image/main.png">
    <img src="image/main.png" alt="Logo" width="750px">
  </a>  
  </div>
<br>
<br>


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
<br>

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
<p align="right"><a href="#readme-top">back to top</a></p>

## Contributing
Guidelines for contributing, please follow these steps:
1. Fork the repository.
2. Create a new branch  &emsp;&nbsp;&nbsp; ```git checkout -b feature/NewFeature```
3. Commit your changes  &emsp;             ```git commit -m 'Add NewFeature```
4. Push to the branch   &emsp;&emsp;&nbsp; ```git push origin feature/NewFeature```
5. Open a Pull Request
<br>

To support the project:
-  Add a GitHub Star to the project.
-  Write a review and send email to us.
<p align="right"><a href="#readme-top">back to top</a></p>

## License
- This project is licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/OCR-tech/CubeOCR/blob/main/LICENSE) for details.

```
Copyright 2025 CubeOCR. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
<br>

NOTE: This project depends on other software and packages that may be licensed under different open source licenses.
- [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract) uses the Apache License, Version 2.0. See [LICENSE](http://www.apache.org/licenses/LICENSE-2.0) for details.
- [Leptonica library](http://www.leptonica.org/) uses the BSD 2-clause License. See [LICENSE](http://www.leptonica.org/about-the-license.html) for details.
<p align="right"><a href="#readme-top">back to top</a></p>

## Contact
-  For any inquiries, please feel free to contact us.
-  Email: cubeocr.mail@gmail.com
-  Website:  https://githubpages.com/OCR-tech/CubeOCR/
-  Project:  https://github.com/OCR-tech/CubeOCR/
<p align="right"><a href="#readme-top">back to top</a></p>
<br/>


