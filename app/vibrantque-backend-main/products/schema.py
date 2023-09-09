import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene.relay.node import Node
from django.db.models import Q
from products.models import (
    CustomUser,ViewerDevice,
    UserProfileDetails,
    RunnerUnitDetails,FloaterUnitDetails,CatalogDetails,ReportUpdate
 
   )

#Type
class CustomUserView(DjangoObjectType):
    class Meta:
        model=CustomUser
        filter_fields = {
            'id': ['exact', 'icontains'],
            'role': ['exact', 'icontains'], 
            'roleStatus': ['exact', 'icontains'],
            'username': ['exact', 'icontains']
        }
        interfaces = (graphene.relay.Node,)

class UserProfileDetailsView(DjangoObjectType):
    class Meta:
        model=UserProfileDetails  
        


class RunnerUnitDetailsView(DjangoObjectType):
    class Meta:
        model=RunnerUnitDetails
        filter_fields = {
           
            'deviceId': ['exact', 'icontains'], 
            'status': ['exact', 'icontains'],
            
        }
        interfaces = (graphene.relay.Node,)   

class FloaterUnitDetailsView(DjangoObjectType):
    class Meta:
        model=FloaterUnitDetails
        filter_fields = {
           
            'deviceId': ['exact', 'icontains'], 
            'status': ['exact', 'icontains'],
            
        }
        interfaces = (graphene.relay.Node,)    


class ViewerDeviceView(DjangoObjectType):
    class Meta:
        model=ViewerDevice
        filter_fields = {
           
            'deviceId': ['exact', 'icontains'], 
            'status': ['exact', 'icontains'],
            
        }
        interfaces = (graphene.relay.Node,)    

        

class CatalogDetailsView(DjangoObjectType):
    class Meta:
        model=CatalogDetails
        filter_fields = {
           
            'user_email': ['exact', 'icontains'], 
            'catalogId': ['exact', 'icontains'], 
            'status': ['exact', 'icontains'],
            
        }
        interfaces = (graphene.relay.Node,) 

class ReportUpdateView(DjangoObjectType):
    class Meta:
        model=ReportUpdate
        filter_fields = {
           
            'user_email': ['exact', 'icontains'], 
            'name': ['exact', 'icontains'], 
            'status': ['exact', 'icontains'],
            
        }
        interfaces = (graphene.relay.Node,)                                                                                                                                                                                                                                                                                                 
         
      
#Query  

class ViewerDeviceQueries(graphene.ObjectType):
    device_detail=graphene.Field(ViewerDeviceView,Id=graphene.String())

    def resolve_device_detail(self,info,Id,**kwargs):
        # _, raw_pk = Node.from_global_id(Id)
        return ViewerDevice.objects.get(deviceId=Id) 
    
class ReportUpdateQueries(graphene.ObjectType):
    report_detail=graphene.List(ReportUpdateView,Email=graphene.String())
    report_collections=graphene.List(ReportUpdateView,Email=graphene.String(),Name=graphene.String())

    def resolve_report_detail(self,info,Email,**kwargs):
        # _, raw_pk = Node.from_global_id(Id)
        return ReportUpdate.objects.filter(user_email=Email)
    
    def resolve_report_collections(self,info,Email,Name,**kwargs):
        # _, raw_pk = Node.from_global_id(Id)
        return ReportUpdate.objects.filter(user_email=Email).filter(name=Name)

class CustomUserQueries(graphene.ObjectType):
    user_details=graphene.List(CustomUserView,search=graphene.String(), first=graphene.Int(), skip=graphene.Int(),orderBy=graphene.List(of_type=graphene.String))
    user_detail=graphene.Field(CustomUserView,Id=graphene.String())
    all_users_detail=graphene.List(CustomUserView)
    
    def resolve_all_users_detail(self,info, **kwargs):
       return CustomUser.objects.all()
    
    def resolve_user_details(self, info, search=None, first=None, skip=None, *args, **kwargs):
        print("search--->",search)
        orderBy =kwargs.get('orderBy',None)
        if search  != '':
            qs = CustomUser.objects.filter(Q(username=search))
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = CustomUser.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
        else:
            qs = CustomUser.objects.all()
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = CustomUser.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
   
    def resolve_user_detail(self,info,Id,**kwargs):
        _, raw_pk = Node.from_global_id(Id)
        return CustomUser.objects.get(id=raw_pk) 


