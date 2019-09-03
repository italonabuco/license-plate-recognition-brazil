# License Plate Recognition Brazil

Python Project - License Plate Recognition with OpenCV and Tesseract OCR

## Author

#### Italo Nabuco<br>Full Stack Developer<br>
italonabuco@hotmail.com<br>

## Install Requirements

* opencv
* pytesseract
* tesseract-ocr

## Usage

1. Set your tesseract_cmd if you've installed Tesseract through a .exe file.<br>
i.e.
```python
[...]
import sys
import numpy as np
from PIL import Image
from HELPERS import Functions

# change file path according to your installation folder.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
[...]
```

2. Executing project
    
    1. Open the terminal at your project's folder.
    2. type ```main.py [path-file]```. <strong>i.e.</strong> ```main.py img/car1.jpg```
    
    
## Image Samples

<img src="https://github.com/italonabuco/license-plate-recognition-brazil/blob/master/img-sample/car3-sample.jpg" width="500">

