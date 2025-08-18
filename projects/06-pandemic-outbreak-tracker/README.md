# 📱 Contact Tracing API System

## 🎯 **Main Learning Focus: Date/Time Logic & Temporal Data Processing**
Master working with timestamps, duration calculations, time overlap detection, and building algorithms that process time-based data relationships.

## 🏥 The Health Challenge
You've been recruited by the **Public Health Department** to build a digital contact tracing system. With a new health concern spreading through the community, they need a simple but effective API to track interactions between people and help identify potential exposure chains.

## 🔬 Mission Requirements
Create a REST API that manages people, locations, and their interactions to help health officials track potential exposure paths. The system should be able to identify who might have been exposed based on time and location data.

### Core Features Required:

#### 👥 Person Management:
- **Person Registration**: Track individuals in the system
- **Health Status**: Healthy, Exposed, Sick, Recovered
- **Contact Information**: Phone, email for notifications
- **Location History**: Track where people have been

#### 📍 Location & Event Tracking:
- **Location Registration**: Businesses, schools, events, etc.
- **Check-ins**: Record when people visit locations
- **Time Tracking**: Duration of visits and interactions
- **Event Management**: Special events with multiple attendees

#### 🔍 Contact Tracing Logic:
- **Exposure Detection**: Find people who were at same place/time
- **Contact Chains**: Trace connections between people
- **Risk Assessment**: Calculate exposure risk based on duration/proximity
- **Alert Generation**: Identify people who need to be notified

### API Endpoints Needed:
```
People:
POST /people
Body: { "name": "John Doe", "phone": "555-0123", "email": "john@email.com", "status": "Healthy" }
GET /people
PUT /people/{id}/status
Body: { "status": "Sick" }

Locations:
POST /locations
Body: { "name": "Coffee Shop Downtown", "address": "123 Main St", "type": "Restaurant" }
GET /locations

Check-ins:
POST /checkins
Body: { "personId": 1, "locationId": 2, "checkInTime": "2024-01-15T09:00:00Z", "checkOutTime": "2024-01-15T10:30:00Z" }
GET /checkins/person/{personId}
GET /checkins/location/{locationId}

Contact Tracing:
GET /contacts/{personId}
Response: [list of people who were at same places/times]

POST /trace-exposure
Body: { "personId": 1, "infectionDate": "2024-01-14" }
Response: { "potentialContacts": [list of exposed people], "locations": [list of visited places] }

GET /people/{id}/risk-level
Response: { "riskLevel": "High", "reason": "Contact with confirmed case", "recommendedAction": "Get tested" }
```

### Technical Requirements:
- **Language**: Choose any (Node.js, Python, Java, etc.)
- **Database**: SQLite with proper relationships
- **Framework**: Express, Flask, Spring Boot, etc.
- **Date/Time Handling**: Proper timezone and duration calculations
- **Validation**: Ensure data integrity and business rules

### Database Schema:
```
People:
- id, name, phone, email, status, createdAt, updatedAt

Locations:
- id, name, address, type, createdAt

CheckIns:
- id, personId, locationId, checkInTime, checkOutTime, createdAt

Status: 'Healthy', 'Exposed', 'Sick', 'Recovered'
Type: 'Restaurant', 'Office', 'School', 'Event', 'Public Transport'
```

### Contact Tracing Logic:
- **Time Overlap Detection**: Find people at same location during overlapping times
- **Exposure Window**: Define how long before/after someone is contagious
- **Duration Calculation**: Calculate how long people were in same space
- **Risk Scoring**: Higher risk for longer exposure times
- **Chain Tracing**: Follow contacts of contacts for broader tracking

### Business Rules:
- People are considered contacts if they were at the same location within 2 hours of each other
- High risk: >15 minutes overlap, Medium risk: 5-15 minutes, Low risk: <5 minutes
- Sick people are contagious 2 days before they report symptoms
- Traced contacts should be marked as "Exposed" status

## ⏱️ **Exact Development Time: 3 days**
- **Basic API & Database Setup**: Half day
- **Person & Location Management**: Half day
- **Check-in System**: Half day
- **Contact Tracing Logic**: 1 day
- **Testing & Validation**: Half day

## 🎯 Success Criteria
- Register people and locations in the system
- Record check-ins with accurate time tracking
- Find all contacts of a sick person based on location overlap
- Calculate risk levels based on exposure duration
- Update health status and track status changes
- Generate exposure reports for health officials
- Handle time calculations correctly (overlaps, durations)
- Proper data validation and error handling

## 📚 Learning Objectives
- Date and time calculations in code
- Complex database queries with time ranges
- Business logic for risk assessment
- Data relationships and joins
- Algorithm design for finding overlaps
- Working with timestamps and durations
- Public health data modeling

*Help protect the community by building effective contact tracing technology!* 🏥📊 