class FloaterUnitQueries(graphene.ObjectType):
    floater_details=graphene.List(FloaterUnitDetailsView,search=graphene.String(), first=graphene.Int(), skip=graphene.Int(),orderBy=graphene.List(of_type=graphene.String))
    floater_detail=graphene.Field(FloaterUnitDetailsView,Id=graphene.String())
    floater_all_Details_data=graphene.List(FloaterUnitDetailsView,status=graphene.String())

    
    def resolve_floater_all_Details_data(self,info,status, **kwargs):
       return FloaterUnitDetails.objects.filter(status=status)
    
    def resolve_floater_details(self, info, search=None, first=None, skip=None, *args, **kwargs):
        print("search--->",search)
        orderBy =kwargs.get('orderBy',None)
        if search  != '':
            qs = FloaterUnitDetails.objects.filter(Q(deviceId=search))
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = FloaterUnitDetails.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
        else:
            qs = FloaterUnitDetails.objects.all()
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = FloaterUnitDetails.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
   
    def resolve_floater_detail(self,info,Id,**kwargs):
        _, raw_pk = Node.from_global_id(Id)
        return FloaterUnitDetails.objects.get(id=raw_pk) 
    
class RunnerUnitQueries(graphene.ObjectType):
    runner_details=graphene.List(RunnerUnitDetailsView,search=graphene.String(), first=graphene.Int(), skip=graphene.Int(),orderBy=graphene.List(of_type=graphene.String))
    runner_detail=graphene.Field(RunnerUnitDetailsView,Id=graphene.String())
    runner_all_Details_data=graphene.List(RunnerUnitDetailsView,status=graphene.String())

    
    def resolve_runner_all_Details_data(self,info,status, **kwargs):
       return RunnerUnitDetails.objects.filter(status=status)
    
    def resolve_runner_details(self, info, search=None, first=None, skip=None, *args, **kwargs):
        print("search--->",search)
        orderBy =kwargs.get('orderBy',None)
        if search  != '':
            qs = RunnerUnitDetails.objects.filter(Q(deviceId=search))
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = RunnerUnitDetails.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
        else:
            qs = RunnerUnitDetails.objects.all()
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = RunnerUnitDetails.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
   
    def resolve_runner_detail(self,info,Id,**kwargs):
        _, raw_pk = Node.from_global_id(Id)
        return RunnerUnitDetails.objects.get(id=raw_pk) 
    

class CatalogDetailsQueries(graphene.ObjectType):
    catalog_details=graphene.List(CatalogDetailsView,search=graphene.String(),subsearch=graphene.String(), first=graphene.Int(), skip=graphene.Int(),orderBy=graphene.List(of_type=graphene.String))
    catalog_detail=graphene.Field(CatalogDetailsView,Id=graphene.String())
    catalog_all_Details_data=graphene.List(CatalogDetailsView,status=graphene.String(),subsearch=graphene.String())
    catalog_all_Details=graphene.List(CatalogDetailsView,subsearch=graphene.String())
    
    def resolve_catalog_all_Details_data(self,info,status,subsearch, **kwargs):
       return CatalogDetails.objects.filter(status=status).filter(user_email=subsearch)
    
    def resolve_catalog_all_Details(self,info,subsearch, **kwargs):
       return CatalogDetails.objects.filter(user_email=subsearch)
    
    def resolve_catalog_details(self, info, search=None,subsearch=None, first=None, skip=None, *args, **kwargs):
        print("search--->",search)
        orderBy =kwargs.get('orderBy',None)
        if search  != '':
            qs = CatalogDetails.objects.filter(Q(catalogId=search)).filter(Q(user_email=subsearch))
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = CatalogDetails.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
        else:
            qs = CatalogDetails.objects.filter(Q(user_email=subsearch))
            if skip:
                qs=qs[skip:]
                return qs
            if first:
                qs=qs[:first]
                return qs
            if orderBy:
                qs1 = CatalogDetails.objects.order_by(*orderBy)
                print(qs1.query)
            return qs1
   
    def resolve_catalog_detail(self,info,Id,**kwargs):
        _, raw_pk = Node.from_global_id(Id)
        return CatalogDetails.objects.get(id=raw_pk)    
       
class ProfileDetailsQueries(graphene.ObjectType):
    profileDetails_data=graphene.List(UserProfileDetailsView)
    
    def resolve_profileDetails_data(self,info):
       return UserProfileDetails.objects.all() 





class RoleUpdateQueries(graphene.ObjectType):
    role_update = graphene.List(CustomUserView)
    role_data=DjangoFilterConnectionField(CustomUserView, search=graphene.String(), orderBy=graphene.List(of_type=graphene.String),  first=graphene.Int(), skip=graphene.Int())

   
    def resolve_role_update(self,info,**kwargs):
        return CustomUser.objects.filter(role="Client") 
    
    def resolve_role_data(self, info, search=None, first=None, skip=None, *args, **kwargs):
        orderBy =kwargs.get('orderBy',None)
        qs = CustomUser.objects.filter(roleStatus=search)
        if skip:
             qs=qs[skip:]
             return qs
        if first:
             qs=qs[:first]
             return qs
        if orderBy:
            qs1 = CustomUser.objects.order_by(*orderBy)
            print(qs1.query)
            return qs1 
        if search:
            _, raw_pk = Node.from_global_id(search)
            qs2 = CustomUser.objects.filter(Q(id__icontains=raw_pk))
            print(qs2.query)
            return qs2
        return CustomUser.objects.all()      

         
