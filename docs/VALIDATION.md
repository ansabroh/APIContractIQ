# Validation record — 2026-11-11

## Local verification

- Python 3.12; `genlayer-test 0.29.2`, `genvm-linter 0.11.0`.
- `genvm-lint check contracts/api_contract_iq.py`: 3 safety checks passed; SDK semantic validation passed; APIContractIQ schema has 2 read and 5 write methods.
- `pytest -q`: **34 passed**, using actual SDK/storage with mocked LLM I/O.
- Validator callbacks separately tested for independent agreement, disagreement, forged quotation, invalid outcome, extra fields, fabricated fail-closed sentinel and leader exception.
- Other coverage: four semantic outcomes, eight structural break scenarios, deprecation floor, malformed model fallback, authorization, immutable evidence/hashes, receipt integrity/history, challenge cap, finalization guards, duplicate/oversized JSON and unsupported features.
- Test/lint outputs are preserved in `evidence/`; pinned dependencies in `requirements-dev.txt` and full dependency snapshot in `requirements-lock.txt`.

## Live Studionet deployment

- Network: stable Studionet (61999), Studio built-in account.
- Source SHA-256: `725e30415b553d1c0767eb1ee8ee54a50c941ac6bdd6f0415c738cf123298de9`.
- Contract: [`0x2780D2C99552B039Fd55C602A0a59Bc79fd3BAA7`](https://explorer-studio.genlayer.com/address/0x2780D2C99552B039Fd55C602A0a59Bc79fd3BAA7).
- Execution mode: **Normal (Full Consensus)**, Simulation Mode unchecked.

| Action | Transaction hash | Observed state |
| --- | --- | --- |
| Deploy | `0xbd1a647fe2e2c23499cc75d7dd64b30ab3ed18291ef53f0236c7cc81b284ada8` | FINALIZED |
| register | `0x1d4f65b0e37372638302b6e5e985b8b11b7714ea8458d3cdb20efe661d487570` | FINALIZED |
| submit | `0x6a41b45e49225551d775c7b0a18d09dfc303d044b971de96ea7de1b4f1947eb4` | FINALIZED |
| evaluate | `0xce94a8af7a515897b7d9871cc966d459e1f05fc612cf2ff1ba99486aaa40da5f` | FINALIZED |
| challenge | `0xe684b65bb1222629aa3c569d34512c37ecfe2980f2e148d2c893de9faf5ffd30` | FINALIZED |
| finalize | `0x23779eb505b7c33c7e7cfc4d901815bc7fe122f277a6cbfcaee2ee4565e9f188` | FINALIZED |

The live `live-users` case uses the committed baseline and compatible fixtures. Round 0 produced **COMPATIBLE** with six exact old/new document citations and mode `independent-semantic-consensus`. Exact returned receipt is `evidence/live-users-round-0.json`; its hash was independently recomputed using `scripts/verify_receipt.py`.

Local direct-mode tests are not distributed consensus. Only the transactions above and any later explicitly recorded rows are live results. A passing compatible example does not establish model accuracy across arbitrary APIs.

Round 1 challenge returned **INCONCLUSIVE** with the fail-closed reason `Invalid or unavailable semantic evidence`, preserving the earlier receipt. This means the review output failed validation or was unavailable after the two allowed attempts; the contract does not expose enough detail to attribute the failure to a particular provider. It must not be described as a second successful compatibility finding. The exact round-1 receipt and its previous-hash linkage were independently verified.

All six lifecycle transactions finalized. Finalization seals the latest INCONCLUSIVE head and does not convert it to approval.
