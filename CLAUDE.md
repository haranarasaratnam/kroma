# CLAUDE.md

Project-specific context for Claude Code sessions on this repo.

## What this is

KROMA — a Flask reference site for STEM tutoring, deployed on
PythonAnywhere's free tier. Tutor uses it during sessions to pull up study
guides, practice problems, video tutorials, and links to interactive tools;
students access content via shared URLs.

Branding: **KROMA**. The wireframes under `docs/` still reference the
original placeholder name ("TUTOR GENIE") — that's reference material and
should **not** be edited.

## Tech stack

- Python 3.10+ (Python 3.12 locally via `.venv`)
- Flask 3 + Jinja2
- `markdown` (used by the `|markdown` Jinja filter for study-guide bodies)
- Vanilla CSS, vanilla JS — no build step, no bundler, no CSS framework

Dependencies are pinned in `requirements.txt`. Keep the list tiny:
PythonAnywhere's free tier has disk and CPU quotas, and every new
dependency slows down cold-reload time.

## Project layout

```
app.py            # Flask app factory + all routes + 404 handler
config.py         # SITE_NAME / TAGLINE / DESCRIPTION constants
content.py        # In-memory SUBJECTS dict; single source of truth for content
wsgi.py           # PythonAnywhere WSGI entry (imports `application` from app)
templates/        # Jinja templates; all extend base.html
  includes/       # header.html, nav.html, footer.html, icons/*.html
static/css/       # style.css only — keep design tokens in :root
static/js/        # main.js only — vanilla, defer-loaded
docs/             # Original wireframe PNGs and architecture markdown (DO NOT EDIT)
```

## Important conventions

### Slug naming (don't conflate the two)

Dict keys in `content.py` are Python-friendly (`study_guides`,
`practice_problems`); URL slugs are hyphenated (`study-guides`,
`practice-problems`). Conversion lives in `content.SLUG_TO_KEY` /
`content.KEY_TO_SLUG`. Routes accept the URL form and translate.

### Jinja gotcha: never name a dict key `items`

`mydict.items` in Jinja resolves to the bound `dict.items()` method, not
the value at key `"items"`. The `topic_detail.html` template uses
`sec.entries` (not `sec.items`) for exactly this reason. If you add a new
data structure passed to a template, avoid the keys `items`, `keys`,
`values`, `update`, `pop`, `get`, `copy`.

### Content lives in `content.py`, not a database (yet)

The MVP intentionally has no SQLite. To add a topic or study guide:
edit the `SUBJECTS` dict, commit, push, pull on PythonAnywhere, reload.
When `content.py` becomes unwieldy, the migration path is
`content.py` → SQLite + SQLAlchemy behind the same helper functions
(`get_subject`, `get_topic`, `list_content`, etc.) — keep that API stable.

### Templates always extend `base.html`

Every page template starts with `{% extends 'base.html' %}` and defines
`{% block title %}` and `{% block content %}`. Header/nav/footer come from
`base.html` via `{% include %}`, and global context (`SITE_NAME`,
`ALL_SUBJECTS`, `CONTENT_TYPES`) is injected by `@app.context_processor`
in `app.py` — don't re-pass these from routes.

### Inline SVG icons, not an icon font

Subject icons live under `templates/includes/icons/<name>.html` and are
included via `{% include 'includes/icons/' + s.icon + '.html' ignore missing %}`.
Adding a new subject means adding a matching icon file.

## Running locally

```bash
source .venv/bin/activate
python app.py
```

Open <http://127.0.0.1:5000>.

If `.venv` doesn't have `pip` (it's a `uv`-managed venv), install deps with:
```bash
uv pip install --python .venv/bin/python -r requirements.txt
```

## Smoke-testing

Boot the app via Flask's test client and hit every URL — faster than
`flask run` and catches missing templates, `url_for` typos, and KeyErrors
in one shot. Example pattern:

```python
from app import app
client = app.test_client()
for p in ['/', '/subjects', '/subjects/mathematics', ...]:
    print(client.get(p).status_code, p)
```

## Deployment

PythonAnywhere free tier — see `README.md` for full steps. Quick update:

```bash
# In a PythonAnywhere Bash console:
cd ~/kroma && git pull
# only if requirements.txt changed:
source .venv/bin/activate && pip install -r requirements.txt
# then click Reload on the Web tab
```

The WSGI file on PythonAnywhere (`/var/www/<user>_pythonanywhere_com_wsgi.py`)
imports `application` from this repo's `wsgi.py`. The repo's `wsgi.py` is the
portable bridge; the platform file is the only piece of platform-specific glue.

## Branching

- `main` = deployable / what's live on PythonAnywhere.
- `dev_<area>` (e.g. `dev_physics`) = work-in-progress content for a single
  subject. Merge to `main` when the new topics render correctly end-to-end.

## What NOT to do

- Don't introduce a JS bundler, npm dependency, or CSS framework — the
  zero-build-step constraint is intentional for free-tier hosting.
- Don't add a database, queue, or background worker without discussing.
  Free tier has no persistent processes and limited outbound network.
- Don't rename the placeholder text in `docs/*` — those files are reference
  artifacts.
- Don't commit `README_mine.txt` (already in `.gitignore`).
- Don't push to `main` without first booting the app and hitting routes.
