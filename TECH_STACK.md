# Tech Stack Options - Poll Results Visualizer

## Option A (Easy)

**Description:** A beginner-friendly Python script that reads a CSV file, cleans poll data, computes percentages, and generates static charts saved as image files. No dashboard, no web framework.

| Component | Choice |
|-----------|--------|
| Language | Python 3.10+ |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Dashboard | None (static PNG/HTML charts only) |
| Data Input | CSV file |
| Difficulty | Easy |
| Best For | Students new to data analysis, quick proof-of-concept |

**Pros:**
- Simple to understand and run
- Minimal dependencies
- No deployment needed
- Easy to debug

**Cons:**
- No interactivity
- No real-time updates
- Charts are static images only

---

## Option B (Intermediate)

**Description:** A Python project with a modular structure (`src/`, `main.py`) that supports CSV/Google Forms export input, cleaning, analysis, visualization, summary insights, and an optional Streamlit dashboard for interactivity.

| Component | Choice |
|-----------|--------|
| Language | Python 3.10+ |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Optional Streamlit dashboard |
| Data Input | CSV, Excel, Google Forms export |
| Difficulty | Intermediate |
| Best For | Placement/internship portfolio projects |

**Pros:**
- Professional folder structure
- Modular, reusable code
- Interactive Streamlit dashboard option
- Industry-relevant stack (Pandas + Streamlit)
- Good balance of complexity and learnability

**Cons:**
- Requires Streamlit installation for dashboard
- Slightly more files to manage

---

## Option C (Advanced)

**Description:** A full-stack application with a FastAPI backend, React frontend, PostgreSQL database, user authentication, real-time polling, and Docker deployment.

| Component | Choice |
|-----------|--------|
| Language | Python (backend), JavaScript/TypeScript (frontend) |
| Data Processing | Pandas, SQLAlchemy |
| Visualization | Plotly, D3.js, Chart.js |
| Dashboard | React + Plotly dashboard |
| Data Input | REST API, CSV upload, real-time polling |
| Database | PostgreSQL |
| Deployment | Docker, AWS/Heroku |
| Difficulty | Advanced |

**Pros:**
- Production-ready, scalable
- Real-time polling and updates
- User authentication and roles
- Full CI/CD and containerization

**Cons:**
- High complexity for a student project
- Steep learning curve
- Requires DevOps knowledge
- Overkill for a placement proof project

---

## SELECTED BEST OPTION FOR STUDENTS: Option B (Intermediate)

**Reasoning:**
Option B is the best choice for students because it:
1. Is beginner-friendly but looks professional on GitHub
2. Uses industry-relevant tools (Pandas, NumPy, Matplotlib, Seaborn, Streamlit)
3. Includes an optional interactive dashboard (Streamlit) which impresses recruiters
4. Has a clean, modular folder structure that's easy to navigate
5. Can be completed in 5 days without DevOps or frontend knowledge
6. Works entirely with public datasets or synthetic CSV data (no enterprise access needed)

**Final Tech Stack (Option B):**
- **Language:** Python 3.10+
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Dashboard:** Streamlit (optional)
- **Data Input:** CSV / Excel / Google Forms export
- **Output:** Static charts (PNG/HTML) + interactive Streamlit dashboard
