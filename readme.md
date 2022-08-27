1. Setup vagrant virtual environment, then a python environment inside it and start the server that you will be hosting using a url port.

2. setting up our Database using a django  models: update profiles_api/models.py by creating multiple class using object oriented programming

First create a user database model class named userProfile which inherits from two parent classes and setup the fields,

second create a user model manager

third add custom  user profile model, manage and migrations which  will create all the models and dependencies in our database

3. Create  superuser  with a django CLI , now
we will setup models in profiles_api/admin.py and now we can access our database on the local server and access the admin section created

4. Creating our own APIView.
an_apiview = [
    "Uses HTTP methods as function (get, post, put, patch, delete)",
    "Is similar to a traditional django view",
    "Gives us most control over our application logic",
    "is mapped manually to urls"

    ]

add get method, post, put....

5. creating viewsets used to work with our database with api's

===================================

6. create profiles API
- create profile viewset and link it with a url router.....now we can retrieve info  on anyone in the database or add new entry or patch it and so on

- but anyone can update anyone elses info so  we add  permissions.py file which prevents that behaviour.

- add filters in permissions.py to search by name or email.


================

7. add authtokens for user to pass in their headers when making api requests

===================

8. now we create a profile feed api and repeat the previous steps of creating a model , setting up serializers, setting a viewset class, add the viewset to router in urls.py and test it

9. adding a new  class in permissions.py to see if the user is updating their own status
