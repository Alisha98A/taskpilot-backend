# TaskPilot 🛫

TaskPilot is a full-stack task and notes management application built with **React** (frontend) and **Django REST Framework** (backend). Users can manage tasks, write notes, and contact support, with authentication and responsive UI.

![Responsice Mockup](documentation/testing/readme_images/responsive.png)

---

## Live Demo

🔗 [Deployed App on Heroku](https://taskpilot-backend-6ee557f05c5b.herokuapp.com/)

---

## Project Goals

TaskPilot is a personal productivity web application built with Django and React. The goal of the project is to help individuals take control of their daily routines, stay organized, and reduce mental clutter by providing a clear and easy-to-use system for managing tasks and notes.

### Primary Goals

- **Daily Task Management:** Allow users to create, view, edit, and delete tasks with deadlines and priority levels to stay on top of their responsibilities.
- **Personal Notes:** Enable users to jot down ideas, reminders, or to-dos in a simple note-taking interface related to a task.
- **Private Accounts:** Provide secure sign-up and login functionality, ensuring that each user’s tasks and notes are stored privately.
- **Minimalist Design:** Deliver a clean and focused interface that minimizes distractions and supports a calm workflow.
- **Mobile-Friendly:** Ensure the application is accessible and easy to use on both desktop and mobile devices.
- **Progress Tracking:** Help users monitor their productivity over time by reviewing completed tasks and personal notes.

### Long-Term Vision

- Add visual progress tracking (e.g., daily/weekly completion charts).
- Implement reminders and notifications for upcoming tasks.
- Enable tagging and color-coding for better organization.
- Introduce a calendar view for visual task planning.
- Add dark mode and customizable themes for a more personal experience.

---


## Table of contents

* [Project goals](#project-goals)
* [Table of contents](#table-of-contents)
* [User stories](#user-stories)
  + [Themes](#themes)
  + [Epics](#epics)
  + [User stories](#user-stories-1)
* [Agile development methodology](#agile-development-methodology)
* [Planning](#planning)
  + [Mockups](#mockups)
  + [Data models](#data-models)
* [Design](#design)
  + [Colours](#colours)
  + [Fonts](#fonts)
* [Features](#features)
  + [Landing page with hero image](#landing-page-with-hero-image)
  + [Registration and login](#registration-and-login)
  + [Dashboard with task overview](#dashboard-with-task-overview)
  + [Task CRUD functionality](#task-crud-functionality)
  + [Note CRUD functionality](#note-crud-functionality)
  + [User profile management](#user-profile-management)
  + [Notifications and alerts](#notifications-and-alerts)
  + [Responsive design and accessibility](#responsive-design-and-accessibility)
* [Frameworks, libraries and dependencies](#frameworks-libraries-and-dependencies)
  + [React](#react)
  + [React Router DOM](#react-router-dom)
  + [Axios](#axios)
  + [Django REST Framework](#django-rest-framework)
  + [Bootstrap](#bootstrap)
  + [Other dependencies](#other-dependencies)
* [React features used to enhance user experience](#react-features-used-to-enhance-user-experience)
  + [Custom hooks](#custom-hooks)
  + [Context API](#context-api)
  + [Private routes and authentication](#private-routes-and-authentication)
* [Testing](#testing)
  + [Manual testing](#manual-testing)
  + [Automated testing](#automated-testing)
  + [Validator testing](#validator-testing)
* [Deployment](#deployment)
* [Credits](#credits)
  + [Code](#code)
  + [Media](#media)


---

## User stories

### Themes

*(High-level themes for your project)*

### Epics

*(Major epics breaking down themes)*

### User stories

*(Specific user stories, prioritized)*

---

## Agile development methodology

*(Explain how you approached the project development in sprints or iterations)*

---

## Planning

### Mockups

*(Add links or images of your wireframes and mockups)*

### Data models

*(Describe your Django models and data schema)*

---

## Design

### Colours

*(Describe your color palette)*

### Fonts

*(Describe font choices and sizes)*

---

## Features


- User registration and login
- Create, update, and delete tasks
- Add and manage personal notes
- Contact form for user support
- Responsive design for mobile and desktop
- Protected routes based on authentication
- Combined deployment: React build served from Django

---

### Landing page with hero image

### Registration and login

### Dashboard with task overview

### Task CRUD functionality

### Note CRUD functionality

### User profile management

### Notifications and alerts

### Responsive design and accessibility

---

## Frameworks, libraries and dependencies

- **Frontend:** React, React-Bootstrap, Axios
- **Backend:** Django, Django REST Framework, dj-rest-auth, SimpleJWT
- **Auth:** JWT-based authentication
- **Deployment:** Heroku (backend + frontend build)

### React

### React Router DOM

### Axios

### Django REST Framework

### Bootstrap

### Other dependencies

---

## React features used to enhance user experience

### Custom hooks

### Context API

### Private routes and authentication

---

### Technologies used

- **[Django](https://www.djangoproject.com/)** – Python-based web framework for building the backend.
- **[Bootstrap](https://getbootstrap.com/)** – For responsive design and UI components.
- **[Favicon.io](https://favicon.io/)** – Used to generate the website favicon.
- **[Balsamiq](https://balsamiq.com/)** – Used to create wireframes for the site.
- **[Coolors](https://coolors.co/)** – Used to generate the color scheme palette.
- **[CSS Validation Service](https://jigsaw.w3.org/css-validator/)** – Used to ensure CSS is error-free and follows web standards.
- **[Diffchecker](https://www.diffchecker.com/)** – Used to compare code snippets and find differences.
- **[Font Awesome](https://fontawesome.com/)** – Provides the iconography used on the website.
- **[Git](https://git-scm.com/)** – Used for version control of the project.
- **[Gitpod](https://www.gitpod.io/)** – Cloud-based development environment for streamlined coding.
- **[GitHub](https://github.com/)** – Used for source code hosting and version control.
- **[Google Fonts](https://fonts.google.com/)** – Used for custom web typography.
- **[Heroku](https://www.heroku.com/)** – Platform used for deploying and hosting the live web application.
- **[HTML Markup Validation Service](https://validator.w3.org/)** – Ensures HTML code is valid and standards-compliant.
- **[NVDA (NonVisual Desktop Access)](https://www.nvaccess.org/)** – Screen reader used to test accessibility for visually impaired users.
- **[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)** – Helps evaluate and improve accessibility of web content.
- **[Am I Responsive?](http://ami.responsivedesign.is/)** – Used to display how the website appears across a range of devices.
- **[Web Disability Simulator](https://chrome.google.com/webstore/detail/web-disability-simulator/djcclplfjjlkcmgkhmjemebegpifnbnj)** – 
- **[Chrome DevTools](https://developer.chrome.com/docs/devtools/)** – Used to edit pages on-the-fly and diagnose issues.
- **[Google DevTools](https://developer.chrome.com/docs/devtools/)** – Utilized for debugging, styling, and testing the website.
Chrome extension used to simulate how people with disabilities experience the site.

---

## Testing

### Manual testing

### Automated testing

### Validator testing

---

## Deployment

*(Instructions for deploying your app)*

## 🛠️ Installation

### 1. Clone the backend repo (contains everything now)

```bash
git clone https://github.com/Alisha98A/taskpilot-backend.git
cd taskpilot-backend
```

---

---

## Credits

I would like to acknowledge and thank the following resources and inspirations that helped me throughout this project:

- **Code Institute** – For their comprehensive walkthrough projects that provided a valuable foundation and learning path.
- **React Bootstrap** – For the UI components and documentation that made building responsive and accessible interfaces much easier. [React Bootstrap](https://react-bootstrap.github.io/)
- **Font Awesome** – For providing the icon library used in the project.
- **Balsamiq** – For wireframing and planning the project layout.
- **Coolors** – For helping create the project’s color palette.
- **MDN Web Docs** – For in-depth documentation on HTML, CSS, JavaScript, and accessibility standards.
- **Stack Overflow** – For community-driven help and solutions to coding challenges.
- **Various online tutorials and articles** – For guidance on specific problems and best practices.

A special thank you to everyone who has helped me complete this project!

- **My mentor Spencer Barriball** – [GitHub Profile](https://code-institute-room.slack.com/team/U07R434AML4)  
- The entire **Code Institute tutoring team**  
- All the supportive members of the **Code Institute Slack community**


I would not have done this without all the fantastic people out there!

---

### Code

#### Code Origin and Adaptation

This project builds upon the foundation provided by **Code Institute's Walkthrough Projects**, which offer a valuable starting point for learning and structuring full-stack applications. Because of this, you may notice that some parts of the code — such as the overall architecture, certain components, or patterns — bear resemblance to those walkthrough examples.

#### Adaptation and Customization

However, I have not simply copied the code verbatim. Instead, I have thoroughly reviewed, adapted, and customized various sections to better suit the specific needs and goals of my project. This includes:

- **Modifying the user interface and styling** to match my design vision.
- **Adjusting business logic** to reflect unique features and requirements.
- **Adding or removing functionalities** to align with the project scope.
- **Refactoring code** for better readability, efficiency, and maintainability.

In summary, while the Code Institute's walkthrough projects provided essential guidance and structure, the final implementation is my own, tailored solution that reflects both learning and practical adaptation.

---

#### Use of React Bootstrap Components

I have used components from **React Bootstrap**, adapting them to fit the requirements of this project.

#### Dropdown in `TaskCreate.js` using React Bootstrap component

```jsx
<Dropdown.Toggle variant="success" id="dropdown-basic">
  Dropdown Button
</Dropdown.Toggle>

<Dropdown.Menu>
  <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
  <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
  <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
</Dropdown.Menu>
```

#### Navbar component  `NavBar.js` using React Bootstrap component

[React Bootstrap Navbar Documentation](https://react-bootstrap-v4.netlify.app/components/navbar/)

```jsx
<Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
<Navbar.Toggle aria-controls="basic-navbar-nav" />
<Navbar.Collapse id="basic-navbar-nav">
  <Nav.Link href="#home">Home</Nav.Link>
  <Nav.Link href="#link">Link</Nav.Link>
  <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
  <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
  <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
  <NavDropdown.Divider />
  <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
  Search
</Navbar.Collapse>
```

#### Additional React Bootstrap Components

Beyond the examples shown above, this project incorporates several other components from **React Bootstrap** to build a consistent and responsive user interface. React Bootstrap offers a comprehensive library of pre-built components that integrate seamlessly with React, making development more efficient and maintaining a polished design easier.

You can explore the full range of components and documentation here:  
[React Bootstrap Documentation](https://react-bootstrap.github.io/)


---

### Media

All media used in this project are either original, free for commercial use, or properly credited as follows:

- **Hero Background Image**:  
  Photo taken from [Unsplash]  
  [https://images.unsplash.com/photo-1634420790251-a0eb48dea935?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D]


- **Desktop Image on Sign Up Page**:  
  Photo taken from [Unsplash]  
  [https://images.unsplash.com/photo-1554415707-6e8cfc93fe23?fit=crop&w=900&q=80]

- **Desktop Image on Sign In Page**:  
  Photo taken from [Unsplash]  
  [https://images.unsplash.com/photo-1554415707-6e8cfc93fe23?fit=crop&w=900&q=80]

- **Icons**:  
  Icons from [Font Awesome](https://fontawesome.com/) and [Heroicons](https://heroicons.com/), licensed under [MIT License](https://opensource.org/licenses/MIT).

- **Wireframes**:  
  Wireframes created on [Balsamiq](https://balsamiq.com/)


---
