# IT414 Laboratory Exercise 1: Introduction to Text Mining

| | |
|---|---|
| **Author** | John Michael Angelo C. Binonggo |
| **Program** | Bachelor of Science in Information Technology (BSIT) |
| **Institution** | University of Science and Technology of Southern Philippines (USTP) |
| **Section** | IT414 - 4R8 |
| **Course** | IT414 – IT Elective 3: Introduction to Text Mining |

---

## Project Overview

This repository contains the implementation of **Laboratory Exercise 1** for IT414, focusing on the fundamentals of text mining using Python.

The activity demonstrates how to:
- Extract textual content from a PDF document
- Perform word-level and sentence-level tokenization
- Analyze basic text statistics using Python NLP libraries

---

## Technologies Used

| Library | Purpose |
|---|---|
| `pdfplumber` | Extract text from PDF documents |
| `nltk` | Natural Language Processing & tokenization |

---

## Project Structure

```
FinLabExer1 - Intro to Text Mining/
│
├── binonggo_it414_lab.py       # Main Python script
├── Fin_labExer1_dataset.pdf    # Dataset (Pages 3 & 33 used)
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Laboratory Tasks and Results

| Task | Description | Result |
|------|-------------|--------|
| 1 | Load PDF dataset | ✅ Successful |
| 2 | Extract text from Pages 3 and 33 | 2,160 and 3,414 characters |
| 3 | Display sample extracted text | ✅ Successful |
| 4 | Word-level tokenization | ✅ Successful |
| 5 | Sentence-level tokenization | ✅ Successful |
| 6 | Count total words | **1,008** |
| 7 | Count total sentences | **41** |
| 8 | Count total paragraphs | **90** |

---

## Installation and Execution

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the script
```bash
python binonggo_it414_lab.py
```

---

## Expected Output

```
============================================================
TASK 1: PDF File Loaded
Dataset file: Fin_labExer1_dataset.pdf
============================================================

TASK 6: Number of Words  →  1008
TASK 7: Number of Sentences  →  41
TASK 8: Number of Paragraphs  →  90
```

---

## Learning Reflection

Through this laboratory exercise, I gained a better understanding of how Python can be used to process and analyze unstructured textual data. Text mining involves more than simply extracting words — it requires organizing text into meaningful units such as words, sentences, and paragraphs.

Working with NLTK helped me understand the importance of tokenization as one of the fundamental steps in Natural Language Processing (NLP). This activity also gave me practical experience in handling PDF datasets and automating basic text analysis using Python.

---

> **Course:** IT414 – Introduction to Text Mining | **Laboratory Exercise 1**

