from flask import Flask, render_template, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from forms import StudentForm, LoginForm, RegisterForm
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
csrf = CSRFProtect()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)


def _default_sqlite_uri() -> str:
    """Return a stable SQLite path shared by create_db.py and app.py."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    instance_dir = os.path.join(project_root, "instance")
    os.makedirs(instance_dir, exist_ok=True)
    db_path = os.path.join(instance_dir, "student_management.db")
    return "sqlite:///" + db_path.replace("\\", "/")


def seed_admin_from_env() -> None:
    """Create the first admin from environment variables if provided."""
    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")

    if admin_username and admin_password and not Admin.query.first():
        admin = Admin(
            username=admin_username.strip(),
            password=generate_password_hash(admin_password),
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created from environment variables.")
    elif admin_username and admin_password:
        print("Admin already exists. Environment admin was not recreated.")


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    flask_env = os.getenv("FLASK_ENV", "development").lower()
    secret_key = os.getenv("SECRET_KEY", "change-this-development-secret")
    csrf_secret = os.getenv("WTF_CSRF_SECRET_KEY", secret_key)

    app.config.update(
        SECRET_KEY=secret_key,
        WTF_CSRF_SECRET_KEY=csrf_secret,
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", _default_sqlite_uri()),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SECURE=(flask_env == "production"),
        SESSION_COOKIE_SAMESITE="Lax",
    )

    db.init_app(app)
    csrf.init_app(app)

    @app.after_request
    def set_security_headers(response):
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/go-to-dashboard", methods=["POST"])
    def go_to_dashboard():
        if "admin" in session:
            return redirect(url_for("dashboard"))
        return redirect(url_for("login"))

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if Admin.query.first():
            flash("Admin already registered. Please log in.", "info")
            return redirect(url_for("login"))

        form = RegisterForm()
        if form.validate_on_submit():
            admin = Admin(
                username=form.username.data.strip(),
                password=generate_password_hash(form.password.data),
            )
            db.session.add(admin)
            db.session.commit()
            session["admin"] = admin.username
            flash("Admin account created successfully.", "success")
            return redirect(url_for("dashboard"))

        return render_template("register.html", form=form)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if not Admin.query.first():
            flash("No admin account exists. Register the first admin.", "info")
            return redirect(url_for("register"))

        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data.strip()
            password = form.password.data
            admin = Admin.query.filter_by(username=username).first()

            if admin and check_password_hash(admin.password, password):
                session.clear()
                session["admin"] = admin.username
                flash("Logged in successfully.", "success")
                return redirect(url_for("dashboard"))

            flash("Invalid credentials. Try again.", "danger")

        return render_template("login.html", form=form)

    @app.route("/logout", methods=["POST"])
    def logout():
        session.pop("admin", None)
        flash("You have been logged out.", "info")
        return redirect(url_for("login"))

    @app.route("/dashboard", methods=["GET", "POST"])
    def dashboard():
        if "admin" not in session:
            return redirect(url_for("login"))

        form = StudentForm()
        if form.validate_on_submit():
            student = Students(
                fname=form.fname.data.strip(),
                lname=form.lname.data.strip(),
                age=form.age.data,
                city=form.city.data.strip(),
                email=form.email.data.strip().lower(),
            )
            db.session.add(student)
            db.session.commit()
            flash("Student record added successfully.", "success")
            return redirect(url_for("dashboard"))

        students = Students.query.order_by(Students.id.desc()).all()
        return render_template("dashboard.html", form=form, students=students)

    @app.route("/update/<int:id>", methods=["GET", "POST"])
    def update(id):
        if "admin" not in session:
            return redirect(url_for("login"))

        student = Students.query.get_or_404(id)
        form = StudentForm(obj=student)

        if form.validate_on_submit():
            form.populate_obj(student)
            student.email = student.email.strip().lower()
            db.session.commit()
            flash("Student record updated successfully.", "success")
            return redirect(url_for("dashboard"))

        return render_template("update.html", form=form, student=student)

    @app.route("/delete/<int:id>", methods=["POST"])
    def delete(id):
        if "admin" not in session:
            return redirect(url_for("login"))

        student = Students.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        flash("Student record deleted successfully.", "info")
        return redirect(url_for("dashboard"))

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_admin_from_env()

    debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=debug_mode)
