
# **EduMentor**  
An online educational platform built with Django.

## About
EduMentor is an online learning platform where users can purchase and participate in various courses. The app provides a seamless experience for both instructors and learners, with interactive classes and resources to enhance the learning journey.

## Features
- **Course Listings**: View available courses and detailed descriptions.
- **Purchase Courses**: Secure payment system to purchase courses and join classes.
- **User Profiles**: Each learner has a profile to track purchased courses and progress.
- **Interactive Classes**: Participate in live and pre-recorded classes with instructors.
- **Progress Tracker**: Track learning progress and milestones for each course.

## Installation

### Requirements
- Python 3.x
- Django 3.x or later
- PostgreSQL (or any other preferred database)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/EduMentor.git
   ```

2. Navigate to the project folder:
   ```bash
   cd EduMentor
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application:
   Open your browser and navigate to `http://127.0.0.1:8000` to see the app in action.

7. Create a superuser (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user for managing the app.

8. Load initial data (if applicable):
   If your app requires loading initial data (such as courses or other configurations), run:
   ```bash
   python manage.py loaddata initial_data.json
   ```

9. Test the application:
   Visit the app in your browser and test all functionalities, including purchasing courses and viewing progress.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
