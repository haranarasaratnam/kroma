"""Content registry for KROMA.

The MVP keeps subjects/topics/content in a Python dict so the site runs on
PythonAnywhere's free tier with zero database setup. Swap this for a SQLite
+ SQLAlchemy layer later without touching the routes -- the route handlers
only call the helper functions at the bottom of this module.
"""

SUBJECTS = {
    "mathematics": {
        "name": "Mathematics",
        "icon": "calc",
        "blurb": (
            "Build strong problem-solving skills and master concepts "
            "from basic to advanced math."
        ),
        "topics": {
            "ap-precalculus": {
                "name": "AP Precalculus",
                "intro": (
                    "AP Precalculus prepares students for calculus by building "
                    "strong foundations in functions, trigonometry, polynomial, "
                    "rational, exponential, and logarithmic concepts. Strengthen "
                    "your understanding and skills through study guides, practice "
                    "problems, video lessons, and interactive tools."
                ),
                "study_guides": {
                    "functions-and-their-properties": {
                        "title": "Functions and Their Properties",
                        "blurb": (
                            "Explore domain, range, compositions, inverses, and "
                            "function operations."
                        ),
                        "body": (
                            "## 1. Key Concepts\n\n"
                            "Functions describe a relationship between inputs (x) "
                            "and outputs (y). Transformations change the position, "
                            "size, or orientation of a function's graph.\n\n"
                            "- **Function**: a rule that assigns each input exactly one output.\n"
                            "- **Domain**: the set of all possible input values (x).\n"
                            "- **Range**: the set of all possible output values (y).\n\n"
                            "## 2. Important Formulas\n\n"
                            "- Linear: f(x) = mx + b\n"
                            "- Quadratic: f(x) = ax^2 + bx + c\n"
                            "- Absolute value: f(x) = a|x - h| + k\n\n"
                            "## 3. Transformation Rules\n\n"
                            "- Vertical shift up: g(x) = f(x) + k\n"
                            "- Vertical shift down: g(x) = f(x) - k\n"
                            "- Horizontal shift right: g(x) = f(x - h)\n"
                        ),
                    },
                    "polynomial-and-rational-functions": {
                        "title": "Polynomial and Rational Functions",
                        "blurb": (
                            "Analyze polynomial and rational functions: zeros, "
                            "rational and asymptotic behavior."
                        ),
                        "body": (
                            "## Overview\n\n"
                            "Polynomial functions are sums of power terms. Rational "
                            "functions are ratios of polynomials and may have vertical, "
                            "horizontal, or slant asymptotes.\n"
                        ),
                    },
                    "exponential-and-logarithmic-functions": {
                        "title": "Exponential and Logarithmic Functions",
                        "blurb": "Understand exponential growth and decay logs and their properties.",
                        "body": (
                            "## Overview\n\n"
                            "Exponential functions model growth and decay. Logarithms "
                            "are their inverses and let us solve equations where the "
                            "unknown is in the exponent.\n"
                        ),
                    },
                    "trigonometric-functions": {
                        "title": "Trigonometric Functions",
                        "blurb": "Study angles, unit circle, identities, and graphs of trig functions.",
                        "body": (
                            "## Overview\n\n"
                            "Trigonometric functions relate angles to ratios of sides "
                            "in right triangles and to coordinates on the unit circle.\n"
                        ),
                    },
                },
                "practice_problems": {
                    "functions-practice-set": {
                        "title": "Functions Practice Set",
                        "blurb": "20 problems to practice function notation, operations, and transformations.",
                        "problems": [
                            {
                                "question": "If f(x) = 2x + 3, find f(5).",
                                "solution": "f(5) = 2(5) + 3 = 13",
                            },
                            {
                                "question": "State the domain of f(x) = 1/(x - 4).",
                                "solution": "All real x except x = 4.",
                            },
                        ],
                    },
                    "polynomial-and-rational-practice-set": {
                        "title": "Polynomial and Rational Practice Set",
                        "blurb": "25 problems covering zeros, factoring, and rational functions.",
                        "problems": [
                            {
                                "question": "Factor x^2 - 9.",
                                "solution": "(x - 3)(x + 3)",
                            }
                        ],
                    },
                    "exponential-and-log-practice-set": {
                        "title": "Exponential and Log Practice Set",
                        "blurb": "25 problems on exponential equations, logarithms, and applications.",
                        "problems": [
                            {
                                "question": "Solve 2^x = 16.",
                                "solution": "x = 4",
                            }
                        ],
                    },
                    "trigonometry-practice-set": {
                        "title": "Trigonometry Practice Set",
                        "blurb": "25 problems on identities, equations, and trig graphs.",
                        "problems": [
                            {
                                "question": "Evaluate sin(pi/2).",
                                "solution": "1",
                            }
                        ],
                    },
                },
                "videos": {
                    "introduction-to-functions": {
                        "title": "Introduction to Functions",
                        "duration": "9:42",
                        "embed_url": "https://www.youtube.com/embed/kvGsIo1TmsM",
                    },
                    "functions-and-transformations": {
                        "title": "Functions and Transformations",
                        "duration": "8:15",
                        "embed_url": "https://www.youtube.com/embed/3xRyfPCai_o",
                    },
                    "polynomial-and-rational-functions": {
                        "title": "Polynomial and Rational Functions",
                        "duration": "10:28",
                        "embed_url": "https://www.youtube.com/embed/JLU5tF2OK4c",
                    },
                    "trigonometric-identities": {
                        "title": "Trigonometric Identities",
                        "duration": "7:33",
                        "embed_url": "https://www.youtube.com/embed/2SWTUm-FhPI",
                    },
                },
                "tools": {
                    "function-graphing-tool": {
                        "title": "Function Graphing Tool",
                        "blurb": "Graph functions, explore transformations, and analyze key features.",
                        "url": "https://www.desmos.com/calculator",
                    },
                    "equation-solver": {
                        "title": "Equation Solver",
                        "blurb": "Solve equations and inequalities step by step.",
                        "url": "https://www.wolframalpha.com/",
                    },
                    "trigonometry-explorer": {
                        "title": "Trigonometry Explorer",
                        "blurb": "Visualize the unit circle, angles, and trig ratios interactively.",
                        "url": "https://www.geogebra.org/m/W7dAdgqc",
                    },
                    "logarithm-explorer": {
                        "title": "Logarithm Explorer",
                        "blurb": "Explore logs and exponential relationships with interactive graphs.",
                        "url": "https://www.desmos.com/calculator/eweg72zkfp",
                    },
                },
            },
            "algebra": {
                "name": "Algebra",
                "intro": "Foundations of algebra: expressions, equations, and inequalities.",
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "geometry": {
                "name": "Geometry",
                "intro": "Shapes, proofs, and the structure of space.",
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "calculus": {
                "name": "Calculus",
                "intro": "Limits, derivatives, integrals, and their applications.",
                "study_guides": {
                    "limits-and-continuity": {
                        "title": "Limits and Continuity",
                        "blurb": "Foundational concepts for calculus.",
                        "body": "## Overview\n\nA limit describes the value a function approaches as the input approaches some value.\n",
                    },
                },
                "practice_problems": {}, "videos": {}, "tools": {},
            },
        },
    },
    "physics": {
        "name": "Physics",
        "icon": "atom",
        "blurb": "Understand the laws of nature through clear explanations.",
        "topics": {
            "mechanics": {
                "name": "Mechanics",
                "intro": "Motion, forces, energy, and Newton's laws.",
                "study_guides": {
                    "newtons-laws-of-motion": {
                        "title": "Newton's Laws of Motion",
                        "blurb": "The three laws that govern classical mechanics.",
                        "body": "## Newton's Three Laws\n\n1. An object in motion stays in motion unless acted on by a net force.\n2. F = ma.\n3. For every action there is an equal and opposite reaction.\n",
                    },
                },
                "practice_problems": {}, "videos": {}, "tools": {},
            },
        },
    },
    "chemistry": {
        "name": "Chemistry",
        "icon": "flask",
        "blurb": "Explore the structure and properties of matter.",
        "topics": {
            "organic-chemistry": {
                "name": "Organic Chemistry",
                "intro": "Carbon-based compounds and their reactions.",
                "study_guides": {
                    "organic-chemistry-basics": {
                        "title": "Organic Chemistry Basics",
                        "blurb": "Functional groups, nomenclature, and core reactions.",
                        "body": "## Overview\n\nOrganic chemistry studies carbon compounds and their transformations.\n",
                    },
                },
                "practice_problems": {}, "videos": {}, "tools": {},
            },
        },
    },
    "biology": {
        "name": "Biology",
        "icon": "leaf",
        "blurb": "Learn about living systems and life processes.",
        "topics": {
            "cell-biology": {
                "name": "Cell Biology",
                "intro": "The structure and function of cells.",
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
        },
    },
    "computer-science": {
        "name": "Computer Science",
        "icon": "code",
        "blurb": "Develop coding skills and understand algorithms and data structures.",
        "topics": {
            "algorithms": {
                "name": "Algorithms",
                "intro": "Searching, sorting, and algorithmic thinking.",
                "study_guides": {},
                "practice_problems": {
                    "binary-search-algorithm": {
                        "title": "Binary Search Algorithm",
                        "blurb": "Practice implementing and analyzing binary search.",
                        "problems": [
                            {
                                "question": "What is the time complexity of binary search?",
                                "solution": "O(log n)",
                            }
                        ],
                    },
                },
                "videos": {}, "tools": {},
            },
        },
    },
}


CONTENT_TYPES = (
    ("study_guides", "study-guides", "Study Guides"),
    ("practice_problems", "practice-problems", "Practice Problems"),
    ("videos", "videos", "Video Tutorials"),
    ("tools", "tools", "Interactive Tools"),
)

SLUG_TO_KEY = {slug: key for key, slug, _ in CONTENT_TYPES}
KEY_TO_LABEL = {key: label for key, _, label in CONTENT_TYPES}
KEY_TO_SLUG = {key: slug for key, slug, _ in CONTENT_TYPES}


def list_subjects():
    return [{"slug": slug, **data} for slug, data in SUBJECTS.items()]


def get_subject(subject_slug):
    return SUBJECTS.get(subject_slug)


def get_topic(subject_slug, topic_slug):
    subject = get_subject(subject_slug)
    if not subject:
        return None
    return subject["topics"].get(topic_slug)


def list_content(subject_slug, topic_slug, content_key):
    topic = get_topic(subject_slug, topic_slug)
    if not topic:
        return None
    return topic.get(content_key, {})


def get_content_item(subject_slug, topic_slug, content_key, item_slug):
    items = list_content(subject_slug, topic_slug, content_key)
    if items is None:
        return None
    return items.get(item_slug)


def recent_additions(limit=4):
    """Return a flat list of recently-added content across all subjects.

    In the MVP we just return the first item from each top-level subject's
    first topic with content, in subject order. Later this can read a real
    `created_at` field from the DB.
    """
    out = []
    for subject_slug, subject in SUBJECTS.items():
        for topic_slug, topic in subject["topics"].items():
            for key, slug, label in CONTENT_TYPES:
                items = topic.get(key, {})
                if not items:
                    continue
                item_slug = next(iter(items))
                item = items[item_slug]
                out.append({
                    "subject_slug": subject_slug,
                    "subject_name": subject["name"],
                    "topic_slug": topic_slug,
                    "content_key": key,
                    "content_slug": slug,
                    "content_label": label,
                    "item_slug": item_slug,
                    "title": item.get("title"),
                })
                break
        if len(out) >= limit:
            break
    return out[:limit]
