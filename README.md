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
   git clone https://github.com/YousefDewidar/RecipeManager.git
   ```

- Update the database connection in env.example to match your environment
- Change DB_SERVER to match you server's name or use "." to use local server(MSQL Developer Edition)
- Change DB_NAME and insure it's created.

```bash
RecipeManager/
├── .env.example
```
