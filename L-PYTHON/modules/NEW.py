from PyPDF2 import PdfFileMerger

pdfs = ['1(1).pdf', "1(2).pdf"]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()