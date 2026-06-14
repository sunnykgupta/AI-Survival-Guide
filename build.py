#!/usr/bin/env python3
"""
AI Survival Guide ... static site builder.

Reads contributor-editable Markdown from content/roles/*.md and HTML partials
from content/sections/*.html, then renders dist/index.html using template.html.

Run:  python3 build.py
Output: dist/index.html  (+ dist/assets copied)

To edit a role: open content/roles/NN-<id>.md and edit the prose under each
heading. The site rebuilds automatically on push via GitHub Actions.
"""
import re, os, glob, html as _html, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
def p(*a): return os.path.join(ROOT, *a)

# ---------------------------------------------------------------- inline MD
def inline_md(text):
    """Convert inline markdown to HTML. Order matters: escape first, then markup."""
    t = _html.escape(text, quote=False)
    # bold then italic (avoid clobbering)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', t)
    # links [text](url)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    return t

# ---------------------------------------------------------------- front matter
def parse_md(path):
    raw = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.DOTALL)
    if not m:
        raise ValueError(f"Missing front matter in {path}")
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    # split body into ## sections
    sections = {}
    cur = None; buf = []
    for line in body.splitlines():
        h = re.match(r'^##\s+(.*)$', line)
        if h:
            if cur is not None:
                sections[cur] = '\n'.join(buf).strip()
            cur = h.group(1).strip(); buf = []
        else:
            buf.append(line)
    if cur is not None:
        sections[cur] = '\n'.join(buf).strip()
    return fm, sections

def get_section(sections, prefix):
    """Find a section whose heading starts with prefix (case-insensitive)."""
    for k, v in sections.items():
        if k.lower().startswith(prefix.lower()):
            return k, v
    return None, ''

def paras(text):
    """Blank-line separated paragraphs -> list."""
    return [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]

