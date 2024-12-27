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
    for cat in category:
        ar_category = cat.ar_category
        area = cat.area
        abnormality = cat.abnormality
        nature_of_abnormality = cat.nature_of_abnormality
        affected_item = cat.affected_item
        print(f"ar_category: {ar_category}, area: {area}, abnormality: {abnormality}, nature_of_abnormality: {nature_of_abnormality}, affected_item: {affected_item}")
    return Response(srlzr.data)

@api_view(["POST"])
def set_values(request):
    srlzr = CategorySerializer(data=request.data)
    if srlzr.is_valid():
        srlzr.save()
        srlzr.instance.ar_no = srlzr.instance.id + 2  # Assign ar_no as id + 2
        srlzr.instance.link = f"{srlzr.instance.id}"
        srlzr.instance.save()

        # ar_category area abnormality nature_of_abnormality affected_item

        for cat in Category.objects.all():
            print(cat.ar_category, cat.area, cat.abnormality, cat.nature_of_abnormality)

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