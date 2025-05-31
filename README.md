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

- User registration and login functionality  
- Create, update, and delete tasks seamlessly  
- Add, edit, and manage personal notes  
- Contact form to reach out for user support  
- Fully responsive design optimized for both mobile and desktop  
- Protected routes that restrict access based on user authentication  
- Combined deployment where the React frontend build is served directly from the Django backend  

---

### Landing Page with Hero Image

The landing page features a large, eye-catching hero image that welcomes users and introduces the app’s core purpose. It provides clear call-to-actions such as registration and login buttons to guide new and returning users.

### Registration and Login

Users can securely register new accounts and log in to access personalized features. The authentication system uses JWT tokens to maintain sessions and protect user data.

### Dashboard with Task Overview

Once logged in, users land on a dashboard that summarizes their current tasks, deadlines, and priorities at a glance. This overview helps users stay organized and focused on what matters most.

### Task CRUD Functionality

Users have full control over their tasks, including creating new tasks, viewing task details, updating information such as status and due date, and deleting completed or unwanted tasks. Task categories and priorities can also be managed for better organization.

### Note CRUD Functionality

The app allows users to manage personal notes alongside their tasks. Users can add new notes, edit existing ones, view detailed content, and delete notes when no longer needed, providing a flexible workspace.

### User Profile Management

Users can view and update their profile information, such as username, email, and other personal details, ensuring their account is up-to-date and secure.

### Notifications and Alerts

The application provides timely notifications and alerts for important events, such as upcoming deadlines or changes to tasks, keeping users informed and engaged.

### Responsive Design and Accessibility

The UI is designed to be fully responsive, adapting smoothly to different screen sizes from desktops to mobile devices. Accessibility best practices are followed to ensure the app is usable by people with various abilities.



---

## Frameworks, Libraries, and Dependencies

- **Frontend:** React, React-Bootstrap, Axios  
- **Backend:** Django, Django REST Framework, dj-rest-auth, SimpleJWT  
- **Authentication:** JWT-based authentication  
- **Deployment:** Heroku (hosting backend and frontend build)

### React

React is the core JavaScript library used for building the user interface. It enables the creation of reusable UI components and manages the application state efficiently.

### React Router DOM

React Router DOM is used for client-side routing, allowing navigation between different components and views without full page reloads. It manages the routing logic, including protected/private routes.

### Axios

Axios is a promise-based HTTP client used for making API requests from the React frontend to the Django REST API backend. It simplifies sending asynchronous requests and handling responses.

### Django REST Framework

Django REST Framework (DRF) is the backend toolkit that powers the API. It provides tools for serialization, authentication, permissions, and routing to create a RESTful API in Django.

### Bootstrap

Bootstrap (via React-Bootstrap) is used for responsive and consistent UI styling. It offers prebuilt components and grid layouts that help build mobile-friendly and accessible user interfaces.

### Other Dependencies

Additional libraries and tools include:

- **dj-rest-auth** for handling authentication workflows like login, logout, password reset  
- **SimpleJWT** for JWT authentication tokens management  
- **Cloudinary** for cloud-based media storage and management 
- Various utility libraries to assist with form validation, date handling, and state management

### Project Development Notes

At the start of the project, I integrated **Cloudinary** to enable file attachments within the app. This included setting up Cloudinary for media storage and adding file upload functionality to relevant components.

However, during the final stages of development and testing, I decided to remove the file attachment feature. This decision was based on factors such as simplifying the user experience, reducing complexity, or project scope adjustments.

Although the file attachment functionality was ultimately excluded from the finished product, the initial setup with Cloudinary remains as a foundation in case it is needed for future enhancements.

---

## React features used to enhance user experience

