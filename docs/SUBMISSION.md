# Submission draft

Category: Intelligent Contracts

Title: APIContractIQ — API Backward Compatibility Verification

Description:
APIContractIQ is a standalone GenLayer primitive for API release compatibility review. Developers lock baseline and candidate primitive-interface schemas, behavioral specifications, changelogs and migration notes as SHA-256-bound canonical JSON. Deterministic checks detect removed operations, stricter inputs and weakened response guarantees. Independent GenLayer leader/validator AI review assesses semantic behavior changes with exact quotations from both releases. Outcomes are COMPATIBLE, CONDITIONAL, BREAKING or INCONCLUSIVE. Owner-authorized bounded challenges preserve append-only hash-linked receipts, and finalization requires the latest decision hash. Live on Studionet with six finalized lifecycle transactions. Includes reproducible fixtures, security and deployment documentation, GenVM lint/schema validation and 34 SDK direct tests. Supports a deliberately bounded interface profile rather than arbitrary OpenAPI; provenance is declared and verdicts are advisory.

Evidence:
- Source: https://github.com/ansabroh/APIContractIQ
- Contract: `contracts/api_contract_iq.py`
- Tests: `tests/test_contract.py`
- Exact verification/deployment records: `docs/VALIDATION.md`

This file is a draft only; no contribution form was submitted automatically.
