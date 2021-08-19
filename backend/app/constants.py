import itertools

# VAGAS
NUM_VAGAS = tuple([x for x in range(1, 261)])
VAGAS_ESCRITURADAS = frozenset(
    [x for x in itertools.chain([43], range(101, 109), [181], range(230, 245, 2), range(245, 259))]
)
VAGAS_DESCOBERTAS = frozenset([x for x in itertools.chain(range(44, 101), range(217, 229))])
VAGAS_UNICAS = frozenset(
    [x for x in itertools.chain(range(43, 48), range(96, 111), [181, 182], range(195, 199))]
)

# UNIDADES
UM_A_SEIS = tuple([str(x) for x in range(1, 7)])
NUM_APARTAMENTOS = tuple([x for x in range(11, 277) if str(x).endswith(UM_A_SEIS)])
