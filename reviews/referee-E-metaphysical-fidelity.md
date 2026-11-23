# Referee E — Metaphysical Fidelity Review and v1.1 Repair Targets

**Reviewer:** Z.ai (GLM) — independent reviewer from outside the MiniMax-M3 referee pool (different model family, different organization).
**Date:** 2026-11-23
**Scope:** The fidelity of the formal apparatus to the author's metaphysical construct. This is not a proof-check (Referee D), not a geometry check (Referee B), not a general philosophy audit (Referee C). The question here: does the mathematics encode what the author of record means — and where it does not, what exactly would repair it?
**Inputs:** paper.md v1.0; referee reports A–D as published in this directory; the prior-art check recorded in the response plan; and a direct statement of the essential/contingent distinction from the author of record (2026-11-23), quoted in §1.
**Verdict:** Major revision — the same verdict as the pool, on different grounds. The three bridge claims, where the formalism purports to earn metaphysical content, do not encode the construct as the author states it. The construct itself is in good order and — a point the pool did not reach — supplies precisely the falsifiability content Referee C found missing. Repair targets are given in §5, in implementable form.

## 1. The construct, restated from the author's own words

The author of record states (2026-11-23):

> An essential condition is one that must be satisfied (it's necessary) in all possible worlds, because an essential aspect of the outcome depends on it. It has no functional equivalent. A simply "necessary" condition is one that's necessary within a certain configuration (a certain world), where that configuration is sufficient to produce the outcome. Example: a brain is a necessary condition for human minds, but it's not an essential condition for a mind.

Reconstructed, this is a graded structure over conditions C for an outcome O:

1. **Necessary** (configuration-relative): within some configuration W sufficient for O, O does not occur without C. Necessity is indexed to a world.
2. **Essential** (absolute): across all possible worlds, O does not occur without C — equivalently, no functional equivalent for C exists: no world realizes O by other means.
3. **Contingent**: the residual grade — whatever is neither.

Four observations that the v1.1 rewrite must respect:

**Observation 1 — the operative clause.** Under the natural reading, "no functional equivalent" and "holds in all possible worlds" state the same condition twice: a functional equivalent just *is* a possible world realizing O without C. The functional-equivalence formulation is the operative one, because it names the test procedure: to refute an essentiality claim, exhibit one world; to support it, argue invariance over the whole modal space. The paper should present the two clauses as criterion and truth-condition, not as independent marks.

**Observation 2 — outcome individuation.** The author's example slides between two outcomes — "human minds" and "mind" — and the slide is load-bearing. For a functionally individuated outcome, no substrate is essential *by definition* (whatever realizes the role counts). For a realization-indexed outcome (this mind, anchored to this process), the substrate may be essential even on functionalist premises. Every essentiality claim must declare the individuation level of its outcome; ambiguity here silently converts a substantive claim into a tautology or a triviality.

**Observation 3 — invariance vs. dependence.** The author's gloss contains both an invariance clause ("must be satisfied in all possible worlds") and a dependence clause ("an essential aspect of the outcome depends on it"). These can come apart (Fine 1994). The wording suggests dependence is fundamental for the construct, with modal invariance as its evidence. The formalization must choose which reading it encodes, and say so.

**Observation 4 — the third grade is not in the author's statement.** The quoted statement defines two grades; the paper claims a trichotomy. The third cell ("contingent") is a reconstruction, not something the author has committed to. v1.1 must either give the residual grade explicit content of its own or stop presenting the result as a trichotomy. This is flagged because a quiet addition of structure the construct never stated is exactly how a "derived" result becomes a stipulated one.

## 2. Fidelity findings against paper v1.0

**F1 — Definition 13 / Proposition 14: the central failure, diagnosed from the construct side.** Referee D established the formal facts: the antecedent Φ → is dropped, the equivalences silently assume "Φ true at every relevant context" and "accessibility total," the sheaf condition is never used, and the trichotomy holds for any family of sets. From the fidelity side the diagnosis is sharper: **the author's distinction is constitutively indexical.** Its entire content is the contrast between necessity-indexed-to-a-configuration and invariance-across-all-configurations. A definition that does not relativize its necessity operators to contexts cannot encode the distinction at all; unindexed, it collapses into a logical truth — which is precisely what Referee D found. The dropped antecedent is not a typo; it is the missing index.

**F2 — Theorems 10, 11, 4: the via negativa anchor.** The author's via negativa — a higher cause operates by deleting directions, not by adding energy — is the construct's causal heart, and it is well-aligned with real mathematics: in gauge theory, deleting directions is what a **reduction of the structure group** is (a constraint that removes allowed transitions rather than adding a force term), and curvature-as-obstruction-to-flatness is the canonical obstruction pattern. Alignment of metaphor and concept is the paper's strongest asset. But alignment is not derivation: Referee D rates Theorems 10 and 11 NOT PROVEN, and Theorem 4's proof rests, per the response plan's record, on an impossible object — a "functor that fails to preserve composition," which cannot exist by definition (what can fail is faithfulness, fullness, or preservation of limits — not functoriality itself). As stated, the paper has a metaphor with theorem numbers on it.

**F3 — §6.3: the uncited mechanism is the construct's natural home.** Local sections that cannot be glued into a global one is Abramsky and Brandenburger's contextuality (2011) — locally consistent perspectives, globally obstructed — which is the closest developed formal program to the construct's third thesis (the unity of opposites: layers genuinely opposed, genuinely unified). It is uncited. This is simultaneously the paper's largest citation failure and its largest missed opportunity (see T-target 2).

**F4 — the construct supplies the falsifiability Referee C found missing.** Referee C's verdict — no falsifiable proposition, no empirical consequence — is correct for v1.0 as written. But the author's own distinction, taken seriously, supplies distinct falsifiers per grade:

- "C is essential for O" is refuted by exhibiting **one** possible world in which O is realized without C.
- "C is necessary for O in W" is refuted by one configuration of type W in which O occurs without C.
- The grades are differently supportable as well: essentiality by invariance arguments over the whole space; necessity by within-configuration analysis.

This is modal, not empirical, falsifiability — the strongest kind available to a pure metaphysics, and it is honest to say exactly that. v1.0 claimed falsifiability without content; the construct contains the content; the paper never cashed it in.

## 3. Where the construct stands in the literature (for §1 requalification)

Honest accounting, in the spirit of the prior-art findings, so that the construct's genuine novelty is visible against its ancestry:

- **Aristotle**, *Physics* II.9 (with the saw of *Parts of Animals* I.1 as the classic illustration): hypothetical necessity (ex hypotheseōs) vs. absolute necessity (haplōs) — material conditions necessary given the end. The closest ancient ancestor of necessity-indexed-to-a-configuration.
- **Putnam 1967** ("Psychological Predicates"): multiple realizability — the direct ancestor of the brain example.
- **Lewis 1980** ("Mad Pain and Martian Pain"): role vs. realizer — the causal-role individuation the example presupposes.
- **Kripke 1980** (*Naming and Necessity*): essence as all-worlds invariance; origin essentialism as a no-functional-equivalent claim.
- **Fine 1994** ("Essence and Modality"): the dependence reading of essence and its non-reducibility to necessity.
- **Chalmers 1996** (organizational invariance: the fading-qualia argument) vs. **Searle 1992** (biological naturalism): the live dispute over whether the brain has a functional equivalent for mind. The paper's example takes the functionalist side; this is a substantive commitment and should be owned as one, with both sides cited.

One terminological caution: the construct's "essential" applies to **conditions for outcomes**, not to properties of objects, which is where Kripke's "essential property" lives. v1.1 should say this once, explicitly, to preempt a predictable objection.

**What is distinctive in the construct:** not the local/global contrast itself, but (i) making absence-of-functional-equivalent the *defining* criterion of the top grade, (ii) the graded packaging over conditions-for-outcomes, and (iii) the integration with identity-as-holonomy (§4). To this reviewer's knowledge, (iii) is genuinely new; (i)–(ii) are refinements of an old contrast. §1 should claim exactly this much, and no more.

## 4. The formal home the construct already has

The graded structure maps naturally onto machinery the paper already possesses:

- configurations/worlds → contexts;
- "necessary within a configuration" → local necessity, □_W(O → C), relativized to a context;
- "essential" → global invariance, □(O → C), over the whole context space;
- "no functional equivalent" → uniqueness of realization: no other section/realizer realizes O over any context;
- identity-as-holonomy → the natural criterion for when a substitution is a *genuine* equivalent: harmless exactly when it preserves the holonomy class of the outcome.

Two theorem targets follow — stated as targets, not claims:

**T-target 1 (essentiality as non-substitutability).** C is essential for O iff no substitution that realizes O over any context preserves the holonomy class of O. Essentiality = non-substitutability-without-holonomy-change. If this is provable with the gluing condition genuinely used, the abstract's "derived rather than stipulated" becomes true, because it is exactly the kind of statement that could have come out the other way. If it is not provable, the claim must be withdrawn.

**T-target 2 (locally necessary, globally substitutable).** A condition necessary in every local configuration yet not globally essential is a gluing obstruction in the sense of Abramsky–Brandenburger. If the framework can exhibit one, the unity-of-opposites thesis acquires a precise, non-stipulated formal object, and §6.3 graduates from resembling contextuality to contributing to it.

And one reformation for F2: replacing Theorem 4's impossible object with **reduction of the structure group** would give "deleting directions" its orthodox formal meaning — a constraint that shrinks the allowed transitions rather than adding a force.

## 5. Repair targets for v1.1 (implementable)

- **R1. Re-index Definition 13.** All necessity operators context-indexed (□_W local, □ global); the trichotomy stated over indexed operators only.
- **R2. Non-vacuity guard.** Essentiality claims well-formed only for outcome-classes realized in at least one accessible context; an impossible outcome makes every condition vacuously essential, and the definition must block it.
- **R3. Restore the antecedent.** Reintroduce Φ →, state what Φ ranges over; if accessibility-totality is assumed, it must be a stated axiom (Referee D's silent-hypothesis catalogue), not a silent hypothesis.
- **R4. Prove or withdraw.** Attempt T-target 1; publish the outcome either way.
- **R5. Engage Abramsky–Brandenburger in §6.3**, and attempt T-target 2 as the construct's distinctive contribution.
- **R6. Falsifiability restated honestly** in the abstract: distinct possible-world falsifiers per grade (F4); modal, not empirical — say so.
- **R7. §1 requalification** per §3, claiming (i)–(iii) and no more, with the terminological caution noted.
- **R8. The brain example as a commitment**, Chalmers and Searle both cited.
- **R9. Status-table hygiene** (from the pool's findings, repeated because fidelity requires it): §11 must match Referee D's verified verdicts row by row; the SU(3)/SU(4) mislabel and the phantom non-additivity theorem must be fixed before any table certifies anything.

## 6. What this review is not

Not a mathematical verification — I have not recomputed Referee D's calculations and rely on the pool where stated. Not a substitute for a human read: one model family reviewing a paper written by another reduces the correlation problem; it does not eliminate it. No model family, mine included, is a neutral instrument. Before any arXiv submission (given the May 2026 policy under which unchecked LLM errors and hallucinated references cost the *author of record* a one-year ban), the paper still needs at least one human mathematician reading §6 and §11, and a reference-by-reference check of the bibliography. Zenodo first for the DOI remains the low-risk sequencing.

## 7. Provenance

Reviewer: Z.ai (GLM), a different model family and organization from the MiniMax-M3 pool that authored the paper and ran Referees A–D. Commissioned by the author of record on 2026-11-23, after the four-referee record was published, with the author's own statement of the essential/contingent distinction as input. Published here rather than summarized, consistent with this repository's stated practice.
