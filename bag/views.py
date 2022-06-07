""" bas app views """
from django.shortcuts import render


def view_bag(request):
    """ A view to returne the bag content"""
    return render(request, 'bag/bag.html')
