from veterinary_medicine.models import VeterinaryMadicine
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from poultry_products.serializers import (
    GovernorateSerializer,
 
)
from rest_framework.permissions import AllowAny

from veterinary_medicine.serializers import VeterinaryMadicineSerializer


class CreateView(APIView):
    """
    create.
    """

    def post(self, request, format=None):
        request.data["creator"] = request.user.id
        serializer = VeterinaryMadicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Successfully Created", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "message": str(failure_error(serializer.errors)),
                "data": None,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class DetailView(APIView):
    """ """

    permission_classes = (AllowAny,)

    def get(self, request, id, format=None):
        try:
            product_feed = VeterinaryMadicine.objects.get(id=id)
        except:
            return Response(
                {
                    "success": False,
                    "message": "id not found",
                    "data": None,
                    "errors": "id not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = VeterinaryMadicineSerializer(product_feed)

        return Response(
            {"success": True, "message": "data retrieved", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


class ListView(generics.ListAPIView):
    """
    List all.
    """

    permission_classes = (AllowAny,)
    serializer_class = VeterinaryMadicineSerializer
    # filter_backends = (DjangoFilterBackend,filters.SearchFilter)  # SearchFilter
    # filter_fields = ("product_name",)
    
    # search_fields = ('product_name',)

    def get_queryset(self):

        products = VeterinaryMadicine.objects.filter()
        return products

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
        except Exception as e:
            errors = []
            for x in e.detail.keys():
                errors.append(x)

            return Response(
                {
                    "success": False,
                    "message": e.detail.get(errors[0])[0],
                    "data": None,
                    "errors": str(e),
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.request.query_params.get("page")
        try:
            if page is None:
                page = 1
            paginate_queryset = self.paginate_queryset(queryset)
            serializer = self.serializer_class(paginate_queryset, many=True)
            tmp = serializer.data
            response = self.get_paginated_response(tmp)
            response.data["success"] = True
            response.data["message"] = "data retrieved"
            response.data["data"] = response.data["results"]
            del response.data["results"]
            return Response(data=response.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {
                    "success": False,
                    "message": "invalid page ",
                    "data": None,
                    "errors": None,
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class UpdateView(APIView):
    """ """

    def put(self, request, id, format=None):
        try:
            product_feed = VeterinaryMadicine.objects.get(id=id)
        except:
            return Response(
                {
                    "success": False,
                    "message": "id not found",
                    "data": None,
                    "errors": "id not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = VeterinaryMadicineSerializer(product_feed, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "Updated Successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "success": False,
                    "message": str(failure_error(serializer.errors)),
                    "data": None,
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


def failure_error(ordered_errors):
    errors = []
    for x in ordered_errors.keys():
        errors.append(x)
    return ordered_errors.get(errors[0])[0]


class DeleteView(APIView):
    """ """

    def delete(self, request, id, format=None):
        try:
            product_feed = VeterinaryMadicine.objects.get(id=id)
        except:
            return Response(
                {
                    "success": False,
                    "message": "id not found",
                    "data": None,
                    "errors": "id not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        product_feed.delete()
        return Response(
            {
                "success": True,
                "message": "Deleted Successfully",
                "data": [],
            },
            status=status.HTTP_204_NO_CONTENT,
        )
