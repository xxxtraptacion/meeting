# Generated by Django 2.1.7 on 2019-04-27 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='name')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('org', models.CharField(max_length=70, unique=True, verbose_name='org')),
                ('man', models.CharField(max_length=50, verbose_name='man')),
                ('theme', models.CharField(max_length=250, verbose_name='theme')),
            ],
        ),
        migrations.CreateModel(
            name='Golos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=100, verbose_name='username')),
                ('flag', models.BooleanField(default=False, verbose_name='flag')),
            ],
        ),
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazv', models.CharField(db_index=True, max_length=100, verbose_name='nazv')),
                ('duration', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RequiredPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listeners', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listeners', to='maket.Collect')),
                ('namesobr', models.ManyToManyField(to='maket.Collect')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namet', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='namet')),
                ('theme', models.CharField(db_index=True, max_length=250, verbose_name='theme')),
                ('leading', models.CharField(max_length=50, verbose_name='lead')),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Userpr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='username')),
                ('password', models.CharField(db_index=True, max_length=120, verbose_name='password')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.AddField(
            model_name='golos',
            name='timemomenst',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='maket.Moment'),
        ),
        migrations.AddField(
            model_name='collect',
            name='peopleincoll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peopleincoll', to='maket.Golos'),
        ),
    ]
