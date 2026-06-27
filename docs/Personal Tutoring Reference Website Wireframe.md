# Personal Tutoring Reference Website Wireframe

## Executive Summary

This document outlines the wireframe for a personal tutoring reference website designed to support high school STEM tutoring sessions, both online and in-person. The platform will serve as a dynamic resource for the tutor to display and share study guides, practice problems, video tutorials, and interactive tools across various STEM subjects. The architecture is designed with Flask for hosting on PythonAnywhere, ensuring simplicity and scalability for future enhancements.

---

## 1. Information Architecture

The website will be organized primarily by STEM subjects, with each subject containing subsections for specific topics, chapters, or exam types (e.g., AP, SAT). Content types within each topic will include study guides, practice problems, video tutorials, and interactive tools.

### Site Structure:

- **Home Page** (`/`)
  - Introduction, featured subjects, recent additions, call-to-action.
- **Subject Listing Page** (`/subjects`)
  - List of all available STEM subjects (e.g., Mathematics, Physics, Chemistry, Biology, Computer Science).
- **Individual Subject Page** (`/subjects/<subject_name>`)
  - Overview of the subject.
  - List of topics/subsections within the subject (e.g., for Mathematics: Algebra, Geometry, Precalculus, Calculus).
- **Topic/Subsection Page** (`/subjects/<subject_name>/<topic_name>`)
  - Introduction to the topic.
  - Navigation to different content types:
    - Study Guides (`/subjects/<subject_name>/<topic_name>/study-guides`)
    - Practice Problems (`/subjects/<subject_name>/<topic_name>/practice-problems`)
    - Video Tutorials (`/subjects/<subject_name>/<topic_name>/videos`)
    - Interactive Tools (`/subjects/<subject_name>/<topic_name>/tools`)
- **Content Detail Page** (e.g., `/subjects/mathematics/precalculus/study-guides/functions`)
  - Displays the specific study guide, practice problem set, video, or interactive tool.

---

## 2. Page-Level Wireframes

### 2.1. Home Page (`/`)

**Layout**: Clean, inviting, and easy to navigate.

**Sections**:

1.  **Header**: 
    - Logo (left)
    - Navigation (right): Home, Subjects, About, Contact, Search Bar
2.  **Hero Section**: 
    - Catchy headline: 
