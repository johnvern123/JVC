# authentication/models.py
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# This the user manager with function to create_user and create_superuser methods. Manager is used to perform query operations
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email Field is required!!!!")
        if not password:
            raise ValueError("Password is required")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_teacher = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# This is the custom user model with type attribute for differentiating user types. Default type is student
class User(AbstractBaseUser,PermissionsMixin):
    class Types(models.TextChoices):
        STUDENT = "STUDENT", "student"
        TEACHER = "TEACHER", "teacher"
    type = models.CharField(
        max_length=8, choices=Types.choices, default=Types.STUDENT)
    email = models.EmailField(unique=True, max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self) -> str:
        return str(self.email)

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        return True

    def save(self, *args, **kwargs):
        if not self.type or self.type == None:
            self.type = User.Types.STUDENT
        return super().save(*args, **kwargs)

# authentication/models.py
# Manager for student
class StudentManager(models.Manager):
    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email is Required!!")
        if not password:
            raise ValueError("Password is Required!!")
        email = email.lower()
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=User.Types.STUDENT)
        return queryset

# Student proxy model
class Student(User):
    class Meta:
        proxy = True

    objects = StudentManager()

    def save(self, *args, **kwargs):
        self.type = User.Types.STUDENT
        self.is_student = True
        super().save(*args, **kwargs)



# Manager for Teacher model
class TeacherManager(models.Manager):
    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email Required!!")
        if not password:
            raise ValueError("Password is Required!!")
        email = email.lower()
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(type=User.Types.TEACHER)
        return queryset

# Teacher proxy model
class Teacher(User):

    class Meta:
        proxy = True

    objects = TeacherManager()

    def save(self, *args, **kwargs):
        self.type = User.Types.TEACHER
        self.is_teacher = True
        self.is_staff = True
        return super().save(*args, **kwargs)
