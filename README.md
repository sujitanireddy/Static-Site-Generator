# Static Site Generator

A lightweight static-site generator that converts a folder of Markdown files into a fully navigable HTML site.
[Live demo of a static site generated from Markdown files](https://sujitanireddy.github.io/Static-Site-Generator/)

- Converts **Markdown → HTML**
- Builds pages **recursively** (nested folders supported)
- Copies **static assets** (CSS/images) into the output

---

## How it works

1. Put your Markdown content in `content/` (you can nest folders).
2. Run the generator.
3. It outputs a ready-to-serve site into `docs/`:
   - `docs/**/*.html` generated from your Markdown
   - `docs/index.css`, `docs/images/`, etc. copied from `static/`

---

## Project structure

```text
Static-Site-Generator/
├─ content/                 # Your markdown content (source)
│  ├─ index.md
│  ├─ blog/
│  └─ contact/
├─ static/                  # Static assets copied as-is (CSS, images, etc.)
│  ├─ index.css
│  └─ images/
├─ template.html            # HTML template with {{ Title }} and {{ Content }}
├─ docs/                    # Build output (generated site)
├─ src/                     # Generator + markdown parser implementation
│  ├─ main.py
│  ├─ gencontent.py
│  ├─ markdown_to_html.py
│  └─ ... + tests
├─ main.sh                  # Build + run local server
├─ build.sh                 # Build using a GitHub Pages-friendly basepath
└─ test.sh                  # Run unit tests
```

---

## Requirements

- Python 3.x  
No external dependencies required.

---

## Quick start (local)

### 1) Generate the site
From the project root:

```bash
python3 src/main.py
```

This will:
- empty the `docs/` directory (if it exists)
- copy everything from `static/` → `docs/`
- generate HTML pages from `content/` → `docs/`

### 2) Serve it locally

```bash
cd docs
python3 -m http.server 8888
```

Open:

```text
http://localhost:8888
```

### Or use the helper script

```bash
./main.sh
```

---

## Deploying to GitHub Pages (base path support)

When hosting on GitHub Pages, your site is usually served from:

```text
https://<username>.github.io/<repo-name>/
```

So links like `/index.css` need a base path (e.g. `/Static-Site-Generator/`).

Use:

```bash
./build.sh
```

This runs:

```bash
python3 src/main.py "/Static-Site-Generator/"
```

The generator updates asset links in the final HTML by rewriting:

- `href="/...` → `href="<basepath>...`
- `src="/...`  → `src="<basepath>...`

---

## Supported Markdown features

### Block-level
- Headings (`#` through `######`)
- Paragraphs
- Unordered lists (`- item`)
- Ordered lists (`1. item`, `2. item`, …)
- Blockquotes (`> quote`)
- Code blocks (triple backticks)

### Inline
- Bold (`**bold**`)
- Italic (`*italic*`)
- Inline code (`` `code` ``)
- Links (`[text](url)`)
- Images (`![alt](url)`)

---

## Running tests

```bash
./test.sh
```

Or directly:

```bash
python3 -m unittest discover -s src
```

---

## Customizing the template

Edit `template.html`. It uses placeholders:

- `{{ Title }}`: pulled from the first H1 (`# Heading`) in the markdown file
- `{{ Content }}`: the generated HTML content

Example:

```html
<title>{{ Title }}</title>
<article>{{ Content }}</article>
```

> Note: Every Markdown page must include an H1 (`# ...`) or the build will raise an error.

---

## Notes / behavior details

- Output directory is **`docs/`** (this is also convenient for GitHub Pages).
- The build step **clears existing files** in `docs/` before regenerating.
- Static assets are copied recursively from `static/`.

---

## License

Use it as you wish.
