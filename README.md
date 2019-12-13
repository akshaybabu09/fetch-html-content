# Fetch HTML Content
To Fetch HTML Page Content from URLs and mail the files in a Compressed Format.

## Problem Statement
Create an API in django rest framework which when given a list of URLs as a post request and email, downloads the URLs as HTML, zips it and sends an email with the zip file as attachment.

##### Example:
```
{
    "urls": [
        "https://www.amazon.in",
        "https://www.google.com"
    ],
    "emails": [
    	"abc@gmail.com",
    	"xyz@gmail.com"
    ]
}
```

The expected response is an email to the email id with a zip file attached The API should return a result immediately and the downloading/sending email should work in the backend.

## Setup
```
git clone https://github.com/akshaybabu09/fetch-html-content.git
cd neobankaccount
sudo apt-get update
sudo apt-get install python3.6
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Execution Flow
##### Django
```
python manage.py makemigrations
python manage.py migrate

export HOST_EMAIL='yourmail@gmail.com'
export HOST_PASSWORD='yourpassword'

python manage.py runserver
```

##### Celery - Async Task
```
export HOST_EMAIL='yourmail@gmail.com'
export HOST_PASSWORD='yourpassword'

celery -A api worker -l info
```

## Explanation
Upon receiving the request in the above format the HTML content from those URLs will be fetched and written into the files and stores in the temporary folder.
Once all the files are generated, tmp folder is compressed and shared over the mail.
