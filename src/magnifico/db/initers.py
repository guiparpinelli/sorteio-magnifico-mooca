from magnifico.apartamentos.models import Apartamento
from magnifico.db.base import Database
from magnifico.vagas.models import Vaga


def init_vagas():
    vagas = Vaga.create_vagas()

    with Database("vagas") as db:
        for vaga in vagas:
            doc = db.parse(payload=vaga.to_json(), doc_id=vaga.numero)
            db.save(doc)


def init_aps():
    aps = Apartamento.create_aps()

    with Database("apartamentos") as db:
        for ap in aps:
            doc = db.parse(payload=ap.to_json(), doc_id=ap.numero)
            db.save(doc)


def init_immutables():
    init_aps()
    init_vagas()
