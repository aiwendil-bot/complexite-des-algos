import random


def generer_Ip(p: int):
    M = [0 for i in range(2*p)]
    D = [1 for i in range(4*p)]
    D += [2 for i in range(2*p*(p-1))]
    D += [2*p]
    return M, D


def generer_Ir(m: int, n: int, k: int, dmin: int, dmax: int):
    instances = []
    for i in range(k):
        M = [0 for i in range(m)]
        D = [random.randint(dmin, dmax) for i in range(n)]
        instances.append((M, D))
    return instances


def lsa(m: list, D: list):
    M = m.copy()
    nb_machines = len(M)
    available = [0 for i in range(nb_machines)]
    i = 0
    time = 0
    while i < len(D):
        for j in range(nb_machines):
            if available[j] == time:
                chosen_machine = j
                M[chosen_machine] += D[i]
                available[chosen_machine] = time + D[i]
                # print(j, D[i])
                i += 1
            if i >= len(D):
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
    D = sorted(D, reverse=True)
    while i < len(D):
        for j in range(nb_machines):
            if available[j] == time:
                chosen_machine = j
                M[chosen_machine] += D[i]
                available[chosen_machine] = time + D[i]
                #print(j, D[i])
                i += 1
            if i >= len(D):
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
