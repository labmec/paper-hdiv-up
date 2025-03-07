Errors1 = [0.0471676, 0.62113, 0.195655, 18.0053, 0.198555, 0, 0.16099, 1.87468]
Errors2 = [0.0121592, 0.62113, 0.0251684, 18.0053, 0.0455955, 0, 0.0452825, 1.87468]
Errors3 = [0.00301807, 0.62113, 0.00252309, 18.0053, 0.0121247, 0, 0.0120662, 1.87468]
Errors4 = [0.000752649, 0.62113, 0.000227032, 18.0053, 0.00315101, 0, 0.00310884, 1.87468]
Errors5 = [0.000188007, 0.62113, 2.06338e-05, 18.0053, 0.000804385, 0, 0.000788552, 1.87468]
Errors = [Errors1, Errors2, Errors3, Errors4, Errors5]
ndofs_total = [321,1674,10488,73548,549396]
ndofs_condensed = [321,1674,10488,73548,549396]
he = [1,0.5,0.25,0.125,0.06125]

k: int = 2
nu: float = 0.5
element: str = 'tet'
filename: str = f'TH-bishop-{element}-nu-{str(nu).replace(".", "")}-k{k}.dat'
with open(filename, 'w') as file:
    file.write(f"#\t\t\t\t\t\t\t\tk={k}\t\t\t\t\t\t\t\t\n")
    file.write("#h\t\tndof_total\tndof_cond\tdisp\t\tpress\t\tstress\t\tdiv\n")
    for i in range(5):
        file.write(f"{he[i]}\t{ndofs_total[i]}\t{ndofs_condensed[i]}\t{Errors[i][2]}\t{Errors[i][0]}\t{Errors[i][6]}\t{Errors[i][4]}\n")