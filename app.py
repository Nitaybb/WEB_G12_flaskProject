from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.home_page.home_page import home_page
app.register_blueprint(home_page)

## About
from pages.about.about import about
app.register_blueprint(about)

## Products
from pages.products.products import products
app.register_blueprint(products)

## Contact Us
from pages.contact_us.contact_us import contact_us
app.register_blueprint(contact_us)

## Registeration
from pages.registeration.registeration import registeration
app.register_blueprint(registeration)

## Review
from pages.reviews.reviews import reviews
app.register_blueprint(reviews)

## Login
from pages.login.login import login
app.register_blueprint(login)

## Appointment_use
from pages.appointment_use.appointment_use import appointment_use
app.register_blueprint(appointment_use)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## menu
from components.menu.menu import menu
app.register_blueprint(menu)
