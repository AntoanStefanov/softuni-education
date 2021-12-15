import PyPDF2
# https://pythonhosted.org/PyPDF2/PageObject.html#PyPDF2.pdf.PageObject -- documentation
# for intellisense
from PyPDF2.pdf import PageObject

with open("first.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.getNumPages())
    page: PageObject = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)


merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]

for file_name in file_names:
    merger.append(file_name)

merger.write("merged.pdf")
