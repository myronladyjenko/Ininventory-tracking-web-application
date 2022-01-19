# Inventory-tracking-web-application

#### Hi, this my web application build in the framework Django. To launch my application follow thess steps:

1. Clone the repo:

    ```sh
    git clone https://github.com/myronladyjenko/Inventory-tracking-web-application.git  
    cd Inventory-tracking-web-application
    ```

2. The database is not available so to run the user would need to create postgresql database and then update the lines 80-84 in myron/settings.py

    ```sh
    DATABASES = {  
       'default': {  
          'ENGINE': '',  
          'NAME': '',  
          'USER': '',  
          'PASSWORD': '',  
          'HOST': ''  
      }
    }
    ```
3. Now, you can migrate the database and start the project
    
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```
