import os
import tempfile
import urllib.request

from api.celery_settings import celery_app
from fetch_html.constants import *
from fetch_html.services import compress_html_pages, email_with_attachment


@celery_app.task
def fetch_html_page(**kwargs):
    urls = kwargs.get('urls')
    emails = kwargs.get('emails')
    file_names = []
    for url in urls:
        response = urllib.request.urlopen(url)
        content = response.read()
        dst_file_name = url.strip().split('.')[1] + HTML_EXTN
        dst_file_path = os.path.join(tempfile.gettempdir(), dst_file_name)
        f = open(dst_file_path, 'w')
        f.write(str(content))

        file_names.append(f.name)
        f.close()

    dst_zip_path = compress_html_pages(file_names)
    email_with_attachment(dst_zip_path, emails)
    os.remove(dst_zip_path)
    for file_name in file_names:
        os.remove(file_name)
