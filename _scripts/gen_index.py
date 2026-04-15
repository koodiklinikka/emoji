from pathlib import Path

REPO_PATH = Path(__file__).parent.parent
image_suffixes = (".jpg", ".png", ".gif")

wrapper = """
<!doctype html><html><head>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style>
{css}
</style>
</head>
<body>
{content}
</body>
</html>
""".lstrip()

css = """
body {
display:grid;
grid-template-columns: repeat(auto-fill, 6rem);
font-family: sans-serif;
font-size: 10pt;
}
div {text-align:center;padding:0.5rem;word-break:break-word;}
div img {display:block;height:4rem;margin:auto;object-fit:contain;width:4rem;}
""".strip()

content = ""
images = set()
for file in REPO_PATH.rglob("*"):
    if file.suffix.lower() in image_suffixes:
        images.add(file)

for file in sorted(images, key=lambda p: p.name.lower()):
    img_path = file.relative_to(REPO_PATH).as_posix()
    content += f"<div><img src='{img_path}' loading='lazy'>{file.stem}</div>\n"

(REPO_PATH / "index.html").write_text(wrapper.format(content=content, css=css))
