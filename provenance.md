---
title: "Provenance and Attribution Table"
subtitle: "Companion to Holonomy, Constraint, and the Unity of Opposites (v1.0)"
date: 2026-11-22
status: preprint
---

# Provenance and Attribution Table

Companion to **Holonomy, Constraint, and the Unity of Opposites: A Categorical Formalization
of Indexical Identity** (v1.0).

Author of record: **Nicolai Gamulea Schwartz** (GitHub handle `CukiG`). Written by **MiniMax-M3 (MCode)**.

## How to read this table

The source corpus for this framework consists of **dialogue transcripts** — working notes in
which a human originator and several AI systems alternate turns, each turn marked with the
speaker's name — plus model-generated digests of those transcripts. Consequently:

- **Source** names the working note in which a claim appears, using the framework's own
  session naming (`Framework at work 1` … `Framework at work 6`).
- **Speaker** names who made the claim in that transcript.
- **Status in the paper** records what the present paper does with it: *proved here*, *cited*,
  *repaired*, *reclassified*, or *not relied upon*.

Two conventions are used throughout:

- **[R]** = the claim is **repaired** in the paper; the paper's statement replaces it.
- **[N]** = the claim is **not relied upon**, and the paper says so.

The paper's §14 gives the same information in author-credit form. This file gives it in
claim-by-claim form, with the caveats attached.

---

## 1. Claims originating with the human originator

These are the framework's own conceptual commitments, and they survive into the paper intact.