#Input      


class ProfileDetailsInput(graphene.InputObjectType):
    pathName = graphene.String()
    component = graphene.String()
    fileName = graphene.String()
    imagePath = graphene.String()
    status=graphene.String()

class UsersDetailsInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()
    username = graphene.String()
    runnerId = graphene.String()
    floaterId = graphene.String() 
    role = graphene.String() 
    roleStatus = graphene.String()  

class UpdateUsersDetailsInput(graphene.InputObjectType):
    email = graphene.String()
    username = graphene.String()
    runnerId = graphene.String()
    floaterId = graphene.String() 
    role = graphene.String() 
    roleStatus = graphene.String() 

class RunnerDetailsInput(graphene.InputObjectType):
    deviceId = graphene.String()
    status=graphene.String()
   

class FloaterDetailsInput(graphene.InputObjectType):
    deviceId = graphene.String()
    status=graphene.String()     
 

class CatalogDetailsInput(graphene.InputObjectType):
    userEmail = graphene.String()
    catalogId = graphene.String()
    status=graphene.String()       
    
          
        
#Mutation 
class UserDetailsData(graphene.Mutation):
    users=graphene.Field(CustomUserView)

    class Arguments: 
        input = UsersDetailsInput(required=True)
        
        
    def mutate(self, info, input):    
        data = CustomUser.objects.create(email= input.email ,password=input.password,username= input.username,runnerId=input.runnerId,floaterId= input.floaterId,role= input.role,roleStatus=input.roleStatus)
        data.save()
        return UserDetailsData(users=data) 
    
class UpdateUserDetailsData(graphene.Mutation):
    users=graphene.Field(CustomUserView)

    class Arguments: 
        input = UpdateUsersDetailsInput(required=True)
        
        
    def mutate(self, info, input):
        print(input.role)  
        data = CustomUser.objects.get(email= input.email)
        data.runnerId=input.runnerId
        data.floaterId= input.floaterId
        data.role= input.role
        data.save()
        return UpdateUserDetailsData(users=data)     


   
class RunnerDetailsData(graphene.Mutation):
    runner=graphene.Field(RunnerUnitDetailsView)

    class Arguments: 
        input = RunnerDetailsInput(required=True)
        
    def mutate(self, info, input):    
        data = RunnerUnitDetails.objects.create(deviceId= input.deviceId ,status=input.status)
        data.save()
        return RunnerDetailsData(runner=data)  
    

class RunnerDetailsUpdate(graphene.Mutation):
    set = graphene.String()
    
    class Arguments:
        id=graphene.String()
        status=graphene.String()
        
    def mutate(self,info,id,status):
        _, raw_pk = Node.from_global_id(id)
        data = RunnerUnitDetails.objects.get(id=raw_pk)
        data.status=status
        print (data)
        data.save()
        return RunnerDetailsUpdate(set=True) 

class FloaterDetailsUpdate(graphene.Mutation):
    set = graphene.String()
    
    class Arguments:
        id=graphene.String()
        status=graphene.String()
        
    def mutate(self,info,id,status):
        _, raw_pk = Node.from_global_id(id)
        data = FloaterUnitDetails.objects.get(id=raw_pk)
        data.status=status
        print (data)
        data.save()
        return FloaterDetailsUpdate(set=True)   


class CatalogDetailsData(graphene.Mutation):
    catalog=graphene.Field(CatalogDetailsView)

    class Arguments: 
        input = CatalogDetailsInput(required=True)
        
    def mutate(self, info, input):    
        data = CatalogDetails.objects.create(user_email=input.userEmail,catalogId= input.catalogId ,status=input.status)
        data.save()
        return CatalogDetailsData(catalog=data)         
    

class CatalogDetailsUpdate(graphene.Mutation):
    set = graphene.String()
    
    class Arguments:
        id=graphene.String()
        status=graphene.String()
        
    def mutate(self,info,id,status):
        _, raw_pk = Node.from_global_id(id)
        data = CatalogDetails.objects.get(id=raw_pk)
        data.status=status
        print (data)
        data.save()
        return CatalogDetailsUpdate(set=True) 
    
class DeleteCatalogDetails(graphene.Mutation):
    set = graphene.Boolean()
    
    class Arguments:
        id=graphene.String()    
        
    def mutate(self,info,id):
        _, raw_pk = Node.from_global_id(id)
        data = CatalogDetails.objects.get(id=raw_pk)
        print (data)
        data.delete()
        return DeleteCatalogDetails(set=True)
    

