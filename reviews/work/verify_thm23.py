import numpy as np
from fractions import Fraction as F

print("="*78)
print("C4.  THEOREM 23 -- independent recomputation of the 'corrected' pair")
print("="*78)
print("(a) STEP SIGN.  Draft:  D(α)=1+ΣΘ(α-α_i)  -> non-decreasing in α.")
print("    Corrected:   D(α)=1+ΣΘ(α_i-α) -> non-increasing.  Numeric check:")
def D(alpha, ais, neg=True):
    return 1 + sum(1.0 if ((ai-alpha) if neg else (alpha-ai)) >= 0 else 0.0 for ai in ais)
ais = [1.0, 2.0, 3.0]
xs = [0.5, 1.5, 2.5, 3.5]
print("     α          draft D(1+ΣΘ(α-α_i))   corrected D(1+ΣΘ(α_i-α))")
for x in xs:
    print("   %6.2f      %8.2f                  %8.2f" % (x, D(x,ais,neg=False), D(x,ais,neg=True)))
print("     -> draft is non-decreasing (wrong asymptotics); corrected -> 1 as α->inf:",
      D(1e6,ais,neg=True), "== 1 ->", D(1e6,ais,neg=True)==1.0)
print("     -> corrected D(α->0-) =", D(-1e-6,ais,neg=True), "(the draft's 'D->8' needs exactly 7 steps)")

print()
print("(b) DERIVATIVE SIGN of the corrected STEP (distributional).")
eps=1e-9
for ai in ais:
    jump = (D(ai-eps,ais,neg=True) - D(ai+eps,ais,neg=True))/(2*eps)
    print("     d/dα of Θ(α_i-α) at α=%s  -> jump in D = %+.1f  (a DROP) => dD/dα = -Σ_i δ(α-α_i)" % (ai, jump))
print("     paper's text says:  dD/dα = Σ_i δ(α − α_i)      <-- SIGN ERROR in the paper's own item (3)")

print()
print("(c) DOES THE 'CORRECTED' IDENTITY HOLD?  dD/dα = +(1/λ) d/dα log|G/H(α)|")
print("    Read both sides as distributions: they agree iff (i) the step locations")
print("    coincide and (ii) every breaking step multiplies |G/H| by exactly e^λ.")
def weights(chain, lam):
    # chain = list of indices |G/H| at successive break points (decreasing)
    w = []
    for i in range(len(chain)-1):
        w.append(np.log(chain[i]/chain[i+1])/lam)
    return w
print()
for name, chain, lam in [("uniform  8->4->2->1, λ=log2", [8,4,2,1], np.log(2)),
                         ("uniform  8->4->2->1, λ=log8/7", [8,4,2,1], np.log(8)/7),
                         ("NON-UNIFORM 12->6->3->1, λ=log2", [12,6,3,1], np.log(2)),
                         ("NON-UNIFORM 12->6->3->1, λ=log8/7", [12,6,3,1], np.log(8)/7)]:
    w = weights(chain, lam)
    print("  %-38s LHS weights (unit steps) = %s" % (name, [1.0]*len(w)))
    print("  %-38s RHS weights (log r / λ)   = %s   -> %s" % ("", [round(x,4) for x in w],
          "MATCH" if all(abs(x-1)<1e-9 for x in w) else "MISMATCH -> the identity is FALSE"))
print()
print("  smooth antiderivative:  D(α) = C + (1/λ) log|G/H(α)|.  With |G/H(α)|->1 as α->inf,")
print("  D(α)->C, so the asymptotic D->1 forces C=1 -- an UNSTATED integration constant:")
for chain,lam in [([8,4,2,1],np.log(2))]:
    print("    with C=1 and λ=log2:  D(α) = 1 + (1/log2) log|G/H(α)|  takes values",
          [round(1+np.log(c)/lam,4) for c in chain], "(continuous & non-integer between steps)")
print("    the step definition D = 1+ΣΘ(α_i-α) takes values", [8,4,2,1], "-> the two 'corrections'")
print("    of Theorem 23 are the SAME formula only in the uniform-ratio case.")
