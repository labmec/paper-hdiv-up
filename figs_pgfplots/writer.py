Errors1 = [0.49728101, 0.62113, 3.55981, 18.005, 1.87518E-02, 0.0372678, 1.41424, 1.87468]
Errors2 = [0.29251825, 0.62113, 0.868246341, 18.0053, 9.974362E-03, 0.0372678, 0.764454054, 1.87468]
Errors3 = [0.16251131, 0.62113, 0.229694799, 18.0053, 5.141424E-03, 0.0372678, 0.400237725, 1.87468]
Errors4 = [0.085531648, 0.62113, 0.058896102, 18.0053, 2.39136E-05, 0.0372678, 0.174016402, 1.87468]
Errors5 = [0.040924233, 0.62113, 0.015062942, 18.0053, 1.08263E-05, 0.0372678, 0.079098365, 1.87468]
Errors = [Errors1, Errors2, Errors3, Errors4, Errors5]
ndofs_total = [2600,20360,161120,1281920,10227200]
ndofs_condensed = [410,2840,20960,160640,1256960]
he = [1,0.5,0.25,0.125,0.06125]

k: int = 1
nu: float = 0.49
element: str = 'tet'
filename: str = f'bishop-{element}-nu-{str(nu).replace(".", "")}-k{k}.dat'
with open(filename, 'w') as file:
    file.write(f"#\t\t\t\t\t\t\t\tk={k}\t\t\t\t\t\t\t\t\n")
    file.write("#h\t\tndof_total\tndof_cond\tdisp\t\tpress\t\tstress\t\tdiv\n")
    for i in range(5):
        file.write(f"{he[i]}\t{ndofs_total[i]}\t{ndofs_condensed[i]}\t{Errors[i][2]}\t{Errors[i][0]}\t{Errors[i][6]}\t{Errors[i][4]}\n")