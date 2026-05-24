from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, Email


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=50),
            Regexp(r"^[A-Za-z0-9_.-]+$", message="Username may contain letters, numbers, dot, underscore, and hyphen."),
        ],
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, max=128, message="Password must be at least 8 characters long."),
        ],
    )


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=128)])


class StudentForm(FlaskForm):
    fname = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Length(max=50),
            Regexp(r"^[A-Za-z]+$", message="First name must contain only letters."),
        ],
    )

    lname = StringField(
        "Last Name",
        validators=[
            DataRequired(),
            Length(max=50),
            Regexp(r"^[A-Za-z]+$", message="Last name must contain only letters."),
        ],
    )

    age = IntegerField(
        "Age",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=120, message="Age must be between 1 and 120."),
        ],
    )

    city = StringField(
        "City",
        validators=[
            DataRequired(),
            Length(max=50),
            Regexp(r"^[A-Za-z ]+$", message="City must contain only letters and spaces."),
        ],
    )

    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Invalid email address."),
            Length(max=100),
        ],
    )
