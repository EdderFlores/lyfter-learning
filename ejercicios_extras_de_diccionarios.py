#Ejercicio 1

sales = [
    {
        "date": "2026-01-29",
        "customer_email": "edder@purchase1.com",
        "items": [
            {
                "name": "iPhone 13",
                "upc": "PHONE-001",
                "unit_price": 799.99,
            }
        ]        
    },
    {
        "date": "2026-01-30",
        "customer_email": "jose@purchase2.com",
        "items": [
            {
                "name": "MacBook Pro",
                "upc": "LAPTOP-001",
                "unit_price": 1299.99,
            }
        ]
    },
    {
        "date": "2026-01-31",
        "customer_email": "maria@purchase3.com",
        "items": [
            {
                "name": "iPad Air",
                "upc": "TABLET-001",
                "unit_price": 599.99,
            }
        ]
    },
    {
        "date": "2026-02-01",
        "customer_email": "luis@purchase4.com",
        "items": [
            {
                "name": "Apple Watch",
                "upc": "WATCH-001",
                "unit_price": 399.99,
            }
        ]
    }
]
total_sales = {}

for sale in sales:
    for item in sale["items"]:
        total_sales[item['upc']] = item['unit_price']

print("")
print("*********************************")
print("")

#Ejercicio 2

employees = [
    {"name": "Carlos", "email": "carlos@veonservices.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@veonservices.com", "department": "TI"},
    {"name": "Luis", "email": "luis@veonservices.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@veonservices.com", "department": "RRHH"},
    {"name": "Edder", "email": "edder@veonservices.com", "department": "Ventas"},
    {"name": "Danny", "email": "danny@veonservices.com", "department": "TI"},
    {"name": "Hannath", "email": "hannath@veonservices.com", "department": "TI"},
    {"name": "Christopher", "email": "chris@veonservices.com", "department": "RRHH"},
]

employees_by_department = {}

for employee in employees:
    department = employee['department']
    if department in employees_by_department:
        employees_by_department[department].append(employee)
    else: 
        employees_by_department[department] = [employee] 

print("")
print("*********************************")
print("")

#Ejercicio 3
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

total_sales_by_category = {}

for product in products:
    category = product['category']
    price = product['price']
    if category in total_sales_by_category:
        total_sales_by_category[category] += price
    else:
        total_sales_by_category[category] = price