### Custom hooks

  <details>
  <summary><strong>Custom Hook: useTasks (click to expand)</strong></summary>

  To keep components clean and promote reusability, a custom React hook called `useTasks` was created. This hook centralizes all logic related to managing tasks, including data fetching, state updates, filtering, and grouping.

  The `useTasks` hook handles the following:

  - Fetching all tasks from the backend API upon component mount
  - Storing the full list of tasks and available categories in state
  - Deleting tasks from both the backend and frontend state
  - Updating a task's state (e.g., from "open" to "done")
  - Filtering and sorting tasks by category, search term, due date, and priority
  - Grouping tasks into "Today", "This Week", and "Later" based on due dates

  **Example: `useTasks.js`**

  ```js
  import { useEffect, useState } from "react";
  import { axiosReq } from "../api/axiosDefaults";

  export const useTasks = () => {
    const [tasks, setTasks] = useState([]);
    const [categories, setCategories] = useState([]);

    useEffect(() => {
      const fetchTasks = async () => {
        try {
          const res = await axiosReq.get("/api/tasks/");
          const taskData = res.data.results;
          setTasks(taskData);
          setCategories(["all", ...new Set(taskData.map((t) => t.category))]);
        } catch (err) {
          console.error("Error fetching tasks:", err);
        }
      };
      fetchTasks();
    }, []);

    const deleteTask = async (id) => {
      if (window.confirm("Are you sure you want to delete this task?")) {
        try {
          await axiosReq.delete(`/api/tasks/${id}/`);
          setTasks((prev) => prev.filter((t) => t.id !== id));
        } catch (err) {
          console.error("Error deleting task:", err);
        }
      }
    };

    const updateTaskState = async (task, newState) => {
      try {
        const isoDueDate = new Date(task.due_date).toISOString();
        await axiosReq.put(`/api/tasks/${task.id}/`, {
          ...task,
          due_date: isoDueDate,
          state: newState,
        });
        setTasks((prev) =>
          prev.map((t) => (t.id === task.id ? { ...t, state: newState } : t))
        );
      } catch (err) {
        console.error("Error updating task state:", err);
      }
    };

    const filterAndSortTasks = ({ selectedCategory, searchTerm, sortBy }) => {
      return tasks
        .filter((task) =>
          selectedCategory === "all" ? true : task.category === selectedCategory
        )
        .filter((task) =>
          `${task.title} ${task.description}`
            .toLowerCase()
            .includes(searchTerm.toLowerCase())
        )
        .sort((a, b) => {
          if (sortBy === "due_date") {
            return new Date(a.due_date) - new Date(b.due_date);
          }
          const priorityRank = { high: 1, medium: 2, low: 3 };
          return priorityRank[a.priority] - priorityRank[b.priority];
        });
    };

    const groupTasks = (taskList) => {
      const today = new Date();
      const endOfWeek = new Date();
      endOfWeek.setDate(today.getDate() + 7);

      const todayTasks = [];
      const weekTasks = [];
      const laterTasks = [];

      taskList.forEach((task) => {
        const due = new Date(task.due_date);
        if (due.toDateString() === today.toDateString()) {
          todayTasks.push(task);
        } else if (due <= endOfWeek) {
          weekTasks.push(task);
        } else {
          laterTasks.push(task);
        }
      });

      return { todayTasks, weekTasks, laterTasks };
    };

    return {
      tasks,
      setTasks,
      categories,
      deleteTask,
      updateTaskState,
      filterAndSortTasks,
      groupTasks,
    };
  };

  </details>

---

### Context API

<details>
  <summary><strong>Context API (click to expand)</strong></summary>

  This project uses the React Context API to manage user authentication state globally. The `CurrentUserProvider` component fetches the current authenticated user on app load, tracks loading status, and handles automatic redirects on unauthorized API responses.

  Multiple contexts are created to provide both the current user data, a setter function to update the user, and a loading flag indicating when the user data is ready.

  Custom hooks make accessing these contexts easier throughout the app:
  - `useCurrentUser` — access the current user object
  - `useSetCurrentUser` — update the current user state
  - `useUserLoaded` — check if user data has finished loading

  **Example: `CurrentUserContext.js`**

  ```jsx
  import { createContext, useContext, useEffect, useState } from "react";
  import { useHistory } from "react-router-dom";
  import { axiosReq, axiosRes } from "../api/axiosDefaults";

  // Create contexts
  export const CurrentUserContext = createContext();
  export const SetCurrentUserContext = createContext();
  export const UserLoadedContext = createContext();

  // Custom hooks for easier usage
  export const useCurrentUser = () => useContext(CurrentUserContext);
  export const useSetCurrentUser = () => useContext(SetCurrentUserContext);
  export const useUserLoaded = () => useContext(UserLoadedContext);

  export const CurrentUserProvider = ({ children }) => {
    const [currentUser, setCurrentUser] = useState(null);
    const [userLoaded, setUserLoaded] = useState(false);
    const history = useHistory();

    // Fetch current user when app loads
    useEffect(() => {
      const handleMount = async () => {
        try {
          const { data } = await axiosReq.get("/api/dj-rest-auth/user/");
          setCurrentUser(data);
        } catch (err) {
          setCurrentUser(null);
        } finally {
          setUserLoaded(true);
        }
      };
      handleMount();
    }, []);

    // Setup Axios interceptors to handle 401 errors globally
    useEffect(() => {
      const requestInterceptor = axiosReq.interceptors.request.use(
        (config) => config,
        (error) => Promise.reject(error)
      );

      const responseInterceptor = axiosRes.interceptors.response.use(
        (response) => response,
        (error) => {
          if (
            error.response?.status === 401 &&
            history.location.pathname !== "/signin"
          ) {
            setCurrentUser(null);
            history.push("/signin");
          }
          return Promise.reject(error);
        }
      );

      // Cleanup interceptors on unmount
      return () => {
        axiosReq.interceptors.request.eject(requestInterceptor);
        axiosRes.interceptors.response.eject(responseInterceptor);
      };
    }, [history]);

    return (
      <CurrentUserContext.Provider value={currentUser}>
        <SetCurrentUserContext.Provider value={setCurrentUser}>
          <UserLoadedContext.Provider value={userLoaded}>
            {children}
          </UserLoadedContext.Provider>
        </SetCurrentUserContext.Provider>
      </CurrentUserContext.Provider>
    );
  };

  </details>

