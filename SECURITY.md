# Security model

- Registration claims a global case ID; owners should use unique names. No admin can overwrite a baseline or candidate. First registration does not establish trademark/project ownership.
- Only the registering sender can submit, evaluate, challenge or finalize their case. This is a developer review primitive, not an adversarial arbitration service. Owner-only challenges prevent outsiders consuming its two review rounds.
- Inline bounded evidence eliminates remote retrieval/SSRF and time-varying documents. Commit URLs are provenance claims, not authenticated retrieval. Hash binding proves integrity after registration, not truth or completeness.
- Model prompts identify every document and challenge as untrusted. Strict fields, finite outcomes, bounded attempts and exact quotation checks reduce hallucination/injection risk. Validators rerun the review independently; outcome agreement is required. Grounded quotations cannot alone prove a model conclusion is correct.
- Structural breaking evidence cannot be overruled by AI. Deprecation cannot be downgraded below CONDITIONAL. Failed consensus writes nothing. Invalid AI results fail closed.
- All chain state is public. Never submit API keys, private schemas or personal data. No tokens, automatic upgrade approval or payments are involved.
- Do not use an advisory COMPATIBLE receipt as the sole production release gate. Unsupported schemas are rejected before registration rather than silently simplified. New constraints and undocumented implementation changes remain beyond this profile.

Report reproducible issues through the repository's GitHub issue tracker without including secrets.
