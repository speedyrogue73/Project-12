# Project 12

A Django web application built with Python and Bootstrap 5.

## Project Structure

```text
R_project_12/
│
├── R/
│   ├── home/               # Application for main views and logic
│   ├── RR/                 # Core project configuration (settings, urls, wsgi)
│   ├── static/             # Static assets (Bootstrap CSS, JS)
│   ├── templates/          # Base and shared HTML templates
│   ├── manage.py           # Django management script
│   └── requirements.txt    # Project dependencies
│
├── requirements.txt        # Root environment requirements
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/speedyrogue73/Project-12.git
cd Project-12
```

### 2. Create and activate a virtual environment
```bash
# On Windows
python -m venv env
.\env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r R/requirements.txt
```

### 4. Run migrations
```bash
python R/manage.py migrate
```

### 5. Start the development server
```bash
python R/manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
