#custom permissions

from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    map_perms={
        'GET':['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
        }
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request,view)
    # def has_permission(self, request, view):
    #     user=request.user
    #     print(user.get_all_permissions())
    #     if request.user.is_staff:
    #         if user.has_perm("products.view_product"):#parentheses me appname and view+ model name in lower case
    #             return True
    #         if user.has_perm("products.change_product"):#parentheses me appname and change+ model name in lower case
    #             return True
    #         if user.has_perm("products.add_product"):#parentheses me appname and add+ model name in lower case
    #             return True
    #         if user.has_perm("products.delete_product"):#"appname.verb_model_name"
    #             return True
    #         return False
        
    #     return False
    
    # def has_object_permission(self, request, view,obj):
    #     return obj.owner==request.user