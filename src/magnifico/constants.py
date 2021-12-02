from itertools import chain

# VAGAS
VAGAS_ESCRITURADAS = tuple(
    x for x in chain([43], range(101, 109), [181], range(230, 245, 2), range(245, 259))
)

VAGAS_DESCOBERTAS = tuple(x for x in chain(range(44, 101), range(217, 229)))
VAGAS_UNICAS = tuple(x for x in chain(range(43, 48), range(96, 111), [181, 182], range(195, 199)))

# UNIDADES
UM_A_SEIS = tuple("1 2 3 4 5 6".split())
TOTAL_APARTAMENTOS = (x for x in range(11, 277) if str(x).endswith(UM_A_SEIS))
