from django.db import models
import secrets

class Member(models.Model):
    member_id = models.CharField(null=True, blank=True, max_length=10,verbose_name='Code ID')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.member_id} - {self.first_name}"
    
    def save(self, *args, **kwargs):
        if not self.member_id:
            while True:
                new_code = secrets.token_urlsafe(3).upper().replace('_', '')[:10]
                if not Member.objects.filter(member_id=new_code).exists():
                    self.member_id = new_code
                    break
        super().save(*args, **kwargs)
        
        
    
