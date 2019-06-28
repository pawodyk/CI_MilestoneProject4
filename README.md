# Milestone Project 4 - ***Unicorn Attractor Games***

[![Build Status](https://travis-ci.org/pwodyk/CI_MilestoneProject4.svg?branch=master)](https://travis-ci.org/pwodyk/CI_MilestoneProject4)

The **Unicorn Attractor Games** is a full stack web page for small indie game studio, with very intresting bussiness model. The games are free to play but the Users can donate to the studio with request for the new features. All the features are stored and evaluated by the team but only the top paid one will receive guaranteed 50% of development time.

The site uses the Django framework, and the most of the operations are evaluated in the back-end, with exception of the dashboard charts that are rendered using `dc.js`, `crossfilter` and `d3.js` libraries

**Note 1** The Game in the *Games* is called a ***Brick Breaker*** and was developed by me for a Unity course I was doing 3 years ago on Udemy. The game was added to the project for demonstrational purposes only, it is far from finished and has only 2 levels. It was compiled for resolution 800x600 and it is in this resolution that it is displayed on the site, hence it is not optimized for smaller screens. Since the game is only for demonstrational purposes only I decided not to recompile it and extra configurations to fit smaller screens.

**Note 2** The stripe payment option is active. please do not use real credit card information, for testing please use one of the [test creadit card](https://stripe.com/docs/testing) numbers provided by Stripe.

### Status: [DEPLOYED on *heroku*](https://ci-milestone-project-4.herokuapp.com/)

<hr>

## UX

I designed the page to have clear contrast between dark and light elements. The buttons use other colors to stand out and encourage the user to click them and engage with the website. The site is minimalistic and clear. The menu bar has a logo on the left and menu items on the right. Each menu item is pointing to the distinct section of the website and provide clear division between page sections. The login button stand out with green outline and the encourage user to login. When the user loges in the button change to the drop down menu with options available only to logged in user like user profile. On top of the menu the user sees the welcome message with their username. 

The dashboard page provides the three most important stats regarding tickets and the user contributions. It uses default color scheme of the `dc.js` library as it nicely compose with the rest of the website. 

The Issue Tracker displays to column design on the desktop computers to utilize the larger screen space. While on smaller screens and smartphones the tickets are placed in rows.
The Ticket design is clear and informational, providing all the most important information at the first glance.

### Responsive design

The Website utilize the bootstrap rows and columns to fit every screen size. On most pages I decided to use two layouts one for desktops (≥992px) and one for smaller screens.

The Games page is optimized as well with bootstrap however the game has been compiled in Unity3d for the resolution of 800x600 and it cause the menu in game to stay in its native resolution even though the game once started resize with the screen. This cause the menu buttons to be unaccessible on the smaller screens.

### User Stories 

1. I want to find some new game to play, but I want it to be free to play.
    - The games are free to play and are accessible without requirement to login
    - The links to games are located directly on the front page and are also accessible from every page via navbar.
    - The user can read about new features and bugs on the issue tracker page.
    - Once the user create the account they can report any bug for free and any feature with any donation amount.

2. I want to have a impact on the game development of my favorite games.
    - The User can support the games by donation after they request the new feature.
    - The User can report bugs from the issue tracker page, or their profile page.
    - The user can also support the tickets already submitted.
    - user can see progress and status of every ticket directly from the ticket tracker page.
    - user can track tickets they submitted from their profile.

3. I want to support indie game developers.
    - User can donate with every requested feature.
    - User can contribute to every existing feature request.

## Features

### Existing Features

#### Features available to all visitors

- **Feature 1** - Page is dynamically created using django templates and data from Postgres Database.

- **Feature 2** - User can view all the currently developed games on the games page without an Account.

- **Feature 3** - The Dashboard allows user to view the current amount of tickets by different types and statuses, financial company state (in the form of Contributions per day).

- **Feature 4** - The issue tracker allows users to view all the currently submitted tickets, view their status and track their progress.

#### Features available to registered users

- **Feature 5** - Issue tracker also gives users ability to submit tickets for reporting bugs or requesting features.

- **Feature 6** - User can make donation when they submit the request for new feature or they contribute to the already existing ticket. The payment are not caped to encourage small donations as well, however more donations make the ticket team priority and ensures quicker implementation. The Payemnts are done with Stripe.

- **Feature 7** - User Profile allows users to track their tickets.

- **Feature 8** - Users can edit tickets they submitted.


### Features Left to Implement

- Games may need to be moved to new pages to prevent them from loading all at once or the unity loader script may need to be modified.

- The tickets may need to be divided into groups based on the game they are supporting or even the request for new games may be inclement in the future.

- Comments section under the ticket would allow user to comment the features and increase user engagement.

- The tickets may need to be blocked from editing when they are for example in progress or completed, alternatively some version of ticket versioning may need to be implemented in the future showing previous ticket versions.

- Some kind of Staff version of issue tracker can be implemented. Ensuring data coherence, for example automate progress to change to 100% when status is set to Completed.

<hr>

## Technologies Used

- [Python 3](https://www.python.org/) 
    The program was developed with Python 3.4.3 and deployed version on Heroku runs on python 3.6.8

- [Django](https://www.djangoproject.com/)
    
    This Page was made with Django framework, utilizing its functionality and templating capabilities

- [Heroku Postgres](https://www.heroku.com/postgres)

    Used to store data

- [Heroku](https://www.heroku.com/home)
    
    Used for deployment

- [Travis](https://travis-ci.org)

    Used for build testing

- HTML5 & CSS3
    
    Backbone of the website

- [Bootstrap 4.3](https://getbootstrap.com/) 

    Used for styling the website, and to provide some functionality to the website like dropdown menus and navigation bar.

- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    
    Used with dc.js to display dashboard graphs

<hr>

## Testing

### Automated Tests

The testing was done via django TestCase class functionality and with the use of Python unittests

The coverage was tested using python coverage package. Almost all apps had 100% coverage and overall coverage of the whole site was [95%](https://pwodyk.github.io/CI_MilestoneProject4_htmlcov/)

During development I used:

```
coverage run --source="." --omit="env.py","manage.py","UnicornAttractor/*"  manage.py test 
coverage html --skip-covered
```

to extract only the apps that I needed to test and to ensure the env.py file with environmental variables has not been compromised in tests.

The final results

[Coverage results in html format](https://pwodyk.github.io/CI_MilestoneProject4_htmlcov/)

Test results and coverage report from console

```
~/workspace (master) $ coverage run --source="." --omit="env.py"  manage.py test 
Database URL not found. Using SQLite instead
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
../usr/local/lib/python3.4/dist-packages/whitenoise/base.py:104: UserWarning: No directory at: /home/ubuntu/workspace/staticfiles/
  warnings.warn(u'No directory at: {}'.format(root))
..................................................
----------------------------------------------------------------------
Ran 52 tests in 3.307s

OK
Destroying test database for alias 'default'...
~/workspace (master) $ coverage html
~/workspace (master) $ coverage report
Name                                                  Stmts   Miss  Cover
-------------------------------------------------------------------------
UnicornAttractor/__init__.py                              0      0   100%
UnicornAttractor/settings.py                             37      6    84%
UnicornAttractor/urls.py                                 10      0   100%
UnicornAttractor/wsgi.py                                  4      4     0%
checkout/__init__.py                                      0      0   100%
checkout/admin.py                                         3      0   100%
checkout/apps.py                                          3      0   100%
checkout/forms.py                                        16      0   100%
checkout/migrations/0001_initial.py                       7      0   100%
checkout/migrations/__init__.py                           0      0   100%
checkout/models.py                                       16      0   100%
checkout/tests.py                                        46      0   100%
checkout/urls.py                                          3      0   100%
checkout/views.py                                        45     29    36%
dashboard/__init__.py                                     0      0   100%
dashboard/admin.py                                        1      0   100%
dashboard/apps.py                                         3      0   100%
dashboard/migrations/__init__.py                          0      0   100%
dashboard/models.py                                       1      0   100%
dashboard/tests.py                                       24      0   100%
dashboard/urls.py                                         3      0   100%
dashboard/views.py                                       14      0   100%
games/__init__.py                                         0      0   100%
games/admin.py                                            1      0   100%
games/apps.py                                             3      0   100%
games/migrations/__init__.py                              0      0   100%
games/models.py                                           1      0   100%
games/tests.py                                           13      0   100%
games/urls.py                                             3      0   100%
games/views.py                                            3      0   100%
home/__init__.py                                          0      0   100%
home/admin.py                                             1      0   100%
home/apps.py                                              3      0   100%
home/migrations/__init__.py                               0      0   100%
home/models.py                                            1      0   100%
home/tests.py                                            13      0   100%
home/views.py                                             3      0   100%
issue_tracker/__init__.py                                 0      0   100%
issue_tracker/admin.py                                    3      0   100%
issue_tracker/apps.py                                     3      0   100%
issue_tracker/forms.py                                    8      0   100%
issue_tracker/migrations/0001_initial.py                  8      0   100%
issue_tracker/migrations/0002_auto_20190625_0904.py       7      0   100%
issue_tracker/migrations/0003_auto_20190625_0906.py       5      0   100%
issue_tracker/migrations/0004_auto_20190626_1537.py       5      0   100%
issue_tracker/migrations/0005_ticket_progress.py          5      0   100%
issue_tracker/migrations/0006_auto_20190628_1445.py       5      0   100%
issue_tracker/migrations/__init__.py                      0      0   100%
issue_tracker/models.py                                  17      0   100%
issue_tracker/tests.py                                  212      0   100%
issue_tracker/urls.py                                     3      0   100%
issue_tracker/views.py                                   69      0   100%
manage.py                                                13      6    54%
user_authentication/__init__.py                           0      0   100%
user_authentication/admin.py                              1      0   100%
user_authentication/apps.py                               3      0   100%
user_authentication/forms.py                             27      1    96%
user_authentication/migrations/__init__.py                0      0   100%
user_authentication/models.py                             1      0   100%
user_authentication/tests.py                             73      0   100%
user_authentication/urls.py                               4      0   100%
user_authentication/urls_pass_reset.py                    4      0   100%
user_authentication/views.py                             38      1    97%
user_profile/__init__.py                                  0      0   100%
user_profile/admin.py                                     1      0   100%
user_profile/apps.py                                      3      0   100%
user_profile/migrations/__init__.py                       0      0   100%
user_profile/models.py                                    1      0   100%
user_profile/tests.py                                    67      0   100%
user_profile/urls.py                                      3      0   100%
user_profile/views.py                                    15      0   100%
-------------------------------------------------------------------------
TOTAL                                                   885     47    95%
```

I tested only applications and did not tested any classes generated by django outside the applications I created. 

The least covered app is checkout where the views.py file has been covered by tests in 36%, however since I have done extensive tests while implementing the payent option to my app I am confident the functionality is working without any app breaking bugs.

The second not covered fully covered app was user_authentication. where I was unable to invoke the error messages, one in views.py and the other one in forms.py. However I extensively tested all the the code in those classes and all the functionality of those classes is fully working.

### Manual Tests

1. Manual testing of the responsive design of different parts of the website was tested and is working correctly.
    - The game container scaling was added during testing since I decided that it would be better if the in-game was partially invisible then the whole game screen to overflow onto the page.

2. Payments were tested during development and then after deployment to heroku I used it create some mock tickets.

3. Tested login in and registration pages.
    - They are working correctly and all the error display correctly however they are lacking styling which I forget to implement at the time of testing.

### Test Conclusion

The page has been fully tested both automatically and manually. No major bugs detected. 


<hr>

## Deployment

The app is deployed on heroku server under: https://ci-milestone-project-4.herokuapp.com/accounts/login/

### System Variables

- `DEVMODE` - allows for quick change to development functionality. Enables DEBUG and the recovery email are set to appear in the console instead of being sent to the user email.

- `SECRET_KEY` - provides encryption for cache and is required for correct functionality of Django.

- `HOST_URL` - holds the url address of the page that is added to Allowed host in django, it is required for page to be displayed.

- `DATABASE_URL` - allows connection with a database via database url. If not present will default to local sqllite database

- `EMAIL_ADDRESS` & `EMAIL_PASSWORD` - provides functionality for sending a user password recovery link.

- `STRIPE_PUBLISHABLE` & `STRIPE_SECRET` - required for stripe to work correctly.

All the variables are need for correct functionality of the website exception of `DEVMODE` and `DATABASE_URL`.

### Deployment Process

The program was deployed on Heroku server.

Steps used to deploy application to Heroku

1. create requirements.txt file
    ```
    sudo pip freeze -l > requirements.txt
    ```

2. create runtime.txt
    ```
    echo python-3.6.8 > runtime.txt
    ```

3. Create Procfile
    ```
    echo "web: gunicorn UnicornAttractor.wsgi:application" > Procfile
    ```

4. Create the application in heroku 
    ```
    heroku apps:create --region=eu <name of the application>
    ```

5. Initialize git repository, set up the remote and push master to heroku
    ```
    git init
    git remote add heroku <URL to heroku git returned in the previous step>
    git push -u heroku master
    ``` 

6. Set up server variables
    ```
    heroku config:set SECRET_KEY="<any random string representing secret key>" 
    heroku config:set HOST_URL="<your page url>" 
    heroku config:set DATABASE_URL="<link to postgres database>" 
    heroku config:set EMAIL_ADDRESS="<email address you wish to use to send the email to the user>" 
    heroku config:set EMAIL_PASSWORD="<your email password>" 
    heroku config:set STRIPE_PUBLISHABLE="<stripe api publishable key>" 
    heroku config:set STRIPE_SECRET="<stripe api secret key>"
    ```

7. run the dyno
    ```
    heroku ps:scale web=1
    ```

This steps assume that the heroku cli and git cli are installed on the machine.


### Steps for Local Deployment
    
To deploy the application locally you need to have Python 3.4.3 or higher installed on your local machine.

Download the application from GitHub on to your Computer. 

Add env.py file to the main directory. Populate the env.py file with to required System Variables using this template:

```
import os

# django enviromental varaibles

# os.environ.setdefault('DEVMODE', "1") ## not mandatory, use only for development

os.environ.setdefault('SECRET_KEY', '<secret_key>')
os.environ.setdefault('HOST_URL', '<host_address or 127.0.0.1>')

os.environ.setdefault("EMAIL_ADDRESS", "<email_address>")
os.environ.setdefault("EMAIL_PASSWORD", "<password>")

os.environ.setdefault("STRIPE_PUBLISHABLE", '<stripe_api_publishable_key>')
os.environ.setdefault("STRIPE_SECRET", '<stripe_api_secret_key>')

os.environ.setdefault('DATABASE_URL', '<link_to_postgress_database>') ## if not present will default to local sqllite database
```

Install required packages from requirements.txt file with command:
```
sudo pip install -r requirements.txt 
```

Once the required packages and their requirements are installed you need to add global variables to your system as specified in the above section System Variables.

Run the application 
```
python manage.py runserver 127.0.0.1:5000
```

Open the browser and type 127.0.0.1:5000

<hr>

## <span id="credits">Resources Used and Credits<span>

### Page Content

* Brick Breaker
    - Was made by me as part of the course [Complete C# Unity Developer 3D: Learn to Code Making Games](https://www.udemy.com/unitycourse/) @ [Udemy](https://www.udemy.com)
    - This game is not finished and was added for demonstrational purposes only.
    - All the resources used were Open Source or under Creative Commons licence.

### Images

* [Unicorn Logo](https://svgsilh.com/image/2674166.html)
    - Licence: [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en)

### Guides / Instructions / Code Samples

* [Code Institute Module: Django Authentication](https://github.com/Code-Institute-Solutions/proposed_django_authentication)
    - User Authentication and Custom Password Reset

* [Code Institute Module: Finding and Purchasing Products](https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce/tree/master/02-FindingAndPurchasingProducts/08-stripe_javascript)
    - Checkout app and stripe configuration

* [Code Institute Module: Testing in Django](https://github.com/Code-Institute-Solutions/TestingDjango)
    - Testing django

* [stackoverflow answer by @Tisho](https://stackoverflow.com/questions/11455756/django-how-to-test-if-message-is-sent#11457068)
   - Capture messages after redirect in tests
