from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

from fetch_html.constants import *
from fetch_html.libs.fetch_html_page import fetch_html_page
from fetch_html.services import check_for_url_email


class FetchHTMLContentAPI(APIView):

    def post(self, request):
        try:
            url, email, data = check_for_url_email(request.data)

            if not (url and email):
                return Response(URLS_EMAILS_FOUND, status=HTTP_412_PRECONDITION_FAILED)
            if not url:
                return Response(URLS_NOT_FOUND, status=HTTP_412_PRECONDITION_FAILED)
            if not email:
                return Response(EMAILS_NOT_FOUND, status=HTTP_412_PRECONDITION_FAILED)

            fetch_html_page.apply_async(kwargs=data)

            return Response(SUCCESS_MSG, status=HTTP_200_OK)
        except:
            return Response(ERROR_MSG, status=HTTP_400_BAD_REQUEST)
