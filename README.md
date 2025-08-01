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
<img width="1655" height="685" alt="image" src="https://github.com/user-attachments/assets/05a47e4f-0589-4c99-9f13-fca8244c5c83" />
<img width="1758" height="703" alt="image" src="https://github.com/user-attachments/assets/a72aaaf9-c5fe-4a9d-a9ba-083fdadfd820" />


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
