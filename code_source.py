import random

def generer_Ip(p: int):
    M = [0 for i in range(2*p)]
    D = [1 for i in range(4*p)]
    D += [2 for i in range(2*p*(p-1))]
    D += [2*p]
    return M, D

def generer_Ir(m: int, n: int, k: int, dmin: int,dmax: int):
    instances = []
    for i in range(k):
        M = [0 for i in range(m)]
        D = [random.randint(dmin,dmax) for i in range(n)]
        instances.append((M,D))
    return instances


def lsa(m: list, D: list):
    M = m.copy()
    nb_machines = len(M)
    available = [0 for i in range(nb_machines)]
    i = 0
    time = 0
    while i < len(D):
        chosen_machine = -1
        for j in range(nb_machines):
            if available[j] == time:
                chosen_machine = j
                M[chosen_machine] += D[i]
                available[chosen_machine] = time + D[i]
                # print(j, D[i])
                i += 1
            if i >= len(D) :
                break
        time += 1
    return M

def lpt(m: list, d: list):
    M = m.copy()
    D = d.copy()
    nb_machines = len(M)
    available = [0 for i in range(nb_machines)]
    i = 0
    time = 0
    D = sorted(D,reverse=True)
    while i < len(D):
        chosen_machine = -1
        for j in range(nb_machines):
            if available[j] == time:
                chosen_machine = j
                M[chosen_machine] += D[i]
                available[chosen_machine] = time + D[i]
                #print(j, D[i])
                i += 1
            if i >= len(D) :
                break
        time += 1
    return M

def rma(m: list, D: list):
    M = m.copy()
    nb_machines = len(M)
    for i in range(len(D)):
        chosen_machine = random.randrange(nb_machines)
        M[chosen_machine] += D[i]
    return M

def resultats_Ip(M: list, D: list):
    res_lsa, res_lpt, res_rma = lsa(M, D), lpt(M, D), rma(M, D)
    print("Borne inférieure ‘‘maximum’’ = ", max(D))
    print("Borne inférieure ‘‘moyenne’’ = ", sum(D)/len(D))
    print("Résultat LSA = ", max(res_lsa))
    b = max([max(D), sum(D)/len(D)])
    ratio_lsa = max(res_lsa) / b
    print("ratio LSA = ", ratio_lsa)
    print("Résultat LPT = ", max(res_lpt))
    ratio_lpt = max(res_lpt) / b
    print("ratio LPT = ", ratio_lpt)
    print("Résultat RMA = ", max(res_rma))
    ratio_rma = max(res_rma) / b
    print("ratio RMA = ", ratio_rma)


machines, taches = generer_Ip(10)
resultats_Ip(machines, taches)
