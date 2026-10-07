with open('src/style.css', 'r') as f:
    css = f.read()

# 1. Update variables
root_old = """:root {
  --main-color: #f6e7ff;
  --bg-dark: rgba(113, 0, 151, 0.3);
  --bg-hover: rgba(150, 0, 200, 0.6);
  --text-color: #f19fff;
  --text-light: #ebb8ff;
  --background-color: #31004b;
  --navbar-color: rgba(40, 0, 61, 0.6);
  --max-w: 1200px;
}"""
root_new = """:root {
  --main-color: #f6e7ff;
  --bg-container: rgba(61, 0, 94, 0.6);
  --bg-hover: rgba(130, 3, 198, 0.2);
  --text-color: #f19fff;
  --text-light: #ebb8ff;
  --background-color: #31004b;
  --navbar-color: rgba(40, 0, 61, 0.6);
  --stroke-color: #5A0389;
  --max-w: 1200px;
}"""
css = css.replace(root_old, root_new)

# Box sizing
html_old = """html {
  scroll-behavior: smooth; 
}"""
html_new = """html {
  scroll-behavior: smooth; 
  box-sizing: border-box;
}

*, *::before, *::after {
  box-sizing: inherit;
}"""
css = css.replace(html_old, html_new)

# Fix app wrapper layout
body_old = """body {
  font-family: 'Geist', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0; padding: 0 16px;
  color: var(--main-color);
  background: var(--background-color);
  display: flex; flex-direction: column; align-items: center;
}"""
body_new = """body {
  font-family: 'Geist', sans-serif;
  margin: 0; padding: 0 16px;
  color: var(--main-color);
  background: var(--background-color);
}

#app {
  width: 100%;
  display: flex; flex-direction: column; align-items: center;
}"""
css = css.replace(body_old, body_new)

# Nav links
nav_old = """  background: var(--navbar-color);
  border: 1px solid rgba(214, 66, 255, 0.35);
  border-radius: 999px;
  backdrop-filter: blur(10px);"""
nav_new = """  background: var(--navbar-color);
  border: 1px solid var(--stroke-color);
  border-radius: 999px;
  backdrop-filter: blur(12px);"""
css = css.replace(nav_old, nav_new)

# Theme toggle
theme_old = """  border: 1px solid rgba(214, 66, 255, 0.35);
  border-radius: 50%;
  background: var(--navbar-color);
  font-size: 42px;
  line-height: 1;
  backdrop-filter: blur(10px);"""
theme_new = """  border: 1px solid var(--stroke-color);
  border-radius: 50%;
  background: var(--navbar-color);
  font-size: 42px;
  line-height: 1;
  backdrop-filter: blur(12px);"""
css = css.replace(theme_old, theme_new)

# About text
about_old = """  background: rgba(113, 0, 151, 0.22);
  border: 1px solid rgba(214, 66, 255, 0.35);"""
about_new = """  background: var(--bg-container);
  border: 1px solid var(--stroke-color);"""
css = css.replace(about_old, about_new)

# Experience item
exp_old = """  border: 1px solid rgba(214, 66, 255, 0.35);
  background: linear-gradient(90deg, rgba(130, 67, 162, 0.52), rgba(104, 28, 123, 0.72));
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);"""
exp_new = """  border: 1px solid var(--stroke-color);
  background: var(--bg-container);"""
css = css.replace(exp_old, exp_new)

# Experience link
link_old = """  background: linear-gradient(135deg, rgba(171, 96, 212, 0.35), rgba(123, 70, 188, 0.72));
  border: 1px solid rgba(214, 66, 255, 0.35);"""
link_new = """  background: linear-gradient(90deg, rgba(130, 3, 198, 0.2), rgba(183, 54, 253, 0.2));
  border: 1px solid var(--stroke-color);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);"""
css = css.replace(link_old, link_new)

hover_old = """.experience-link:hover {
  transform: translateY(-1px);
  filter: brightness(1.05);
}"""
hover_new = """.experience-link:hover {
  background: linear-gradient(90deg, #8203C6, #B736FD);
}"""
css = css.replace(hover_old, hover_new)

# Project block
proj_old = """.project {
  padding: 10px; 
  text-align: center;
  display: flex; 
  flex-direction: column; 
  justify-content: space-between; 
  height: 100%; 
}"""
proj_new = """.project {
  padding: 24px; 
  text-align: center;
  display: flex; 
  flex-direction: column; 
  justify-content: space-between; 
  height: 100%;
  background: var(--bg-container);
  border: 1px solid var(--stroke-color);
  border-radius: 20px;
}"""
css = css.replace(proj_old, proj_new)

# cv-box
cv_old = """.cv-box {
  padding: 32px;
  display: flex; 
  align-items: center; 
  justify-content: center; 
  text-align: center;

}
.cv-box:hover {
  transform: scale(1.05);
}"""
cv_new = """.cv-box {
  padding: 32px;
  display: flex; 
  align-items: center; 
  justify-content: center; 
  text-align: center;
  background: linear-gradient(90deg, rgba(130, 3, 198, 0.2), rgba(183, 54, 253, 0.2));
  border: 1px solid var(--stroke-color);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
  border-radius: 999px;
  transition: all 0.2s;
}
.cv-box:hover {
  background: linear-gradient(90deg, #8203C6, #B736FD);
}"""
css = css.replace(cv_old, cv_new)

with open('src/style.css', 'w') as f:
    f.write(css)
