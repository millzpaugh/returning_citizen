DEBUG = False
TEMPLATE_DEBUG = False

AWS_ENVIRONMENT = 'Default-Environment'

DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'returning_citizen',
        'USER': 'amillspaugh',
        'PASSWORD': 'knew1for!',
        'HOST': 'returning-citizen.c0yzerzzjkbe.us-west-2.rds.amazonaws.com',
        'PORT': 3306,
    }
}