import os


class Config:
    SITE_NAME = "KROMA"
    TAGLINE = "Master STEM with Expert Guidance"
    DESCRIPTION = (
        "High-quality study guides, practice problems, and expert insights "
        "to help you learn, practice, and excel in STEM subjects."
    )
    SECRET_KEY = os.environ.get("KROMA_SECRET_KEY", "dev-secret-change-me")
