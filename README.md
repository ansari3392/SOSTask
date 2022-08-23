# Rest-API-OnlineShop


how to run?
1. Enter your database credentials in SOSTask/settings.py
2. Run python manage.py migrate
3. Run python manage.py runserver
 
logic of project:
- when user register for the first time, user type will be normal
- user can request several services. but each in separate request
- if user doesnt confirm request till one day. request will be cancelled(didnt complete code) 
- when user confirm request, the state changes to confirmed and user cannot change it.
- staff can change user request state to finalized or cancelled. if they want to cancel it, they must send description to send as email to users.
