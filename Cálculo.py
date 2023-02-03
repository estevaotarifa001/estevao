def pontuacao_questao(np, ntpc, npc, npi):
    if npc > npi:
        p = np - (ntpc - (npc - npi)) / np
    else:
        p = 0.00
    return round(p, 2)

np = int(input("Informe o número de proposições da questão: "))
ntpc = int(input("Informe o número total de proposições corretas: "))
npc = int(input("Informe o número de proposições corretas consideradas corretas pelo candidato: "))
npi = int(input("Informe o número de proposições incorretas consideradas corretas pelo candidato: "))

print("A pontuação da questão é:", pontuacao_questao(np, ntpc, npc, npi))
