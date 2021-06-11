from django.core import mail


class Services:
    @staticmethod
    def send_mail(subject, body, to, **kwargs):
        message = mail.EmailMessage(subject, body, to=to, **kwargs)
        message.send()
'''
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NotificationPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
'''


"""
        # for i in range(1, len(data)):
        #     for j in range(len(data[0]['full_relations'])):
        #         if data[0]['full_relations'][j]['has'] != data[i]['full_relations'][j]['has']:
        #             data[0]['full_relations'][j]['has'] = True
        # return Response(data=data[0])
"""
