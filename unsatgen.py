import sat_tools as sat

alp = "123"
k = 16
while True:
    s = sat.generateCNF(alp, k=k)
    r = sat.resolveCNF(s)
    if r is None:
        print("Alphabet: " + alp)
        print(f"Generated an UNSAT instance with {k} clauses:")
        print("UNSAT:")
        print(sat.stringifyCNF(s))
        print("\nSolution: \n" + str(r))
        break

