from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from yomarket.models import QRcoupon
from api.yomarket.qrcode.serializers import QRcouponSerializator
from rest_framework import status
from yomarket.models import Offer

def custom_api_response(serializer=None, content=None, metadata=None):
    if content:
        response = {'metadata': {}, 'content': content}
        return response

    if not hasattr(serializer, '_errors'):
        response = {'metadata': {}, 'content': serializer.data}
    else:
        response = {'metadata': {}, 'errors': serializer._errors}
    return response



@api_view(['GET'])
@permission_classes([AllowAny])
def qr_checkout(request,uuid):
    coupon=QRcoupon.objects.get(uuid=uuid)
    serializer=QRcouponSerializator(coupon)
    serializer.validate_expiry_date(value=coupon.expiry_date)

    response = Response(custom_api_response(serializer), status=status.HTTP_200_OK)
    coupon.available=False
    coupon.save()
    return response




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def offer_make_qr(request,offer_id):
    offer=Offer.objects.get(id=offer_id)
    serializer=QRcouponSerializator()
    serializer.create(user=request.user,offer=offer)
    return Response(status=status.HTTP_200_OK)
