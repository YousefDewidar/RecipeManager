# RecipeManager  

**RecipeManager** is a web-based application for managing food recipes. It allows users to perform CRUD (Create, Read, Update, Delete) operations on a SQL Server database, making it easy to organize and search for recipes.

![Screenshot 2024-12-27 233438](https://github.com/user-attachments/assets/218e2aa0-308a-4122-8842-6cd0e7cfcbe2)

---

## Features  
- **Add Recipes**: Users can create new recipes with details like name, description, cooking time, and category.  
- **View Recipes**: Browse through all recipes stored in the database.  
- **Update Recipes**: Modify existing recipe details.  
- **Delete Recipes**: Remove recipes no longer needed.  
- **Search Functionality**: Search for recipes by name.  

---

## Mapping
![WhatsApp Image 2024-12-27 at 23 37 05_72100bc4](https://github.com/user-attachments/assets/e60bca89-1091-412e-8c25-adf73e854d31)



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

- Update the database connection in `env.example` to match your environment and make sure to **Rename** it to `.env`

```bash
RecipeManager/
├── .env.example
```

- Change DB_SERVER to match you server's name or use "." to use local server(MSQL Developer Edition)
- Change DB_NAME and insure it's created.
