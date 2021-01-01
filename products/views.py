from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
# from .serializers import *
from rest_framework import viewsets

from .forms import Product_Form

# Create your views here.
class ProductApiView(APIView):
    def get(self,request):
        products = Product.objects.all().values()
        return Response(products)

    
#     def post(self,request):
#         Product.objects.create(id=request.data["id"], name= request.data["name"], description= request.data["description"]
# )

# 18

#         book=Book.objects.all().filter(id=request.data["id"]).values()

# 19

#         return Response({"Message":"New Book Added!", "Book":book})


def create_profile(request):
    form = Product_Form()
    if request.method == 'POST':
        form = Product_Form(request.POST)
        # form = Product_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
#             user_pr.display_picture = request.FILES['display_picture']
#             file_type = user_pr.display_picture.url.split('.')[-1]
#             file_type = file_type.lower()
#             if file_type not in IMAGE_FILE_TYPES:
# return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'products/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'products/create.html', context)