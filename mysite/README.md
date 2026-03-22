# Pet Memory Garden - Django Web Application

A peaceful and respectful online garden where users can share photos and heartfelt writings for pets they have lost.

## 🌸 Features

### User Authentication
- Sign up with username and password
- Secure login/logout functionality
- Password validation required
- Session-based authentication using Django's built-in system

### Post Management
- Upload pet photos (ImageField)
- Add pet name (optional)
- Write memories, poems, or stories (required caption)
- View all posts in chronological order
- Only authenticated users can upload

### Candle Lighting System
- Click candle icon 🕯️ to honor pet memories
- Real-time candle count updates via AJAX
- No page reload required
- Glowing animation on click

### Responsive Design
- Mobile-first responsive design
- Beautiful garden theme with soft colors
- Smooth animations and transitions
- Works on desktop, tablet, and mobile devices

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project directory:**
   ```bash
   cd mysite
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install Django Pillow
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```
   When prompted:
   - Username: admin (or your choice)
   - Email: admin@petgarden.com (or your choice)
   - Password: (create a secure password)

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Open your browser and go to http://localhost:8000
   - The landing page will appear with the "Continue to Garden" button

## 📚 Usage

### For Regular Users

1. **Landing Page**
   - Welcome to the Pet Memory Garden
   - Click "Continue to Garden" button

2. **Authentication**
   - First-time users: Click "Create Account" to sign up
   - Returning users: Click "Sign In" to log in
   - Username and password are required

3. **Upload Memory**
   - Navigate to the upload page after login
   - Select a pet photo
   - Enter pet's name (optional)
   - Write your memory, poem, or story (required)
   - Click "Save Memory & See the Wall" to publish

4. **View Memory Wall**
   - See all shared pet memories in a responsive grid
   - Each card shows: pet photo, name, caption, username, and date
   - Click the candle icon 🕯️ to light a candle for any pet
   - Candle count updates in real-time with animation

### For Administrators

1. **Access Admin Panel:**
   - Go to http://localhost:8000/admin
   - Log in with your superuser credentials

2. **Manage Posts:**
   - View all user submissions
   - Filter posts by user or creation date
   - Search by title, caption, or username
   - Edit or delete posts if needed

## 📂 Project Structure

```
mysite/
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── media/                  # User-uploaded images directory
│   └── pets/              # Pet photos storage
│
├── mysite/                 # Main project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing configuration
│   ├── asgi.py             # ASGI configuration
│   └── wsgi.py             # WSGI configuration
│
└── homepage/               # Main application
    ├── models.py           # Database models
    ├── views.py            # View functions
    ├── urls.py             # App URL patterns
    ├── forms.py            # Django forms
    ├── admin.py            # Admin configuration
    │
    ├── static/             # Static files
    │   ├── css/
    │   │   └── styles.css   # Main stylesheet
    │   └── js/
    │       ├── script.js    # Main JavaScript
    │       └── upload-preview.js  # Upload preview handler
    │
    └── templates/          # HTML templates
        └── homepage/
            ├── base.html       # Base template
            ├── landing.html    # Landing page
            ├── login.html      # Login page
            ├── signup.html     # Sign up page
            ├── upload.html     # Upload page with preview
            └── wall.html       # Memory wall page
```

## 🎨 Design Theme

### Color Palette
- **Primary Green**: #a8d5ba (soft, calming)
- **Sage Green**: #8fbf8f (nature-inspired)
- **Dark Green**: #5a8a5a (accents)
- **Light Green**: #d4e8d4 (backgrounds)
- **Beige**: #f5f1e8 (soft backgrounds)
- **Sky Blue**: #d4e4f7 (light accents)
- **Warm Yellow**: #ffd700 (candle highlights)

### Typography
- Clean, readable fonts
- Good contrast for accessibility
- Responsive text sizing

### Animations
- Floating petals on landing page
- Smooth page transitions
- Candle glow effect on click
- Hover effects on cards

## 🔧 Database Model

### Post Model
```python
- id: AutoField (Primary Key)
- user: ForeignKey (User)
- title: CharField (max_length=200, optional)
- caption: TextField (required)
- image: ImageField (upload_to='pets/')
- candle_count: IntegerField (default=0)
- created_at: DateTimeField (auto_now_add=True)
```

## 🌐 API Endpoints

### Page Views
- `/` - Landing page
- `/login/` - Login page
- `/signup/` - Sign up page
- `/upload/` - Upload/share memory (login required)
- `/wall/` - View all memories (login required)
- `/logout/` - Log out (login required)

### AJAX Endpoints
- `POST /candle/<post_id>/` - Increment candle count for a post

## 📝 Technical Details

### Backend
- **Framework**: Django 6.0.3
- **Database**: SQLite
- **Authentication**: Django's built-in User model
- **Image Handling**: Pillow library

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Responsive design with flexbox/grid
- **JavaScript**: Vanilla (no frameworks)
- **File I/O**: HTML5 FileReader for image preview

### Security Features
- CSRF protection (Django middleware)
- Password hashing (Django authentication)
- SQL injection prevention (ORM)
- XSS protection (Django template escaping)

## 🚀 Optional Enhancements

### Implemented
- Live preview in upload form
- Floating petals animation on landing page
- Responsive grid layout for memory wall
- Smooth transitions and animations

### Can Be Added
- Anonymous posting option
- Background music toggle
- Email notifications
- Search functionality
- Post tagging system
- Comment/condolence system
- Photo gallery view
- Social sharing buttons
- Print memories feature

## 📱 Browser Compatibility

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🐛 Troubleshooting

### Issue: Images not uploading
**Solution**: Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in settings.py and the media directory exists.

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` in production. In development, Django serves static files automatically.

### Issue: Database errors
**Solution**: Delete `db.sqlite3` and run migrations again:
```bash
python manage.py migrate --run-syncdb
```

### Issue: Port 8000 already in use
**Solution**: Use a different port:
```bash
python manage.py runserver 8080
```

## 📧 Support

For issues or questions:
1. Check the Django documentation: https://docs.djangoproject.com
2. Review the code comments in the view functions
3. Check browser console for JavaScript errors

## 📄 License

This project is created for educational and memorial purposes.

## 🙏 Acknowledgments

This application was built to provide a peaceful space for pet lovers to share and honor the memories of their beloved companions.

---

**Enjoy your Pet Memory Garden! 🕯️🌸**
