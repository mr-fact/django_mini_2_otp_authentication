# django_mini_2_otp_authentication

مینی ۲. یک پروژه کوچک برای احراز هویت کاربر ها با استفاده از شماره تلفن و رمز یکبار مصرف میباشد.
به صورت کلی سه سناریو برای این پروژه مطرح شده

1. ثبت نام در سایت با شماره تلفن و کد پیامک شده یکبار مصرف به تلفن شخص
2. ورود به سایت به همراه شماره تلفن و کد پیامک شده یکبار مصرف به تلفن شخص
3. ورود به سایت به وسیله شماره تلفن و رمز از قبل تعریف شده برای کاربر

همچنین میتوان در هر مرحله از وضعیت کاربر با خبر شد
1. کاربری با این شماره تلفن در سیستم وجود ندارد
2. کاربر با این شماره تلفن در سیستم رمز ثابت دارد
3. کاربر با این شماره تلفن در سیستم رمز ثابت ندارد

### ثبت نام با شماره و otp
برای ثبت نام باید دو مرحله طی شود
- ارسال شماره تفلن کاربر به سرور و دریافت پیامک otp
- ورود با شماره تلفن و otp
در این مرحله پس از تایید شماره تلفن و کد پیامکی حساب جدیدی برای کاربر ساخته شده و کاربر در همان حساب لاگین میشود
لازم به ذکر است که به کد یکبار مصرف باید با کلید password ارسال شود

### ورود با شماره و otp
برای ورود با کد پیامکی باید دو مرحله طی شود   
- ارسال شماره تفلن کاربر به سرور و دریافت پیامک otp
- ورود با شماره تلفن و otp
لازم به ذکر است که به کد یکبار مصرف باید با کلید password ارسال شود
   
### ورود با شماره و رمز عبور از قبل تعیین شده
برای ورود بااین روش تنها باید یک مرحله طی شود
- ورود با شماره تلفن و رمز عبور


## Endpoints
### check user status
 - **URL:** `/accounts/api/status/<phone_number>/`
 - **Method:** GET
 - **Response:**
   - status code **200**: User found
     - `{"password": True}` when the user has a fixed password
     - `{"password": False}` when the user does not have a fixed password
   - status code **404**: User not found

### send otp
 - **URL:** `/accounts/api/otp/<phone_number>/`
 - **Method:** GET
 - **Response:**
   - status code **200**
     - `{"details": "otp sent"}` when the OTP is sent

### login and get tokens
 - **URL:** `/accounts/api/token/`
 - **Method:** POST
 - **Body:**
   ```json
   {
      "phone_number": "09112223344",
      "password": "otp"
   }
   ```
   ```json
   {
      "phone_number": "09112223344",
      "password": "fixed password"
   }
   ```
 - **Response:**
   - status code **200**
     - access and refresh token body

### refresh token
 - **URL:** `/accounts/api/token/refresh/`
 - **Method:** POST
 - **Body:**
   ```json
   {
      "refresh": ""
   }
   ```
 - **Response:**
   - status code **200**
     - new access token body

### verify token
 - **URL:** `/accounts/api/token/verify/`
 - **Method:** POST
 - **Body:**
   ```json
   {
      "token": ""
   }
   ```
 - **Response:**
   - status code **200**: If the token is valid
