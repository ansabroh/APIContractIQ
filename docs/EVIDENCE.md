# Evidence profile v1

See the six `fixtures/*.json` bundles. Exact top-level fields: `version`, `source`, `operations`, `documents`. Source syntax: `https://github.com/OWNER/REPO/tree/FULL_40_LOWERCASE_HEX_COMMIT`. Documents must have exactly `behavior`, `changelog`, `migration`, each at most 4,000 UTF-8 bytes. Behavior must be nonempty. Max 32 operations, max 32 fields per input/output side. Accepted primitive types: string/integer/number/boolean. Types are conservatively exact; even integer/number changes are classified BREAKING.

Canonical serialization is Python `json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)`. Hash is lower-case SHA-256 hex of its UTF-8 bytes. Bundle hash commits the complete interface, documents, version and source. Duplicate JSON keys are rejected. Whitespace or key order changes do not alter the hash.

A field marked `required` on inputs means callers must supply it; on responses it means the producer always returns it. Input removal is treated conservatively as breaking, even if a particular implementation ignores unknown inputs. Optional input addition is structurally safe; response additions are structurally safe only under clients accepting additive fields. Semantic review must consider stricter consumers and behavior changes. The profile cannot express complete JSON Schema or OpenAPI and must not be represented as a full OpenAPI compatibility checker.

Receipt hash excludes its own `receipt_hash` field and includes every other field including `previous_hash`, `round`, `api_id`, `baseline_hash` and `candidate_hash`. Round zero has empty previous hash. Challenge reasons are included verbatim and treated as untrusted claims; challenges cannot change the evidence. A new evidence bundle requires a new case.
