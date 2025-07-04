# 🚀 Galactic URL Shortener API

## 🎯 **Main Learning Focus: HTTP Redirects & Unique ID Generation**
Master HTTP redirect responses, URL validation, and algorithms for generating unique, collision-free identifiers in distributed systems.

## 🌌 The Scenario
The year is 2157, and humanity has colonized multiple star systems. As a Communications Engineer aboard the Interstellar Command Ship *Odyssey*, you need to create a **simple URL Shortener API** because space communication has limited bandwidth and long URLs waste precious transmission capacity!

## 📋 Mission Details
Build a basic REST API that takes long URLs and converts them into short codes, then redirects users when they visit the short code. Perfect for sharing star charts and mission data efficiently!

### Core Features Required:
- **URL Shortening**: Convert long URLs into short codes (e.g., abc123)
- **URL Redirection**: Redirect short codes back to original URLs  
- **Basic Analytics**: Track how many times each link was clicked
- **URL Management**: List all shortened URLs

### API Endpoints Needed:
```
POST /shorten
Body: { "url": "https://galaxy-maps.space/sector-7/planet-details?id=12345" }
Response: { "shortCode": "abc123", "originalUrl": "https://...", "id": 1 }

GET /{shortCode}
Response: Redirect (302) to original URL + increment click count

GET /links
Response: [
  { "id": 1, "shortCode": "abc123", "originalUrl": "https://...", "clicks": 5, "createdAt": "2024-01-01T10:00:00Z" }
]

GET /stats/{shortCode}
Response: { "shortCode": "abc123", "originalUrl": "https://...", "clicks": 5, "createdAt": "2024-01-01T10:00:00Z" }

DELETE /links/{id}
Response: { "message": "Link deleted" }
```

### Technical Requirements:
- **Language**: Choose any (Node.js, Python, Java, etc.)
- **Database**: SQLite or simple file storage
- **Framework**: Express, Flask, Spring Boot, etc.
- **Short Code Generation**: Random strings (6-8 characters)
- **URL Validation**: Ensure valid URLs are provided
- **Click Tracking**: Increment counter on each redirect

### Short Code Requirements:
- Use alphanumeric characters (a-z, A-Z, 0-9)
- 6-8 characters long
- Ensure uniqueness (no duplicates)
- Easy to type and remember

## ⏱️ **Exact Development Time: 2 days**
- **Basic API Setup**: Half day
- **URL Shortening Logic**: 1 day
- **Redirection & Click Tracking**: Half day

## 🎯 Mission Success Criteria
- URLs are successfully shortened to 6-8 character codes
- Short codes redirect to original URLs correctly
- Click counts are tracked and updated
- Can list all shortened URLs with statistics
- Proper URL validation (reject invalid URLs)
- No duplicate short codes are generated
- Returns appropriate HTTP status codes

## 📚 Learning Objectives
- URL handling and validation
- HTTP redirects (302 status codes)
- Unique ID/code generation
- Basic analytics and counters
- Database relationships
- API design patterns

*Efficient communication across the galaxy depends on your shortener!* 🛸✨ 