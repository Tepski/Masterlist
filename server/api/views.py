from . models import Category
from . serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
filterList = ["ar_no", "ar_category", "area", "abnormality", "nature_of_abnormality", "affected_item"]

# Create your views here.

def check_occurence(data, list):
    data1 = [data[i] for i in filterList]
    data2 = [[x[j] for j in filterList] for x in list]

    for item in reversed(data2[:-1]):
        if data1[1:] == item[1:]:
            print(item[0])
            if  item[0].count("-") == 1:
                new_id = f"{item[0]}-001"
                return new_id
            else:
                id_inc = str(int(item[0].split("-")[-1]) + 1)
                while len(id_inc) != 3:
                    id_inc = "0" + id_inc
                split_data = item[0].split("-")
                new_id = split_data[0] + "-" + split_data[1] + "-" +id_inc
                print("increment", id_inc, item[0])
                return new_id                
        else: return

def get_non_occurence_count(items):
    count = 0
    for item in items:
        if item['ar_no'].count("-") == 1:
            count += 1
    print(count)
    return count
        
@api_view(["GET"])
def get_values(request):
    category = Category.objects.all()
    srlzr = CategorySerializer(category, many=True)
    
    return Response(srlzr.data)

@api_view(["POST"])
def set_values(request):
    srlzr = CategorySerializer(data=request.data)
    if srlzr.is_valid():
        srlzr.save()

        count = Category.objects.all()
        count_srlz = CategorySerializer(count, many=True)
        str_count = str(get_non_occurence_count(count_srlz.data))
        while len(str_count) != 5:
            str_count = "0" + str_count
        srlzr.instance.ar_no = f"ARUTP-{str_count}"
        srlzr.instance.link = f"{srlzr.instance.id}"
        srlzr.instance.save()

        category = Category.objects.all()
        cat = CategorySerializer(category, many=True)

        reoccurrence_id = check_occurence(srlzr.data, cat.data)
        
        if reoccurrence_id:
            srlzr.instance.ar_no = f"{reoccurrence_id}"
            srlzr.instance.save()

        return Response(srlzr.data, status=status.HTTP_201_CREATED)
    else:
        return Response(srlzr.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_value(request, pk):
    try:
        data = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"message": "Error deleting, does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    data.delete()
    return Response({"Message": "Item deleted Succesfully"}, status=status.HTTP_204_NO_CONTENT)