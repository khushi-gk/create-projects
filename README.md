# create-projects
# 🏨 Hospitality Management System

A web-based Hospitality Management System built with **Django** and **Python** to manage hotel rooms, bookings, and guest records efficiently.

## 📌 Project Overview

The Hospitality Management System provides a simple and user-friendly platform for managing day-to-day hotel operations.

It allows users to:

- Manage hotel rooms
- Check room availability
- Add, edit, and delete rooms
- Create and manage bookings
- Search guest records
- Manage guest information
- Access Django Admin for database management

## ✨ Features

### 🏨 Room Management
- Add new rooms
- Edit room details
- Delete rooms
- View room type and price
- Check room availability
- Prevent duplicate room numbers

### 📅 Booking Management
- Create new bookings
- Select rooms for guests
- Set check-in and check-out dates
- Edit bookings
- Delete bookings
- Validate booking dates

### 👥 Guest Management
- View guest records
- Search guests by name
- View guest booking details

### 📊 Dashboard
The dashboard provides a quick overview of:

- Total rooms
- Available rooms
- Total bookings
- Total guests
- Quick action buttons

### 🔐 Django Admin
The system includes Django's built-in administration panel for managing:

- Rooms
- Bookings
- Users
- Groups

## 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub Codespaces

## 📂 Project Structure

```text
create-projects/
│
├── hospitality/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── rooms/
│   ├── migrations/
│   ├── templates/
│   │   └── rooms/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── README.md
└── .gitignore