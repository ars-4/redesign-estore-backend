from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from .models import CustomUser

from .serializers import *

# Create your views here.


@api_view(["GET"])
def index(request):
    return Response({"MESSAGE": "WELCOME TO THE WEBSITE!"})


@api_view(["POST"])
def login(request):
    data = request.data
    username = data.get("username", None)
    password = data.get("password", None)

    if username is None or password is None:
        return Response(
            {"error": "Please provide both username and password"}, status=400
        )

    user = CustomUser.objects.get(email=username)

    if user.check_password(password):
        token = get_or_create_token(user)
        return Response({"token": token, "user": user.email})
    

@api_view(["POST"])
def register(request):
    data = request.data
    username = data.get("username", None)
    password = data.get("password", None)
    email = data.get("email", None)
    first_name = data.get("first_name", None)
    last_name = data.get("last_name", None)
    address = data.get("address", None)
    role = 'customer'
    for user in CustomUser.objects.all():
        if user.email == email:
            return Response({"error": "User already exists"}, status=400)
        else:
            break

    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        username=username,
        first_name=first_name,
        last_name=last_name,
    )
    user.save()
    street = address.split(',')[0]
    city = address.split(',')[1]
    country = address.split(',')[2]
    Person.objects.create(user=user, street=street, city=city, country=country, role=role, first_name=first_name, last_name=last_name, email=email)
    return Response({"user": user.email})


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self):
        data = self.request.data
        serializer = PersonSerializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=201)


class CategorySerializer(ModelViewSet):
    model = Category
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def create(self, request):
    #     data = request.data
    #     product = Product.objects.create(
    #         title=data.get('title'),
    #         description=data.get('description'),
    #         old_price=data.get('old_price'),
    #         shipping_price=data.get('shipping_price'),
    #         total_price=data.get('total_price'),
    #         commission=data.get('commission'),
    #         badge=Badge.objects.get(id=int(data.get('badge')))
    #     )
    #     for item in data.get('bundle'):
    #         ListField.objects.create(title=item, product=product)

    #     for item in data.get('images'):
    #         Images.objects.create(title=item, product=product)

    #     for item in data.get('category'):



class CartViewSet(ModelViewSet):
    model = Cart
    serializer_class = CartSerializer


class OrderViewSet(ModelViewSet):
    model = Order
    serializer_class = OrderSerializer



@api_view(["GET"])
def get_faqs(request, pk):
    product = Product.objects.get(id=pk)
    faq = FrequentlyAskedQuestions.objects.filter(model=product)
    serializer = FrequentlyAskedQuestionsSerializer(faq, many=True)
    return Response(serializer.data)
