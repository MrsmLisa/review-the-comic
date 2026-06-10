# [Review the comic](https://review-the-comic-ac6c1ec7e7bf.herokuapp.com)

Developer: Lisa Scott ([MrsmLisa](https://www.github.com/MrsmLisa))

project introduction

---
![screenshot](documentation/images/mock-up.png)

source: [review-the-comic amiresponsive](https://ui.dev/amiresponsive?url=https://review-the-comic-ac6c1ec7e7bf.herokuapp.com)

## UX

### The 5 Planes of UX

#### 1. Strategy
**Purpose**

 - Provide comic enthusiasts with a platform to create, manage, and share reviews of graphic novels and comics.
 - Offer users and guests an intuitive platform to explore, engage with, and contribute to comic book discussions.

**Primary User Needs**

 - Registered users need seamless tools for publishing and managing their own comic reviews.
 - Registered users need the ability to engage with other reviews through comments and likes.
 - Guests need the ability to browse and read reviews without registration.

**Business Goals**

 - Foster a dynamic comic review community with active user participation.
 - Build a sense of community through comments, likes, and shared passion for comics.
 - Ensure easy review management for both users and admins.


#### 2. Scope

**[Features](#features)** (see below)
Content Requirements

 - Review management (create, edit, delete and publish).
 - Comment system with admin moderation.
 - User account features (register, log in, log out).
 - Success and info notifications for user actions such as submitting a review or comment.
 - 404 and 500 error pages for a polished user experience.


#### 3. Structure

#### Information Architecture

**Navigation Menu:**
- Links to Home, Create Review, Sign In and Sign Up for guests, and Logout for logged in users.

**Hierarchy:**
- Comic reviews displayed prominently in a paginated grid for easy browsing.
- Clear call-to-action buttons for account creation and engagement such as commenting and liking.

**User Flow:**
1. Guest users browse comic reviews → read full reviews and see comments and likes.
2. Guest users register for an account → log in to interact with reviews.
3. Registered users create a review → review is published and visible on the homepage.
4. Registered users leave comments → comment is submitted and visible immediately.
5. Registered users like or unlike reviews → like count updates instantly.
6. Admin manages all reviews, comments and users through the Django admin panel.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

The site uses a strict black and white colour scheme inspired by classic comic book print design.

- `#000000` navbar, borders, headings, footer.
- `#FFFFFF` background, text on dark backgrounds.

The high contrast black and white palette was chosen deliberately to reflect the bold, graphic nature of comic book art. This keeps the focus firmly on the comic cover images and review content uploaded by users, allowing them to provide the colour and personality of each page.

![screenshot](documentation/coolors.png)

### Typography

- [Luckiest Guy](https://fonts.google.com/specimen/Luckiest+Guy?preview.script=Latn) was used for the primary headers and titles.
- [SN Pro](https://fonts.google.com/specimen/SN+Pro?preview.script=Latn) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used for the like/unlike button.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Blog Post | ![screenshot](documentation/wireframes/mobile-blog-post.png) | ![screenshot](documentation/wireframes/tablet-blog-post.png) | ![screenshot](documentation/wireframes/desktop-blog-post.png) |



## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As an admin | I would like to view, create, edit and delete all material | so that I have full control over the website. |
| As an admin | I would like to approve or delete comments | so that I can maintain control over user interactions. |
| As an admin | I would like to publish or unpublish any review | so that I can manage the content visible to users. |
| As a registered user | I would like to register for an account | so that I can become part of the community and engage with reviews. |
| As a registered user | I would like to log in to the site | so that I can create reviews and interact with other users. |
| As a registered user | I would like to create my own comic review | so that I can share my thoughts with other comic fans. |
| As a registered user | I would like to edit my own reviews | so that I can update or correct my content after publishing. |
| As a registered user | I would like to delete my own reviews | so that I can remove content I no longer want to share. |
| As a registered user | I would like to save a review as a draft | so that I can finish writing it later before publishing. |
| As a registered user | I would like to like and unlike reviews | so that I can show appreciation for content I enjoy. |
| As a registered user | I would like to leave a comment on a review | so that I can share my thoughts with other users. |
| As a registered user | I would like to delete my account | so that I can remove my presence from the site if I choose. |
| As a guest user | I would like to read comic reviews without registering | so that I can enjoy the content without needing to log in. |
| As a guest user | I would like to browse a paginated list of reviews | so that I can explore all the reviews on the site. |
| As a guest user | I would like to click on a review and read the full content | so that I can read the full review and see comments and likes. |
| As a guest user | I would like to see the names of commenters on reviews | so that I can get a sense of community before registering. |
| As a guest user | I would like to register for an account | so that I can participate in the community by leaving comments and likes. |
| As a user | I would like the site to be easy to navigate | so that I can find what I am looking for quickly and easily. |
| As a user | I would like the site to work on mobile and desktop | so that I can access it from any device. |
| As a user | I would like to see a 404 error page if I get lost | so that it is obvious I have stumbled upon a page that does not exist. |
| As a user | I would like to see a 500 error page if something goes wrong | so that I know the site has encountered an error and can navigate back home. |

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Funny Quote | At the top of the homepage there is a quote that changes every time the page loads. | ![screenshot](documentation/features/hero.png) |
| Blog List | The homepage displays basic information about blog posts, including image, title, author, date, and a brief excerpt. | ![screenshot](documentation/features/blog-list.png) |
| View Post | Users can view the full blog post details, including any comments. | ![screenshot](documentation/features/view-post.png) ![screenshot](documentation/features/view-post2.png) |
| Pagination | Blog posts are displayed in pages, with six posts per page. This provides better navigation for users through the post list. | ![screenshot](documentation/features/pagination.png) |
| Add Comments | Authenticated visitors can comment on blog posts. | ![screenshot](documentation/features/add-comment.png) |
| Like/Unlike | Authenticated users can like or unlike a review. | ![screenshot](documentation/features/about.png) |
| Edit and Delete Comments | Authenticated visitors can edit and delete their own comments. | ![screenshot](documentation/features/edit-comment.png)|
| Create Post | Authenticated users can create/publish blog posts, including setting a featured image using Cloudinary, all from the Django admin dashboard. | ![screenshot](documentation/features/create-post.png) |
| Update Post | Authenticated users can update/delete blog posts. | ![screenshot](documentation/features/update-post.png) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/features/messages.png) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/features/heroku.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |
| 500 | The 500 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |


### Future Features


- **Rating System**: Allow reviewers to rate comics on a scale alongside their written review, giving readers a quick visual indicator of the reviewer's opinion before reading the full content.

- **User Profile Pages**: Give registered users a dedicated profile page where they can manage their reviews, comments, and likes, as well as personalise their presence on the site.

- **Comic of the Week**: A special featured section on the homepage highlighting a standout comic each week, chosen by the admin to drive engagement and discovery.

- **Extended Review Details**: Add additional fields to the review detail page such as genre, publisher, and ISBN, giving readers more context about the comic being reviewed.

- **Email Verification**: Send a verification email upon registration to confirm user identity and improve the security and integrity of the community.

- **Member Chat**: Introduce a chat feature allowing registered members to communicate directly with each other, fostering a stronger sense of community among comic fans.

- **Post Categories and Tags**: Allow users to categorise and tag their reviews by genre, publisher, or theme, making it easier for visitors to filter and discover content based on their interests.

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |
| [![badge](https://img.shields.io/badge/Perplexity-grey?logo=perplexity&logoColor=1FB8CD)](https://www.perplexity.ai) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/favicon.io-grey?logo=fi&logoColor=209CEE)](https://favicon.io) | Generating the favicon. |
| [![badge](https://img.shields.io/badge/Claude-grey?logo=claude&logoColor=D97757)](https://claude.ai) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Whimsicle-grey?logo=wattpad&logoColor=BF65FF)](https://whimsical.com/wireframes) | Creating wireframes. |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.png)

I have used `Mermaid` to generate an interactive ERD of my project.

source:[Mermaid](https://mermaid.live/edit#pako:eNqNU01PwzAM_SuRz2Nam20dvYK4cEEILqjSFBrTRWuSyUnYYPS_k3aMsRXBcnL88d6z42yhtBIhB6RrJSoSujAsnkeHxLY7uz3KeKYku7s9uJwnZSoWYqYRGnsB1ELVPe9KOLe2JHeBpjA74x5fFa7PY_TK1326Z2uXcxH8wtIh5nHjWWmNR-P7Ajcl0qrvd3WojnU4L3xwB58UHr3SyErCaMq5-IFS1jZIZQS9sZcYDRTjSosKjzF3UuexxZvbk2FcWa2j4H-m8Xtvf0prUaib9E_eMxQ9iKpWBs98nyjspL5bp4-Piwu73T91zgpYk_LoCugn7UfQz_oq_yVvIY6hGnvKV6tlCwQDqEhJyD0FHIBGiqsar9C1V4BfYNxnaCukoGUL2sSalTBP1up9GdlQLSB_EbWLt7BqJ__1h769hEYiXdlgPOQJTzoQyLewgTyd8CHnWTLm6WWapNl0AG-QTyfD6Xg0uuTZeDrjSTJrBvDesY6GWcZTPptk4zSZjLKs-QS4ViGN)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/MrsmLisa/review-the-comic/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/MrsmLisa/review-the-comic/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues-search/MrsmLisa/review-the-comic?query=is%3Aissue%20is%3Aopen%20-label%3Abug&label=Open%20Issues&color=yellow)](https://www.github.com/MrsmLisa/review-the-comic/issues?q=is%3Aissue%20is%3Aopen%20-label%3Abug) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-search/MrsmLisa/review-the-comic?query=is%3Aissue%20is%3Aclosed%20-label%3Abug&label=Closed%20Issues&color=green)](https://www.github.com/MrsmLisa/review-the-comic/issues?q=is%3Aissue%20is%3Aclosed%20-label%3Abug) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://review-the-comic-ac6c1ec7e7bf.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)
- [.python-version](.python-version)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

The **[.python-version](.python-version)** file tells Heroku the specific version of Python to use when running your application.

- `3.12` (or similar)

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/MrsmLisa/review-the-comic).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/MrsmLisa/review-the-comic.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Ona (formerly Gitpod), you can click below to create your own workspace using this repository.

[![Open in Ona-Gitpod](https://ona.com/run-in-ona.svg)](https://gitpod.io/#https://www.github.com/MrsmLisa/review-the-comic)

**Please Note**: in order to directly open the project in Ona (Gitpod), you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/MrsmLisa/review-the-comic).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Whimsical](https://whimsical.com/) | For making wireframe |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Dev.to](https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg) | For inspiration on the like/unlike code |
| [Dev.to](https://dev.to/rishav_upadhaya/day-9-adding-edit-delete-features-to-my-blog-project-li6) | For inspiration on the edit/delete code |
| [Django documentation](https://docs.djangoproject.com/en/1.11/ref/contrib/messages/) | For my success messages |
| [Stackoverflow](https://stackoverflow.com/questions/44667161/page-moving-left-and-right-while-in-mobile-browser) | Code copied for CSS |
| [Claude](https://claude.ai/) | Help with code logic and explanations |

### Media

- Images
    - [Image Comics](https://imagecomics.com/) (Cover of Headlopper, Paper girls, I hate Faryland and News from the fallout)
    - [Sci-fi bookshop](https://www.sfbok.se/) (Cover of V for vendetta, Dungen crawler Carl, Star Wars: New republic, Watchmen, My perfectly imperfect body and Kent state: four dead in Ohio)
    - [Magnific](https://www.magnific.com/app) (Comic bubble for logo)

- Image Compression
   - [Photoshop](https://www.adobe.com/)

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- Also my tutor Marko Tot for the support during the classes and the project.
- To Jessica and Stephen Duffy Fransson and Jenny Bergman for the help with testing the website.
- And to my family, Daniel and Keegan, for the love , support and patience. 