---

### Private routes and authentication

  <details>
  <summary><strong>Private Routes and Authentication (click to expand)</strong></summary>

  Private routes are used to restrict access to specific pages based on whether a user is authenticated. If a user is not logged in, they are redirected to the login page, protecting sensitive or user-specific parts of the app.

  This project uses a custom `PrivateRoute` component to enforce these restrictions within a React Router setup.

  **Example: App routing setup with private routes**

  ```jsx
  import { useEffect } from "react";
  import { Route, Switch, useLocation } from "react-router-dom";
  import Container from "react-bootstrap/Container";
  import styles from "./App.module.css";

  import NavBar from "./components/NavBar";
  import PrivateRoute from "./components/PrivateRoute";

  import "./api/axiosDefaults";

  // Pages
  import WelcomePage from "./pages/home/WelcomePage";
  import Dashboard from "./pages/home/Dashboard";
  import SignUpForm from "./pages/auth/SignUpForm";
  import SignInForm from "./pages/auth/SignInForm";

  // Task Pages
  import TaskList from "./pages/tasks/TaskList";
  import TaskDetail from "./pages/tasks/TaskDetail";
  import TaskCreate from "./pages/tasks/TaskCreate.js";
  import TaskEdit from "./pages/tasks/TaskEdit";

  // Note Pages
  import NoteList from "./pages/notes/NoteList";
  import NoteDetail from "./pages/notes/NoteDetail";
  import NoteCreate from "./pages/notes/NoteCreate.js";
  import NoteEdit from "./pages/notes/NoteEdit";
  import NoteDelete from "./pages/notes/NoteDelete";

  // Contact Page
  import ContactForm from "./pages/contact/ContactForm";

  // Context
  import { useUserLoaded } from "./contexts/CurrentUserContext";

  function App() {
    const location = useLocation();
    const userLoaded = useUserLoaded();

    useEffect(() => {
      document.body.classList.toggle("no-scroll", location.pathname === "/");
    }, [location.pathname]);

    if (!userLoaded) return null;

    return (
      <div className={styles.App}>
        <NavBar />

        {location.pathname === "/" ? (
          <WelcomePage />
        ) : (
          <Container className={styles.Main}>
            <Switch>
              {/* Home */}
              <Route exact path="/" component={WelcomePage} />

              {/* Dashboard */}
              <PrivateRoute exact path="/dashboard" component={Dashboard} />

              {/* Tasks */}
              <PrivateRoute exact path="/tasks" component={TaskList} />
              <PrivateRoute exact path="/tasks/create" component={TaskCreate} />
              <PrivateRoute exact path="/tasks/:id" component={TaskDetail} />
              <PrivateRoute exact path="/tasks/:id/edit" component={TaskEdit} />

              {/* Notes */}
              <PrivateRoute exact path="/notes" component={NoteList} />
              <PrivateRoute exact path="/notes/create" component={NoteCreate} />
              <PrivateRoute exact path="/notes/:id" component={NoteDetail} />
              <PrivateRoute exact path="/notes/:id/edit" component={NoteEdit} />
              <PrivateRoute exact path="/notes/:id/delete" component={NoteDelete} />

              {/* Contact */}
              <PrivateRoute exact path="/contact" component={ContactForm} />

              {/* Auth */}
              <Route exact path="/signin" component={SignInForm} />
              <Route exact path="/signup" component={SignUpForm} />

              {/* Fallback */}
              <Route render={() => <p>Page not found!</p>} />
            </Switch>
          </Container>
        )}
      </div>
    );
  }

  export default App;


  </details>

---


  <details>
  <summary><strong>PrivateRoute Component (click to expand)</strong></summary>

  The `PrivateRoute` component protects routes that require the user to be authenticated. It checks if there is a current user available via context, and if not, redirects the user to the sign-in page.

  This component wraps the standard React Router `Route` and conditionally renders either the requested component or a redirect.

  **Example: `PrivateRoute.js`**

  ```jsx
  import React from "react";
  import { Route, Redirect } from "react-router-dom";
  import { useCurrentUser } from "../contexts/CurrentUserContext";

  function PrivateRoute({ component: Component, ...rest }) {
    const currentUser = useCurrentUser();

    return (
      <Route
        {...rest}
        render={(props) =>
          currentUser ? <Component {...props} /> : <Redirect to="/signin" />
        }
      />
    );
  }

  export default PrivateRoute;

  </details>

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

