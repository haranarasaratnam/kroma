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
                            "A comprehensive guide to understanding functions and "
                            "their transformations for AP Precalculus."
                        ),
                        "sections": [
                            {
                                "id": "key-concepts",
                                "title": "Key Concepts",
                                "icon": "bulb",
                                "blocks": [
                                    {
                                        "type": "definitions",
                                        "intro": (
                                            "Functions describe a relationship between inputs (x) "
                                            "and outputs (y). Transformations change the position, "
                                            "size, or orientation of a function's graph."
                                        ),
                                        "entries": [
                                            {"term": "Function", "definition": "A rule that assigns each input exactly one output."},
                                            {"term": "Domain", "definition": "The set of all possible input values (x)."},
                                            {"term": "Range", "definition": "The set of all possible output values (y)."},
                                            {"term": "Transformations", "definition": "Shifts, stretches, compressions, and reflections of a parent function."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "important-formulas",
                                "title": "Important Formulas",
                                "icon": "calc",
                                "blocks": [
                                    {
                                        "type": "formula_cards",
                                        "cards": [
                                            {"title": "Linear Function", "formula": "f(x) = mx + b", "note": "m = slope, b = y-intercept"},
                                            {"title": "Quadratic Function", "formula": "f(x) = ax² + bx + c", "note": "a ≠ 0"},
                                            {"title": "Absolute Value Function", "formula": "f(x) = a|x − h| + k", "note": "Vertex: (h, k)"},
                                            {"title": "Specific to Transformations", "formula": "g(x) = a·f(b(x − h)) + k", "note": "a, b ≠ 0"},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "transformation-rules",
                                "title": "Transformation Rules",
                                "icon": "swap",
                                "blocks": [
                                    {
                                        "type": "table",
                                        "headers": ["Transformation", "Form of g(x)", "Effect on Graph", "Example"],
                                        "rows": [
                                            ["Vertical Shift Up", "g(x) = f(x) + k", "Shift up k units", "g(x) = f(x) + 3"],
                                            ["Vertical Shift Down", "g(x) = f(x) − k", "Shift down k units", "g(x) = f(x) − 2"],
                                            ["Horizontal Shift Right", "g(x) = f(x − h)", "Shift right h units", "g(x) = f(x − 4)"],
                                            ["Horizontal Shift Left", "g(x) = f(x + h)", "Shift left h units", "g(x) = f(x + 1)"],
                                            ["Vertical Stretch", "g(x) = a·f(x), |a| > 1", "Stretch vertically by factor a", "g(x) = 2f(x)"],
                                            ["Reflection (x-axis)", "g(x) = −f(x)", "Flip across x-axis", "g(x) = −f(x)"],
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "graphing-steps",
                                "title": "Graphing Steps",
                                "icon": "chart",
                                "blocks": [
                                    {
                                        "type": "steps",
                                        "entries": [
                                            {"title": "Identify the parent function", "detail": "Recognize whether the base is linear, quadratic, absolute value, etc."},
                                            {"title": "Apply horizontal shifts and reflections", "detail": "Work inside the parentheses first: (x − h) shifts right, −x reflects across the y-axis."},
                                            {"title": "Apply vertical stretches and compressions", "detail": "Multiply outputs by a; |a| > 1 stretches, 0 < |a| < 1 compresses."},
                                            {"title": "Apply vertical shifts last", "detail": "Add or subtract k to move the entire graph up or down."},
                                            {"title": "Label key points", "detail": "Plot the vertex or intercepts and at least two more points for accuracy."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "examples",
                                "title": "Examples",
                                "icon": "book",
                                "blocks": [
                                    {
                                        "type": "examples",
                                        "entries": [
                                            {
                                                "title": "Evaluating a function",
                                                "prompt": "If f(x) = 2x + 3, find f(5).",
                                                "solution": "f(5) = 2(5) + 3 = 13.",
                                            },
                                            {
                                                "title": "Identifying transformations",
                                                "prompt": "Describe how g(x) = (x − 2)² + 1 transforms the parent f(x) = x².",
                                                "solution": "Shift right 2 units, then up 1 unit.",
                                            },
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "practice-problems",
                                "title": "Practice Problems",
                                "icon": "pencil",
                                "blocks": [
                                    {
                                        "type": "practice",
                                        "entries": [
                                            {"question": "State the domain of f(x) = 1 / (x − 4).", "solution": "All real x except x = 4."},
                                            {"question": "Given f(x) = x², write the equation for the graph shifted left 3 and down 5.", "solution": "g(x) = (x + 3)² − 5."},
                                            {"question": "Find the range of f(x) = |x| + 2.", "solution": "[2, ∞)."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "common-mistakes",
                                "title": "Common Mistakes",
                                "icon": "alert",
                                "blocks": [
                                    {
                                        "type": "mistakes",
                                        "entries": [
                                            {"mistake": "Confusing horizontal shift direction", "fix": "f(x − h) shifts the graph to the right, not the left."},
                                            {"mistake": "Applying transformations in the wrong order", "fix": "Inside-the-parentheses changes happen first, vertical shifts last."},
                                            {"mistake": "Forgetting domain restrictions", "fix": "Watch for division by zero and even roots of negatives."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "quick-review",
                                "title": "Quick Review",
                                "icon": "clipboard",
                                "blocks": [
                                    {
                                        "type": "review",
                                        "entries": [
                                            "A function maps each input to exactly one output.",
                                            "Transformations stack: inside-then-outside, horizontal-then-vertical.",
                                            "Memorize parent-function shapes: line, parabola, |x|, √x, 1/x.",
                                            "Always verify domain and range after transforming.",
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    "polynomial-and-rational-functions": {
                        "title": "Polynomial and Rational Functions",
                        "blurb": (
                            "Analyze polynomial and rational functions: zeros, "
                            "end behavior, and asymptotes."
                        ),
                        "sections": [
                            {
                                "id": "key-concepts",
                                "title": "Key Concepts",
                                "icon": "bulb",
                                "blocks": [
                                    {
                                        "type": "definitions",
                                        "intro": (
                                            "Polynomial functions are sums of power terms. Rational "
                                            "functions are ratios of polynomials and may have vertical, "
                                            "horizontal, or slant asymptotes."
                                        ),
                                        "entries": [
                                            {"term": "Polynomial", "definition": "A sum of terms of the form a·xⁿ with non-negative integer exponents."},
                                            {"term": "Degree", "definition": "The largest exponent; controls end behavior and the maximum number of real zeros."},
                                            {"term": "Rational function", "definition": "A ratio p(x)/q(x) of polynomials with q(x) ≠ 0."},
                                            {"term": "Asymptote", "definition": "A line the graph approaches but does not cross (vertical, horizontal, or slant)."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "important-formulas",
                                "title": "Important Formulas",
                                "icon": "calc",
                                "blocks": [
                                    {
                                        "type": "formula_cards",
                                        "cards": [
                                            {"title": "Standard Polynomial", "formula": "f(x) = aₙxⁿ + ... + a₁x + a₀", "note": "Degree n, leading coefficient aₙ"},
                                            {"title": "Factored Form", "formula": "f(x) = a(x − r₁)(x − r₂)...", "note": "rᵢ are the real zeros"},
                                            {"title": "Rational Function", "formula": "f(x) = p(x) / q(x)", "note": "Vertical asymptote when q(x) = 0"},
                                            {"title": "Horizontal Asymptote", "formula": "y = aₙ / bₙ (deg p = deg q)", "note": "y = 0 if deg p < deg q"},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "common-mistakes",
                                "title": "Common Mistakes",
                                "icon": "alert",
                                "blocks": [
                                    {
                                        "type": "mistakes",
                                        "entries": [
                                            {"mistake": "Calling every zero of q(x) a vertical asymptote", "fix": "If the same factor appears in p(x), it cancels to a hole, not an asymptote."},
                                            {"mistake": "Assuming end behavior matches the constant term", "fix": "End behavior is set by the leading term, not the constant."},
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    "exponential-and-logarithmic-functions": {
                        "title": "Exponential and Logarithmic Functions",
                        "blurb": "Understand exponential growth and decay, logs, and their inverse relationship.",
                        "sections": [
                            {
                                "id": "key-concepts",
                                "title": "Key Concepts",
                                "icon": "bulb",
                                "blocks": [
                                    {
                                        "type": "definitions",
                                        "intro": (
                                            "Exponential functions model growth and decay. Logarithms "
                                            "are their inverses and let us solve equations where the "
                                            "unknown is in the exponent."
                                        ),
                                        "entries": [
                                            {"term": "Exponential function", "definition": "f(x) = a·bˣ with b > 0, b ≠ 1."},
                                            {"term": "Logarithm", "definition": "log_b(y) = x means bˣ = y."},
                                            {"term": "Natural log", "definition": "ln(x) = log_e(x) with e ≈ 2.71828."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "important-formulas",
                                "title": "Important Formulas",
                                "icon": "calc",
                                "blocks": [
                                    {
                                        "type": "formula_cards",
                                        "cards": [
                                            {"title": "Continuous Growth", "formula": "A = A₀ eᵏᵗ", "note": "k > 0 growth, k < 0 decay"},
                                            {"title": "Compound Interest", "formula": "A = P(1 + r/n)ⁿᵗ", "note": "n compoundings per year"},
                                            {"title": "Change of Base", "formula": "log_b(x) = ln(x) / ln(b)", "note": "Convert between log bases"},
                                            {"title": "Log Rules", "formula": "log(xy) = log x + log y", "note": "Also: log(xⁿ) = n·log x"},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "quick-review",
                                "title": "Quick Review",
                                "icon": "clipboard",
                                "blocks": [
                                    {
                                        "type": "review",
                                        "entries": [
                                            "Exponentials and logs are inverses; their graphs reflect over y = x.",
                                            "Always check the domain of a log: argument must be positive.",
                                            "Use change-of-base to evaluate any log with a calculator.",
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    "trigonometric-functions": {
                        "title": "Trigonometric Functions",
                        "blurb": "Study angles, the unit circle, identities, and graphs of trig functions.",
                        "sections": [
                            {
                                "id": "key-concepts",
                                "title": "Key Concepts",
                                "icon": "bulb",
                                "blocks": [
                                    {
                                        "type": "definitions",
                                        "intro": (
                                            "Trigonometric functions relate angles to ratios of sides "
                                            "in right triangles and to coordinates on the unit circle."
                                        ),
                                        "entries": [
                                            {"term": "Unit circle", "definition": "Circle of radius 1 centered at the origin; (cos θ, sin θ) gives any point."},
                                            {"term": "Radian", "definition": "Angle measure where one full revolution equals 2π radians."},
                                            {"term": "Period", "definition": "The horizontal length over which a trig function repeats."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "important-formulas",
                                "title": "Important Formulas",
                                "icon": "calc",
                                "blocks": [
                                    {
                                        "type": "formula_cards",
                                        "cards": [
                                            {"title": "Pythagorean Identity", "formula": "sin²θ + cos²θ = 1", "note": "Foundation of all trig identities"},
                                            {"title": "Reciprocal Identities", "formula": "cscθ = 1/sinθ", "note": "sec = 1/cos, cot = 1/tan"},
                                            {"title": "Law of Sines", "formula": "a/sin A = b/sin B = c/sin C", "note": "Any triangle"},
                                            {"title": "Law of Cosines", "formula": "c² = a² + b² − 2ab·cos C", "note": "Extends Pythagoras"},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "common-mistakes",
                                "title": "Common Mistakes",
                                "icon": "alert",
                                "blocks": [
                                    {
                                        "type": "mistakes",
                                        "entries": [
                                            {"mistake": "Mixing degrees and radians", "fix": "Set your calculator mode before evaluating; π only makes sense in radian mode."},
                                            {"mistake": "Forgetting reference angles", "fix": "Sketch the angle in standard position to find the right sign in each quadrant."},
                                        ],
                                    },
                                ],
                            },
                        ],
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
                        "sections": [
                            {
                                "id": "key-concepts",
                                "title": "Key Concepts",
                                "icon": "bulb",
                                "blocks": [
                                    {
                                        "type": "definitions",
                                        "intro": (
                                            "A limit describes the value a function approaches as "
                                            "the input approaches some value, even if the function "
                                            "is undefined there."
                                        ),
                                        "entries": [
                                            {"term": "Limit", "definition": "lim x→a f(x) = L means f(x) approaches L as x approaches a."},
                                            {"term": "One-sided limit", "definition": "The value approached from either the left (x → a⁻) or right (x → a⁺)."},
                                            {"term": "Continuity at a", "definition": "f is continuous at a if lim x→a f(x) = f(a)."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "important-formulas",
                                "title": "Important Formulas",
                                "icon": "calc",
                                "blocks": [
                                    {
                                        "type": "formula_cards",
                                        "cards": [
                                            {"title": "Sum Rule", "formula": "lim (f + g) = lim f + lim g", "note": "When both limits exist"},
                                            {"title": "Product Rule", "formula": "lim (f·g) = (lim f)(lim g)", "note": "Distributes over multiplication"},
                                            {"title": "Squeeze Theorem", "formula": "g ≤ f ≤ h ⇒ lim f = L", "note": "If lim g = lim h = L"},
                                        ],
                                    },
                                ],
                            },
                        ],
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
                "intro": (
                    "Vectors, kinematics, forces and Newton's laws, gravitation, "
                    "linear momentum and impacts, and rotational motion."
                ),
                "study_guides": {
                    "newtons-laws-of-motion": {
                        "title": "Newton's Laws of Motion",
                        "blurb": "The three laws that govern classical mechanics.",
                        "sections": [
                            {
                                "id": "key-concepts",
                                "title": "Key Concepts",
                                "icon": "bulb",
                                "blocks": [
                                    {
                                        "type": "definitions",
                                        "intro": (
                                            "Newton's three laws together describe how forces "
                                            "affect the motion of everyday objects."
                                        ),
                                        "entries": [
                                            {"term": "First law (inertia)", "definition": "An object at rest stays at rest, and an object in motion stays in motion, unless acted on by a net external force."},
                                            {"term": "Second law", "definition": "Net force equals mass times acceleration: F = ma."},
                                            {"term": "Third law", "definition": "For every action there is an equal and opposite reaction."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "important-formulas",
                                "title": "Important Formulas",
                                "icon": "calc",
                                "blocks": [
                                    {
                                        "type": "formula_cards",
                                        "cards": [
                                            {"title": "Second Law", "formula": "F = m·a", "note": "Newtons = kg·m/s²"},
                                            {"title": "Weight", "formula": "W = m·g", "note": "g ≈ 9.81 m/s² on Earth"},
                                            {"title": "Friction", "formula": "f = μ·N", "note": "μ = coefficient of friction"},
                                            {"title": "Momentum", "formula": "p = m·v", "note": "Vector quantity"},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "common-mistakes",
                                "title": "Common Mistakes",
                                "icon": "alert",
                                "blocks": [
                                    {
                                        "type": "mistakes",
                                        "entries": [
                                            {"mistake": "Treating mass and weight as the same thing", "fix": "Mass is in kg and is invariant; weight is a force in newtons and depends on g."},
                                            {"mistake": "Using F = ma with a non-net force", "fix": "Sum all forces on the object first; only the net force equals ma."},
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                },
                "practice_problems": {}, "videos": {}, "tools": {},
            },
            "energy-and-oscillations": {
                "name": "Energy & Oscillations",
                "intro": (
                    "Work, power, kinetic and potential energy, conservation of "
                    "energy, and simple harmonic motion of springs and pendulums."
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "waves-and-sound": {
                "name": "Waves & Sound",
                "intro": (
                    "Pulses, wave motion, types of waves, standing waves and "
                    "resonance, sound, and the Doppler effect."
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "fluids": {
                "name": "Fluids",
                "intro": (
                    "Static fluids, Pascal's principle, buoyancy and Archimedes' "
                    "principle, fluids in motion, and Bernoulli's equation. (AP Physics 2)"
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "thermodynamics": {
                "name": "Thermodynamics",
                "intro": (
                    "Temperature, the ideal gas law, kinetic-molecular theory, the "
                    "first and second laws of thermodynamics, and heat transfer. (AP Physics 2)"
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "electricity-and-circuits": {
                "name": "Electricity & Circuits",
                "intro": (
                    "Electric charges, Coulomb's law, electric fields and potential, "
                    "capacitance, current, resistance, and series and parallel circuits."
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "magnetism-and-electromagnetism": {
                "name": "Magnetism & Electromagnetism",
                "intro": (
                    "Magnetic fields and forces, magnetic effects of currents, induced "
                    "EMF, and Faraday's law of induction. (AP Physics 2)"
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "optics": {
                "name": "Optics",
                "intro": (
                    "Reflection, refraction, interference, diffraction, and image "
                    "formation in plane mirrors, curved mirrors, and lenses. (AP Physics 2)"
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
            },
            "modern-physics": {
                "name": "Modern Physics",
                "intro": (
                    "Photoelectric and Compton effects, matter waves, atomic models, "
                    "special relativity, and nuclear structure, fission, and fusion. (AP Physics 2)"
                ),
                "study_guides": {}, "practice_problems": {}, "videos": {}, "tools": {},
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
                        "sections": [
                            {
                                "id": "key-concepts",
                                "title": "Key Concepts",
                                "icon": "bulb",
                                "blocks": [
                                    {
                                        "type": "definitions",
                                        "intro": (
                                            "Organic chemistry studies carbon compounds and their "
                                            "transformations. Recognizing functional groups is the "
                                            "first step in predicting reactivity."
                                        ),
                                        "entries": [
                                            {"term": "Hydrocarbon", "definition": "A compound containing only carbon and hydrogen."},
                                            {"term": "Functional group", "definition": "An atom or group of atoms that defines the reactivity of a molecule."},
                                            {"term": "Isomers", "definition": "Compounds with the same molecular formula but different structures."},
                                        ],
                                    },
                                ],
                            },
                            {
                                "id": "important-formulas",
                                "title": "Important Formulas",
                                "icon": "calc",
                                "blocks": [
                                    {
                                        "type": "formula_cards",
                                        "cards": [
                                            {"title": "Alkane", "formula": "CₙH₂ₙ₊₂", "note": "Single bonds only"},
                                            {"title": "Alkene", "formula": "CₙH₂ₙ", "note": "One C=C double bond"},
                                            {"title": "Alkyne", "formula": "CₙH₂ₙ₋₂", "note": "One C≡C triple bond"},
                                            {"title": "Alcohol", "formula": "R−OH", "note": "Hydroxyl functional group"},
                                        ],
                                    },
                                ],
                            },
                        ],
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
