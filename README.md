# APIContractIQ

A standalone GenLayer Intelligent Contract for reviewing whether an API release preserves an immutable published interface. No frontend is required. Results are advisory: **COMPATIBLE**, **CONDITIONAL**, **BREAKING**, or **INCONCLUSIVE**.

## What it does

An API owner registers a baseline and one candidate release under a unique case ID. Both become immutable canonical JSON with SHA-256 commitments. Deterministic checks find removed operations/parameters, new required inputs, changed primitive types, removed response fields and weakened response guarantees. Newly deprecated operations establish a CONDITIONAL floor.

When no structural break is proven, GenLayer's real `gl.vm.run_nondet_unsafe` runs semantic review. The leader and each validator independently call an LLM on identical version-locked evidence. Validators compare outcomes and verify the leader's exact quotations from both versions. Semantic review covers behavior, units, authentication, errors, changelogs and migration requirements. Malformed or unavailable AI evidence receives two bounded attempts, then INCONCLUSIVE. Consensus disagreement reverts without a receipt.

Each successful evaluation appends a canonical receipt containing baseline/candidate hashes, evidence quotes, deterministic findings, previous receipt hash and decision hash. The owner may request two reviews against the same evidence, then finalize the latest head. Finalization is an acknowledgement, not proof that a release is safe.

## Quick start

Python 3.12+:

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
genvm-lint check contracts/api_contract_iq.py
pytest -q
python scripts/prepare.py users-v1 fixtures/baseline.json
python scripts/prepare.py users-v1 fixtures/compatible.json
```

Deploy `contracts/api_contract_iq.py` in [GenLayer Studio](https://studio.genlayer.com) with its built-in account; constructor takes no arguments. Use `register`, `submit`, `evaluate`, `get_receipt`, optional `challenge`, and `finalize`. See [deployment instructions](docs/DEPLOYMENT.md) and [evidence format](docs/EVIDENCE.md).

## Deliberately bounded format

This release accepts the **APIContractIQ primitive-interface profile**, not arbitrary OpenAPI. Operations are `METHOD /path`; flat input and response fields have explicit primitive type and required flags. Input field names should include location, e.g. `query:limit`, `header:authorization`, `body:name`. Keep response names stable. Nested objects, arrays, enums, numeric constraints, unions, `$ref`, media/status variants and extra fields are rejected. Normalize only APIs actually expressible in this profile; omitted constraints make any positive verdict incomplete. Do not strip unsupported constraints to get acceptance.

Evidence is submitted inline (max 24,000 bytes per bundle), so validators review exactly the same text without URL fetches, redirects, SSRF or mutable web pages. `source` must identify a full Git commit. That reference is **declared provenance**: the contract binds supplied bytes but does not fetch or authenticate their correspondence to that repository. Verify provenance externally. All data is public. Fixtures reference the immutable fixture snapshot commit; only the provenance metadata was subsequently updated to point at that snapshot.

## Verification and limits

**34 tests pass.** The test suite uses the real GenLayer SDK/storage through `gltest.direct` with mocked LLM responses. It verifies contract logic, not production model accuracy. Independent validator rejection tests explicitly exercise the validator callback; direct mode alone is not distributed consensus. Live status and receipts belong in [validation evidence](docs/VALIDATION.md).

Compatibility depends on the supplied documents and supported profile; the contract does not run an API, inspect implementation code, prove document truth or guarantee every client behavior. Human release review and consumer integration tests remain necessary.

Built from the immutable-evidence/append-only-history architecture used by RemedySeal, adapted to directional API compatibility. Official references: [SDK/contract setup](https://docs.genlayer.com/developers/intelligent-contracts/tooling-setup), [storage](https://docs.genlayer.com/developers/intelligent-contracts/features/storage), [independent equivalence validation](https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle).
