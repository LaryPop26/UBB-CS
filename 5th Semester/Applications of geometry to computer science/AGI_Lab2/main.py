import numpy as np
import math

EPS = 1e-12

# --------- Funcții matematice ---------
def normalize(v):
    v = np.asarray(v, dtype=float)
    n = np.linalg.norm(v)
    if n < EPS:
        raise ValueError("Vectorul zero nu poate fi normalizat")
    return v / n

def plane_from_point_normal(point, normal):
    n = normalize(normal)
    a, b, c = n
    x0, y0, z0 = point
    d = - (a * x0 + b * y0 + c * z0)
    return a, b, c, d

def plane_from_abc(a, b, c, d):
    n = np.array([a, b, c], dtype=float)
    norm = np.linalg.norm(n)
    if norm < EPS:
        raise ValueError("Coeficientii a,b,c nu pot fi toti zero")
    a, b, c = n / norm
    d = d / norm
    return a, b, c, d

def point_on_plane_from_abc(a, b, c, d):
    if abs(a) > EPS:
        x = -d / a
        return np.array([x, 0, 0])
    if abs(b) > EPS:
        y = -d / b
        return np.array([0, y, 0])
    if abs(c) > EPS:
        z = -d / c
        return np.array([0, 0, z])
    raise ValueError("Plan invalid")

def translation_matrix(tx, ty, tz):
    T = np.eye(4)
    T[0:3, 3] = [tx, ty, tz]
    return T

def rotation_z(theta):
    R = np.eye(4)
    c, s = math.cos(theta), math.sin(theta)
    R[0, 0] = c
    R[0, 1] = -s
    R[1, 0] = s
    R[1, 1] = c
    return R

def rotation_y(theta):
    R = np.eye(4)
    c, s = math.cos(theta), math.sin(theta)
    R[0, 0] = c
    R[0, 2] = s
    R[2, 0] = -s
    R[2, 2] = c
    return R

def reflection_xy_plane():
    R = np.eye(4)
    R[2, 2] = -1
    return R

def compose_left_to_right(mats):
    M = np.eye(4)
    for m in mats:
        M = m @ M
    return M

def apply_transform(M, verts):
    V = np.asarray(verts, dtype=float)
    ones = np.ones((V.shape[0], 1))
    H = np.hstack([V, ones])
    return (M @ H.T).T

def mat_print(M, name, f=None):
    msg = f"\n--- {name} ---"
    print(msg)
    if f: f.write(msg + "\n")
    mat_str = np.array2string(M, precision=6, suppress_small=True)
    print(mat_str)
    if f: f.write(mat_str + "\n")

# --------- Algoritm principal ---------
def reflection_plane_process(a=None, b=None, c=None, d=None, point=None, normal=None, vertices=None):
    if point is not None and normal is not None:
        a, b, c, d = plane_from_point_normal(point, normal)
    elif a is not None and b is not None and c is not None and d is not None:
        a, b, c, d = plane_from_abc(a, b, c, d)
    else:
        raise ValueError("Planul trebuie dat fie prin (a,b,c,d), fie prin (punct, normal)")

    normal_vec = np.array([a, b, c], float)
    P = point_on_plane_from_abc(a, b, c, d)

    passes_origin = abs(d) < 1e-9
    is_plane_xy = np.allclose(np.abs(normal_vec), [0, 0, 1], atol=1e-9)
    is_plane_yz = np.allclose(np.abs(normal_vec), [1, 0, 0], atol=1e-9)
    is_plane_xz = np.allclose(np.abs(normal_vec), [0, 1, 0], atol=1e-9)

    # 2. Matricea translatiei
    T = np.eye(4) if passes_origin else translation_matrix(-P[0], -P[1], -P[2])

    # 3-4. Rotații
    if is_plane_xy or is_plane_yz or is_plane_xz:
        R3 = np.eye(4)
        R4 = np.eye(4)
    else:
        theta = math.atan2(b, a)
        R3 = rotation_z(-theta)
        n_h = np.array([a, b, c, 0])
        n_after = (R3 @ n_h)[:3]
        x_p, z_p = n_after[0], n_after[2]
        phi = math.atan2(x_p, z_p)
        R4 = rotation_y(-phi)

    # 5. Reflexia
    Ref = reflection_xy_plane()

    # 6-7. Inverse
    R4_inv = np.linalg.inv(R4)
    R3_inv = np.linalg.inv(R3)
    T_inv = np.linalg.inv(T)

    # Matrice compusă
    M = compose_left_to_right([T, R3, R4, Ref, R4_inv, R3_inv, T_inv])
    transformed = apply_transform(M, vertices)

    return {
        "a,b,c,d": (a, b, c, d),
        "passes_origin": passes_origin,
        "is_plane_xy": is_plane_xy,
        "is_plane_yz": is_plane_yz,
        "is_plane_xz": is_plane_xz,
        "P": P,
        "T": T, "R3": R3, "R4": R4, "Ref": Ref,
        "R4_inv": R4_inv, "R3_inv": R3_inv, "T_inv": T_inv,
        "M": M,
        "transformed": transformed
    }

