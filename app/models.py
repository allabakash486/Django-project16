from django.db import models

# Create your models here.
class dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=20)
    loc = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.dname + str(self.deptno)
class emp(models.Model):
    empno = models.IntegerField(primary_key=True,)
    ename = models.CharField(max_length=25,null=False)
    mgr = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)       
    job = models.CharField(max_length=25)
    comm = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    sal = models.DecimalField(max_digits=10,decimal_places=2)
    deptno = models.ForeignKey('dept',on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.ename + str(self.empno)
