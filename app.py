"""KROMA -- Flask app for a STEM tutoring reference site.

Designed to run on PythonAnywhere's free tier:
- Single-process WSGI app (see wsgi.py).
- No database, no Celery, no Redis.
- Static assets served from `static/`; Jinja2 templates in `templates/`.
"""
from flask import Flask, abort, render_template, request

import markdown as md

from config import Config
import content as content_store


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.template_filter("markdown")
    def render_markdown(text):
        if not text:
            return ""
        return md.markdown(text, extensions=["fenced_code", "tables"])

    @app.context_processor
    def inject_globals():
        return {
            "SITE_NAME": app.config["SITE_NAME"],
            "TAGLINE": app.config["TAGLINE"],
            "DESCRIPTION": app.config["DESCRIPTION"],
            "ALL_SUBJECTS": content_store.list_subjects(),
            "CONTENT_TYPES": content_store.CONTENT_TYPES,
        }

    register_routes(app)
    return app


def register_routes(app):

    @app.route("/")
    def home():
        return render_template(
            "index.html",
            featured=content_store.list_subjects(),
            recent=content_store.recent_additions(limit=4),
        )

    @app.route("/subjects")
    def subjects():
        return render_template(
            "subjects.html",
            subjects=content_store.list_subjects(),
        )

    @app.route("/subjects/<subject_slug>")
    def subject_detail(subject_slug):
        subject = content_store.get_subject(subject_slug)
        if not subject:
            abort(404)
        topics = [
            {"slug": slug, **data} for slug, data in subject["topics"].items()
        ]
        return render_template(
            "subject_detail.html",
            subject_slug=subject_slug,
            subject=subject,
            topics=topics,
        )

    @app.route("/subjects/<subject_slug>/<topic_slug>")
    def topic_detail(subject_slug, topic_slug):
        subject = content_store.get_subject(subject_slug)
        topic = content_store.get_topic(subject_slug, topic_slug)
        if not subject or not topic:
            abort(404)
        sections = []
        for key, slug, label in content_store.CONTENT_TYPES:
            items = topic.get(key, {})
            sections.append({
                "key": key,
                "slug": slug,
                "label": label,
                "entries": [
                    {"slug": item_slug, **item} for item_slug, item in items.items()
                ],
            })
        return render_template(
            "topic_detail.html",
            subject_slug=subject_slug,
            subject=subject,
            topic_slug=topic_slug,
            topic=topic,
            sections=sections,
        )

    @app.route("/subjects/<subject_slug>/<topic_slug>/<content_slug>")
    def content_list(subject_slug, topic_slug, content_slug):
        subject = content_store.get_subject(subject_slug)
        topic = content_store.get_topic(subject_slug, topic_slug)
        content_key = content_store.SLUG_TO_KEY.get(content_slug)
        if not subject or not topic or content_key is None:
            abort(404)
        items = topic.get(content_key, {})
        return render_template(
            "content_list.html",
            subject_slug=subject_slug,
            subject=subject,
            topic_slug=topic_slug,
            topic=topic,
            content_slug=content_slug,
            content_key=content_key,
            content_label=content_store.KEY_TO_LABEL[content_key],
            items=[{"slug": s, **v} for s, v in items.items()],
        )

    @app.route("/subjects/<subject_slug>/<topic_slug>/<content_slug>/<item_slug>")
    def content_item(subject_slug, topic_slug, content_slug, item_slug):
        subject = content_store.get_subject(subject_slug)
        topic = content_store.get_topic(subject_slug, topic_slug)
        content_key = content_store.SLUG_TO_KEY.get(content_slug)
        if not subject or not topic or content_key is None:
            abort(404)
        item = content_store.get_content_item(
            subject_slug, topic_slug, content_key, item_slug
        )
        if not item:
            abort(404)
        template_map = {
            "study_guides": "study_guide.html",
            "practice_problems": "practice_problems.html",
            "videos": "video_detail.html",
            "tools": "tool_detail.html",
        }
        return render_template(
            template_map[content_key],
            subject_slug=subject_slug,
            subject=subject,
            topic_slug=topic_slug,
            topic=topic,
            content_slug=content_slug,
            content_key=content_key,
            content_label=content_store.KEY_TO_LABEL[content_key],
            item_slug=item_slug,
            item=item,
        )

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/search")
    def search():
        query = (request.args.get("q") or "").strip().lower()
        results = []
        if query:
            for subject_slug, subject in content_store.SUBJECTS.items():
                if query in subject["name"].lower():
                    results.append({
                        "type": "Subject",
                        "title": subject["name"],
                        "url": f"/subjects/{subject_slug}",
                    })
                for topic_slug, topic in subject["topics"].items():
                    if query in topic["name"].lower():
                        results.append({
                            "type": "Topic",
                            "title": f"{subject['name']} -- {topic['name']}",
                            "url": f"/subjects/{subject_slug}/{topic_slug}",
                        })
                    for key, slug, _ in content_store.CONTENT_TYPES:
                        for item_slug, item in topic.get(key, {}).items():
                            title = item.get("title", "")
                            if query in title.lower():
                                results.append({
                                    "type": content_store.KEY_TO_LABEL[key],
                                    "title": title,
                                    "url": f"/subjects/{subject_slug}/{topic_slug}/{slug}/{item_slug}",
                                })
        return render_template("search.html", query=query, results=results)

    @app.errorhandler(404)
    def not_found(_):
        return render_template("404.html"), 404


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
