# Quick fix for pre-commit linting issues
import json

# Fix vspec.json - format properly with indentation
print("Formatting vspec.json...")
with open('app/vspec.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('app/vspec.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    f.write('\n')  # Ensure trailing newline

print("Formatting AppManifest.json...")
with open('app/AppManifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('app/AppManifest.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    f.write('\n')  # Ensure trailing newline

print("Done! Files formatted with proper indentation and trailing newlines.")
