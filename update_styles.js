const fs = require('fs');
let css = fs.readFileSync('src/style.css', 'utf8');

// Update Root variables
css = css.replace(/:root\s*{[^}]*}/, `:root {
  --main-color: #f6e7ff;
  --bg-container: rgba(61, 0, 94, 0.6); /* #3D005E 60% */
  --background-color: #31004b;
  --navbar-color: rgba(40, 0, 61, 0.6); /* #28003D 60% */
  --stroke-color: #5A0389;
  --text-light: #ebb8ff;
  --max-w: 1200px;
}`);

// Update body font and color
css = css.replace(/font-family:[^;]+;/, "font-family: 'Geist', sans-serif;");

// Navbar / theme toggle
css = css.replace(
  /background:\s*var\(--navbar-color\);\s*\n\s*border:\s*1px solid [^;]+;\s*\n\s*border-radius:\s*999px;\s*\n\s*backdrop-filter:\s*blur\([^)]+\);/,
  `background: var(--navbar-color);
  border: 1px solid var(--stroke-color);
  border-radius: 999px;
  backdrop-filter: blur(12px);`
);

// Theme toggle
css = css.replace(
  /border:\s*1px solid [^;]+;\s*\n\s*border-radius:\s*50%;\s*\n\s*background:\s*var\(--navbar-color\);\s*\n\s*font-size:\s*42px;\s*\n\s*line-height:\s*1;\s*\n\s*backdrop-filter:\s*blur\([^)]+\);/,
  `border: 1px solid var(--stroke-color);
  border-radius: 50%;
  background: var(--navbar-color);
  font-size: 42px;
  line-height: 1;
  backdrop-filter: blur(12px);`
);

// About text (container)
css = css.replace(
  /background:\s*rgba\([^)]+\);\s*\n\s*border:\s*1px solid [^;]+;/,
  `background: var(--bg-container);
  border: 1px solid var(--stroke-color);`
);

// Experience item (container)
css = css.replace(
  /border:\s*1px solid rgba\([^)]+\);\s*\n\s*background:\s*linear-gradient\([^)]+\);/,
  `border: 1px solid var(--stroke-color);
  background: var(--bg-container);`
);

// Buttons (experience link)
css = css.replace(
  /background:\s*linear-gradient\([^)]+\);\s*\n\s*border:\s*1px solid rgba\([^)]+\);/,
  `background: linear-gradient(90deg, rgba(130, 3, 198, 0.2), rgba(183, 54, 253, 0.2));
  border: 1px solid var(--stroke-color);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);`
);

// Hover for buttons (experience link)
css = css.replace(
  /\.experience-link:hover\s*{[^}]*}/,
  `.experience-link:hover {
  background: linear-gradient(90deg, #8203C6, #B736FD);
  transform: none;
  filter: none;
}`
);

fs.writeFileSync('src/style.css', css);
