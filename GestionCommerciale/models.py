from django.db import models

class ModePaiement (models.Model):
    mode=models.CharField(null=False,blank=True,max_length=50,unique=True)
    is_visible=models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.mode = self.mode.lower()  # convertir en minuscule
        super(ModePaiement, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.supprimer= not self.supprimer
        super(ModePaiement, self).save(*args, **kwargs)


    def __str__(self):
        return  self.mode

class Commande(models.Model):
    code_commande=models.CharField(primary_key=True,max_length=100)
    duree=models.PositiveIntegerField(null=False)
    mode_paiement=models.ForeignKey(ModePaiement,on_delete=models.CASCADE)

