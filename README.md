Step 1: Create a new folder named CoffeShop in your desktop.

Step 2: open that folder in Visual Studio Code.

Step 3: Open the terminal and create a virtual environment using 
virtualenve venv

Step 4: Creating virtual environment is followed by 
activating environment. We use ‘venv\Scripts\activate’. 
Step 5: Install Django using ‘pip install Django’. 
Step 6: After installed Django then create a project named Coffee using ‘Django-admin 
startproject Coffee'.
Step 7: Then run manage.py with code python manage.py runserver’. 
Step 8: Stop terminal with ctrl+c then create a new app named ‘base’ using code ‘python 
manage.py startapp base’. 
Step 9: Go to base folder then open ‘views.py’ create a function.
Step 10: Now, go to Coffee folder and open ‘urls.py’ then modifying it to include the ‘base’ 
app views .
Step 11: Create a templates folder and make html file.
Step 12: Go to base folder and views.py and write code for render. Now go to models.py file create a class. 
Step 13: Go to Coffee folder and open urls.py files link with base file. 
Step 14: Now go to setting.py of Coffee folder there is a thing we to edit it.In 
INSTALLED_APPS write ‘base’,.TEMPLATES write Base_DIR/’templates’
Step 15: Open terminal to run server manage.py ‘python manage.py runserver’. 





