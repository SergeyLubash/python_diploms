# Generated by Django 4.0.1 on 2023-01-12 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалена')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
            ],
            options={
                'verbose_name': 'Доска',
                'verbose_name_plural': 'Доски',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'К выполнению'), (2, 'В процессе'), (3, 'Выполнено'), (4, 'Архив')], default=1, verbose_name='Статус')),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Низкий'), (2, 'Средний'), (3, 'Высокий'), (4, 'Критический')], default=2, verbose_name='Приоритет')),
                ('due_date', models.DateField(verbose_name='Дата выполнения')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
            ],
        ),
        migrations.CreateModel(
            name='GoalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='goals.goal', verbose_name='Цель')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='GoalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалена')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='goals.board', verbose_name='Доска')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.AddField(
            model_name='goal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='goals.goalcategory', verbose_name='категория'),
        ),
        migrations.AddField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.CreateModel(
            name='BoardParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Владелец'), (2, 'Редактор'), (3, 'Читатель')], default=1, verbose_name='Роль')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to='goals.board', verbose_name='Доска')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
                'unique_together': {('board', 'user')},
            },
        ),
    ]
