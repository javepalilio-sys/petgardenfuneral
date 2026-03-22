# Pet Memory Garden - API & Endpoint Reference

## Overview

The Pet Memory Garden API provides endpoints for:
- User authentication (login, signup, logout)
- Memory post management (create, view)
- Candle interactions
- Admin functions

All endpoints except landing page require the user to be authenticated.

---

## 🔓 Public Endpoints (No Authentication Required)

### 1. Landing Page
**Endpoint:** `GET /`  
**Template:** `landing.html`  
**Purpose:** Welcome page with garden theme  
**Redirects:** If user is authenticated, redirects to `/upload/`

**Response:**
- Displays welcome message
- Shows "Continue to Garden" button
- Animated flowers and petals
- Mobile responsive

---

### 2. User Registration (Sign Up)
**Endpoint:** `GET /signup/`  
**Method:** GET for form display, POST for submission  
**Template:** `signup.html`  
**Redirects (on success):** To `/upload/` after login

**Form Fields:**
- `username` (CharField, max_length=150, required)
- `password1` (CharField, required, min 8 chars recommended)
- `password2` (CharField, confirm password, required)

**Validation:**
- Username must be unique
- Passwords must match
- Password validation rules applied (Django defaults)

**Response (GET):**
- HTML form for registration

**Response (POST - Success):**
- User created and logged in
- Redirect to upload page

**Response (POST - Error):**
- Form with error messages displayed to user

---

### 3. User Login
**Endpoint:** `GET /login/`  
**Method:** GET for form display, POST for submission  
**Template:** `login.html`  
**Redirects (on success):** To `/upload/` after login

**Form Fields:**
- `username` (CharField, max_length=150, required)
- `password` (CharField, required)

**Validation:**
- Username exists
- Password is correct

**Response (GET):**
- HTML login form

**Response (POST - Success):**
- User authenticated and logged in
- Session cookie created
- Redirect to upload page

**Response (POST - Error):**
- Form error: "Invalid username or password"

---

## 🔒 Protected Endpoints (Authentication Required)

### 4. Upload Memory Post
**Endpoint:** `GET /upload/`  
**Method:** GET for form display, POST for submission  
**Authorization:** Login required  
**Template:** `upload.html`  
**Redirects (on success):** To `/wall/` after post creation

**Form Fields:**
- `image` (ImageField, required, accepts: JPEG, PNG, GIF, WebP)
- `title` (CharField, max_length=200, optional)
- `caption` (TextField, required)

**Validation:**
- Image is valid and readable
- Caption must not be empty
- File size reasonable (Pillow handles)

**Response (GET):**
- HTML form with live preview area
- Previous posts (if any) not shown

**Response (POST - Success):**
- Post saved to database
- Clear confirmation redirect to wall
- Post linked to authenticated user

**Response (POST - Error):**
- Form with validation error messages
- User can correct and resubmit

**Database Record Created:**
```python
Post(
    user=authenticated_user,
    title=request.POST.get('title', ''),
    caption=request.POST.get('caption'),
    image=request.FILES['image'],
    candle_count=0,
    created_at=auto_now_add
)
```

---

### 5. View Memory Wall
**Endpoint:** `GET /wall/`  
**Authorization:** Login required  
**Template:** `wall.html`  
**HTTP Method:** GET  
**Query Parameters:** None

**Response (Success):**
- HTML page displaying all posts
- Posts ordered by creation date (newest first)
- Post cards show:
  - Pet photo
  - Pet name (or "Beloved Pet")
  - Creator username
  - Creation date
  - Memory excerpt
  - Candle count
  - Candle button

**Response (No Posts):**
- Empty state message shown
- Link to create first memory
- Eventually will show user posts from all users

**Database Query:**
```python
posts = Post.objects.all().order_by('-created_at')
```

---

### 6. User Logout
**Endpoint:** `GET /logout/`  
**Authorization:** Login required  
**HTTP Method:** GET (typically, sometimes POST)  
**Redirects:** To landing page (`/`)

**Response:**
- Session cookie cleared
- User logged out
- Redirect to landing page

**Side Effects:**
- User session destroyed
- CSRF token invalidated
- Protected pages redirect to login

---

## 📡 AJAX Endpoints

### 7. Add Candle (Like System)
**Endpoint:** `POST /candle/<post_id>/`  
**Authorization:** Login required  
**HTTP Method:** POST  
**Content-Type:** application/json

**URL Parameters:**
- `post_id` (Integer, required) - ID of the post to add candle to

**Request Headers Required:**
```
X-CSRFToken: [csrf_token_value]
Content-Type: application/json
```

**Request Body:**
```json
{}
```

**Response (Success - HTTP 200):**
```json
{
    "success": true,
    "candle_count": 5
}
```

**Response (Not Found - HTTP 404):**
- Post not found
- Standard Django 404 response

**Response (Unauthorized - HTTP 403):**
- User not authenticated (redirects to login)

**Response (Bad Method - HTTP 405):**
- Only POST method allowed

**Side Effects:**
- Post.candle_count incremented by 1
- Changes saved to database
- Returned value is new candle_count

