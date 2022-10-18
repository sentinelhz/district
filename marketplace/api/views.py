from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.edit import CreateView
from marketplace.models import Product, Order, Category, ShippingAddress
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer,OrderProductSerializer,CartSerializer, ShippingAddressSerializer


@api_view(['GET'])
def default_product(request):
    product = Product.objects.all
    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


class HomeViewAPI(APIView):
    """
        Get various type of data for home
    """

    def get(self, request, format=None):
        product_queryset = product.objects.all()
        serializer = ProductSerializer(data=product_queryset, many=True, context={'request': request})
        serializer.is_valid()

        return Response({'products': serializer.data})


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class ProductsByCategoryListAPIView(ListAPIView):
    """
        List of Products by Category
    """
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        try:
            category_id = self.kwargs
            return self.model.objects.filter(category_id=category_id).order_by('-created_at')
        except:
            return self.model.objects.all().order_by('-created_at')


class OrderListAPIView(ListAPIView):
    """
        List of Orders
    """
    serializer_class = OrderSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class OrderRetrieveAPIView(RetrieveAPIView):
    """
        Order details view with Products
    """
    serializer_class = OrderProductSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class CategoryListAPIView(ListAPIView):
    """
        List of categories
    """
    serializer_class = CategorySerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    """
        Get Product details
    """
    serializer_class = ProductSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


# class TestimonialsAPIView(ListAPIView):
#     serializer_class = TestimonialsSerializer
#     model = serializer_class.Meta.model
#     queryset = model.objects.all()


class CartCreateAPIView(CreateAPIView):

    """
        Create Cart details
    """
    serializer_class = CartSerializer
    fields = "__all__"
    model = serializer_class.Meta.model



class CartListView(ListAPIView):

    serializer_class = CartSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


    def get_queryset(self):
        try:
            card_id = self.kwargs
            return self.model.objects.filter(card_id=card_id).order_by('-user')
        except:
            return self.model.objects.all().order_by('-user')


class ShippingListView(ListAPIView):

    serializer_class = ShippingAddressSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

class ShippingAddressCreateView(CreateAPIView):
    """ create createview API for frontend """


    serializer_class = ShippingAddressSerializer
    fields = "__all__"
    model = serializer_class.Meta.model
