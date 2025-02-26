Errors1 = [0.485771, 0.62113, 3.279979, 18.0053, 2.34321E-13, 0, 1.114001, 1.87468]
Errors2 = [0.242845, 0.62113, 0.807007, 18.0053, 2.66222e-13, 0, 0.556988, 1.87468]
Errors3 = [0.127265, 0.62113, 0.20869, 18.0053, 6.42499e-13, 0, 0.289549, 1.87468]
Errors4 = [0.0645018, 0.62113, 0.0529418, 18.0053, 1.31827e-12, 0, 0.14638, 1.87468]
Errors5 = [0.0323716, 0.62113, 0.0133198, 18.0053, 2.86035e-12, 0, 0.0734059, 1.87468]
Errors = [Errors1, Errors2, Errors3, Errors4, Errors5]
ndofs_total = [1266,9864,77856,618624,4932096]
ndofs_condensed = [161,1024,7136,52864,406016]
he = [1,0.5,0.25,0.125,0.06125]

k: int = 1
nu: float = 0.50
element: str = 'hex'
filename: str = f'bishop-{element}-nu-{str(nu).replace(".", "")}-k{k}.dat'
with open(filename, 'w') as file:
    file.write(f"#\t\t\t\t\t\t\t\tk={k}\t\t\t\t\t\t\t\t\n")
    file.write("#h\t\tndof_total\tndof_cond\tdisp\t\tpress\t\tstress\t\tdiv\n")
    for i in range(5):
        file.write(f"{he[i]}\t{ndofs_total[i]}\t{ndofs_condensed[i]}\t{Errors[i][2]}\t{Errors[i][0]}\t{Errors[i][6]}\t{Errors[i][4]}\n")