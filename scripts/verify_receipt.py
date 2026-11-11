"""Verify a receipt's canonical hash and optional predecessor."""
import hashlib
import json
import sys
from pathlib import Path


def verify(path, previous=None):
    receipt = json.loads(Path(path).read_text())
    recorded = receipt.pop('receipt_hash')
    encoded = json.dumps(receipt, sort_keys=True, separators=(',', ':'), ensure_ascii=True)
    computed = hashlib.sha256(encoded.encode()).hexdigest()
    if recorded != computed:
        raise SystemExit('Receipt hash mismatch')
    if previous is not None and receipt['previous_hash'] != previous:
        raise SystemExit('Previous receipt hash mismatch')
    print(json.dumps({'verified': True, 'outcome': receipt['outcome'], 'receipt_hash': recorded}))
    return recorded


if __name__ == '__main__':
    if not 2 <= len(sys.argv) <= 3:
        raise SystemExit('Usage: python scripts/verify_receipt.py receipt.json [PREVIOUS_HASH]')
    verify(*sys.argv[1:])
