# EVO_web
### test task for EVO Python Lab 2022 by Mykhailo Pidlisnyi

On **Home page** there is a registration form 
Enter yor name an password to get to **Hello page**
If such username already exists you'll still be take to **Hello page** but another message will be displayed

**All visitors page** shows usernames of all visitors that signed up

To delete users from list you'll need to go to **admin page** 
To get to **admin page** add  `/admin` to **home page** url

**To enter _admin page_ you'll need to create _superuser_**
Create supeuser by running `py manage.py createsuperuser` in terminal
*You need to be in project's root directory where `manage.py` is located* 