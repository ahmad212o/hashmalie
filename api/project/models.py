from django.db import models

class Contractor(models.Model):
    first_name =models.CharField(max_length=30,blank=True)
    second_name=models.CharField(max_length=30,blank=True)
    phone_no=models.CharField(max_length=25,blank=True)
   
    def __str__(self):
      if not self.second_name:
          return "no name"
      return self.second_name



class Architect(models.Model):
    first_name =models.CharField(max_length=30,blank=True)
    second_name=models.CharField(max_length=30,blank=True)
    phone_no=models.CharField(max_length=25,blank=True)
    email=models.EmailField(blank=True)
    def __str__(self):
      if not self.second_name:
          return "no name"
      return self.second_name




class Address(models.Model):
    address_link=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=20,null=True)
    street=models.CharField(max_length=20,null=True)
    property_no=models.CharField(max_length=20,null=True)
    def __str__(self):
      if not self.property_no:
          return "no property number"
      return str(self.property_no)



class Owner(models.Model):
    first_name =models.CharField(max_length=30,blank=True)
    second_name=models.CharField(max_length=30,blank=True)
    phone_no=models.CharField(max_length=25,blank=True)
    email=models.EmailField(blank=True)
    def __str__(self):
      if not self.second_name:
          return "no name"
      return self.second_name

class File(models.Model):
   # project_code=models.ForeignKey(Project,related_name='file',on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20,null=True)
    file1=models.FileField(upload_to='files/',null=True,blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return str(self.name)


class Project(models.Model):
   
    property_type=models.CharField(max_length=20,null=True)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    project_code=models.CharField(max_length=20,blank=True,null=True)
    contractor=models.OneToOneField(Contractor,on_delete=models.CASCADE,null=True)
    architect=models.OneToOneField(Architect,on_delete=models.CASCADE,null=True)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    owner=models.OneToOneField(Owner,on_delete=models.CASCADE,null=True)
    file=models.ForeignKey(File,related_name='file',on_delete=models.CASCADE,null=True)
    REQUIRED_FIELDS=['property_type','project_code']
    def __str__(self):
      if not self.project_code:
          return "no project code"
      return str(self.project_code)




