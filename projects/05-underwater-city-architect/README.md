# 📋 Task Management System API

## 🎯 **Main Learning Focus: Database Relationships & Complex Queries**
Learn to design and implement database relationships, foreign keys, joins, and advanced SQL queries for interconnected data models.

## 🏗️ The Project Challenge
You've been hired as a backend developer for **TaskMaster Pro**, a growing productivity company. They need a comprehensive **Task Management API** that can handle complex project organization, team collaboration, and deadline tracking. Build a system that helps teams stay organized and productive!

## 🎯 System Requirements
Create a REST API that manages tasks, projects, and team members with proper relationships and business logic. This system should handle task assignments, priority management, and project progress tracking.

### Core Features Required:

#### 👥 User & Team Management:
- **User Registration**: Create accounts for team members
- **Team Creation**: Organize users into teams/departments
- **Role Management**: Admin, Manager, Member permissions
- **User Profiles**: Basic information and preferences

#### 📋 Project & Task Management:
- **Project Creation**: Organize tasks into projects
- **Task CRUD**: Create, read, update, delete tasks
- **Task Assignment**: Assign tasks to team members
- **Priority Levels**: High, Medium, Low priority tasks
- **Status Tracking**: Todo, In Progress, Review, Completed
- **Due Dates**: Set and track deadlines

#### 📊 Progress Tracking:
- **Project Progress**: Calculate completion percentage
- **Team Workload**: Track tasks per team member
- **Overdue Tasks**: Identify and flag late tasks
- **Task Statistics**: Count tasks by status, priority, etc.

### API Endpoints Needed:
```
Users & Teams:
POST /auth/register
POST /auth/login
GET /users
GET /teams
POST /teams
Body: { "name": "Development Team", "description": "Backend developers" }

Projects:
GET /projects
POST /projects
Body: { "name": "Website Redesign", "description": "...", "teamId": 1, "deadline": "2024-12-31" }
PUT /projects/{id}
DELETE /projects/{id}
GET /projects/{id}/progress

Tasks:
GET /tasks
POST /tasks
Body: { "title": "Fix login bug", "description": "...", "projectId": 1, "assignedTo": 2, "priority": "High", "dueDate": "2024-02-15" }
PUT /tasks/{id}
DELETE /tasks/{id}
PATCH /tasks/{id}/status
Body: { "status": "In Progress" }

Queries & Analytics:
GET /analytics
```

### Technical Requirements:
- **Language**: Choose any (Node.js, Python, Java, etc.)
- **Database**: SQLite with proper relationships
- **Authentication**: JWT tokens for session management
- **Framework**: Express, Flask, Spring Boot, etc.
- **Validation**: Input validation for all fields
- **Error Handling**: Proper error messages and status codes

### Database Schema:
```
Users:
- id, username, email, password (hashed), role, teamId, createdAt

Teams:
- id, name, description, createdAt

Projects:
- id, name, description, teamId, deadline, status, createdAt

Tasks:
- id, title, description, projectId, assignedTo, priority, status, dueDate, createdAt, updatedAt

Priority: 'High', 'Medium', 'Low'
Status: 'Todo', 'In Progress', 'Review', 'Completed'
Role: 'Admin', 'Manager', 'Member'
```

### Complex Business Logic:
- **Task Assignment Validation**: Only assign to team members
- **Permission Checks**: Users can only edit tasks in their teams
- **Progress Calculations**: Calculate project completion percentage
- **Workload Balancing**: Track how many tasks each user has
- **Deadline Tracking**: Identify overdue and upcoming deadlines

## ⏱️ **Exact Development Time: 3 days**
- **Database Design & Setup**: Half day
- **Authentication System**: 1 day
- **Project & Task CRUD**: 1 day
- **Business Logic & Analytics**: 1 day
- **Testing & Validation**: Half day

## 🎯 Success Criteria
- Users can register, login, and join teams
- Projects can be created and managed by teams
- Tasks can be assigned to team members with proper validation
- Task status can be updated through the workflow
- Project progress is calculated correctly
- Users can view their assigned tasks and workload
- Overdue tasks are identified and flagged
- Proper authorization (users can only access their team's data)
- All business rules are enforced consistently

## 📚 Learning Objectives
- Database relationships and foreign keys
- User authentication and authorization
- Complex SQL queries and aggregations
- Business logic implementation
- Data validation and constraints
- API design for complex domains
- Permission-based access control
- Date/time handling and calculations

*Build the system that keeps teams organized and projects on track!* 📈⚡ 