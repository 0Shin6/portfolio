with open('src/style.css', 'r') as f:
    css = f.read()

import re

# Box sizing
if 'box-sizing: border-box;' not in css:
    css = css.replace('html {\n  scroll-behavior: smooth; \n}', 'html {\n  scroll-behavior: smooth;\n  box-sizing: border-box;\n}\n\n*, *::before, *::after {\n  box-sizing: inherit;\n}')

css = re.sub(
    r'\.project\s*\{\s*padding:\s*10px;\s*text-align:\s*center;\s*display:\s*flex;\s*flex-direction:\s*column;\s*justify-content:\s*space-between;\s*height:\s*100%;\s*\}',
    r'.project {\n  padding: 24px;\n  text-align: center;\n  display: flex;\n  flex-direction: column;\n  justify-content: space-between;\n  height: 100%;\n  background: var(--bg-container);\n  border: 1px solid var(--stroke-color);\n  border-radius: 20px;\n}',
    css
)

css = re.sub(
    r'\.cv-box\s*\{\s*padding:\s*32px;\s*display:\s*flex;\s*align-items:\s*center;\s*justify-content:\s*center;\s*text-align:\s*center;\s*\}',
    r'.cv-box {\n  padding: 32px;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  text-align: center;\n  background: linear-gradient(90deg, rgba(130, 3, 198, 0.2), rgba(183, 54, 253, 0.2));\n  border: 1px solid var(--stroke-color);\n  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3);\n  backdrop-filter: blur(10px);\n  border-radius: 999px;\n}',
    css
)

css = re.sub(
    r'\.cv-box:hover\s*\{\s*transform:\s*scale\(1\.05\);\s*\}',
    r'.cv-box:hover {\n  background: linear-gradient(90deg, #8203C6, #B736FD);\n}',
    css
)

css = re.sub(
    r'\.experience-link:hover\s*\{\s*transform:\s*translateY\(-1px\);\s*filter:\s*brightness\(1\.05\);\s*\}',
    r'.experience-link:hover {\n  background: linear-gradient(90deg, #8203C6, #B736FD);\n}',
    css
)

with open('src/style.css', 'w') as f:
    f.write(css)
