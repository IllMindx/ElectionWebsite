from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=60)
    number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name

class AccountManager(BaseUserManager):
	def create_user(self, card_id, name, email, password=None):
		if not card_id:
			raise ValueError('Users must have a card id')
		if not name:
			raise ValueError('Users must have a name')
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
            card_id=card_id,
            name= name,
			email=self.normalize_email(email)
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, card_id, name, email, password):
		user = self.create_user(
            name=name,
			email=self.normalize_email(email),
			password=password,
			card_id=card_id
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=60)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, default='')
    card_id = models.PositiveIntegerField(unique=True)
    password = models.CharField(max_length=60)
    candidate_voted = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True)
    date_joined	= models.DateTimeField(verbose_name='date joined', default=timezone.now())
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'card_id'
    REQUIRED_FIELDS = ['name', 'email']

    objects = AccountManager()

    def __str__(self):
        return self.name

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
