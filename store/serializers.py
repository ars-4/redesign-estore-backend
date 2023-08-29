from rest_framework import serializers
from .models import Person,  Images, ListField, FrequentlyAskedQuestions, Category, Badge, Product, CartProduct, Cart, Order
from rest_framework.authtoken.models import Token
from .utils import get_or_create_token


class PersonSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Person
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ListFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListField
        fields = '__all__'

class FrequentlyAskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)
    category = CategorySerializer(many=True)
    bundle = ListFieldSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model = CartProduct
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    cart_products = CartProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(many=False)
    class Meta:
        model = Order
        fields = '__all__'
