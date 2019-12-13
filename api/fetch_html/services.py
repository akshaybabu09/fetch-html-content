import os
import tempfile
from zipfile import ZipFile

from django.core.mail import EmailMessage

from api.settings import EMAIL_HOST_USER
from fetch_html.constants import *


def check_for_url_email(data):
    urls = data.get('urls')
    emails = data.get('emails')
    if urls and emails:
        return True, True, {"urls": urls, "emails": emails}
    elif not urls:
        return False, True, None
    else:
        return True, False, None


def compress_html_pages(file_names):
    dst_zip_name = ZIP_FILE_NAME
    dst_zip_path = os.path.join(tempfile.gettempdir(), dst_zip_name)
    zipobj = ZipFile(dst_zip_path, 'w')
    for file_name in file_names:
        zipobj.write(file_name)
    zipobj.close()
    return dst_zip_path


def email_with_attachment(attachment_file, receiver_mails):
    email = EmailMessage(
        subject=MAIL_SUBJECT,
        body=MAIL_BODY,
        from_email=EMAIL_HOST_USER,
        to=receiver_mails
    )
    email.attach_file(attachment_file)
    email.send()
