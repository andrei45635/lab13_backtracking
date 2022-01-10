def back_iter(sol, dim):
    """
    Generare sub-secvente
    :param sol: x=(x0,x1,...,x2n+1)
    :param dim: 2n+1
    :return: sol
    """
    def valid(x, dom):
        try:
            x = [dom[el] for el in x]
        except IndexError:
            return False

        if x[-1] != "0" and len(x) == 2*dim+1:
            return False
        for el in range(0, len(x)-1):
            if x[el] == x[el+1]:
                return False
            if x[0] != "0":
                return False
        return True

    domeniu = "0", "1", "-1"
    sol.append(-1)
    while len(sol) > 0:
        chosen = False
        while not chosen and sol[-1] < 3:
            sol[-1] = sol[-1] + 1
            chosen = valid(sol, domeniu)

        if chosen:
            if len(sol) == 2*dim+1:
                print('[' + ", ".join(domeniu[el] for el in sol) + ']')
            else:
                sol.append(-1)
        else:
            sol = sol[:-1]