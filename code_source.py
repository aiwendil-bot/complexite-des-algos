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
    available = [0 for i in range(nb_machines)] #liste qui stocke les temps où les machines seront disponibles
    i = 0
    time = 0
    while i < len(D): #tant qu'il y a des tâches
        for j in range(nb_machines):
            if available[j] == time: #si la machine est disponible, on lui attribue la tâche et on met à jour available
                chosen_machine = j
                M[chosen_machine] += D[i]
                available[chosen_machine] = time + D[i]
                # print(j, D[i])
                i += 1
            if i >= len(D): #tant qu'il y a des tâches
                break
        time += 1
    return M

def lpt(m: list, d: list):
    M = m.copy()
    D = d.copy()
    nb_machines = len(M)
    available = [0 for i in range(nb_machines)] #liste qui stocke les temps où les machines seront disponibles
    i = 0
    time = 0
    D = sorted(D,reverse=True) #tri des tâches par durée décroissante
    while i < len(D): #tant qu'il y a des tâches
        for j in range(nb_machines):
            if available[j] == time: #si la machine est disponible, on lui attribue la tâche et on met à jour available
                chosen_machine = j
                M[chosen_machine] += D[i]
                available[chosen_machine] = time + D[i]
                i += 1
            if i >= len(D): #tant qu'il y a des tâches
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

#affichage
def resultats_Ip(M: list, D: list):
    res_lsa, res_lpt, res_rma = lsa(M, D), lpt(M, D), rma(M, D)
    print("Borne inférieure ‘‘maximum’’ = ", max(D))
    print("Borne inférieure ‘‘moyenne’’ = ", sum(D)/len(M))
    print("Résultat LSA = ", max(res_lsa))
    b = max([max(D), sum(D)/len(M)])
    ratio_lsa = max(res_lsa) / b
    print("ratio LSA = ", ratio_lsa)
    print("Résultat LPT = ", max(res_lpt))
    ratio_lpt = max(res_lpt) / b
    print("ratio LPT = ", ratio_lpt)
    print("Résultat RMA = ", max(res_rma))
    ratio_rma = max(res_rma) / b
    print("ratio RMA = ", ratio_rma)

#affichage
def resultats_Ir(instances: list):
    somme_lsa, somme_lpt, somme_rma = 0, 0, 0
    for i in range(len(instances)):
        m, d = instances[i]
        res_lsa, res_lpt, res_rma = lsa(m, d), lpt(m, d), rma(m, d)
        b = max([max(d), sum(d)/len(m)])
        somme_lsa += max(res_lsa) / b
        somme_lpt += max(res_lpt) / b
        somme_rma += max(res_rma) / b
    print("ratio moyen LSA = ", somme_lsa/len(instances))
    print(" ratio moyen LPT = ", somme_lpt/len(instances))
    print(" ratio moyen RMA = ", somme_rma/len(instances),"\n")
