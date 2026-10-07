import re

with open('src/style.css', 'r') as f:
    css = f.read()

# Update root variables
css = re.sub(r':root\s*\{[^}]*\}', ''':root {
  --main-color: #f6e7ff;
  --bg-container: rgba(61, 0, 94, 0.6);
  --background-color: #31004b;
  --navbar-color: rgba(40, 0, 61, 0.6);
  --stroke-color: #5A0389;
  --text-light: #ebb8ff;
  --max-w: 1200px;
}''', css)

# Box sizing
if 'box-sizing: border-box;' not in css:
    css = css.replace('html {\n  scroll-behavior: smooth; \n}', 'html {\n  scroll-behavior: smooth;\n  box-sizing: border-box;\n}\n\n*, *::before, *::after {\n  box-sizing: inherit;\n}')

# Navbar links background
css = re.sub(
    r'background:\s*var\(--navbar-color\);\s*\n\s*border:\s*1px solid [^;]+;\s*\n\s*border-radius:\s*999px;\s*\n\s*backdrop-filter:\s*blur\([^)]+\);',
    r'background: var(--navbar-color);\n  border: 1px solid var(--stroke-color);\n  border-radius: 999px;\n  backdrop-filter: blur(12px);',
    css
)

# Theme toggle
css = re.sub(
    r'border:\s*1px solid [^;]+;\s*\n\s*border-radius:\s*50%;\s*\n\s*background:\s*var\(--navbar-color\);\s*\n\s*font-size:\s*42px;\s*\n\s*line-height:\s*1;\s*\n\s*backdrop-filter:\s*blur\([^)]+\);',
    r'border: 1px solid var(--stroke-color);\n  border-radius: 50%;\n  background: var(--navbar-color);\n  font-size: 42px;\n  line-height: 1;\n  backdrop-filter: blur(12px);',
    css
)

# About text
css = re.sub(
    r'\.about-text\s*\{[^}]*\}',
    r'.about-text {\n  padding: 34px 60px;\n  background: var(--bg-container);\n  border: 1px solid var(--stroke-color);\n  border-radius: 35px;\n}',
    css
)

# Experience item
css = re.sub(
    r'\.experience-item\s*\{[^}]*\}',
    r'.experience-item {\n  display: grid;\n  grid-template-columns: minmax(150px, 200px) minmax(0, 1fr) 84px minmax(190px, 300px);\n  align-items: center;\n  gap: 18px;\n  width: 100%;\n  padding: 20px 28px;\n  border-radius: 30px;\n  border: 1px solid var(--stroke-color);\n  background: var(--bg-container);\n}',
    css
)

# Buttons
css = re.sub(
    r'\.experience-link\s*\{[^}]*\}',
    r'.experience-link {\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n  gap: 10px;\n  min-height: 58px;\n  padding: 0 18px;\n  border-radius: 999px;\n  background: linear-gradient(90deg, rgba(130, 3, 198, 0.2), rgba(183, 54, 253, 0.2));\n  border: 1px solid var(--stroke-color);\n  color: var(--main-color);\n  text-decoration: none;\n  font-weight: 600;\n  text-align: center;\n  transition: all 0.2s ease;\n  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3);\n  backdrop-filter: blur(10px);\n}',
    css
)

# Button hover
css = re.sub(
    r'\.experience-link:hover\s*\{[^}]*\}',
    r'.experience-link:hover {\n  background: linear-gradient(90deg, #8203C6, #B736FD);\n  transform: none;\n  filter: none;\n  color: var(--main-color);\n}',
    css
)

# Project
css = re.sub(
    r'\.project\s*\{[^}]*\}',
    r'.project {\n  padding: 24px;\n  text-align: center;\n  display: flex;\n  flex-direction: column;\n  justify-content: space-between;\n  height: 100%;\n  background: var(--bg-container);\n  border: 1px solid var(--stroke-color);\n  border-radius: 20px;\n  transition: transform 0.2s;\n}',
    css
)

# cv-box
css = re.sub(
    r'\.cv-box\s*\{[^}]*\}',
    r'.cv-box {\n  padding: 32px;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  text-align: center;\n  background: linear-gradient(90deg, rgba(130, 3, 198, 0.2), rgba(183, 54, 253, 0.2));\n  border: 1px solid var(--stroke-color);\n  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3);\n  backdrop-filter: blur(10px);\n  border-radius: 999px;\n  transition: all 0.2s;\n}',
    css
)

css = re.sub(
    r'\.cv-box:hover\s*\{[^}]*\}',
    r'.cv-box:hover {\n  background: linear-gradient(90deg, #8203C6, #B736FD);\n  transform: none;\n}',
    css
)

with open('src/style.css', 'w') as f:
    f.write(css)

