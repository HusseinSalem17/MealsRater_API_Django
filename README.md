# MealsRater_APi_Django

# Buisiness requirements as per the mockup

1- Meals list screen has the following information
- Meal name
- Meal number of stars
- Meals average rate
- Login
- Register
- Showing already logged in user

2- Popup error if the user already rated

3- Add rate screen, stars from 1 to 5 only and save

# Technical requirements
Using Django Rest framework please implement the following:

1- Models
- Meals
- Stars
- User

2- Validation if the user already rated the meal

3- validation to rate min 1 and max 5

4- CRUD API for Meals
    https://127.0.0.1:8000/api/meals
    it should return the averae rating and number of rating a long with the meal name and detail

5- CRUD API for Stars
    https://127.0.0.1:8000/api/stars
    no one should be able to use this crud for rating !!

6- Rate API
    https://127.0.0.1:8000/api/meals/meal_pk/rate_meal
    create and upadte API

7- Token authentication 

8- Login and register API

9- Token request API

10- Deploy to Heroku