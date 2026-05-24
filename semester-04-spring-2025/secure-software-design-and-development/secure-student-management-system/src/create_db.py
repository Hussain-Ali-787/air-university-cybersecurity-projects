from app import create_app, db, seed_admin_from_env

app = create_app()

with app.app_context():
    db.create_all()
    seed_admin_from_env()
    print("Database tables are ready.")
