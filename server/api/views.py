from django.shortcuts import render
from . models import Category
from . serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def get_values(request):
    category = Category.objects.all()
    srlzr = CategorySerializer(category, many=True)
    print(category)
    return Response(srlzr.data)

@api_view(["POST"])
def set_values(request):
    srlzr = CategorySerializer(data=request.data)
    if srlzr.is_valid():
        srlzr.save()
        srlzr.instance.ar_no = srlzr.instance.id + 2  # Assign ar_no as id + 2
        srlzr.instance.save()

        #ar_category area abnormality nature_of_abnormality affected_item

        print(srlzr.data)

        return Response(srlzr.data, status=status.HTTP_201_CREATED)
    else:
        return Response(srlzr.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
def delete_value(request, pk):
    try:
        data = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    data.delete()
    return Response({"Message": "Item deleted Succesfully"}, status=status.HTTP_204_NO_CONTENT)