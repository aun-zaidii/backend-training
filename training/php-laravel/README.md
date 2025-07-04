# 🐘 **PHP Laravel Backend Training**

*Master backend development with PHP's most popular and elegant framework*

---

## 🎯 **Learning Path Overview**

This comprehensive Laravel training covers building modern web applications and APIs with Laravel's elegant syntax, powerful ORM (Eloquent), and rich ecosystem of tools and packages.

---

## 📚 **Training Modules (10 Days)**

### **Day 1-2: PHP Fundamentals**
- Variables, arrays, and functions
- Object-oriented programming
- Namespaces and autoloading
- Composer package management
- Error handling and exceptions
- **PHP-specific:** PHP 8 features (attributes, match expressions)
- **PHP-specific:** PHP type declarations and return types
- **PHP-specific:** PHP traits and interface implementation
- **PHP-specific:** PHP autoloading with PSR-4 and Composer

### **Day 3-4: Laravel Fundamentals**
- MVC architecture and routing
- Controllers and middleware
- Blade templating system
- Forms and validation
- Service container and dependency injection
- **Laravel-specific:** Laravel service container and service providers
- **Laravel-specific:** Laravel facades and helper functions
- **Laravel-specific:** Laravel collections and array helpers
- **Laravel-specific:** Laravel caching and session management

### **Day 5-6: Eloquent ORM & Databases**
- Model definitions and relationships
- Database migrations and seeders
- Query builder and Eloquent queries
- Model validations and callbacks
- Database optimization
- **Eloquent-specific:** Eloquent model events and observers
- **Eloquent-specific:** Eloquent accessors and mutators
- **Eloquent-specific:** Eloquent scopes and local scopes
- **Eloquent-specific:** Eloquent eager loading and N+1 problem prevention

### **Day 7-8: REST API Development**
- API routes and controllers
- Resource classes and API resources
- API authentication with Sanctum
- API versioning strategies
- API documentation
- **Laravel-specific:** Laravel API resources and resource collections
- **Laravel-specific:** Laravel form requests and validation
- **Laravel-specific:** Laravel API rate limiting and throttling
- **Laravel-specific:** Laravel API documentation with L5-Swagger

### **Day 9: Authentication & Authorization**
- Laravel Sanctum setup
- JWT authentication implementation
- Policies and gates for authorization
- Role-based access control
- Security best practices
- **Laravel-specific:** Laravel Sanctum token abilities and expiration
- **Laravel-specific:** Laravel policies and policy authorization
- **Laravel-specific:** Laravel gates and authorization helpers
- **Laravel-specific:** Laravel password reset and email verification

### **Day 10: Testing & Deployment**
- Unit testing with PHPUnit
- Feature testing
- Database testing
- Production configuration
- Deployment strategies
- **Laravel-specific:** Laravel testing helpers and factories
- **Laravel-specific:** Laravel database transactions in tests
- **Laravel-specific:** Laravel queue testing and job testing
- **Laravel-specific:** Laravel deployment with Forge and Envoyer

---

## 🛠️ **Development Setup**

```bash
# Install PHP and Composer
# Laravel requirements: PHP 8.1+, Composer

# Create new Laravel project
composer create-project laravel/laravel myapp
cd myapp

# Install common packages
composer require laravel/sanctum
composer require spatie/laravel-permission
composer require --dev phpunit/phpunit

# Database setup
php artisan migrate
php artisan db:seed
```

---

## 📋 **Practice Projects**

Practice projects for this training are located in the `projects` directory of this repository. Choose any relevant project to apply your Laravel skills.

1. **Blog API**: Posts, comments, authentication
2. **E-commerce Backend**: Products, orders, payments
3. **Task Management**: Teams, projects, assignments
4. **Social Network**: Users, posts, relationships

---

## 🎯 **Skills You'll Master**

- ✅ Laravel MVC architecture
- ✅ Eloquent ORM and relationships
- ✅ API development and resources
- ✅ Authentication and authorization
- ✅ Testing and deployment

---

## ⏱️ **Total Training Duration: 10 days**

Build elegant, maintainable backends with Laravel! 🚀 