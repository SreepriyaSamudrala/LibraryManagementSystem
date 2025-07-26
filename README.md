📚 Library Management System using Django

This is a **Library Management System** developed using **Python 3.7.2** and **Django 2.1.7**. It allows you to manage books, users, and records in a library efficiently.


## 🔧 Requirements

- Python 3.7.2  
- Django 2.1.7

🚀 Setup Instructions

 1. Install Python 3.7.2

Download and install from:  
🔗 https://www.python.org/downloads/release/python-372/

Ensure you **add Python to system environment variables**.


2. Create Project Folder

Create a folder for your project, for example:  
`C:\Users\YourName\Documents\LibrarySystem`

Go inside the folder → click the **address bar** → type `cmd` → hit **Enter** to open Command Prompt there.


 3. Install Django 2.1.7

In the opened Command Prompt, type:

```bash
pip install django==2.1.7

4. Start Project and App
In the same CMD window:

bash
Copy
Edit
django-admin startproject LibraryManagement
cd LibraryManagement
django-admin startapp library
📁 Full Project Structure
plaintext
Copy
Edit
LibrarySystem/
├── LibraryManagement/
│   ├── __init__.py
│   ├── settings.py           ← Project-wide settings
│   ├── urls.py               ← Main URL routing for project
│   ├── wsgi.py
│   └── asgi.py
│
├── library/
│   ├── views.py              ← Handles request/response logic
│   ├── models.py             ← Defines database models
│   ├── urls.py               ← App-specific routing (you create this)
│   ├── admin.py              ← Registers models in Django admin
│   ├── apps.py
│   ├── templates/
│   │   └── library/
│   │       ├── index.html        ← Homepage
│   │       ├── aboutus.html      ← About page
│   │       ├── contactus.html    ← Contact page
│   │       ├── addbooks.html     ← Add books form
│   │       └── viewbooks.html    ← Book list view
│
├── manage.py                ← Django CLI tool
⚙️ Configuration in settings.py
Inside TEMPLATES, set the template directory:

python
Copy
Edit
'DIRS': [os.path.join(BASE_DIR, 'library/templates')],
Also, add 'library', inside the INSTALLED_APPS list.

🌐 URL Routing
LibraryManagement/urls.py
python
Copy
Edit
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
]
library/urls.py
📌 Create this file manually inside the library/ app folder.

python
Copy
Edit
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contactus'),
    path('add-book/', views.add_book, name='add_book'),
    path('view-books/', views.view_books, name='view_books'),
]
🧠 Views in library/views.py
python
Copy
Edit
from django.shortcuts import render

def index(request):
    return render(request, 'library/index.html')

def aboutus(request):
    return render(request, 'library/aboutus.html')

def contactus(request):
    return render(request, 'library/contactus.html')

def add_book(request):
    return render(request, 'library/addbooks.html')

def view_books(request):
    return render(request, 'library/viewbooks.html')
🎨 Templates (HTML)
index.html
html
Copy
Edit
<h1>Welcome to Library Management System</h1>
<nav>
  <a href="/">Home</a> |
  <a href="/about/">About</a> |
  <a href="/contact/">Contact</a> |
  <a href="/add-book/">Add Book</a> |
  <a href="/view-books/">View Books</a>
</nav>
aboutus.html
html
Copy
Edit
<h2>About Us</h2>
<p>This Library Management System was created to manage books and records efficiently.</p>
contactus.html
html
Copy
Edit
<h2>Contact Us</h2>
<p>Email: library@example.com | Phone: +91-9876543210</p>
addbooks.html
html
Copy
Edit
<h2>Add a New Book</h2>
<form method="post">
  {% csrf_token %}
  <label>Book Title:</label><input type="text" name="title"><br>
  <label>Author:</label><input type="text" name="author"><br>
  <input type="submit" value="Add Book">
</form>
viewbooks.html
html
Copy
Edit
<h2>Available Books</h2>
<ul>
  {% for book in books %}
    <li>{{ book.title }} by {{ book.author }}</li>
  {% empty %}
    <li>No books found.</li>
  {% endfor %}
</ul>
🛠 Django Admin Commands
bash
Copy
Edit
# Start development server
python manage.py runserver

# Create database migrations
python manage.py makemigrations
python manage.py migrate

# Create admin account
python manage.py createsuperuser



![alt img]("https://github.com/SreepriyaSamudrala/LibraryManagementSystem/blob/main/Screenshot%202025-07-26%20165839.png?raw=true")
