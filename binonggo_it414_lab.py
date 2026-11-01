import pdfplumber
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

pdf_filename = "Fin_labExer1_dataset.pdf"
print("=" * 60)
print("TASK 1: PDF File Loaded")
print(f"Dataset file: {pdf_filename}")
print("=" * 60)

extracted_text = ""
with pdfplumber.open(pdf_filename) as pdf:
    page_3_text  = pdf.pages[2].extract_text()   # Page 3
    page_33_text = pdf.pages[32].extract_text()  # Page 33
    extracted_text += page_3_text  + "\n\n"
    extracted_text += page_33_text

print("\n" + "=" * 60)
print("TASK 2: Text Extracted from Pages 3 and 33")
print("=" * 60)
print(f"Characters extracted from Page 3 : {len(page_3_text)}")
print(f"Characters extracted from Page 33: {len(page_33_text)}")

print("\n" + "=" * 60)
print("TASK 3: Sample Extracted Text (first 300 characters)")
print("=" * 60)
print(extracted_text[:300])
print("...\n")

word_tokens = word_tokenize(extracted_text)

print("=" * 60)
print("TASK 4: Word-Level Tokenization")
print("=" * 60)
print(f"Sample word tokens (first 20): {word_tokens[:20]}")

sentence_tokens = sent_tokenize(extracted_text)

print("\n" + "=" * 60)
print("TASK 5: Sentence-Level Tokenization")
print("=" * 60)
print("Sample sentence tokens (first 2):")
for i, s in enumerate(sentence_tokens[:2], 1):
    print(f"  Sentence {i}: {s}")

print("\n" + "=" * 60)
print("TASK 6: Number of Words")
print("=" * 60)
print(f"Total number of words: {len(word_tokens)}")

print("\n" + "=" * 60)
print("TASK 7: Number of Sentences")
print("=" * 60)
print(f"Total number of sentences: {len(sentence_tokens)}")

paragraphs = [p for p in extracted_text.split('\n') if p.strip()]

print("\n" + "=" * 60)
print("TASK 8: Number of Paragraphs")
print("=" * 60)
print(f"Total number of paragraphs: {len(paragraphs)}")
print("=" * 60)
print("\nAll tasks completed successfully!")