# Django Media Processing API

Django-based API that efficiently processes two types of media files a PDF document and an image and stores the extracted data in a structured database. A working API that accepts PDF and image files, processes them, and stores extracted text and a properly structured and labeled database containing the extracted content.

## 🛠 Tech Stack
- **Backend Framework**: Django & Django REST Framework
- **Database**: SQLite (default, can be configured for PostgreSQL/MySQL)
- **Text Extraction**: pdfplumber (for PDFs), pytesseract (for images)
- **Programming Language**: Python
- **Deployment**: Local development with Django runserver (can be deployed on AWS, Heroku, etc.)

## 🛠 Setup Instructions

### 1️⃣ Ensure Your Virtual Environment is Activated
Before running the project, activate the virtual environment:

#### **For Windows**:
```sh
.venv\Scripts\activate
```

#### **For Mac/Linux**:
```sh
source .venv/bin/activate
```

### 2️⃣ Run Django Server
Once the virtual environment is activated, start the Django development server:
```sh
cd saulikhbackend
python manage.py runserver
```
If the server starts successfully, you should see an output like:
```
Django version X.X.X, using settings 'saulikhbackend.settings'
Starting development server at http://127.0.0.1:8000/
```

### 3️⃣ Test Your API in Postman

#### **Uploading a File (Image/PDF) via Postman**:
1. Open **Postman**.
2. Create a **POST** request to:
   ```
   http://127.0.0.1:8000/api/upload/
   ```
3. In **Body**, select **form-data**.
4. Add a new key:
   - **Key:** `file` (Type: File)
   - **Value:** Choose an image (`.jpg`, `.png`) or PDF file.
5. Click **Send**.

If successful, the response will contain the extracted text.

### 4️⃣ Retrieve Extracted Texts

#### **Fetching Extracted Texts via Postman**:
1. Open **Postman**.
2. Create a **GET** request to:
   ```
   http://127.0.0.1:8000/api/texts/
   ```
3. Click **Send**.

This will return a list of extracted texts stored in the database.
