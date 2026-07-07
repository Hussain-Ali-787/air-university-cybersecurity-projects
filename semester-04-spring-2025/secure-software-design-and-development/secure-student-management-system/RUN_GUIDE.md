# Run Guide

## Docker Run and Test

### 1. Create `.env`

```powershell
Copy-Item .env.example .env
```

Edit `.env` and set strong values:

```env
SECRET_KEY=your-random-secret-key
WTF_CSRF_SECRET_KEY=your-random-csrf-key
FLASK_ENV=production
FLASK_DEBUG=0
ADMIN_USERNAME=adminuser
ADMIN_PASSWORD=StrongPassword123
```

Production mode will not start with the development fallback `SECRET_KEY`. Set a unique, high-entropy value before running the container.

### 2. Build Image

```powershell
docker build -t secure-student-management-system .
```

### 3. Run Container

```powershell
docker run --env-file .env -p 5000:5000 --name ssdd-student-app secure-student-management-system
```

Open:

```text
http://127.0.0.1:5000
```

### 4. Test Checklist

```text
1. Home page opens.
2. Click Login or Go to Dashboard.
3. Login using ADMIN_USERNAME and ADMIN_PASSWORD from .env.
4. Add a student record.
5. Edit the student record.
6. Delete the student record.
7. Logout.
8. Try opening /dashboard again. It should redirect to login.
```

### 5. Stop and Remove Container

```powershell
docker stop ssdd-student-app
docker rm ssdd-student-app
```

## Important: rebuild cleanly after applying this fix

```powershell
docker stop ssdd-student-app
docker rm ssdd-student-app
docker rmi secure-student-management-system
docker build --no-cache -t secure-student-management-system .
docker run --env-file .env -p 5000:5000 --name ssdd-student-app secure-student-management-system
```

## Persist SQLite Database

By default, the database is inside the container. To persist it:

```powershell
mkdir instance
docker run --env-file .env -p 5000:5000 --name ssdd-student-app -v ${PWD}\instance:/app/instance secure-student-management-system
```

## Useful Debug Commands

```powershell
docker logs ssdd-student-app
docker exec -it ssdd-student-app sh
docker ps
```

## Local Run Without Docker

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
Copy-Item .env.example .env
python src/create_db.py
python src/app.py
```

Open:

```text
http://127.0.0.1:5000
```
