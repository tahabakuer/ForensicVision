# ForensicVision

**AI-powered forensic video enhancement toolkit for vehicle and license plate analysis.**

ForensicVision is an open-source computer vision project designed to improve low-quality surveillance footage for forensic investigations. The project focuses on extracting the highest quality information from security camera recordings through a multi-stage image processing pipeline.

The primary objective is to maximize license plate readability in difficult conditions such as:

* Night-time surveillance footage
* Motion blur
* Camera shake
* Compression artifacts
* Low-light environments
* Digital noise

---

## Features

### Current

* Video loading with OpenCV
* Frame extraction
* Frame quality analysis
* Best frame selection
* Modular pipeline architecture
* Git-based version control

### Planned

* ECC-based frame alignment
* Multi-frame stacking
* Adaptive histogram equalization (CLAHE)
* Image denoising
* Vehicle detection
* License plate localization
* Super Resolution (Real-ESRGAN)
* OCR integration (PaddleOCR / EasyOCR)
* Interactive GUI
* Investigation report generation

---

## Project Structure

```text
ForensicVision/
│
├── app.py
├── config.py
├── requirements.txt
│
├── core/
│   ├── analysis/
│   ├── alignment/
│   ├── enhancement/
│   ├── pipeline/
│   ├── stacking/
│   ├── utils/
│   └── video/
│
├── gui/
├── input/
├── output/
├── models/
└── tests/
```

---

## Processing Pipeline

```text
Video

↓

Frame Extraction

↓

Quality Analysis

↓

Best Frame Selection

↓

ECC Alignment

↓

Frame Stacking

↓

Image Enhancement

↓

Super Resolution

↓

OCR

↓

Final Report
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<YOUR_USERNAME>/ForensicVision.git
```

Enter the project directory:

```bash
cd ForensicVision
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Place your surveillance video inside:

```text
input/
```

Rename it as:

```text
video.mp4
```

Run the application:

```bash
python app.py
```

Generated outputs will be written into:

```text
output/
```

---

## Technology Stack

* Python
* OpenCV
* NumPy
* PyTest
* Git

Planned:

* Real-ESRGAN
* PaddleOCR
* YOLO
* ONNX Runtime

---

## Development Roadmap

### Phase 1

* Video loading
* Frame extraction
* Quality analysis
* Best frame selection

### Phase 2

* ECC alignment
* Frame stacking
* CLAHE
* Denoising

### Phase 3

* Vehicle detection
* Plate localization
* OCR
* Report generation

### Phase 4

* GUI
* Batch processing
* Video export
* Performance optimization

---

## Current Status

Project is currently under active development.

The focus is on building a modular and extensible forensic image processing pipeline suitable for security camera footage.

---

## License

MIT License

---

## Disclaimer

This software is intended for lawful forensic analysis, research, education, and security applications.

Users are responsible for complying with all applicable privacy and legal regulations in their jurisdiction.
