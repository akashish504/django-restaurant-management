# import decouple 
# import config

SECRET_KEY = 'abc'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('MYSQL_DATABASE'),
#         'USER': config('MYSQL_USER'),
#         'PASSWORD': config('MYSQL_PASSWORD'),
#         'HOST': config('DB_HOST', '127.0.0.1'),  # Use 'db' as default from .env
#         'PORT': config('DB_PORT', '3306'),  # Use '3306' as default from .env
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurant_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',  # Set to the appropriate MySQL host
        'PORT': '3306',       # Set to the appropriate MySQL port
    }
}

# DATABASES = {  
#     'default': {  
#         'ENGINE': 'django.db.backends.mysql',  
#         'NAME': 'my_database',  
#         'USER': 'root',  
#         'PASSWORD': 'your_password',  
#         'HOST': '127.0.0.1',  
#         'PORT': '3306',  
#         'OPTIONS': {  
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
#         }  
#     }  
# }  


# ... Other settings in your Django project