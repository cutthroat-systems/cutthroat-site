import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent.resolve()
EXT_FILE = HERE / "assets" / "vscode-extensions.txt"
VS_SETTINGS_FILE = HERE.parent / ".vscode" / "settings.json"
SETTINGS_FILE = HERE / "assets" / "settings.json"
REQUIREMENTS_FILE = HERE / "assets" / "requirements.txt"

# ─────────────────────────────────────────────────
# Install Python requirements from requirements.txt
# ─────────────────────────────────────────────────
print("\n🔧 Installing Python requirements...\n")
result = subprocess.run(
    [sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE), "-qqq"],
    stderr=subprocess.PIPE,
    text=True,
)

if result.returncode == 0:
    print("✅ Required packages (if any) installed.")
else:
    print(f"❌ pip requirements install failed:\n{result.stderr}")

# ─────────────────────────────────────────────────
# Create or update .vscode/settings.json
#     - Ensures local environment activation
#     - Merges in project-level settings
# ─────────────────────────────────────────────────
print("\n🛠  Updating VS Code settings.json...\n")

# Create or open .vscode settings and load
if not VS_SETTINGS_FILE.parent.exists():
    print("⚠️  No existing VS Code settings. Creating a new one.")
    VS_SETTINGS_FILE.parent.mkdir(parents=True)

try:
    if (
        not VS_SETTINGS_FILE.exists()
        or not VS_SETTINGS_FILE.read_text(encoding="utf-8").strip()
    ):
        raise json.JSONDecodeError("Empty or missing file", "", 0)

    with VS_SETTINGS_FILE.open("r", encoding="utf-8") as f:
        current_settings = json.load(f)

except json.JSONDecodeError:
    print("⚠️ .vscode/settings.json is missing, empty, or invalid. Replacing it.\n")
    VS_SETTINGS_FILE.write_text("{}", encoding="utf-8")
    current_settings = {}

# Merge with new settings
if SETTINGS_FILE.exists():
    with SETTINGS_FILE.open("r", encoding="utf-8") as f:
        new_settings = json.load(f)
    current_settings.update(new_settings)
else:
    print(f"\n❌ Error: {SETTINGS_FILE} not found.")
    sys.exit(1)

# Write updated settings
with VS_SETTINGS_FILE.open("w") as f:
    json.dump(current_settings, f, indent=4)
print("✅ VS Code settings updated.")

# ─────────────────────────────────────────────────
# Install VS Code extensions listed in assets/
#     - Skips comments and blank lines
#     - Cleans extension names for display
#     - Checks for availability of `code` CLI
# ─────────────────────────────────────────────────
if not EXT_FILE.exists():
    print(f"\n❌ Error: {EXT_FILE} not found.")
    sys.exit(1)

print("\n📦 Installing VS Code extensions...\n")
if not shutil.which("code"):
    print("⚠️ VS Code CLI ('code') not found. Skipping extension installs.\n")
else:
    with EXT_FILE.open() as f:
        for line in f:
            ext = line.strip()
            if not ext or ext.startswith("#"):
                continue
            ext = ext.split("#", 1)[0].strip()
            _clean_ext = ext.split(".", 1)[-1]
            print(f"➡ Installing: {_clean_ext}")
            result = subprocess.run(
                f"code --install-extension {ext} --force",
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
            )

            if result.returncode == 0:
                print(f"✅ Installed: {_clean_ext}")
            else:
                print(f"❌ Failed to install extension {_clean_ext}:\n{result.stderr}")

print(
    "\n🎉 All done! Please reopen VS Code to apply changes. You can use Ctrl+Shift+P → Reload Window.\n"
)
