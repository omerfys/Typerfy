import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("HTML size:", len(text))

# Find themes
theme_matches = re.findall(r'data-theme="([^"]+)"', text)
print("Themes:", set(theme_matches))

# Find presets
preset_matches = re.findall(r'data-preset="([^"]+)"', text)
print("Presets:", set(preset_matches))

# Find all buttons
button_matches = re.findall(r'<button[^>]*>([^<]+)</button>', text)
print("Buttons found:", len(button_matches))
for b in set(button_matches):
    b_clean = b.strip()
    if b_clean:
        print("  -", b_clean)

# Find exports
export_matches = re.findall(r'data-export="([^"]+)"', text)
print("Exports:", set(export_matches))

# Look for JS constants / objects
const_matches = re.findall(r'const\s+([A-Z_0-9]+)\s*=', text)
print("Consts:", const_matches[:15])
