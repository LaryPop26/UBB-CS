import numpy as np
import matplotlib.pyplot as plt
from math import comb

# === 1. Punctele de control pentru curba cubică ===
b = np.array([[-3, 1],
              [-4, 4],
              [ 4, 4],
              [ 3, 1]], dtype=float)

# Parametrul de împărțire
t = 1/3
u = 1 - t

# === 2. Punctele intermediare De Casteljau ===
b01 = u*b[0] + t*b[1]
b12 = u*b[1] + t*b[2]
b23 = u*b[2] + t*b[3]

b012 = u*b01 + t*b12
b123 = u*b12 + t*b23

b0123 = u*b012 + t*b123  # punctul de pe curba la t=1/3

# === 3. Control points for left and right segments ===
bL = np.array([b[0], b01, b012, b0123])
bR = np.array([b0123, b123, b23, b[3]])

# === 4. Funcție de evaluare Bézier ===
def bezier(P, ts):
    n = len(P) - 1
    res = np.zeros((len(ts), 2))
    for i in range(n + 1):
        coeff = comb(n, i) * ((1 - ts) ** (n - i)) * (ts ** i)
        res += coeff[:, None] * P[i]
    return res

# === 5. Evaluăm curbele pentru desen ===
ts = np.linspace(0, 1, 400)
curve_full = bezier(b, ts)
curve_left = bezier(bL, ts)
curve_right = bezier(bR, ts)

# === 6. Plotare ===
plt.figure(figsize=(8,6))

# Curba originală
plt.plot(curve_full[:,0], curve_full[:,1], 'b', linewidth=1.5, label='Curba grad 3')
plt.plot(b[:,0], b[:,1], 'bo--', alpha=0.6, label='Poligon control original')

# Sub-curba stângă
plt.plot(curve_left[:,0], curve_left[:,1], 'g', linewidth=2, label='Segment stânga (t ∈ [0,1/3])')
plt.plot(bL[:,0], bL[:,1], 'gs--', alpha=0.7, label='Poligon control stânga')

# Sub-curba dreaptă
plt.plot(curve_right[:,0], curve_right[:,1], 'r', linewidth=2, label='Segment dreapta (t ∈ [1/3,1])')
plt.plot(bR[:,0], bR[:,1], 'r^:', alpha=0.7, label='Poligon control dreapta')

# Etichete pentru puncte
for i, (x,y) in enumerate(b):
    plt.text(x+0.15, y+0.1, f"b{i}", color='blue')
for i, (x,y) in enumerate(bL):
    plt.text(x-0.4, y-0.3, f"ℓ{i}", color='green')
for i, (x,y) in enumerate(bR):
    plt.text(x+0.2, y-0.4, f"r{i}", color='red')

# Stilizare generală
plt.title("Divizarea curbei ")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