All testing instructions and details are documented separately in the [`TESTING.md`](https://github.com/Alisha98A/taskpilot-backend/blob/main/TESTING.md) file.  
Please refer to that file for comprehensive guidance on how to run, write, and understand the tests used in this project.

---

## Deployment


### Initial Setup (for Django Backend Application)

- Sign up for a Heroku account at [heroku.com](https://www.heroku.com/).
- Download and install the Heroku CLI to interact with Heroku from your local machine.
- Alternatively, you can use the Heroku web interface for management tasks.

---

### Creating a Heroku App

1. Log into your Heroku account.
2. Click **New** > **Create new app**.
3. Enter a unique app name.
4. Choose your preferred region.
5. Click **Create app**.

---

### Preparing the Application

1. **Create a `Procfile`** in your project’s root directory.  
   For Django, the `Procfile` should contain:

```bash
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn taskpilot_api.wsgi
```

This tells Heroku how to start your web server using Gunicorn.

2. Ensure your project has an up-to-date requirements.txt file listing all dependencies:

```bash
pip freeze > requirements.txt
```

3. Configure necessary environment variables in Heroku:
	•	Go to your Heroku app dashboard.
	•	Navigate to Settings > Config Vars.
	•	Add variables such as SECRET_KEY, DATABASE_URL, and any others your project requires.

4.	Add your Heroku domain to the Django ALLOWED_HOSTS in settings.py:

```bash
ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost', '127.0.0.1']
```

---

### Configure Buildpacks

Heroku needs buildpacks to install dependencies not listed in `requirements.txt`:

1. Go to your app’s **Settings** > **Buildpacks**.
2. Add **Python** buildpack first.
3. Add **Node.js** buildpack second.

> The order is important: Python first, then Node.js. You can reorder by dragging if necessary.

---

### Deployment Process

You can deploy your project in multiple ways:

- **Using GitHub integration:**
  - In your Heroku app dashboard, go to the **Deploy** tab.
  - Select **GitHub** as the deployment method.
  - Search for your repository `taskpilot-backend`.
  - Click **Connect**.
  - Scroll down to **Automatic Deploys** and click **Enable Automatic Deploys** to auto-deploy on every push, or
  - Click **Deploy Branch** to manually deploy.

- **Using Heroku CLI:**

  From your local project folder, run:

```bash
heroku login
heroku git:remote -a your-heroku-app-name
git push heroku main
```

### Running Migrations on Heroku

After deployment, run your Django migrations on the Heroku server:

```bash
heroku run python manage.py migrate
```

### Final Steps
  • Verify that the Web Dyno is running in the Heroku dashboard under the Resources tab.
  • Open your deployed application via the Heroku dashboard or run:

```bash
heroku open
```

### Local Deployment

### How to Clone

To work locally on your project:

1. Navigate to the GitHub repository **taskpilot-backend**.  
2. Click the **Code** dropdown.  
3. Select **HTTPS** and copy the URL.  
4. Open VSCode or your terminal.  
5. Navigate to the directory where you want your project.  
6. Run the command:

```bash
git clone https://github.com/Alisha98A/taskpilot-backend.git
```

7. Your project is now cloned locally.

---

### Install Dependencies

Make sure you have Python and pip installed. Then, run:

```bash
pip install -r requirements.txt
```

### Run Application Locally

Start your Django development server:

```bash
python manage.py runserver
```

Visit http://localhost:8000 to see your app running locally.


### How to Fork a Repository

Forking lets you copy someone else’s project to your own GitHub account to make changes safely.
  1.  Log into GitHub.
  2.  Navigate to the repository you want to fork.
  3.  Click the Fork button in the top-right corner.
  4.  Optionally rename your fork and add a description.
  5.  Choose whether to fork just the main branch or all branches.
  6.  Click Create fork.
  7.  Your forked repository will appear in your GitHub account, ready for cloning and development.


This concludes the deployment and version control guide tailored to TaskPilot backend repo project using VSCode.

---
## Frontend Setup

To set up the React frontend, please follow the instructions in the [TaskPilot Frontend README](https://github.com/Alisha98A/taskpilot-frontend/blob/main/README.md).

---

## Deployment Guide for React Front-End and Django API Back-End

Once both the backend and frontend are set up individually, follow the steps below to integrate them and enable full-stack functionality.

### Setting Up WhiteNoise for Serving Static Files

Because your React application contains static resources, you need to gather them for deployment through WhiteNoise. WhiteNoise will also take care of static files used by the Django Admin panel, ensuring they are served correctly on your live site.

---

### Steps to follow in your terminal:

1. Navigate to the root folder of your project if you aren’t already there.

2. Install WhiteNoise by executing the following command:

```bash
   pip3 install whitenoise==6.4.0
```

3.	Update your requirements.txt file to reflect the newly installed package by running:

4.	Create a directory named staticfiles inside the root directory with this command:

```bash
mkdir staticfiles
   ```

---

### Modifying `settings.py`

- Inside the `INSTALLED_APPS` list, verify that `'cloudinary_storage'` appears **after** `'django.contrib.staticfiles'`. This order prevents Cloudinary from disrupting static file management, enabling WhiteNoise to fully manage them.

- Here is an example snippet of the `INSTALLED_APPS` section from `settings.py`.

- In the `MIDDLEWARE` configuration, add the WhiteNoise middleware **right below** `SecurityMiddleware` and **above** `SessionMiddleware` as shown:

```bash
  'whitenoise.middleware.WhiteNoiseMiddleware',
```

-  Under the TEMPLATES configuration, at the DIRS key, add this path to let Django and WhiteNoise locate React’s index.html during deployment:


```bash
os.path.join(BASE_DIR, 'staticfiles', 'build')
```

- Finally, in the static files section, define both STATIC_ROOT and WHITENOISE_ROOT to point Django and WhiteNoise to the appropriate locations for the Admin static files and React static assets:

```bash
STATIC_ROOT = BASE_DIR / 'staticfiles'
WHITENOISE_ROOT = BASE_DIR / 'staticfiles' / 'build'
```

---

### Configuring the Route to Serve the React Front-End

- To serve the React frontend at the root URL, we'll configure Django to load the React app instead of the default DRF interface. All 404s will redirect to React for client-side routing with `react-router-dom`.

- We'll also prefix all API routes with `/api/` to avoid conflicts between React and DRF routes.

⸻

### Editing `urls.py` in Your Django Rest Framework Project

- Delete the import of the `root_route` view from the `.views` imports.

- Add an import for `TemplateView` from Django’s generic views with the following line:

```bash
  from django.views.generic import TemplateView
  ```

- Inside the `urlpatterns` list, remove the existing `root_route` entry and substitute it with a `TemplateView` that delivers the React `index.html` file:

```bash
  path('', TemplateView.as_view(template_name='index.html')),
```

- At the end of the file, include a 404 error handler so that React can manage routing when a page isn’t found:

```bash
  handler404 = TemplateView.as_view(template_name='index.html')
  ```
- Add the prefix api/ to all API URL patterns, excluding the homepage and admin panel routes:

---

### Updating `axiosDefaults.js`

Because the API base URL has been modified, you need to update all API calls in the React application to start with `/api`. 

Open `axiosDefaults.js`, locate the line that sets `axios.defaults.baseURL`, uncomment it, and set its value to:

```bash
axios.defaults.baseURL = "/api"
```
---

### Gathering Static Files

Run the following command in your terminal to collect static assets from both the Django Admin and DRF into the `staticfiles` folder you created earlier:

```bash
python3 manage.py collectstatic
```
---

### Build and Transfer React Files

1. Open a new terminal window and change directory to the React front-end folder by running:

```bash
   cd frontend
   ```
---

### Compile the React App and Move Files

- If you're using PowerShell in the VS Code Terminal, start by running:

```bash
  npm run build

- Once the build process finishes, transfer the compiled files to the `staticfiles` directory with:

```bash
mv build ../staticfiles/
```

- For other terminal environments, you can run this combined command:

```bash
npm run build && mv build ../staticfiles/.
```
---

### Updating Static Files During Deployment

Whenever you want to deploy changes to your static assets (including updates to the React app), you need to rebuild and replace the existing files.

To remove the old build and replace it with a new one:

- **If using PowerShell**, run these commands one by one, making sure each finishes before starting the next:

```bash
  npm run build
  rm "../staticfiles/build" -Recurse -Force
  mv build ../staticfiles/.
  ```
- For other terminals, use this one-liner command:

```bash
  npm run build && rm -rf ../staticfiles/build && mv build ../staticfiles/
  ```


---

### Adding a `runtime.txt` File

This file tells Heroku which Python version to use when deploying your project.

1. In your project’s root directory, create a new file called `runtime.txt`.

2. Inside the `runtime.txt` file, add the following line:

```bash
python-3.12.8 
 ```

---

### Switching from `psycopg2-binary` to `psycopg2`

When you last ran `pip freeze` to update your `requirements.txt`, it probably included `psycopg2-binary`, which is suitable for development but not recommended for production. Before your final GitHub push for deployment, make sure to replace it with the production-ready `psycopg2`.

- Open your `requirements.txt` file and locate the line:

```bash
psycopg2-binary==2.x.x
```

- Edit this line by removing the `-binary` suffix so it becomes:

```bash 
psycopg2==2.x.x
 ```

- Now that everything is set up, let's check that both parts of the project run together on the same server port.

1. Stop any running servers by pressing **Ctrl + C** in any open terminal window.

2. Open your `env.py` file and verify that the `DEBUG` and `DEV` environment variables are commented out.


3. Launch the Django server by executing the following command in the terminal:

```bash
python3 manage.py runserver
```

4.	To verify your application is running, open the browser by Ctrl + click (Windows) or Cmd + click (MacOS) on the localhost URL displayed in the terminal.

> **Note:** The React development server must **not** be running at this stage. This step ensures that Django is properly serving the React static files.

5. After verifying everything works as expected, make sure to commit and push your changes. Your project is now prepared for deployment to Heroku.

---

### Update Heroku Config Vars for Combined Deployment

1. Log in to your Heroku account and open the dashboard for your DRF application.

2. Go to the **Settings** tab and find the **Config Vars** section.

3. Check that your application includes an `ALLOWED_HOST` key set to the URL of your combined project. Make sure to omit the `https://` prefix and remove any trailing slash `/` at the end.

4. Make sure your application includes a `CLIENT_ORIGIN` key configured with the full URL of your combined project. This time, **keep** the `https://` prefix, but **do not** add a trailing slash.

5. If you had previously configured `CLIENT_ORIGIN` for a separately deployed React frontend on Heroku, update this value to point to the URL of the unified project.

6. If there is a `CLIENT_ORIGIN_DEV` variable still present, remove it by clicking the **“X”** next to it.

7. Review all configuration values to ensure everything is properly set, including those specified in the Deployment section of the Django REST Framework module. Be sure to save, commit, and push any updates to your codebase.

8. Use the **Deploy** tab in your Heroku dashboard to launch your application.

9. **Congratulations!** Your combined app is now set up and ready for production!

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
