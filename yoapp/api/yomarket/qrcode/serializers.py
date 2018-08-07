
from django.utils import timezone
import uuid
from yomarket.models import QRcoupon
from api.yomarket.offer.serializers import OfferSerializer
from rest_framework import serializers

class QRcouponSerializator(serializers.ModelSerializer):
    offer=OfferSerializer()

    def validate_expiry_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Coupon is expiried. ")
        return value
    def validate_available(self, attrs):
        pass

    def create(self,user,offer):
        f_uuid=uuid.uuid4()
        s_uuid=str(f_uuid)[:8]
        qrcoupon=self.Meta.model(uuid=f_uuid,short_uuid=s_uuid,expiry_date=timezone.now(),user=user,offer=offer)
        qrcoupon.save()

        return qrcoupon

    class Meta:
        model=QRcoupon
        fields=('short_uuid','uuid','offer','available')
