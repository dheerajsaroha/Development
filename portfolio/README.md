# Dheeraj Saroha - Portfolio Website

A personal portfolio website built with Django showcasing my journey as a Software Engineer transitioning into AI/ML Engineering. The site features sections for about, education, experience, projects, and contact information.

## 🚀 Features

- **Responsive Design**: Modern, mobile-friendly interface with smooth animations
- **Multi-page Navigation**: Clean routing for Home, About, Education, Experience, Projects, and Contact pages
- **Professional Showcase**: Highlights technical skills, work experience, and AI/ML projects
- **Resume Download**: Direct download link for PDF resume
- **Social Integration**: Links to GitHub and email contact
- **Custom Styling**: Advanced CSS with custom fonts and FontAwesome icons

## 🛠️ Tech Stack

- **Backend**: [Django 6.1.2](https://www.djangoproject.com/)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS variables, FontAwesome 6.4.0
- **Fonts**: Inter & Fira Code (Google Fonts)
- **Database**: SQLite (development)

## 📁 Project Structure

```
portfolio/
├── dheerajportfolio/          # Main app
│   ├── templates/            # App-specific templates
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── education.html
│   │   ├── experience.html
│   │   ├── home.html
│   │   └── projects.html
│   ├── urls.py              # App URL routing
│   └── views.py             # View functions
├── portfolio/                # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL routing
│   └── wsgi.py              # WSGI config
├── static/                   # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── docs/
│   │   └── Dheeraj_Resume.pdf
│   └── images/
│       └── Dheeraj_Profile.jpeg
├── templates/               # Project-level templates
│   └── base.html           # Base template with nav/footer
├── db.sqlite3              # SQLite database
└── manage.py               # Django management script
```

## 🏃‍♂️ Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser**
   Navigate to `http://127.0.0.1:8000/` to view the site.

## 📄 Pages

| Page | Route | Description |
|---|---|---|
| Home | `/` | Hero section with introduction and CTA buttons |
| About & Pivot | `/about/` | Career transition story and skills |
| Education | `/education/` | Academic background |
| Experience | `/experience/` | Professional work history |
| Projects | `/projects/` | Showcase of software and AI/ML projects |
| Contact | `/contact/` | Contact information and links |

## 🎨 Customization

- **Styling**: Modify `static/css/style.css` for design changes
- **Content**: Edit templates in `dheerajportfolio/templates/` or `templates/`
- **Profile**: Update `static/images/Dheeraj_Profile.jpeg`
- **Resume**: Replace `static/docs/Dheeraj_Resume.pdf`
- **Social Links**: Update contact links in `templates/base.html`

## 📧 Contact

- **Email**: [dheerajsaroha2892002@gmail.com](mailto:dheerajsaroha2892002@gmail.com)
- **GitHub**: [github.com/dheerajsaroha](https://github.com/dheerajsaroha)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with Django & Advanced CSS* | © 2026 Dheeraj Saroha
