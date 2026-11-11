"""Create canonical bundle hash and copyable Studio method arguments (no signing)."""
import hashlib
import json
import sys
from pathlib import Path


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python scripts/prepare.py CASE_ID fixtures/baseline.json')
    bundle = json.loads(Path(sys.argv[2]).read_text())
    encoded = canonical(bundle)
    print(json.dumps({'api_id': sys.argv[1], 'bundle_json': encoded,
                      'expected_hash': hashlib.sha256(encoded.encode()).hexdigest()}, indent=2))
