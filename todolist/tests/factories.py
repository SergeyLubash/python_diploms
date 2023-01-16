import factory

from django.contrib.auth import get_user_model

from goals.models import GoalCategory, Board, BoardParticipant, Goal


USER_MODEL = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = USER_MODEL
    username = factory.Faker('name')
    email = factory.Faker('email')
    password = 'qazxsw23'


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker('name')


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    title = factory.Faker('name')


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = factory.Faker('name')