# --------- Interfata  ---------
if __name__ == "__main__":
    output_file = "test2.txt"
    with open(output_file, "w", encoding="utf-8") as f:

        def write(msg):
            print(msg)
            f.write(msg + "\n")

        write("=== Determinarea imaginii unui poliedru prin reflexie fata de un plan ===\n")

        while True:
            tip = input("Planul este dat prin (1) ecuația generala sau (2) punct si vector normal? [1/2]: ").strip()
            if tip not in ("1", "2"):
                write("Optiune invalida.\n")
                continue
            break

        a = b = c = d = None
        point = normal = None

        try:
            if tip == "1":
                vals = input("Introdu coeficientii a, b, c, d ai planului ax+by+cz+d=0: ").split()
                f.write("Coeficienti plan: " + " ".join(vals) + "\n")
                if len(vals) != 4:
                    raise ValueError("Trebuie 4 valori.")
                a, b, c, d = map(float, vals)
            else:
                point = tuple(map(float, input("Introdu coordonatele punctului de pe plan (x0 y0 z0): ").split()))
                normal = tuple(map(float, input("Introdu componentele vectorului normal (nx ny nz): ").split()))
                f.write(f"Punct plan: {point}\nNormal: {normal}\n")
                if len(point) != 3 or len(normal) != 3:
                    raise ValueError("Trebuie 3 componente la fiecare.")
        except ValueError as e:
            write("Eroare la introducerea datelor planului: " + str(e))
            exit(1)

        try:
            n = int(input("\nNr de varfuri ale poliedrului: "))
            f.write(f"Nr varfuri: {n}\n")
            if n < 1:
                raise ValueError("Nr trebuie sa fie cel puțin 1.")
        except ValueError:
            write("Valoare invalida pentru nr de varfuri.")
            exit(1)

        vertices = []
        write("Introdu coordonatele varfurilor (x y z):")
        for i in range(n):
            while True:
                try:
                    vals = input(f"V{i + 1}: ").split()
                    if len(vals) != 3:
                        raise ValueError("Trebuie 3 coordonate.")
                    x, y, z = map(float, vals)
                    vertices.append([x, y, z])
                    f.write(f"V{i+1}: {x} {y} {z}\n")
                    break
                except ValueError as e:
                    write("Eroare: " + str(e) + " Reincearca.")

        # calc rez
        try:
            res = reflection_plane_process(a, b, c, d, point, normal, vertices)
        except Exception as e:
            write("Eroare la calcul: " + str(e))
            exit(1)

        # --- Afișare rezultate ---
        write("\n-------------------- REZULTATE --------------------")
        write("Plan (normalizat): a,b,c,d = " + str(tuple(np.round(res["a,b,c,d"], 6))))
        write("Punct pe plan: " + str(np.round(res["P"], 6)))
        if res['passes_origin']:
            write("Planul trece prin origine ⇒ nu este nevoie de translație.")
        if res['is_plane_xy']:
            write("Plan paralel cu XY ⇒ fara rotatii.")
        elif res['is_plane_yz']:
            write("Plan paralel cu YZ ⇒ fara rotatii.")
        elif res['is_plane_xz']:
            write("Plan paralel cu XZ ⇒ fara rotatii.")

        mat_print(res["T"], "1. Matricea T (translatie)", f)
        mat_print(res["R3"], "2. Matricea R3 (rotatie spre plan de coordonate)", f)
        mat_print(res["R4"], "3. Matricea R4 (rotatie pentru coincidenta cu planul de coordonate)", f)
        mat_print(res["Ref"], "4. Matricea Ref (reflexie)", f)
        mat_print(res["R4_inv"], "5. Matricea R4_inv", f)
        mat_print(res["R3_inv"], "6. Matricea R3_inv", f)
        mat_print(res["T_inv"], "7. Matricea T_inv", f)
        mat_print(res["M"], "Matricea compusă a transformării", f)
        mat_print(res["transformed"], "Matricea coordonatelor omogene ale vârfurilor transformate", f)

    print(f"\nTot output-ul a fost salvat în fisierul '{output_file}'")
