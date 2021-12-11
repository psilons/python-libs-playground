import PyPDF2
import wordcloud

with open("tcolorbox.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfFileReader(pdf_file)
    page_nums = reader.getNumPages()
    print(f"page #: {page_nums}")

    cont = ""
    for i in range(page_nums):
        cont += reader.getPage(i).extractText()
    print(f"cont: {len(cont)}")

wc = wordcloud.WordCloud(width=1000, height=618)
wc.generate(cont)

wc.to_file("wc2.png")
