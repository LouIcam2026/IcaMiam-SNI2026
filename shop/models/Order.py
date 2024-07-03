from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    email = models.EmailField()
    time_slot = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.nom} {self.prenom}"
