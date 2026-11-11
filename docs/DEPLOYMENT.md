# Deploy and reproduce

Use stable [GenLayer Studio](https://studio.genlayer.com) (Studionet chain 61999) and its built-in account. Do not import a real wallet or seed phrase. This contract has no constructor arguments and requires no funds or payment logic.

1. Import `contracts/api_contract_iq.py`; open Run and Debug. Keep **Normal (Full Consensus)** selected, with Simulation Mode unchecked.
2. Deploy, then wait for FINALIZED. Record the contract address and deployment transaction hash. ACCEPTED and FINALIZED are distinct network states.
3. Run `python scripts/prepare.py live-users fixtures/baseline.json`. Expand `register`, paste case ID, `bundle_json` value and `expected_hash`, then send.
4. Run the same command with `fixtures/compatible.json`. Expand `submit`, paste the values into `api_id`, `candidate_json`, `expected_hash`, then send. Wait for finalization after each write.
5. Call `evaluate("live-users")`. This invokes actual leader/validator semantic review. A valid structurally unchanged fixture should produce COMPATIBLE, but provider failures may produce INCONCLUSIVE and validator disagreement may revert. Do not relabel failed runs as successful.
6. Read `get_receipt("live-users", 0)` and `get_case("live-users")` using Finalized state. Save exact returned JSON and transaction evidence. Verify the receipt hash by removing only `receipt_hash`, canonicalizing the remaining object, and computing SHA-256.
7. Optional: `challenge("live-users", "Please recheck documented input semantics.")` repeats review of identical evidence (at most twice). Read the new receipt and preserve the earlier one.
8. `finalize("live-users", LATEST_HEAD_HASH)` seals the case. A stale head is rejected. Register a new case for another release or changed evidence.

Use unique IDs for additional fixtures. `breaking.json` exercises deterministic detection without an LLM call; `semantic-breaking.json` changes parameter meaning without changing its type, so its BREAKING result depends on actual AI consensus. `conditional.json` introduces deprecation. `inconclusive.json` deliberately lacks sufficient behavioral documentation.

Local checks use the SDK pinned in the source header (GenVM v0.2.16), Python 3.12 and pinned dev dependencies. Direct tests mock LLM responses and invoke captured validators separately; Studio is the separate distributed-consensus verification step.
