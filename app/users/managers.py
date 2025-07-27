from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Modelo de usuário customizado onde o email é o único identificador
    para autenticação. Ele substitui o nome do usuário (username).
    """

    def create_user(self, email, password, username='', **extra_fields):
        """
        Cria e salva um usuário com o email e senha.
        """
        if not email:
            raise ValueError(_("O email deve ser definido."))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username='', **extra_fields):
        """
        Cria e salva um SuperUser com o email e senha.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser precisa ter is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser precisa ter is_superuser=True."))
        return self.create_user(email, password, username, **extra_fields)
