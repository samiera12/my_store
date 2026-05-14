from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    ProductSerializer, OrderSerializer,
    OrderItemSerializer, RegisterSerializer, UserSerializer
)

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer


class ProductListView(generics.ListAPIView):
    serializer_class   = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Product.objects.all()
        search   = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer
    permission_classes = [permissions.AllowAny]


class OrderListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        items = request.data.get('items', [])
        if not items:
            return Response({'error': 'No items provided'}, status=status.HTTP_400_BAD_REQUEST)

        total = 0
        resolved = []

        for item in items:
            product = get_object_or_404(Product, id=item['productId'])
            qty     = int(item['quantity'])

            if product.stock_quantity < qty:
                return Response(
                    {'error': f'Insufficient stock for {product.name}'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            total += product.price * qty
            resolved.append({'product': product, 'qty': qty, 'price': product.price})

        order = Order.objects.create(user=request.user, total_price=total)

        for r in resolved:
            OrderItem.objects.create(
                order      = order,
                product    = r['product'],
                quantity   = r['qty'],
                unit_price = r['price']
            )
            r['product'].stock_quantity -= r['qty']
            r['product'].save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class   = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            return Response({
                'user':    UserSerializer(user).data,
                'refresh': str(refresh),
                'access':  str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)