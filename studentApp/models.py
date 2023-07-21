from django.db import models

# Create your models here.
class Student(models.Model):
    COHORTS=[
        ("FS","FullStack"),
        ("DS","DataScience"),
        ("AWS","AWS DevOps")
    ]
        

    number=models.IntegerField()
    first_name=models.CharField(max_length=30)#charfield de max lenght zorunlu 
    last_name=models.CharField(max_length=40)#charfield de max lenght zorunlu
    comment=models.TextField(null=True)
    register_date=models.DateTimeField(auto_now_add=True, null=True)
    update_date=models.DateTimeField(auto_now=True, null=True)
    is_active=models.BooleanField(default=True)
    cohort=models.CharField(max_length=3, choices=COHORTS, default="FS")
    
    

# model olusturduysan önce 
# python manage.py makemigrations
# sonra 
# python manage.py migrate
# veritabani silmek istersem delete yaptiktan sonra tekrar migrate yapmak lazim 
# yukaridaki yapida kurulum yaptiktan sonra degisiklik yaptik. 
# degisiklik yaptiktan sonra databs dosyasini sil.
# Appiin migration pycache icerisinden 0001_initial.py sil (ona ait migration fail)
# daha sonra yeniden bu komut python manage.py makemigrations
# sonradan bu komut python .\manage.py migrate
# model.py de yaptigim degisikligi database e nasil bildirmeliyim. 
# makemigrations
# migrate