# Travel India Tourism – Django Website

A full-featured Travel & Tourism website inspired by [travelindiatourism.com](https://travelindiatourism.com/), built with **Python (Django)** and **SQLite**. Users can browse curated tour packages, book flights, reserve hotels, and interact with a built-in chatbot for instant recommendations. Admins manage everything from the Django admin dashboard.

![Hero](https://images.unsplash.com/photo-1506059612708-99d6c258160e?auto=format&fit=crop&w=1400&q=80)

---

## ✨ Features

### Customer (User) Module
- **Register / Login / Profile** – Secure account creation with contact details.
- **Browse Tour Packages** – Filter by destination, featured packages, detailed itineraries.
- **Flights** – Search by origin/destination/airline, view fare, book seats.
- **Hotels** – Search by city, view star-rating, amenities, and reserve rooms.
- **Book & Cancel** – Instant confirmation, release of inventory on cancellation.
- **Booking History** – View all past & upcoming bookings with status.
- **Chatbot Assistant** – Keyword-based bot for queries like *"show flights"*, *"list hotels"*, *"view tourism packages"*, *"my bookings"*. Floating widget on every page + a full chat page.

### Admin Module
- **Django Admin Dashboard** – Single sign-on admin with:
  - Add / edit / delete **Flights** (airline, route, schedule, class, price, seats)
  - Add / edit / delete **Hotels** (city, star rating, amenities, price, rooms)
  - Add / edit / delete **Tour Packages** (destination, duration, itinerary, featured flag)
  - View **All Bookings** (type, traveler, status, total amount, dates)
  - View **Registered Users** and their profiles
- Filtering, searching, and date hierarchy on all admin lists.

---

## 🧱 Tech Stack

| Layer        | Technology                          |
| ------------ | ----------------------------------- |
| Framework    | Django 5.x                          |
| Database     | SQLite3                             |
| Templating   | Django Templates                    |
| Frontend     | Vanilla HTML/CSS/JS, Font Awesome, Google Fonts |
| Auth         | Django built-in auth                |
| Media        | Pillow (optional image uploads)     |

---

## 📦 Project Structure

```
travel-tourism-website/
├── manage.py
├── requirements.txt
├── db.sqlite3                  # created after migrate
├── travel_tourism/             # settings + root URLs
├── core/                       # home, about, contact, seed command
├── accounts/                   # User profile, register, login
├── flights/                    # Flight model, views, admin
├── hotels/                     # Hotel model, views, admin
├── packages/                   # Destination + Package, views, admin
├── bookings/                   # Booking model + booking flow
├── chatbot/                    # Simple keyword chatbot API
├── templates/                  # HTML templates
└── static/css,js/              # Site styles & chatbot script
```

---

## 🚀 Quick Start

**Requirements**: Python 3.10+ (tested on 3.12)

```bash
# 1. Clone
git clone https://github.com/Siva4121/travel-tourism-website.git
cd travel-tourism-website

# 2. Create virtualenv
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate

# 3. Install deps
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Seed sample data (destinations, packages, hotels, flights + admin/demo users)
python manage.py seed_data

# 6. Run the server
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Default Accounts

Created by `seed_data`:

| Role     | Username | Password     |
| -------- | -------- | ------------ |
| Admin    | admin    | admin12345   |
| Customer | demo     | demo12345    |

Change these in production!

---

## 🤖 Chatbot

The chatbot is a **keyword-matching engine** (simple, deterministic, no external APIs). It reads from the live database and returns real results.

Try these:

- `hi` / `hello`
- `show me all flights`
- `list hotels`
- `view tourism packages` / `holiday ideas`
- `my bookings`
- `help` / `what can you do`

Access it via:
1. The floating **Ask AI** button (bottom right on every page), **or**
2. The full chat page at `/chatbot/`.

The backend endpoint is `POST /chatbot/api/` with JSON `{ "message": "..." }`.

---

## 🛠 Admin Panel

Log in at `/admin/` with the `admin` user. You can manage:

- **Flights** – `/admin/flights/flight/`
- **Hotels** – `/admin/hotels/hotel/`
- **Destinations & Packages** – `/admin/packages/`
- **Bookings** – `/admin/bookings/booking/`
- **Users** & **User Profiles** – `/admin/auth/user/`, `/admin/accounts/userprofile/`

---

## 📑 About This Project

> Planning a travel itinerary, booking hotel rooms, and reserving flights often become a major hassle. This Travel and Tourism Website, developed using **Python (Django framework)**, offers a comprehensive solution to help users plan their itineraries efficiently. The system comprises two entities: **User** and **Admin**.
>
> Users can browse available travel packages, and the system also includes a **chatbot** to enhance user-friendliness by assisting with itinerary planning. The Django framework ensures a robust, scalable web application.

### Advantages
- Real-time information for travelers
- Centralised data handling
- Reduced time consumption
- Computerised record keeping
- Cost reduction and operational efficiency

### System Development Life Cycle
The project follows the **Waterfall Model**: Requirements → Design → Implementation → Testing → Deployment → Maintenance.

### System Requirements
- **Hardware**: Intel i3+ / 4 GB RAM / 100 GB storage / Windows 7+
- **Software**: Python 3.x, Django, SQLite3, a code editor (VS Code/Sublime), a modern web browser

### Limitations
- Requires an active internet connection.
- Chatbot responses are limited to the keywords it understands.

---

## 📚 References

- https://ieeexplore.ieee.org/document/6121641
- https://ieeexplore.ieee.org/document/9230090
- https://github.com/topics/tourism-website
- https://ijcsmc.com/docs/papers/October2019/V8I10201903.pdf
- https://travelindiatourism.com/

---

## 📝 License

This project is for educational/demo use. Feel free to fork and adapt.
