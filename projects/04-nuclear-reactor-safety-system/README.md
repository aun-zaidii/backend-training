# 📊 Inventory Management System API

## 🎯 **Main Learning Focus: Business Logic & Validation Rules**
Master business rule implementation, data validation, mathematical calculations in code, and building robust validation systems that enforce business constraints.

## 🏭 The Business Challenge  
You've been hired as a software developer for **MegaCorp Industries**, a large manufacturing company. They need a **smart inventory management system** that can handle complex business rules for tracking products, managing stock levels, and processing orders with various business logic requirements.

## ⚠️ Mission Requirements
Build a REST API that manages inventory with complex business logic, validation rules, and automatic calculations. This system needs to handle different product categories, stock management, and order processing with sophisticated business rules.

### Core Business Logic Components:

#### 📦 Product Management:
- **Product Categories**: Electronics, Clothing, Food, Books (each with different rules)
- **Stock Tracking**: Current quantity, minimum stock levels, maximum capacity
- **Price Management**: Base price, discount rules, bulk pricing
- **Product Validation**: Different validation rules per category

#### 📋 Order Processing Logic:
- **Order Validation**: Check stock availability before confirming orders
- **Discount Calculations**: Apply bulk discounts, category discounts, customer loyalty discounts
- **Shipping Calculations**: Calculate shipping costs based on weight, distance, priority
- **Inventory Updates**: Automatically update stock levels when orders are placed

#### 🧮 Business Rules to Implement:
- **Stock Alerts**: Automatically flag when products are below minimum stock
- **Bulk Pricing**: Different prices for quantity ranges (1-10, 11-50, 51+)
- **Category Rules**: Food items expire, electronics have warranties
- **Order Limits**: Maximum order quantities per customer per day
- **Seasonal Pricing**: Apply seasonal multipliers to certain categories

### API Endpoints Needed:
```
Products:
GET /products
POST /products
Body: { "name": "Laptop", "category": "Electronics", "price": 999.99, "stock": 50, "minStock": 10 }

PUT /products/{id}
DELETE /products/{id}
GET /products/low-stock
GET /products/category/{category}

Orders:
POST /orders
Body: { "customerId": 1, "items": [{ "productId": 1, "quantity": 2 }] }
Response: { "orderId": 1, "total": 1899.98, "discount": 100.00, "shipping": 15.99 }

GET /orders/{id}
GET /orders/customer/{customerId}

Business Logic:
GET /products/{id}/pricing?quantity=25
Response: { "unitPrice": 899.99, "totalPrice": 22499.75, "discountApplied": "bulk-discount-10%" }

POST /inventory/check-availability
Body: { "items": [{ "productId": 1, "quantity": 100 }] }
Response: { "available": false, "reason": "Insufficient stock: only 50 available" }
```

### Technical Requirements:
- **Language**: Choose any (Node.js, Python, Java, etc.)
- **Database**: SQLite with proper relationships
- **Framework**: Express, Flask, Spring Boot, etc.
- **Validation**: Input validation for all business rules
- **Error Handling**: Detailed error messages for business rule violations

### Complex Business Logic Scenarios:
1. **Multi-Item Order Processing**: Calculate totals with different discount rules per item
2. **Stock Validation**: Prevent overselling, handle partial fulfillment
3. **Dynamic Pricing**: Real-time price calculation based on quantity and customer type
4. **Inventory Alerts**: Automatic notifications when restocking is needed
5. **Order History Analysis**: Calculate customer lifetime value and loyalty discounts

## ⏱️ **Exact Development Time: 2 days**
- **Basic API & Database Setup**: Half day
- **Product Management Logic**: Half day
- **Order Processing & Business Rules**: 1 day
- **Testing Complex Scenarios**: Half day

## 🎯 Success Criteria
- Handle all product CRUD operations correctly
- Implement complex pricing calculations (bulk, seasonal, loyalty)
- Process orders with proper stock validation
- Apply business rules consistently
- Prevent invalid operations (overselling, negative stock)
- Calculate shipping costs accurately
- Generate proper error messages for business rule violations
- Handle edge cases gracefully

## 📚 Learning Objectives
- Complex business logic implementation
- Data validation and business rules
- Mathematical calculations in code
- Error handling for business scenarios
- Database relationships and constraints
- Input sanitization and validation
- API design for complex operations

*Build the logic that keeps a business running smoothly and profitably!* 📈⚡ 