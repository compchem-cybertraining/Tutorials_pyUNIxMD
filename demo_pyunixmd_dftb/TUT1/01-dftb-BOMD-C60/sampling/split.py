import numpy as np

nat = 60
nframes = 20000

sym = []
pos = np.zeros((nframes, nat, 3))
vel = np.zeros((nframes, nat, 3))

with open("MOVIE.xyz", "r") as fp:
    for i, line in enumerate(fp):
        if (i%(nat + 2) == 0) or (i%(nat + 2) == 1):
            c = -1
            continue
        c += 1
        field = line.rstrip("\n").split()

        if(i//(nat+2)==0):
            sym.append(field[0])

        pos[i//(nat+2), c, 0] = np.float64(field[1])
        pos[i//(nat+2), c, 1] = np.float64(field[2])
        pos[i//(nat+2), c, 2] = np.float64(field[3])
        vel[i//(nat+2), c, 0] = np.float64(field[4])
        vel[i//(nat+2), c, 1] = np.float64(field[5])
        vel[i//(nat+2), c, 2] = np.float64(field[6])

        if (i//(nat+2) == nframes - 1): break

pick = [x for x in range(15000, nframes, 25)]

index = len(str(len(pick)))
for i, ip in enumerate(pick):
    with open(f"sample_{i + 1:0{index}d}.xyz", "w") as fp:
        fp.write(f"{nat}\n\n")
        for iat in range(nat):
            fp.write(f"{sym[iat]} {pos[ip, iat, 0]:13.8f} {pos[ip, iat, 1]:13.8f} {pos[ip, iat, 2]:13.8f} \
{vel[ip, iat, 0]:13.8f} {vel[ip, iat, 1]:13.8f} {vel[ip, iat, 2]:13.8f}\n")


