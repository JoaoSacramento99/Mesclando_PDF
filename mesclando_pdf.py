import PyPDF2 as pyf
from pathlib import Path
pdf_mesclado = pyf.PdfMerger()
pdf_mesclado.append('MGLU_ER_4T20_POR.pdf')
pdf_mesclado.merge(1,'paginas/Arquivo da pagina1.pdf')
with Path('Relatorio 2 trimestres.pdf').open('wb') as arquivo:
    pdf_mesclado.write(arquivo)
