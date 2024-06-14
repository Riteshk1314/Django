from rest_framework import serializers
from .models import carlist,showroomlist



class carserializer(serializers.ModelSerializer):
    # id=serializers.IntegerField(read_only=True)
    # name=serializers.CharField()
    # description=serializers.CharField()
    # active=serializers.BooleanField(read_only=True)
    # chasisnum=serializers.CharField(validators=[alphanumeric])
    # price=serializers.DecimalField(max_digits=9,decimal_places=2)
    
    
    # def create(self,validated_data):
    #     return carlist.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.chasisnum = validated_data.get('chasisnum', instance.chasisnum)
    #     instance.price= validated_data.get('price', instance.price)
    #     instance.save() 
    #     return instance 
    discounted_price=serializers.SerializerMethodField()
    
    class Meta:
        model=carlist
        fields="__all__"
    def get_discounted_price(self,object):
        discountprice=object.price-5000
        return discountprice
    
    
    
    def validate_price(self, value):#this is for field level validator 
        if value <=20000:
            raise serializers.ValidationError("price is too low ")
        return value
    
    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError('name and description must be different ')
        return data
    
    
class showroomserializer(serializers.ModelSerializer):
    showrooms=carserializer(many=True, read_only=True)
    class Meta:
        model = showroomlist
        fields ="__all__"

