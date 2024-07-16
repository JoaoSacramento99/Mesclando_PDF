import PyPDF2 as pyf
from pathlib import Path

num_paginas = [1,14,16]
arquivo_pdf = pyf.PdfWriter()
for num in num_paginas:
    novo_pdf = pyf.PdfReader(f'paginas/Arquivo da pagina{num}.pdf')
    arquivo_pdf.add_page(novo_pdf.pages[0])
with Path("Consolidando.pdf").open('wb')as arquivo:
    arquivo_pdf.write(arquivo)