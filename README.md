# Classroom Web App

## Description
Classroom Web App is a Django-based platform that allows users to create, join, and manage virtual classrooms. Teachers can post assignments and announcements, while students can submit their work and participate in discussions.

## Features
- 🧑‍🏫 User authentication (Sign up, Login, Logout)
- 📚 Create and join classrooms
- 📝 Post assignments and announcements
- 📂 Submit and manage assignments
- 💬 Comment on posts and submissions

## Installation and Running Locally

### **1. Clone the Repository**
Run the following command in your terminal or Git Bash:

```bash
git clone https://github.com/MalikHashirShakeel/Classroom-Web-App.git
cd Classroom-Web-App
```

### **2. Activate Virtual Environment**
Make sure you have Python installed. Then activate the virtual environment:

- **For Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **For macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **3. Navigate to Project Directory**
Move into the Django project folder:

```bash
cd classroom_web_app
```

### **4. Install Dependencies**
Run the following command to install required packages:

```bash
pip install -r requirements.txt
```

### **5. Run Migrations**
Before running the server, apply migrations:

```bash
python manage.py migrate
```

### **6. Run the Server**
Start the Django development server:

```bash
python manage.py runserver
```

Then, open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Contributing
Feel free to fork this repository and contribute by submitting a pull request.

## License
This project is licensed under the **MIT License**.

