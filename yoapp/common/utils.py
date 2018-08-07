# class DisableCSRF(object):
#     def process_request(self, request):
#         setattr(request, '_dont_enforce_csrf_checks', True)

ROLES = (
    ('ADMIN', 'ADMIN'),
    ('CUSTOMER', 'CUSTOMER'),
    ('OWNER', 'OWNER'),
    ('MANAGER', 'MANAGER'),
)

DEFAULT_USER_ROLE = 'CUSTOMER'