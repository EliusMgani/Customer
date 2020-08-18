from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer


def customerprofile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='Customer')
		instance.groups.add(group)
		Customer.objects.create(
			user=instance, 
			name=instance.username
		)
		print('Profile Created')
post_save.connect(customerprofile, sender=User)