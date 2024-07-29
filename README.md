# eLearning Django Website 

### Overview

The eLearning Django Website is a comprehensive, beginner-friendly platform designed to provide an engaging and interactive learning experience. Developed using Django, this project serves as a practical example of creating a dynamic and responsive educational website. The site incorporates essential features such as a contact form with a map display and dynamically inherited pages, ensuring a consistent and user-friendly interface across all sections.

This project showcases the integration of modern web technologies and best practices in web development. It leverages Django’s robust framework for backend operations, while the frontend utilizes HTML, CSS, JavaScript, and Bootstrap to deliver a polished and responsive design. The website’s architecture emphasizes modularity and reusability, making it a valuable resource for both learning and practical application.

**Key Components:**

- **Dynamic Page Inheritance**: Achieved through Django’s template inheritance system, ensuring a unified design and layout across all pages. This approach simplifies updates and maintenance by centralizing common elements like headers and footers.
  
- **Contact Form with Map Display**: Enables users to get in touch with the site administrators and view the location on an embedded map. This feature is designed to enhance user interaction and provide easy access to contact information.
  
- **Responsive Design**: Utilizes Bootstrap to ensure the website is mobile-friendly and accessible across various devices and screen sizes. This design approach guarantees a seamless user experience regardless of the device used.
  
- **Courses Page**: Lists the available courses with detailed descriptions, making it easy for users to explore and enroll in educational programs.
  
- **About Page**: Provides insights into the mission and objectives of the e-learning platform, helping users understand the purpose and value of the site.
  
- **Our Team Page**: Highlights the team members behind the platform, offering a personal touch and fostering a sense of connection with the users.
  
- **Thank You Page**: Displays a confirmation message after a user submits the contact form, ensuring that users are aware their message has been received.

### Features

- **Contact Form with Map Display**: Allows users to send inquiries and view the location.
  
- **Dynamically Inherited Pages**: Ensures consistent layout across different pages.
  
- **Responsive Design**: Mobile-friendly layout using Bootstrap.
  
- **Courses Page**: Displays available courses.
  
- **About Page**: Provides information about the e-learning platform.
  
- **Our Team Page**: Information about the team members.
  
- **Thank You Page**: A page displayed after contacting through the form.

### Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django
- **Database**: SQLite
- **Template Source**: [Free CSS eLearning Template](https://www.free-css.com/free-css-templates/page291/elearning)

### Installation

To set up and run this project on your local machine, follow these steps:

#### Prerequisites

- Python 3.x

#### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ladybug-Rupali/eLearningDjangoWebsite.git
    
    cd eLearning-Django-Website
    ```

2. **Create and activate a virtual environment:**

    ```bash
    pip install virtualenv

    virtualenv venv

    Activate -->

    venv\scripts\activate

    ```

3. **Install the required packages:**

    ```bash
    pip install django
    ```

4. **Apply the database migrations:**

    ```bash
    python manage.py makemigrations
    
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Open the website:**

    Open your web browser and go to `http://127.0.0.1:8000/elearn/index/`.

### Usage

- **Home Page**: Overview of available courses, latest news, and links to other sections.
- **About Page**: Information about the e-learning platform and its mission.
- **Courses Page**: Browse available courses and view course details.
- **Our Team Page**: Information about the team members behind the e-learning platform.
- **Contact Page**: Send messages via the contact form, which includes a map display. Submissions are stored in the database and can be viewed by administrators.
- **Thank You Page**: Displayed after a user submits the contact form.

### Image Modifications and Design

- **Image Modifications**: The images from the original template were modified using WhatsApp Meta AI. These images were resized and converted into JPG format to provide a more personalized look for the website.
- **Image Designing**: Additional image designs were created using Canva to enhance the visual appeal of the website.

### Contributing

Contributions are welcome! If you have suggestions or find any bugs, please fork the repository and submit a pull request.

### Credits

This project uses a free template from [Free CSS eLearning Template](https://www.free-css.com/free-css-templates/page291/elearning).

### Contact

For any questions, please contact [rupaligurav0306@gmail.com](mailto:rupaligurav0306@gmail.com).
