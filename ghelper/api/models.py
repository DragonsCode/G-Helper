from django.db import models

from .gesture import gesture

def frameFile(instance, filename):
    return '/'.join( ['frames', str(instance.id), filename] )

class Frame(models.Model):
    image = models.ImageField(upload_to=frameFile)
    result = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Call the original save method to save the image first
        super().save(*args, **kwargs)
        
        # Process the image and get the result
        result = gesture(self.image.path)
        
        # Update the result field with the processed result
        self.result = result[0] if result else 'No gesture detected'
        
        # Save the instance again with the updated result
        self.save()