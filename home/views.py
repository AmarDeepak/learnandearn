# from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

class Home(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        context = {
            'sometext': "Hello World",
        }
        # return render(request, 'home/home.html', context)
        return Response(context)
