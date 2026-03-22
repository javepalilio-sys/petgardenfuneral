# Quick Start Guide - Pet Memory Garden

## ⚡ Get Started in 5 Minutes

### 1️⃣ Install Dependencies
```bash
cd mysite
pip install Django Pillow
```

### 2️⃣ Setup Database
```bash
python manage.py migrate
```

### 3️⃣ Create Admin Account
```bash
python manage.py createsuperuser
```
- Username: `admin`
- Password: (your choice)

### 4️⃣ Run Server
```bash
python manage.py runserver
```

### 5️⃣ Access Application
- 🌍 Open: http://localhost:8000
- 🔐 Admin: http://localhost:8000/admin

---

## 🎯 What You Get

✅ **Landing Page** - Beautiful welcome screen with garden theme  
✅ **User Authentication** - Sign up and login system  
✅ **Photo Upload** - Upload pet photos  
✅ **Memory Sharing** - Write poems, letters, or stories  
✅ **Memory Wall** - View all shared memories  
✅ **Candle System** - Light virtual candles for pets  
✅ **Responsive Design** - Works on all devices  
✅ **Admin Panel** - Manage all posts  

---

## 👤 Test User Accounts

Once the server is running, you can:
1. Go to http://localhost:8000
2. Click "Continue to Garden"
3. Click "Create Account" and make a new user
4. Or login with admin credentials

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `models.py` | Database models (Post) |
| `views.py` | Page logic and AJAX handlers |
| `urls.py` | URL routing |
| `forms.py` | Form definitions |
| `templates/` | HTML files |
| `static/css/` | Styling |
| `static/js/` | JavaScript functionality |
| `admin.py` | Admin interface setup |

---

## 🎨 Key Features

### 🌸 Landing Page
- Soft garden visuals
- Welcoming message
- Animated flowers and petals

### 📸 Upload Page
- Live preview of memory card
- Image upload
- Pet name (optional)
- Memory text (required)

### 🧱 Memory Wall
- Responsive grid layout
- All user posts displayed
- Candle lighting system
- Real-time updates

### 🕯️ Candle System
- Click to honor a pet
- Animated glow effect
- Count persists in database
- No page reload needed

---

## 🔐 Admin Access

Login with your superuser credentials:
- Go to: http://localhost:8000/admin
- View all posts
- Manage users and content
- View statistics

---

## 📝 Creating Test Data

1. Sign up as a new user
2. Go to /upload/
3. Upload an image
4. Enter a pet name
5. Write a memory
6. Submit

Now your post will appear on /wall/ for all users to see!

---

## ⚙️ Configuration Notes

All important settings are in `mysite/settings.py`:

```python
# Database
DATABASES['default']['NAME'] = BASE_DIR / 'db.sqlite3'

# Media files (uploaded images)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Debug mode (set to False in production)
DEBUG = True
```

---

## 🐛 Common Issues

**Q: Port 8000 is already in use**  
A: Run with different port: `python manage.py runserver 8080`

**Q: Image won't upload**  
A: Make sure you installed Pillow: `pip install Pillow`

**Q: Pages look blank/unstyled**  
A: Static files serve automatically in development mode

---

## 📞 Need Help?

Refer to the full README.md for detailed documentation or check the code comments in each file!

**Ready to create meaningful memories? Start now! 🌸**
