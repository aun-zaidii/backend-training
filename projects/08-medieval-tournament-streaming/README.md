# 🏰 Medieval Tournament Event Management API

## 🎯 **Main Learning Focus: Event Scheduling & Bracket Generation Algorithms**
Master complex scheduling algorithms, tournament bracket generation, conflict detection, and building systems that manage time-based event workflows.

## ⚔️ The Tournament Challenge
Welcome to the realm of **Camelot Events Management**! King Arthur has tasked you with creating a digital system to manage the kingdom's grand tournaments. You must build an **Event Management API** that handles tournament registration, participant management, scheduling, and results tracking for epic medieval competitions!

## 🛡️ Quest Objectives
Create a comprehensive REST API that manages tournaments, knights, events, and match results. This system will help tournament organizers schedule competitions, track participants, and record the glorious victories (and defeats) of brave knights across the realm!

### Core Features Required:

#### 🏆 Tournament Management:
- **Tournament Creation**: Set up new tournaments with dates and locations
- **Event Scheduling**: Different competition types (Jousting, Archery, Sword Fighting)
- **Registration Management**: Allow knights to register for tournaments
- **Capacity Management**: Limit participants per event
- **Status Tracking**: Registration, Active, Completed tournaments

#### ⚔️ Participant & Knight Management:
- **Knight Registration**: Manage participant profiles and information
- **Skill Tracking**: Record knight specialties and experience levels
- **Equipment Management**: Track armor, weapons, and horse details
- **Achievement Records**: Historical tournament performance
- **Team Management**: Group knights into households or regions

#### 📅 Event Scheduling & Results:
- **Match Scheduling**: Organize brackets and match pairings
- **Score Recording**: Track match results and tournament standings
- **Leaderboards**: Rank knights by performance
- **Prize Management**: Track tournament rewards and honors
- **Historical Records**: Maintain tournament archives

### API Endpoints Needed:
```
Tournament Management:
GET /tournaments
POST /tournaments
Body: { "name": "Spring Jousting Championship", "location": "Camelot Arena", "startDate": "2024-06-01", "endDate": "2024-06-03", "maxParticipants": 64 }
PUT /tournaments/{id}
DELETE /tournaments/{id}
GET /tournaments/{id}/participants
POST /tournaments/{id}/register
Body: { "knightId": 1, "events": ["jousting", "archery"] }

Knight Management:
GET /knights
POST /knights
Body: { "name": "Sir Lancelot", "region": "Camelot", "speciality": "Jousting", "experience": "Expert", "horse": "Thunderbolt" }
PUT /knights/{id}
GET /knights/{id}/tournaments
GET /knights/{id}/achievements

Event Management:
GET /tournaments/{id}/events
POST /tournaments/{id}/events
Body: { "name": "Jousting Finals", "type": "jousting", "date": "2024-06-02", "maxParticipants": 16 }
GET /events/{id}/matches
POST /events/{id}/matches
Body: { "knight1Id": 1, "knight2Id": 2, "scheduledTime": "2024-06-02T10:00:00Z" }

Results & Scoring:
POST /matches/{id}/result
Body: { "winnerId": 1, "score": "3-1", "notes": "Excellent joust by Sir Lancelot" }
GET /tournaments/{id}/leaderboard
GET /tournaments/{id}/standings
GET /knights/{id}/statistics
```

### Technical Requirements:
- **Language**: Choose any (Node.js, Python, Java, etc.)
- **Database**: SQLite with proper relationships
- **Framework**: Express, Flask, Spring Boot, etc.
- **Date/Time Handling**: Tournament scheduling and match timing
- **Validation**: Business rules for tournament management

### Database Schema:
```
Tournaments:
- id, name, description, location, startDate, endDate, status, maxParticipants, createdAt

Knights:
- id, name, region, speciality, experience, horse, armor, weapon, wins, losses, createdAt

Events:
- id, tournamentId, name, type, date, maxParticipants, status

Registrations:
- id, tournamentId, knightId, events, registrationDate, status

Matches:
- id, eventId, knight1Id, knight2Id, winnerId, score, notes, scheduledTime, completedAt

EventTypes: 'jousting', 'archery', 'sword-fighting', 'horse-racing'
Status: 'upcoming', 'registration-open', 'active', 'completed', 'cancelled'
Experience: 'novice', 'experienced', 'expert', 'legendary'
```

### Business Logic Requirements:
- **Registration Validation**: Ensure knights can only register for open tournaments
- **Capacity Management**: Prevent over-registration for events
- **Bracket Generation**: Automatically create match pairings
- **Score Calculations**: Update knight statistics after each match
- **Conflict Detection**: Ensure knights aren't double-booked
- **Prize Distribution**: Calculate and assign tournament rewards

### Tournament Logic:
- Only allow registration during "registration-open" status
- Generate match brackets when tournament becomes "active"
- Update knight win/loss records automatically
- Calculate tournament standings based on match results
- Prevent scheduling conflicts for the same knight
- Track historical performance across tournaments

## ⏱️ **Exact Development Time: 4 days**
- **Database Design & Setup**: Half day
- **Tournament & Knight Management**: 1 day
- **Event & Match Scheduling**: 1 day
- **Results & Statistics System**: 1 day
- **Testing & Validation**: Half day

## 🎯 Victory Conditions
- Create and manage tournaments with proper scheduling
- Register knights and manage participant lists
- Generate match brackets and schedule events
- Record match results and update standings
- Calculate accurate leaderboards and statistics
- Proper validation for all business rules
- Handle tournament lifecycle (registration → active → completed)
- Prevent scheduling conflicts and over-registration

## 📚 Learning Objectives
- Complex database relationships and foreign keys
- Date/time handling and scheduling logic
- Tournament bracket generation algorithms
- Statistical calculations and aggregations
- Business rule validation and constraints
- Event-driven system design
- Domain modeling for complex workflows

*Organize the most legendary tournaments the realm has ever seen!* 🏆⚔️ 