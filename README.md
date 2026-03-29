# CommunityFix (HCI-Assignment)

A community fault reporting system built with Django, designed to help residents report and track service delivery issues such as water leaks, potholes, electricity faults, and waste collection problems.

Built as part of the NHCI63110 Human-Computer Interaction assignment at Sol Plaatje University.

## Features

- Report a fault without creating an account
- Upload a photo as evidence
- Receive a unique reference number upon submission
- Track your report status using your reference number
- Edit or cancel a pending report
- Receive status updates as your report progresses
- Dispute a resolution if the fault has not been fixed
- Admin dashboard for municipal workers to manage and update reports

## Tech Stack

- Python 3.13
- Django 6.0
- SQLite
- Plain CSS
- Vanilla JavaScript



## Setup

### Clone the repository and navigate into the project directory.
```bash
git clone https://github.com/Di-exGeneral/HCI-Assignment.git
cd HCI-Assignment
```

### Create and activate a virtual environment.
```bash
python -m venv env
```

### Activate 

Windows
```cmd
env\Scripts\activate
```

Kali
```bash
source env/bin/activate
```



### Install dependencies.
```bash
pip install django pillow
```

### Run migrations.
```bash
python manage.py migrate
```

### Create a superuser for the admin dashboard.
```bash
python manage.py createsuperuser
```

### Start the development server.
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Admin Dashboard

The admin dashboard is available at `/reports/admin-dashboard/`. Log in using your superuser credentials via the Django admin panel at `/admin/`.

## Project Structure
```
HCI-Assignment/
├── hydrowatch/        # Project settings and URLs
├── reports/           # Fault reporting app
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── tracking/          # Report tracking app
│   ├── templates/
│   ├── views.py
│   └── urls.py
├── env/               # Virtual environment
└── manage.py
```

## Author

Tlotliso Ledwaba