**JavaScript Handler:**
```javascript
function addCandle(postId, button) {
    fetch(`/candle/${postId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            button.querySelector('.candle-count').textContent = data.candle_count;
            button.classList.add('glow');
            setTimeout(() => button.classList.remove('glow'), 600);
        }
    });
}
```

---

## 🔐 Authentication Flow

### Login Flow
```
User at landing page
    ↓
Click "Continue to Garden"
    ↓
Redirected to /login/
    ↓
Submit credentials
    ↓
Validate username & password
    ↓
CREATE session (if valid)
    ↓
Redirect to /upload/
    ↓
User can now create posts
```

### Protected Page Access Flow
```
User not logged in
    ↓
Tries to access /upload/
    ↓
@login_required decorator triggers
    ↓
Redirects to /login/?next=/upload/
    ↓
User logs in
    ↓
Redirects to original page /upload/
```

---

## 📊 Data Models

### User Model
Django's built-in User model:
```python
{
    'id': int,
    'username': str,
    'email': str,
    'password': str (hashed),
    'first_name': str,
    'last_name': str,
    'is_active': bool,
    'is_staff': bool,
    'is_superuser': bool,
    'date_joined': datetime,
    'last_login': datetime,
}
```

### Post Model
```python
{
    'id': int,
    'user': int (ForeignKey),
    'title': str,
    'caption': str,
    'image': str (file path),
    'candle_count': int,
    'created_at': datetime,
}
```

---

## 🔄 Common Request/Response Patterns

### Form Submission Pattern
```
POST /upload/
Content-Type: multipart/form-data

image: [binary file]
title: "Max"
caption: "A wonderful companion..."
```

**Response (Success - 302 Redirect):**
```
Location: /wall/
```

**Response (Error - 200 OK):**
```html
[Form with error messages displayed]
```

---

### AJAX Request Pattern
```
POST /candle/5/
Headers:
  X-CSRFToken: [token]
  Content-Type: application/json
```

**Response:**
```json
{"success": true, "candle_count": 3}
```

---

## 🛡️ Security Considerations

### CSRF Protection
- All POST requests require CSRF token
- Token included in forms via `{% csrf_token %}`
- Token included in AJAX headers via `X-CSRFToken`

### Authentication
- Session-based (Django default)
- Password hashing (PBKDF2)
- Login required decorators

### Authorization
- Users can upload any memory
- Users can light candles for any post
- Users can only logout their own session

---

## ⚠️ Error Responses

### 404 Not Found
- Accessing non-existent post
- Accessing `/candle/999/` for non-existent post

### 403 Forbidden
- Attempting protected endpoint without login
- Actually redirects to login page

### 405 Method Not Allowed
- Using GET on `/candle/` endpoint
- Using POST on `/wall/` endpoint

### 400 Bad Request
- Invalid form data
- Missing required fields
- Invalid file format

---

## 🔗 URL Reference Table

| Path | Method | Auth | Purpose | Response |
|------|--------|------|---------|----------|
| `/` | GET | ❌ | Landing page | HTML |
| `/login/` | GET | ❌ | Login form | HTML |
| `/login/` | POST | ❌ | Process login | Redirect \| HTML |
| `/signup/` | GET | ❌ | Signup form | HTML |
| `/signup/` | POST | ❌ | Process signup | Redirect \| HTML |
| `/logout/` | GET | ✅ | Logout | Redirect |
| `/upload/` | GET | ✅ | Upload form | HTML |
| `/upload/` | POST | ✅ | Create post | Redirect \| HTML |
| `/wall/` | GET | ✅ | View posts | HTML |
| `/candle/<id>/` | POST | ✅ | Add candle | JSON |

---

## 📞 Status Codes

- **200 OK** - Request successful
- **302 Found** - Redirect (successful form submission)
- **400 Bad Request** - Invalid form data
- **403 Forbidden** - Authentication required
- **404 Not Found** - Resource not found
- **405 Method Not Allowed** - Wrong HTTP method

---

## 🧪 Testing Endpoints

### Test Signup
```bash
curl -X POST http://localhost:8000/signup/ \
  -d "username=testuser" \
  -d "password1=testpass123" \
  -d "password2=testpass123"
```

### Test Login
```bash
curl -X POST http://localhost:8000/login/ \
  -d "username=testuser" \
  -d "password=testpass123" \
  -c cookies.txt
```

### Test Upload (requires login)
```bash
curl -X POST http://localhost:8000/upload/ \
  -b cookies.txt \
  -F "image=@pet.jpg" \
  -F "title=My Pet" \
  -F "caption=Beloved companion"
```

### Test Candle AJAX
```bash
curl -X POST http://localhost:8000/candle/1/ \
  -b cookies.txt \
  -H "X-CSRFToken: [token]" \
  -H "Content-Type: application/json"
```

---

## 📚 Related Documentation

- Full documentation: [README.md](README.md)
- Quick start: [QUICKSTART.md](QUICKSTART.md)
- Installation: [INSTALL.txt](INSTALL.txt)
- Deployment: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

**Last Updated:** March 21, 2026  
**Version:** 1.0
