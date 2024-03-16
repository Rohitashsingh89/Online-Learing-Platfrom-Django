# Online Learning Platform Django 

A learning management and online assessment system for academic education.

###### Due to the large file size, the demo video exceeds Github's upload limit. Please access the video using the following link
[![Alt text](https://img.youtube.com/vi/5QumgqWzc60/0.jpg)](https://youtu.be/5QumgqWzc60?si=7WFa6E2Y3rdS3eRf)

## Features

- Admin adds courses, teachers, and students and assigns them courses.
- The teacher creates course content, announcements, assignments, quizzes, takes attendance, etc. A teacher can see the details and analysis of the assessments.
- Students can enroll in the courses using the access key, see the course content of the enrolled courses, participate in assessments and see their results in detail.
- Discussion section for both teacher and student.

## Technologies Used

- **DJango**
- **HTML**
- **CSS**
- **JavaScript**
- **Bootstrap**
- **Froala Editor**

## Installation

1. Clone the project

```bash
git clone https://github.com/Rohitashsingh89/Online-Learing-Platfrom-Django.git
```

2. Go to the project directory

```bash
cd Online-Learing-Platfrom-Django
```

3. Create a virtual environment and activate it - windows (Optional)

```bash
python -m venv env
```

```bash
env\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If you're using newer versions of python(3.10+), you may need to add the `--use-deprecated=legacy-resolver` option when installing dependencies with `pip` to avoid errors :

```bash
pip install -r requirements.txt --use-deprecated=legacy-resolver
```

5. Make migrations and migrate

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

6. Create admin/superuser

```bash
python manage.py createsuperuser
```

7. Finally run the project

```bash
python manage.py runserver
```

Now the project should be running on http://127.0.0.1:8000/

Login as admin and add some courses, teacher and students.

We greatly appreciate your support! Your contribution helps us maintain this project and ensures its continuous improvement.
Thank you for supporting open-source software! 🙌


## Usage

1. Register for an account or log in if you already have one.
2. Create a new chat room or join an existing one.
3. Start Learning by getting enrolling into the courses.
4. Log out when you're done.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

