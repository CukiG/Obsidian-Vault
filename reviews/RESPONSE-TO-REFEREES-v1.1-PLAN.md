# Response to Referees and Revision Plan for v1.1

**Paper:** *Holonomy, Constraint, and the Unity of Opposites: A Categorical Formalization of Indexical Identity*
**Round:** 1 (v1.0, published 22 November 2026) → 4 adversarial referees
**Prepared by:** MiniMax-M3 (MCode), 23 November 2026
**Status:** open — this document is published alongside v1.1 so that the review history is part of the record

---

## 0. Summary of verdicts

| Referee | Specialism | Recommendation | Score | Findings |
|---|---|---|---|---|
| **A** | Category theory, sheaf theory, higher gauge theory | **Major revision** | 4/10 | 40 numbered (6 blocker, 19 major, 15 minor) |
| **B** | Differential geometry, holonomy, mathematical physics | *(pending)* | — | — |
| **C** | Philosophy of science, formal logic, metaphysics | **Major revision** | 4/10 | 5 required revisions + claim-by-clause audit of §12 |
| **D** | Proof checking, line by line | **Major revision** | — | 35 numbered items classified; 19 silent hypotheses catalogued |

**The verdict is unanimous on the central point: the paper's claim that "every theorem is
proved" is false.** Four numbered items have no proof at all, three more are asserted rather
than proved, and the status table certifies as proved items that are not proved. That is a
serious defect and it is stated plainly here rather than buried, because the paper's claim to
be falsifiable cannot be made while its status table overstates what has been established.

**The good news is equally concrete.** The referee that checked the mathematics
*computationally* (D) recomputed every checkable calculation and found it sound: the SU(4)
characteristic polynomials, both traces, the SU(3) trace-completeness argument, the
group-algebra index, and the Heaviside/derivative sign analysis all reproduce exactly as
printed. The failures are concentrated in three places — the sheaf-theoretic section, the
constraint section, and the status/claims layer — not in the algebra.

**Referees A, C and D independently reached the same conclusion on the paper's headline
claim.** Proposition 14 does not derive the essential/contingent distinction; it stipulates
it. That finding alone forces a revision of the abstract.

---

## 1. Convergent findings (two or more referees, independently)

These are the items to fix first. Where a finding is marked BLOCKER, the paper as published
makes a claim that is false or unsupported.

### B1 — BLOCKER — Proposition 14 does not derive the essential/contingent distinction

> **A:** "Definition 13 drops `Φ` and the proof silently uses the product-frame semantics that Remark 6 rejects."
> **C:** "Definition 13 *stipulates* it, the sheaf condition is never used, and the asserted equivalence with the draft's modal formulas fails in **both** directions."
> **D:** "The proof drops the antecedent `Φ →`; the equivalence needs `Φ` true everywhere and accessibility total; and the trichotomy is a purely logical partition of `W_C` using **no** sheaf hypothesis."

The abstract says the distinction is "derivable rather than stipulated". Three independent
readers say it is stipulated. **This must be fixed.** Either the derivation is supplied
(with the missing hypotheses stated and the sheaf condition actually used), or the claim is
withdrawn and the paper says what it actually does: *it gives a precise formalization of
essential and contingent in terms of global versus local sections of a presheaf, and shows
how that formalization relates to — but does not derive — the draft's modal predicates.*

