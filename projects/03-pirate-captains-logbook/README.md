# 🏴‍☠️ Pirate Captain's Logbook API

## 🎯 **Main Learning Focus: Authentication & Security Implementation**
Learn to implement secure user authentication with JWT tokens, password hashing, role-based access control, and API security best practices.

## ⚓ The Legend
Ahoy! The year is 1723, and as the Captain of the mighty ship *Black Pearl*, you need a digital system to keep track of your adventures, crew, and treasure hunts. Create a **simple Blog API** where you can document your pirate adventures and manage different types of posts!

## 📜 The Quest
Build a basic REST API for a pirate-themed blog where you can create, read, update, and delete blog posts. Include simple user authentication so only authorized pirates can create posts, but anyone can read the adventures!

### Core Features Required:

#### 🗝️ Simple Authentication:
- **User Registration**: Pirates can sign up with username/password
- **User Login**: Get a token to authenticate requests
- **Protected Routes**: Only authenticated users can create/edit posts
- **Public Reading**: Anyone can read published adventures

#### 📖 Blog Post Management:
- **Create Posts**: Write about treasure hunts and adventures
- **Read Posts**: List all posts or get individual posts
- **Update Posts**: Edit existing adventures  
- **Delete Posts**: Remove old or incorrect entries
- **Post Categories**: Different types of posts (Adventure, Treasure, Battle, Port Review)

### API Endpoints Needed:
```
Authentication:
POST /auth/register
Body: { "username": "blackbeard", "password": "treasure123" }
Response: { "message": "User created", "userId": 1 }

POST /auth/login  
Body: { "username": "blackbeard", "password": "treasure123" }
Response: { "token": "jwt-token-here", "userId": 1 }

Blog Posts:
GET /posts
Response: [{ "id": 1, "title": "Found Treasure Island", "content": "...", "category": "Treasure", "author": "blackbeard", "createdAt": "..." }]

GET /posts/{id}
Response: { "id": 1, "title": "Found Treasure Island", "content": "...", "category": "Treasure", "author": "blackbeard", "createdAt": "..." }

POST /posts (requires authentication)
Headers: { "Authorization": "Bearer jwt-token" }
Body: { "title": "New Adventure", "content": "Today we sailed...", "category": "Adventure" }
Response: { "id": 2, "title": "New Adventure", ... }

PUT /posts/{id} (requires authentication + ownership)
DELETE /posts/{id} (requires authentication + ownership)

GET /posts/category/{category}
Response: [all posts in that category]
```

### Technical Requirements:
- **Language**: Choose any (Node.js, Python, Java, etc.)
- **Database**: SQLite or simple file storage
- **Authentication**: JWT tokens for session management
- **Framework**: Express, Flask, Spring Boot, etc.
- **Password Security**: Hash passwords (bcrypt recommended)
- **Authorization**: Users can only edit/delete their own posts

### Database Schema:
```
Users:
- id, username, password (hashed), createdAt

Posts:
- id, title, content, category, authorId, createdAt, updatedAt

Categories:
- Adventure, Treasure, Battle, Port Review
```

## ⏱️ **Exact Development Time: 3 days**
- **Basic API Setup**: Half day
- **User Authentication System**: 1 day
- **Blog Post CRUD Operations**: 1 day
- **Testing & Error Handling**: Half day

## 🎯 Victory Conditions
- Users can register and login successfully
- JWT tokens are generated and validated
- Authenticated users can create, edit, delete their posts
- Anyone can read all published posts
- Posts can be filtered by category
- Passwords are properly hashed and secured
- Proper error handling for invalid requests
- Only post authors can edit/delete their own posts

## 📚 Learning Objectives
- User authentication and authorization
- JWT token generation and validation
- Password hashing and security
- CRUD operations with relationships
- Database schema design
- Protected routes and middleware
- Error handling and validation

*Document your legendary adventures for future generations of pirates!* ⚔️🦜 