# CRM

A fully functional Customer Relationship Management (CRM) system built with Django, designed to help you manage leads, agents, and customer interactions efficiently.

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Lead Management: Create, update, categorize, and assign leads to agents.
- Agent Management: Register, edit, and manage sales agents.
- User Authentication: Sign up, log in, password reset, and secure authentication flows.
- Role-based Access: Organisors can assign leads and agents; agents can view and manage their assigned leads.
- Categories: Organize leads into customizable categories.
- Email Notifications: Sends emails on key actions (e.g., lead creation, agent invitation).
- Responsive UI: Styled with Tailwind CSS for a modern look and feel.

---

## Demo

> ![Landing Page Example](https://dummyimage.com/720x600)
>
> The CRM's landing page. The UI is clean and built with Tailwind CSS.

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Virtualenv (recommended)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/theonlykingpin/CRM.git
   cd CRM
   ```

2. **Create a virtual environment and activate:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the app:**
   - Go to `http://127.0.0.1:8000/` in your browser.

---

## Project Structure

```
CRM/
├── agents/            # Agent management app
├── crm/               # Project settings and urls
├── leads/             # Lead management app
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
│   ├── base.html
│   ├── landing.html
│   └── ...
├── manage.py
└── requirements.txt
```

---

## Usage

### User Roles

- **Organisors:** Can create leads, assign agents, manage categories, and view all data.
- **Agents:** Can view and update only their assigned leads.

### Common Actions

- **Signup:** Visit `/signup/` to create a new account.
- **Login:** Visit `/login/`.
- **View Leads:** After logging in, go to `/leads/`.
- **Create Lead:** Organisors can add new leads from the dashboard.
- **Assign Agent:** Organisors can assign agents to leads.
- **Password Reset:** Visit `/reset-password/` to reset your password.

### Example: Creating and Assigning a Lead

1. Login as an Organisor.
2. Navigate to `Leads` and click `Create a new lead`.
3. Fill out the lead details and submit.
4. Assign an agent from the lead's detail page.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.

Please ensure your code follows the style of the project and is well-documented.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/) and [Tailwind CSS](https://tailwindcss.com/).
- Inspired by modern CRM requirements.

---

## Contact

For questions or support, open an issue or contact [theonlykingpin](https://github.com/theonlykingpin).
