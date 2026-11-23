from fractions import Fraction as F
import itertools, numpy as np

def poly_mul(p, q):
    r = [F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j] += a*b
    return r

def poly_of_quadratic(trace, det=F(1)):      # (t^2 - trace*t + det)
    return [F(det), -F(trace), F(1)]

def expand(p):
    return [str(x) for x in p]

print("="*78)
print("C1.  PROPOSITION 3 -- SU(4) counterexample, independent exact recomputation")
print("="*78)

# --- A = diag(e^{i pi/3}, e^{-i pi/3}, 1, 1):  2cos(pi/3) = 1
A_trace = F(1)                     # lambda + lambda^-1 = 2 cos(pi/3) = 1
A_quad   = poly_of_quadratic(A_trace)        # (t^2 - t + 1) = char poly of the 2x2 block
A_line  = poly_mul(A_quad, poly_mul([F(1),F(-1)], [F(1),F(-1)]))   # times (t-1)^2
print("chi_A(t) = (t^2 - t + 1)(t-1)^2 =", expand(A_line))
paper_A = [F(1), F(-3), F(4), F(-3), F(1)]
print("paper   = t^4 - 3t^3 + 4t^2 - 3t + 1   ->", "MATCH" if A_line == paper_A else "MISMATCH")

# --- B = diag(e^{i th}, e^{-i th}, e^{i th}, e^{-i th}), cos th = 3/4  => 2cos th = 3/2
B_trace = F(3,2)
B_quad   = poly_of_quadratic(B_trace)        # (t^2 - 3/2 t + 1)
B_line   = poly_mul(B_quad, B_quad)
print("chi_B(t) = (t^2 - 3/2 t + 1)^2 =", expand(B_line))
paper_B = [F(1), F(-3), F(17,4), F(-3), F(1)]
print("paper   = t^4 - 3t^3 + 17/4 t^2 - 3t + 1 ->", "MATCH" if B_line == paper_B else "MISMATCH")

# elementary symmetric sums checked independently from eigenvalues
def esym(eigs):
    s=[F(1)]
    for x in eigs:
        s=poly_mul(s,[F(1),-x])
    return s
# A eigenvalues: zeta=e^{i pi/3}, zeta^-1, 1, 1  (zeta+zeta^-1 = 1, zeta*zeta^-1 = 1)
# s2(A) = 4 ; s3(A) = 3 ; s4(A) = 1
s2A = F(2) + F(2)*A_trace
s3A = F(2) + A_trace
print("independent:  s2(A) =", s2A, " s3(A) =", s3A, " s4(A)=det A = 1")
# B eigenvalues zeta,zeta^-1,zeta,zeta^-1 ; zeta+zeta^-1 = 3/2
s2B = F(4) + (B_trace**2 - F(2))
print("independent:  s2(B) =", s2B, "(= 4 + (zeta^2+zeta^-2) = 4 + ((3/2)^2-2) = 4+1/4 = 17/4)")
print("coefficient of t^2 in chi_B = s2(B) =", s2B, "->", "MATCH" if s2B==F(17,4) else "MISMATCH")

# traces and determinants
trA = F(2)*F(1,2) + F(2)          # 2cos(pi/3) + 2
trB = F(4)*F(3,4)                  # 4 cos th
print("tr A =", trA, " tr B =", trB, "-> equal:", trA==trB==F(3))
print("det A = 1 (e^{i pi/3} e^{-i pi/3}), det B = e^{2i th} e^{-2i th} = 1")

# non-conjugacy: eigenvalue multisets differ
zA = np.exp(1j*np.pi/3); zB = np.exp(1j*np.arccos(0.75))
mA = sorted([zA, zA.conjugate(), 1+0j, 1+0j], key=lambda v:(round(v.real,6),round(v.imag,6)))
mB = sorted([zB, zB.conjugate(), zB, zB.conjugate()], key=lambda v:(round(v.real,6),round(v.imag,6)))
print("eig(A) =", [complex(round(v.real,6),round(v.imag,6)) for v in mA])
print("eig(B) =", [complex(round(v.real,6),round(v.imag,6)) for v in mB])
print("multisets differ -> not conjugate in SU(4):", mA != mB)

# also verify numerically with numpy char polys
Anp = np.diag([zA, zA.conjugate(), 1, 1]); Bnp = np.diag([zB, zB.conjugate(), zB, zB.conjugate()])
print("numpy poly A:", np.round(np.poly(Anp),12))
print("numpy poly B:", np.round(np.poly(Bnp),12))

print()
print("="*78)
print("C1b.  Does I_gamma distinguish a loop from its reverse?  (A ~ A^{-1} in SU(4))")
print("="*78)
h = np.array([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)  # double transposition
print("det h =", np.linalg.det(h), " h h* =", np.allclose(h@h.conj().T, np.eye(4)))
hAhn = h@Anp@h.conj().T
print("h A h^-1 =", np.round(np.diag(hAhn),8))
print("A^-1      =", np.round(np.diag(Anp.conj().T),8))
print("A and A^-1 CONJUGATE in SU(4) ->", np.allclose(hAhn, Anp.conj().T))
print("=> the conjugacy class [A] equals [A^-1]; the 'indexical identity' of a loop")
print("   cannot distinguish it from the reversed loop.")