| Claim | Source | Speaker | Status in the paper |
|---|---|---|---|
| Indexical identity as a persistent pointer to a causal thread, distinct from numerical identity | Working notes, Sessions 1–2 | originator | **Cited** and formalized (§4.1) |
| The constraint specification `P_t : TQ → 𝔤` a submersion, with `Σ_t := ker P_t` the sub-bundle of admissible velocities, and the gloss "the field does not add energy; it removes forbidden directions" | Working notes, Session 1 (constraint passage) | originator | **Cited verbatim** as the framework's own local formalization (§6.1); the paper adds the global half |
| `κ = ‖[F, P]‖`, the author's own extension of the "causal torque" commutator into a quantity | Working notes, Session 1 | originator | **Cited** as the author's extension (§6.2, §6.3) |
| The instruction to pursue a modal-logical plus assembly-theoretic formalism, and the question "what constituents are essential for an observed outcome?" | Working notes, Session 1 | originator | **Cited** as the origin of the Kripke-frame construction (§14, provenance.md §3) |
| The aggregation tower as an index `k` of increasingly aggregated levels | Working notes, Sessions 2–5 | originator | **Cited** in §10 (the correspondence with Constructor Theory's locality principle) |

---

## 2. Claims made by AI systems, and their treatment in the paper

### 2.1 Repaired

| Claim | Source | Speaker | Why it was repaired | Repair |
|---|---|---|---|---|
| "Curvature = failure of `𝒫` to preserve composition" | Session 3 | Kimi K2 | Category error: a functor preserves composition by definition, so no functor can fail to | §5, Theorem 4: curvature is the obstruction to descent of parallel transport to `Π₁(M)` |
| "`𝔤 = Lie algebroid of 𝔓`" alongside "`𝔓∞` = ∞-groupoid of indexical pointers" | Session 3 (Lie algebroid); Session 4 (`𝔓∞`) | Kimi K2 | `𝔓` denotes incompatible structures, and a Lie algebroid has no meaning for an ∞-groupoid | §8, §9.3: the renames separate the label groupoid from the pointer ∞-groupoid |
| "curvature becomes a functor rather than a Lie-algebra-valued 2-form" | Session 3 | Kimi K2 | The passage correctly identifies that a discrete structure group admits no connection 1-form, but the draft retained `F = dA + A∧A` anyway | §5: the descent formulation is adopted; the 1-form formulation is dropped for this framework |
| "An abstraction event exists iff there is a lossless (or bounded-loss) morphism … preserving its `Iγ` up to equivalence" | Session 3 | ChatGPT | This is a **review item** — a model asking the originator to supply a criterion that was never supplied. "Bounded loss" is undefined anywhere in the corpus | §4.3: the condition is rewritten as injectivity on conjugacy classes, and the loss criterion is separated from the identity criterion (§8, §9) |
| `\|G/H(α)\| = dim{Hopf}(ℂ[G] ⊗_{ℂ[H]} ℂ)`, glossed as "linearly independent holonomy eigenvalues" | Session 4 | Kimi K2; reinforced by Gemini | Conflates the coset count, the sector count, and eigenvalues; the "Hopf" framing is inapplicable because `G` is not a group | §9.1, Proposition 22 |
| `D(α) = 1 + Σ Θ(α − α_i)` with "D ↘ 1 as α → ∞", and `dD/dα = −(1/λ) d/dα log\|G/H(α)\|` | Session 4 | Kimi K2 | The Heaviside argument is not negated; the derivative's sign contradicts the stated behaviour; `dD/dα` is a distribution, not a function | §9.2, Theorem 23 |
| The interval ladder, in which the symbol `ℱ` denotes four different objects | Session 3 | Kimi K2 | The collision made the ladder unreadable and concealed that it is a recursion | §8, §9.3: potentials `𝒜, ℬ, ℭ`; curvatures `ℱ, 𝒢, ℋ` |

### 2.2 Cited as structure, without repair

| Claim | Source | Speaker | Status in the paper |
|---|---|---|---|
| Multi-layer Kripke frames `𝔉_M, 𝔉_F, 𝔉_T`; graded assembly functor `A`; the essential and "necessary" predicates | Session 1 | Kimi K2 | **Cited** (§6.3, §6.4). The predicate labelled "necessary" is a contingency formula and is renamed; the semantic content is retained |
| The groupoid-bundle construction: indexical label fibers, re-labelling as gauge transformation | Session 3 | Kimi K2 | **Cited** (§3, §5) |
| The structure group `G = ISO(1,3) ⋉ ℝ⁴ × U(1) × 𝔓∞` and the pointer ∞-groupoid `𝔓∞` as "identity grammar" | Session 4 | Kimi K2 | **Cited** (§8), with the 2-group consequence drawn out |
| The α*/β* classifier family, `β* = ¬∃ℓ ∈ C_ont : □_ℓ Φ` | Session 1 | Grok | **Cited** (§10), with `β*` redefined as the descent obstruction |
| The "causal torque" commutator `[F, P]` | Session 1 | Kimi K2 | **Cited** (§6.2, §6.3) and given a typed reading |
| The symmetry-breaking pattern along the axis, and the connection fields assigned to shrinking groups | Session 4 | Kimi K2 | **Cited** (§9.2) |
| The ladder detector and the PCA formulation of the tower's compression operator `C_k` | Session 5 | Gemini, Kimi K2 | **Cited** (§10) — and correctly labelled a *statistical* construction rather than a categorical one |
| The "α-bounce" deconstruction and the "persistent background / local emergence" revision of the axis | Session 6 | Gemini 2.5 Pro | **Cited** as an unresolved tension (§9.2, §13.3). The paper does not adopt either orientation |

### 2.3 Not relied upon

| Item | Source | Speaker | Note |
|---|---|---|---|
| The Grok-associated framework synthesis paper | Papers | Grok 4.1 | A model-written synthesis, not a source of mathematical claims here |
| The model-written "theoretical synthesis" paper | Papers | Gemini | Same: a digest of the originator's notes, not an independent source of claims |
| The super-selection-sector remark "the next natural step is to quantize the restriction field …" | Session 1 | Kimi K2 | **Not relied upon as a commitment** — it is phrased as a suggestion for future work. The paper's sector-counting result (§9.1) is derived independently |
| Critique of the groupoid claims ("add a one-line precise object") | Session 3 | ChatGPT | Read as a review item; the paper's Theorem 4 is the "one-line precise object" that was asked for |
| Session-6 cosmology revision | Session 6 | Gemini 2.5 Pro | Flagged as unresolved (§13.3) rather than adopted |
| Single-turn contributions in Sessions 1, 2, 6 by DeepSeek, Perplexity, Sonoma Sky Alpha, and Gemini 3.0 Pro | Sessions 1, 2, 6 | various | No specific claim relied upon |

---

## 3. The modal-assembly construction: the one case where the record is decisive

This is worth setting out in full, because it is the case in which the corpus most clearly
distinguishes *request* from *implementation*, and in which a synthesis step can most easily
reverse the attribution.

| Turn | Speaker | Content |
|---|---|---|
| 1 | originator | Asks what kind of mathematical or logical formalism can express the layered causality, and proposes "modal logic (with some tweaks), perhaps supplemented with assembly theory"; asks what constituents are *essential* for an observed outcome. |
| 2 | Kimi K2 | Proposes and implements the modal-assembly hybrid: each causal layer as a separate Kripke frame, stitched by an assembly functor recording which parts are essential (in all accessible worlds) versus merely necessary; writes the `Essential` and `Necessary` predicates. |
| 3 | Grok | Labels the result, in a comparison table, as "Kimi K2's latest proposal — a modal-assembly hybrid formalism using multi-layer Kripke frames …, an assembly functor …". |

**Reading.** The construction is *author-requested and model-implemented*, and it was
labelled as a proposal by a third model. It should therefore be **promoted**, not demoted:
the originator chose the direction, the model supplied the formalization, and a peer
model reviewed it in proposal terms. The paper treats it accordingly: §6.3 and §6.4 build
on it, with the one substantive repair (renaming the "necessary" predicate, §6.4).

**Why this case is instructive.** A synthesis step that reports only the second turn
presents a *reviewer's* label as a *framework's* status, and thereby invites the reader to
discount a piece of the framework that the originator had in fact asked for. The moral for
anyone building on multi-model transcripts: **the turn structure is evidence, and any
process that flattens transcripts loses it.**

---

## 4. Mathematical statements introduced by this paper

Everything in the following list is **proved in the paper** and does not depend on any
source material. In each case the proof is short and self-contained.

| # | Statement | Section |
|---|---|---|
| Theorem 1 | Gauge- and homotopy-invariance of the holonomy class | §4.2 |
| Corollary 2 | The "pointer survives" reformulation | §4.2 |
| Proposition 3 | The trace is not a complete conjugacy invariant, with an `SU(4)` counterexample | §4.3 |
| Remark 3a | In `SU(3)` the trace *is* complete: `s₂ = s̄` is forced, so the characteristic polynomial is determined | §4.3 |
| Theorem 4 | Curvature as the obstruction to descent of parallel transport | §5 |
| Theorem 5 | Frobenius integrability as the local obstruction to constraint consistency | §6.2 |
| Remark 6 | Iterated modality over a product of frames encodes layer-independence | §6.3 |
| Definition 7 | The composite constraint frame | §6.3 |
| Definition 8 | The assembly as a sheaf of admissible states | §6.3 |
| Theorem 9 | Impossibility as emptiness of the admissible sheaf at a context | §6.3 |
| Theorem 10 | The descent obstruction: local admissibility does not imply global realization | §6.3 |
| Theorem 11 | Via negativa: the constraint is a monomorphism and adds no energy, constructor, or law | §6.3 |
| Theorem 12 | The unity of opposites as the pair (constraint distribution, its failure of commutation with the dynamics) | §6.3 |
| Definition 13 / Proposition 14 | Essential and contingent, derived from global versus local sections | §6.4 |
| Fact 16 | Lawvere–Tierney topologies as interior operators, in bijection with geometric endomorphisms | §7 |
| Observation 19 / Consequence 20 | The structure group is a 2-group, and the required upgrades | §8 |
| Definition 21 / Proposition 22 | Coset count versus sector count | §9.1 |
| Theorem 23 | Three defects in the dimensional-explosion formulae, with corrections | §9.2 |
| Observation 24 | The interval ladder is a recursion | §9.3 |

---

## 5. Notes on method

**Two mis-attributed references were caught during verification and corrected before
publication.** An earlier draft attributed `arXiv:hep-th/0412325` to Grandis and Foli; it is
in fact Baez and Schreiber, *Higher gauge theory: 2-connections on 2-bundles*. The same
draft attributed `arXiv:0710.4310` to Grandis and Foli and `arXiv:1505.02122` to an unnamed
pair of authors; they are in fact Martins and Picken, *On two-dimensional holonomy*, and
Zucchini, *On higher holonomy invariants in higher gauge theory II*. All three are now
attributed correctly in the reference list.

**One algebraic claim was caught by computation rather than by reading.** An earlier draft
offered an `SU(3)` pair of non-conjugate elements with equal trace as the counterexample in
Proposition 3. Such a pair does not exist: in `SU(3)` the trace is a complete invariant of
conjugacy classes, because unitarity and determinant one force the second symmetric sum to
be the complex conjugate of the trace, and hence determine the characteristic polynomial.
The counterexample was replaced by an `SU(4)` pair, and the `SU(3)` fact was promoted to
Remark 3a, since the threshold at which traces become lossy is itself informative.

**On the status of models as witnesses.** No claim in the paper rests on a model's
authority. Where a claim is attributed to a model, the paper's use of it is either
(a) as a *structural* commitment the paper then formalizes, or (b) as a *defect* the paper
repairs. In no case is a model's assertion treated as evidence that a mathematical statement
is true.

**On what a reader can check.** Every theorem, proposition, definition and observation in
§§4–9 is stated with a proof or an argument that requires no access to the source corpus,
no access to the working notes, and no trust in the transcription. A reader who rejects the
entire underlying framework may still check the mathematics, and §13 lists the six ways in
which the formalization may nonetheless fail to capture its intended notion.

---

## 6. Repository contents

| File | Contents |
|---|---|
| `README.md` | Abstract, summary, author credits with versions, claim-status table, citation |
| `paper.md` | The full paper |
| `paper.pdf` | Rendered PDF |
| `provenance.md` | This file |
