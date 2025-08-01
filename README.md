# Student Marks  Tracker

A web-based application to manage students, courses, departments and  grades. Built using Django (CBV-based) and deployed on Render.
---
## 🌐 Live Demo
🔗 [live demo](https://marksub.onrender.com/)

##  Features

- Add and manage departments
- Assign courses to departments
- Register students under departments
- Record student marks per course
- Prevent invalid course-department combinations (validated)
- User-friendly admin panel for superusers

---

## 🛠 Tech Stack

- **Backend:** Django 5.x
- **Database:** SQLite (default, can be changed)
- **Frontend:** HTML, CSS (basic styling)
- **Deployment:** Render
- **Python version:** 3.11+

---
📸 Screenshots

<img width="1829" height="778" alt="image" src="https://github.com/user-attachments/assets/ca18ca4e-a0ee-43c7-8a8c-16c0b2361d56" />
---

## ⚙️ Setup Instructions

### 🔧 Local Development

 **Clone the repository**


### Prerequisites

- Python 3.10+
- pip

### Clone and run locally

```bash
git clone https://github.com/Jona555/markSub.git
cd tracker
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
