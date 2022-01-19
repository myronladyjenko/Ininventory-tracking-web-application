# Inventory-tracking-web-application

#### Hi, this my web application build in the framework Django. To launch my my application follow this steps:

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