# ---------------------------------------------------------------- role icons
icons = {}
try:
    import importlib.util
    spec = importlib.util.spec_from_file_location("role_icons", p("role_icons.py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    icons = mod.ROLE_ICONS
except Exception as e:
    print("warn: role_icons not loaded:", e)

# ---------------------------------------------------------------- render role
LAYER_META = {
    1: ("commodity", "dot-red", "L1, COMMODITY"),
    2: ("leverage", "dot-amber", "L2, LEVERAGE"),
    3: ("irreplaceable", "dot-green", "L3, IRREPLACEABLE"),
}

def render_role(path):
    fm, sec = parse_md(path)
    rid = fm['id']; full = fm['title']; stack = fm.get('stack',''); order = int(fm.get('order', 0))
    icon = icons.get(fm.get('icon', rid), '')

    lead = get_section(sec, 'Lead')[1]
    intro = get_section(sec, 'Intro')[1]

    layer_html = []
    for n in (1, 2, 3):
        key, dot, label = LAYER_META[n]
        hk, body = get_section(sec, f'Layer {n}')
        # title is text after the colon in the heading, fallback generic
        title = ''
        if hk and ':' in hk:
            title = hk.split(':', 1)[1].strip()
        elif hk:
            title = re.sub(r'^Layer \d+\s*[\u2014-]\s*\w+\s*', '', hk).strip()
        layer_html.append(f'''<div class="layer-card layer-{key}">
<div class="layer-label"><span class="layer-dot {dot}"></span>{_html.escape(label)}</div>
<div class="layer-title">{inline_md(title)}</div>
<p class="layer-body">{inline_md(body)}</p>
</div>''')

    pull = get_section(sec, 'Pull Quote')[1]
    realtalk = get_section(sec, 'Real Talk')[1]
    trap = get_section(sec, 'Trap')[1]
    bonus = get_section(sec, 'Bonus')[1]

    # roadmap: ordered list "1. **lead** rest"
    road_raw = get_section(sec, 'Roadmap')[1]
    moves = []
    for line in road_raw.splitlines():
        lm = re.match(r'^\s*\d+\.\s+(.*)$', line)
        if lm:
            moves.append(lm.group(1).strip())
    moves_html = '\n'.join(
        f'<div class="roadmap-move"><div class="move-num">{i+1}</div><div class="move-text">{inline_md(mv)}</div></div>'
        for i, mv in enumerate(moves)
    )

    intro_html = '\n'.join(f'<p>{inline_md(x)}</p>' for x in paras(intro))

    return order, rid, full, fm.get('short', full), f'''<section class="role role-{rid}" id="{rid}">
<div class="role-page">

<div class="role-header">
<div class="role-icon-chip">{icon}</div>
<div class="role-number-badge">Role {order:02d} of 09</div>
<h2>{_html.escape(full)}</h2>
<p>{inline_md(stack)}</p>
</div>

<p class="lead">{inline_md(lead)}</p>

{intro_html}

{layer_html[0]}

{layer_html[1]}

{layer_html[2]}

</div>
<div class="role-page-cont">

<div class="pull-quote">{inline_md(pull)}</div>

<div class="real-talk">
<div class="real-talk-label">The Real Talk</div>
<p>{inline_md(realtalk)}</p>
</div>

<div class="roadmap">
<div class="roadmap-title">90-Day Top-1% Roadmap for {_html.escape(full)}s</div>
{moves_html}
</div>

<div class="trap-box">
<div class="trap-label">THE TRAP, Don't Waste Time Here</div>
<p class="trap-body">{inline_md(trap)}</p>
</div>

<div class="bonus-tip">
<div class="bonus-tip-label">BONUS MOVE</div>
<p>{inline_md(bonus)}</p>
</div>

</div>
</section>'''

# ---------------------------------------------------------------- gather roles
role_files = sorted(glob.glob(p('content/roles/*.md')))
rendered = [render_role(f) for f in role_files]
rendered.sort(key=lambda x: x[0])
roles_block = "\n\n".join(r[4] for r in rendered)
nav_links = "\n".join(
    f'        <a href="#{rid}" data-target="{rid}"><span class="nav-num">{order:02d}</span>{short}</a>'
    for (order, rid, full, short, _) in rendered
)

# ---------------------------------------------------------------- sections
problem_model = open(p('content/sections/01-problem-and-model.html'), encoding='utf-8').read()
universal = open(p('content/sections/02-universal-os.html'), encoding='utf-8').read()
manifesto = open(p('content/sections/03-manifesto.html'), encoding='utf-8').read()

# inject 3-layer illustration + reveal hooks
model_illus = ('<div class="section-illus illus-model reveal">'
    '<img src="./assets/ill_model.png" alt="Three-layer pyramid: a large red commodity base, an amber leverage middle, and a small green irreplaceable top" loading="lazy"></div>')
problem_model = problem_model.replace('<div class="model-visual">', model_illus + '\n<div class="model-visual">', 1)
for cls in ('commodity', 'leverage', 'irreplaceable'):
    problem_model = problem_model.replace(f'class="model-row model-row-{cls}"', f'class="model-row model-row-{cls} reveal"')

# manifesto art behind box
manifesto = manifesto.replace('<div class="manifesto">',
    '<div class="manifesto"><div class="manifesto-art"><img src="./assets/ill_manifesto.png" alt="" aria-hidden="true"></div>', 1)

# ---------------------------------------------------------------- assemble
OUT = open(p('template.html'), encoding='utf-8').read()
OUT = OUT.replace('<!--CONTENT_SECTIONS-->', problem_model)
OUT = OUT.replace('<!--ROLES-->', roles_block)
OUT = OUT.replace('<!--UNIVERSAL-->', universal)
OUT = OUT.replace('<!--MANIFESTO-->', manifesto)
OUT = OUT.replace('<!--NAV_LINKS-->', nav_links)

os.makedirs(p('dist'), exist_ok=True)
open(p('dist/index.html'), 'w', encoding='utf-8').write(OUT)

# copy assets
src_assets = p('assets')
dst_assets = p('dist/assets')
if os.path.isdir(src_assets):
    shutil.rmtree(dst_assets, ignore_errors=True)
    shutil.copytree(src_assets, dst_assets)

# CNAME for custom domain (GitHub Pages reads dist/CNAME if present in published dir)
cname = p('CNAME')
if os.path.exists(cname):
    shutil.copy(cname, p('dist/CNAME'))
# .nojekyll so GitHub Pages serves files as-is
open(p('dist/.nojekyll'), 'w').write('')

print(f"Built dist/index.html ({len(OUT)} chars) from {len(rendered)} roles.")
