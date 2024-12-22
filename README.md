# RecipeManager  

**RecipeManager** is a web-based application for managing food recipes. It allows users to perform CRUD (Create, Read, Update, Delete) operations on a SQL Server database, making it easy to organize and search for recipes.

---

## Features  
- **Add Recipes**: Users can create new recipes with details like name, description, cooking time, and category.  
- **View Recipes**: Browse through all recipes stored in the database.  
- **Update Recipes**: Modify existing recipe details.  
- **Delete Recipes**: Remove recipes no longer needed.  
- **Search Functionality**: Search for recipes by name.  

---

## Tech Stack  
- **Frontend**: HTML, CSS (Static templates).  
- **Backend**: Flask (Python Framework).  
- **Database**: Microsoft SQL Server.  

---

## Folder Structure
```bash
RecipeManager/
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates for rendering
├── app.py              # Main Flask application
├── requirements.txt    # Dependencies for the project
├── README.md           # Project documentation
```

## Installation  

### Prerequisites 

   - Clone this repository:  
   ```bash
   git clone https://github.com/YousefDewida/RecipeManager.git
   ```
  - Update the database connection in app.py to match your environment
```bash
server = "YourServerName"
database = "recipe"
conn = pyodbc.connect(
    f"Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;"
)
```