class DeleteUsersDetails(graphene.Mutation):
    set = graphene.Boolean()
    
    class Arguments:
        id=graphene.String()    
        
    def mutate(self,info,id):
        _, raw_pk = Node.from_global_id(id)
        data = CustomUser.objects.get(id=raw_pk)
        print (data)
        data.delete()
        return DeleteUsersDetails(set=True)  

class DeleteRunnerDetails(graphene.Mutation):
    set = graphene.Boolean()
    
    class Arguments:
        id=graphene.String()    
        
    def mutate(self,info,id):
        _, raw_pk = Node.from_global_id(id)
        data = RunnerUnitDetails.objects.get(id=raw_pk)
        print (data)
        data.delete()
        return DeleteRunnerDetails(set=True)   


class DeleteFloaterDetails(graphene.Mutation):
    set = graphene.Boolean()
    
    class Arguments:
        id=graphene.String()    
        
    def mutate(self,info,id):
        _, raw_pk = Node.from_global_id(id)
        data = FloaterUnitDetails.objects.get(id=raw_pk)
        print (data)
        data.delete()
        return DeleteFloaterDetails(set=True)       
    
class FloaterDetailsData(graphene.Mutation):
    floater=graphene.Field(FloaterUnitDetailsView)

    class Arguments: 
        input = FloaterDetailsInput(required=True)
        
    def mutate(self, info, input):    
        data = FloaterUnitDetails.objects.create(deviceId= input.deviceId ,status=input.status)
        data.save()
        return FloaterDetailsData(floater=data)      
    
class UsersRoleStatusUpdate(graphene.Mutation):
    set = graphene.String()
    
    class Arguments:
        id=graphene.String()
        status=graphene.String()
        
    def mutate(self,info,id,status):
        _, raw_pk = Node.from_global_id(id)
        data = CustomUser.objects.get(id=raw_pk)
        data.roleStatus=status
        print (data)
        data.save()
        return UsersRoleStatusUpdate(set=True)   

class RoleUpdate(graphene.Mutation):
    set = graphene.String()
    
    class Arguments:
        id=graphene.String()
        role=graphene.String()
        
    def mutate(self,info,id,role):
        _, raw_pk = Node.from_global_id(id)
        data = CustomUser.objects.get(id=raw_pk)
        data.roleStatus=role
        print (data)
        data.save()
        return RoleUpdate(set=True)

 
 
    
          
class ProfileDetailsData(graphene.Mutation):
    profile=graphene.Field(UserProfileDetailsView)

    class Arguments: 
        input = ProfileDetailsInput(required=True)
        
    def mutate(self, info, input):    
        print("input->",input)
        data = UserProfileDetails.objects.create(pathName= input.pathName, component=input.component, fileName=input.fileName, imagePath= input.imagePath, status= input.status)
        data.save()
        return ProfileDetailsData(profile=data)
    
  
        

            
class DeleteProfileDetails(graphene.Mutation):
    set = graphene.Boolean()
    
    class Arguments:
        id=graphene.Int()    
        
    def mutate(self,info,id):
        data = UserProfileDetails.objects.get(id=id)
        print (data)
        data.delete()
        return DeleteProfileDetails(set=True)
             
class UpdateProfileDetails(graphene.Mutation):
    set = graphene.Boolean()
    
    class Arguments:
        id=graphene.Int()
        status=graphene.String()
        
    def mutate(self,info,id,status):
        data = UserProfileDetails.objects.get(id=id)
        data.status=status
        print (data)
        data.save()
        return DeleteProfileDetails(set=True)             
             
             
class UserstMutations(graphene.ObjectType):
    
 
    role_update = RoleUpdate.Field()         
    add_user_profile_details = ProfileDetailsData.Field()
    delete_user_profile_details = DeleteProfileDetails.Field()
    update_user_profile_details = UpdateProfileDetails.Field()
    createUser = UserDetailsData.Field()
    update_user_detail = UpdateUserDetailsData.Field()
    runner_re_update =RunnerDetailsUpdate.Field()
    runner_update = RunnerDetailsData.Field()
    floater_update = FloaterDetailsData.Field()
    delete_runner = DeleteRunnerDetails.Field()
    delete_floater = DeleteFloaterDetails.Field()
    delete_catalog = DeleteCatalogDetails.Field()
    delete_users = DeleteUsersDetails.Field()
    floater_re_update  = FloaterDetailsUpdate.Field()
    role_status = UsersRoleStatusUpdate.Field()
    catalog_update = CatalogDetailsData.Field()
    catalog_status_update = CatalogDetailsUpdate.Field()
   
   
   
  