A defensible resolution exists and should be preferred: the theorem is true in a weaker,
honest form ("the trichotomy partitions `W_C`; membership is determined by the
globality-or-locality of the corresponding section"), and the paper's interest is then the
**relationship to the draft**, which requires the missing hypotheses and must be stated as
a conditional.

### B2 — BLOCKER — Theorem 10 is not proved, and is false in the paper's own formalism

> **D:** "On a frame/preorder site `Γ(𝔉_C, A) ≅ A(top)`, so `A(u) ≠ ∅` for all `u` (including top) *does* imply `Γ ≠ ∅`. The phenomenon needs a locale/topological site."
> **A:** "Theorem 10 has no proof — its proof asserts the claim, no site is specified, contexts/stalks/opens are conflated, and the étale space is never used."

The statement that descends to `Π₁(M)` is the paper's central "corrected" claim about
curvature, and the corrected CTT indicator `β*(Φ) = 1 ⟺ Γ(𝔉_C, A) = ∅` depends on it.
Repair: specify the site (a locale, not a frame), state the theorem on a *locale/topos*
site where the étale space is genuine, and give the Čech `H¹` obstruction. Add the counter
example that shows the frame-site version is vacuous.

### B3 — BLOCKER — Theorem 11 clauses (ii)–(iii) are unproved or circular

> **C:** "The proof establishes only 'an inclusion is a monomorphism'; the clauses about unchanged dynamics and about CTT are unproved (and (ii) is false in general)."
> **D:** "No dynamics exists in the formalism, so 'the equations of motion are unchanged' has no content; (iii) assumes 'no constructor and no law' in order to conclude it, and imports 'energy' into a theory (CTT) that has none."

**Split the theorem.** Keep the monomorphism clause, which is proved. Demote the rest to a
stated modelling assumption, or drop it. As it stands, §12(i) ("via negativa is neither
trivial nor question-begging") does not follow from what was shown.

### B4 — BLOCKER — the status table certifies as proved items that are not

> **A:** "The §11 status table misstates six of its own rows — including 'SU(3) counterexample' for an SU(4) example, and a 'non-additivity of constraint' theorem that does not exist."
> **D:** "Status table rows 2/5/9 are misstated: 'SU(3) counterexample' is SU(4); Theorems 10, 11 and 23 are not proved."
> **C:** "§11 row 6."

The §11 table is the paper's honesty guarantee. It has to be right. Every row must be
re-checked against D's verdict table.

### B5 — BLOCKER — "every theorem is stated with a proof" is false

> **D:** "Four numbered items have no proof, three more are asserted rather than proved, and the status table certifies as proved items that are not."
> **A:** "Theorem 12, Observation 19, Observation 24 and Consequence 20 have none."

The claim appears in the abstract, in §11, in §14 and in `README.md`. It must be corrected
everywhere it appears, or the missing proofs must be supplied. The authors' note in the
paper says *"No model is treated as an authority for any mathematical claim in this paper:
every theorem is stated with a proof"* — that sentence is currently false and must be fixed.

### B6 — BLOCKER — the curvature regime is contradictory

> **A:** "§5 declares Lie-algebra-valued curvature 'mutually exclusive' for this framework, and §9.3 then writes `𝓖 = d𝒜 + 𝒜∧𝒜`, while §3 defines the connection on `Π₁(M)` so that curvature is identically zero in the framework's own model. One regime must be chosen."
> **C:** the same contradiction, phrased as "resolve the contradiction between the adopted descent-formalism and the retained 1-form/`F = dA + A∧A`/Pesin machinery."

Also: §2's claim that "holonomy is non-additive … not reducible to the holonomies of its
parts" is false as stated — holonomy is order-sensitive, not non-additive. Fix the wording.

### B7 — MAJOR — the "2-group" inference is invalid

> **A:** "'A product of a Lie group with an ∞-groupoid is a 2-group' is invalid. 2-truncation is required, the §11 hedge 'contingent on `𝔓∞` being an ∞-groupoid' is vacuous, and no crossed-module or principal 2-bundle is ever constructed. Remark 3b's 'exactly the machinery needed' over-extends Zucchini, whose 2-trace is by construction a lossy quotient of the 2-holonomy."

Construct the crossed module (or state the hypothesis and cite it), or drop the claim to a
proposal. Remark 3b must be rewritten: Zucchini's machinery is *sufficient* and its 2-trace
is *lossy*, which is not "exactly what is needed".

### B8 — MAJOR — the notation repair is incomplete

> **A:** "The advertised symbol repair assigns `𝔊` to both the structure groupoid and an interval curvature in Appendix A's own table, and leaves §8's paragraph using the pre-repair names `𝒜, 𝒫, 𝓕`."
> **D:** "Three 'G's unreconciled — the defect the paper charges the draft with."

v1.0 already separated the structure groupoid (`𝔊`) from the interval curvature (`𝓖`), but
Appendix A's table and §8 were not updated. **The paper must not commit the error it
charges the draft with.** A full notation audit is required, not a spot fix.

### B9 — MAJOR — the falsifiability claim must be retracted

> **C:** "No falsifiable proposition, no empirical consequence. The abstract and README claim the framework can be falsified; §12 must say what would count as a counterexample, and there is currently none."

The framework is a formalization: it constrains what a future physics must look like, but
it does not itself make testable predictions. The honest claim is **"checkable and
refutable by argument, not by measurement"** — and even that needs the §13 threats expanded.

---

## 2. Single-referee findings, grouped by severity

### Math corrections (from D, all independently recomputed)

| Item | Finding | Repair |
|---|---|---|
| Thm 4 | **MISSTATED.** "`P̃` is a functor, so no 'commutator-region' factor can appear — the paper's own category-error charge against the draft." Its "i.e." clause is either vacuous (by Thm 1(ii)) or weaker than descent. | Define "flat" independently of descent; delete the "i.e."; drop the commutator-region phrasing. This is a self-inflicted version of the error the paper corrects in the draft. |
| Thm 23(2) | "A sign-consistency argument dressed as a corrected formula. The `1/λ` factor is derived from nothing; Pesin does not supply it." | Either derive the factor or present the corrected equation as a *shape* constraint, not an identity. |
| Thm 23(3) | "A sign slip: `dD/dα = −Σδ`, not `+Σδ`." | Fix the sign and re-verify. |
| Consequence 20 | "Misdiagnoses a numerically **true** draft identity: `dim_ℂ(ℂ[G] ⊗_{ℂ[H]} ℂ) = [G:H]`. The defect is the 'Hopf' label and the 2-holonomy codomain, not the identity." | Rewrite the correction. The paper currently claims a numerical error where there is only a mislabel — this is an over-claim in the paper's own direction and must be fixed. |
| Obs 24 | "MISSTATED. The displayed ladder contradicts the paper's own renaming (App. A); the claimed pattern is never shown; 1-form = 2-form." | Rewrite or downgrade to a remark about the intended pattern. |
| Thm 1(ii) | Circular: the proof assumes "which we assumed". | Replace with the conjugation lemma plus the Wess–Zumino hypotheses and a nice homotopy region. |
| Thm 5 | Hypotheses unstated: `Q` smooth finite-dimensional, `P_t` a *smooth submersion*, leafwise integrability, `t` fixed. | Add the hypotheses. |
| Thm 9 | Proven but **vacuous**: local emptiness is not Constructor-Theory impossibility (which is global). | Say so, and distinguish local from global impossibility. |
| Def 1 / Prop 3 | `τ` requires `hol(γ)` to be matrix-valued. | State it. |
| Def 7 | `𝔠`/`C` collision; `□_C^cross` undefined; `R_C` must be a preorder. | Fix. |
| Def 13 | "Irrelevant" undefined; the partition not stated. | Fix. |
| Fact 16 | Axioms mis-stated and partly ill-typed (`u∘j = id` has the wrong type). Standard: `j∘⊤ = ⊤`, `j∘j = j`, `j∘∧ = ∧∘(j×j)`, with `j` natural. | Restate. |
| Obs 19 | Conditional on `𝔓∞` genuinely being higher; "2-groupoid" vs "2-group"; reconcile `G`/`𝔤`/`G_c`. | Fix. |
| Prop 22 | `G`, `H(α)` must be finite; "disjoint union of orbits" does not apply to `G/H`. | Fix. |
| Def 21, Def 8, Remark 6, Remark 3a, Prop 3's computation, Thm 1(i), Thm 1(iii), the abstraction condition | **PROVEN.** | No action. |

### Nineteen silent hypotheses

D's most valuable contribution is a catalogue of hypotheses that appear in proofs but not in
statements: site structure and coverage of `𝔉_C`; contexts as atoms/opens with genuine
covers; `Φ` true at every context with total accessibility; existence of a transport on
`X(u)`; `𝔤` group-like and "flat" independent of descent; `Q` smooth finite-dimensional with
`P_t` a submersion and leafwise integrability; Wess–Zumino and a nice homotopy region;
`hol(γ)` matrix-valued; well-typedness of `g_x^{-1}hol(γ)g_x`; finiteness of `G` and `H(α)`;
`𝔓∞` genuinely higher; `α_i > 0`, `N = 7`, fixed axis orientation; `𝒞` compatible with
componentwise relations; `j` natural; `W_C ≠ ∅`; the draft notes being available to check;
the identification of "pointer" with conjugacy class; the type-level identification
`𝒞 = ℱ`; and `G` of Part V being the structure groupoid of Part I.

**Every one of these belongs in the statement it is used in.** This is mechanical, and it is
the single cheapest way to move the paper from "4/10" to something defensible.

### Cross-references and the correction log

D found a broken cross-reference ("Remark 14" does not exist) and that the correction log
is §18, not §16. The `SU(3)`/`SU(4)` mislabelling also appears in the correction log row 2
and in `README.md`.

---

## 3. Findings from the editor's own prior-art check (not from the referees)

A separate check — the one a hostile reviewer does first — searched for prior work
overlapping the paper's core moves. It found substantial **uncited** literature. This is
independent of the referees' findings and must be addressed in v1.1's §10 and §1.

| Prior work | Overlap with this paper | Where it should be cited |
|---|---|---|
| **Abramsky & Brandenburger**, *The sheaf of quantum states* (arXiv:1110.1843) | Contextuality as **absence of a global section** — the exact mechanism of §6.3 | §6.3, §10 |
| **arXiv:2105.14132**, *Contextuality in the Fibration Approach and the Role of Holonomy* | Holonomy tied directly to global-section failure | §4, §6.3 |
| **Aof & Brown** (1992), *The holonomy groupoid of a locally topological groupoid*; **Pradines** (1966) | The holonomy groupoid and its globalisation theorem | §2, §4, §6 |
| **arXiv:2507.01226**, *Obstructions to Reality: Torsors & Visual Paradox* | Torsors: no global section ⟺ obstruction to globalising local data | §6.3 |
| **arXiv:2607.15629**, *A cubical formalisation of topos causal models* | Machine-checked contextuality obstruction; Čech `H¹`; holonomy as obstruction | §6.3, §9.3 |
| *Homotopic Identities and the Limits of the Interpretation of Gauge Symmetries as Descriptive Redundancy* (Springer, 2020) | Groupoid-theoretical reconceptualisation of **equality**; category of *identity*; Leibniz's identity of indiscernibles | §1, §4 — **this is the closest published treatment of the paper's central §4 claim** |
| arXiv:1505.07084, *Categories and the Foundations of Classical Field Theories* | Holonomy formalism vs. fibre-bundle formalism; relationalism vs. substantivalism on identity | §1.2.3, §4 |
| *Rethinking Constitutive Metaphysics* (PhilArchive) | Local structure → global realization template; extension classes; an "indexical bridge" | §6.3, §7 |
| *The Formalization of Dialectics* (Taylor & Francis, 2023; Priest, d'Agostini, Redding, Beall & Ficara, Nuzzo, Moss) | Formalising the **unity of opposites** in paraconsistent logic | §7, §9, §12 — **the paper's title claim** |

**Consequence for §1.** The paper's contribution statement must not imply that the
groupoid-theoretic treatment of identity, the sheaf-obstruction mechanism, or the
formalisation of dialectical relations are new. The paper's genuine contributions are the
*corrections*, the *explicit 2-group upgrade with its conditions*, and the *proved
impossibility results* — and they should be stated as such. Referee C's independent verdict
("zero philosophical literature") supports this.

---

## 4. Prioritised revision plan for v1.1

### Tier 1 — must change before any further dissemination (the abstract's claims)

| # | Action | Sections |
|---|---|---|
| 1 | Rewrite the abstract: drop "derivable rather than stipulated"; drop "every theorem is stated with a proof"; drop the falsifiability claim | Abstract |
| 2 | Supply or downgrade Proposition 14 (B1) | §6.4, Definition 13 |
| 3 | Restate Theorem 10 on a locale/topos site; add the frame-site counterexample (B2) | §6.3 |
| 4 | Split Theorem 11 into the proved monomorphism clause and an explicit modelling assumption (B3) | §6.3 |
| 5 | Rewrite the §11 status table against D's verdict table (B4) | §11 |
| 6 | Correct the authors' note in §14 and the same claim in `README.md` (B5) | §14, README |
| 7 | Resolve the curvature regime: pick descent-formalism **or** 1-form formalism and say so (B6) | §5, §9.3, §3, §2 |
| 8 | Fix Theorem 4's mis-statement — including deleting the commutator-region phrasing (D) | §5 |
| 9 | Fix Theorem 23(2) and the sign slip in 23(3); rewrite Consequence 20 (D) | §9.2, Appendix C |
| 10 | Withdraw or reconstruct the 2-group inference (B7) | §8, Remark 3b, Observation 19 |
| 11 | Full notation audit (B8) | §8, Appendix A, throughout |
| 12 | Retract the falsifiability claim; expand §13's threats (B9) | §13, §12 |
| 13 | Add the missing prior art; requalify the contribution statement | §1, §10, References |
| 14 | Write proofs for Theorem 12, Observation 19, Observation 24, Consequence 20, or downgrade each | §6.3, §8, §9.3, §9.1 |
| 15 | Add the 19 silent hypotheses to the statements that use them | throughout |

### Tier 2 — quality

Fix Theorem 1(ii)'s circularity; add Theorem 5's hypotheses; state that Theorem 9 is local
rather than global impossibility; fix Definitions 1, 7, 13; restate Fact 16's axioms and
types; add finiteness to Proposition 22; fix the cross-references and the correction-log
numbering; fix the `SU(3)`/`SU(4)` mislabelling in the correction log and README.

### Tier 3 — presentation

Add the 19-hypothesis appendix; add a "Claim → Status → Evidence" table so a reader can
audit the paper's own claims; number every proposition and observation that currently has
no number.

---

## 5. What the referees did *not* attack

Worth stating, because it tells us what to keep.

- The **entire computable core** — SU(4) counterexample, characteristic polynomials,
  traces, the SU(3) completeness threshold, the group-algebra index, the Heaviside and
  derivative sign analysis — recomputes exactly as printed (Referee D, independently).
- **Theorem 1(i) and (iii)**, **Definitions 8 and 21**, **Remark 3a**, **Remark 6** and the
  **abstraction condition** are proved.
- **Theorem 4's underlying idea** is right even though its statement is not.
- The **correction log's instinct** is sound — the draft formulae really are defective — but
  two of the diagnoses are over-claims (Consequence 20) or under-derivations (Theorem
  23(2)) and must be adjusted.
- The **framing of the paper's ambition** was not criticised as grandiose; it was
  criticised as *insufficiently defended*, which is the better failure to have.

---

## 6. Bottom line

v1.0 overclaims. Specifically, three claims in the abstract are false or unsupported: that
the essential/contingent distinction is derived rather than stipulated, that every theorem
is proved, and that the framework can be falsified. Everything computable in the paper is
sound.

v1.1 should therefore do three things, and nothing else:

1. **Say what the paper actually establishes**, and withdraw the three claims above.
2. **Repair the four unproved items and the mis-stated theorem**, which is weeks of work
   in anyone's hands but is bounded here.
3. **Concede the prior art** and reframe the contribution as the corrections, the
   conditional 2-group upgrade, and the impossibility results.

That is a smaller paper than v1.0 advertised, and a better one. The framework's survival
does not depend on the overclaims: the corrections are real, the SU(4) counterexample is
real, the descent-obstruction theorem is real, and the impossibility results are real. A
reviewer who cannot catch the paper out on an unsupported claim is not reading carefully,
and this round has now shown that the careful readers are looking.
