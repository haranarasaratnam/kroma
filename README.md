# KROMA

Personal STEM tutoring reference site -- a Flask app designed to run on
PythonAnywhere's free tier.

## Tech stack

- Python 3.12
- Flask 3 + Jinja2
- `markdown` for rendering study-guide bodies
- Vanilla CSS, vanilla JS (no build step)

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

## Project layout

```
kroma/
├── app.py            # Flask app factory + routes
├── config.py         # SITE_NAME / branding constants
├── content.py        # In-memory subject/topic/content data
├── wsgi.py           # PythonAnywhere WSGI entry point
├── requirements.txt
├── static/
│   ├── css/style.css
│   └── js/main.js
└── templates/
    ├── base.html
    ├── index.html, subjects.html, subject_detail.html, topic_detail.html,
    │   content_list.html, study_guide.html, practice_problems.html,
    │   video_detail.html, tool_detail.html, about.html, contact.html,
    │   search.html, 404.html
    └── includes/
        ├── header.html, nav.html, footer.html
        └── icons/*.html
```

## Deploying to PythonAnywhere (free tier)

1. Create a free account at <https://www.pythonanywhere.com/>.
2. Open a **Bash console** and clone or upload the project:
   ```bash
   git clone <your-repo-url> kroma
   cd kroma
   python3.10 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
   (The app runs on any Python 3.10+; pick a version PythonAnywhere supports.)
3. Go to the **Web** tab -> **Add a new web app** -> choose **Manual configuration**
   and pick the Python version that matches your virtualenv.
4. In the web app config:
   - **Source code**: `/home/<username>/kroma`
   - **Working directory**: `/home/<username>/kroma`
   - **Virtualenv**: `/home/<username>/kroma/.venv`
5. Edit the **WSGI configuration file** (link near the top of the Web tab)
   and replace its contents with:
   ```python
   import sys
   path = '/home/<username>/kroma'
   if path not in sys.path:
       sys.path.insert(0, path)
   from wsgi import application
   ```
6. Under **Static files** add a mapping:
   - URL: `/static/`
   - Directory: `/home/<username>/kroma/static/`
7. Click **Reload** at the top of the Web tab.

Your site is live at `https://<username>.pythonanywhere.com`.

### Updating content

Edit `content.py` (the `SUBJECTS` dict), commit, pull on PythonAnywhere, then
click **Reload** on the Web tab. No database migration needed.

## Future scalability

The architecture doc in `docs/` describes the upgrade path: swap `content.py`
for a SQLite + SQLAlchemy layer behind the same helper functions, add
Flask-Login for student accounts, and add Flask-Admin for content editing
without code changes.
