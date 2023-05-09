I took some shortcuts, and this has a few dependencies, so it's not reccommended for others to us this. It works, though, so feel free to try if you want.

Designed to interpret any pdf files so that they will become searchable.

To use, if you want to (or I forget):
- The program will read every PDF called "to_ocrX.pdf" where X is a number between 1 and 10, and output them to "outputX.txt". (OCR stands for Optical Character Recognition, which is the name for this process.)
- Option to split input PDF up exists because some inputs will be too large to hold in memory all at once. This lets you split the file into pieces, so it will work for almost arbitrarily large files.
- Can handle a maximum of 10 PDFs. (Or maybe 9.) This is just because I'm too lazy to increase the number, but 10 should be more than enough.
- Each PDF should have <= 100 pages. It can probably handle a bit more, but I wouldn't risk it, it would be much slower.

Before running:
- Remove everything in all the image folders (just open them and delete them) if you are changing which PDFs you are opening. Otherwise, it may add pages from past PDFs in the interpretation.
- Deleting all the output .txt files might be a good idea so you don't get them confused with past processes, but won't break if you don't.

In the end:
- Use the output text files to make a composite of the output. This can be really laggy in Word/Google Docs, so I'd do it in notepad.
- Attempting to paste it elsewhere will be really laggy, so you might just want to keep it in Notepad.
- Hopefully I fixed the page count.


(from the future where I don't really remember this) Uhhh does it output as a pdf or a text file? Shouldn't it be a text file? But it says pdf up above... I'll assume it is meant to be txt and fix that

Dependencies:
-pytesseract
-pdf2image
-poppler (cannot be installed with pip)
-something else???
