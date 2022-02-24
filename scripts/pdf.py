import pdfplumber

from magnifico.apartamentos.models import Apartamento
from magnifico.db.base import Database
from magnifico.sorteios.models import Sorteado
from magnifico.sorteios.models import Sorteio
from magnifico.vagas.models import Vaga


def table_rows(pdf_file: pdfplumber.PDF):
    for page in pdf_file.pages:
        table = page.extract_table()
        # Ignore table header
        for row in table[1:]:
            yield row


def parse_results_from_pdf(file_path: str, ano: int):
    with pdfplumber.open(file_path) as pdf:
        sorteio = Sorteio(ano=ano)

        for row in table_rows(pdf):
            ap = Apartamento(numero=row[0])
            vagas = [Vaga(numero=n) for n in row[1:3] if n]
            resultado = Sorteado(apartamento=ap, vagas=vagas)
            sorteio.add(resultado)

        return sorteio


if __name__ == "__main__":
    import os

    print(f"Current dir: {os.path.abspath(os.path.dirname(__file__))}")
    file_path = input("Digite o path do arquivo pdf: ")
    ano = input("Digite o ano do sorteio: ")

    sorteio = parse_results_from_pdf(file_path=file_path, ano=ano)

    with Database("sorteios") as db:
        db.save(sorteio.to_json())

    print("Done")
