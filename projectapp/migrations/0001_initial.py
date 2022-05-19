# Generated by Django 2.1.15 on 2022-05-19 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminmodel',
            fields=[
                ('ID', models.CharField(db_column='ID', max_length=9, primary_key=True, serialize=False)),
                ('firstname', models.TextField(db_column='firstname')),
                ('lastname', models.TextField(db_column='lastname')),
                ('password', models.CharField(db_column='password', max_length=10)),
                ('messagesent', models.TextField(db_column='messagesent')),
            ],
            options={
                'db_table': 'admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='cartModel',
            fields=[
                ('CID', models.CharField(db_column='CID', max_length=9, primary_key=True, serialize=False)),
                ('MIDS', models.CharField(db_column='MIDS', max_length=50)),
                ('totalprice', models.IntegerField(db_column='totalprice')),
                ('name', models.TextField(db_column='name')),
            ],
            options={
                'db_table': 'customercart',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DoctorModel',
            fields=[
                ('ID', models.CharField(db_column='ID', max_length=9, primary_key=True, serialize=False)),
                ('firstname', models.TextField(db_column='firstname')),
                ('lastname', models.TextField(db_column='lastname')),
                ('password', models.CharField(db_column='password', max_length=10)),
                ('workdays', models.TextField(db_column='workday')),
                ('adminmess', models.TextField(db_column='adminmess')),
                ('adminanswer', models.TextField(db_column='adminanswer')),
                ('speciality', models.TextField(db_column='speciality')),
            ],
            options={
                'db_table': 'doctor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedsModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='name')),
                ('description', models.TextField(db_column='description')),
                ('price', models.FloatField(db_column='price')),
                ('reason', models.TextField(db_column='reason')),
                ('type', models.TextField(db_column='type')),
                ('estock', models.IntegerField(db_column='estock')),
                ('pstock', models.IntegerField(db_column='pstock')),
            ],
            options={
                'db_table': 'meds',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('ID', models.CharField(db_column='ID', max_length=9, primary_key=True, serialize=False)),
                ('message', models.TextField(db_column='message')),
            ],
            options={
                'db_table': 'generalmessage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='newcustomerModel',
            fields=[
                ('firstname', models.TextField(db_column='firstname')),
                ('lastname', models.TextField(db_column='lastname')),
                ('email', models.TextField(db_column='email')),
                ('phone', models.CharField(db_column='phone', max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'newcustomer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('ID', models.CharField(db_column='ID', max_length=9, primary_key=True, serialize=False)),
                ('firstname', models.TextField(db_column='firstname')),
                ('lastname', models.TextField(db_column='lastname')),
                ('password', models.CharField(db_column='password', max_length=10)),
                ('messagesent', models.TextField(db_column='messagesent')),
                ('doctoranswer', models.TextField(db_column='doctoranswer')),
                ('DID', models.CharField(db_column='DID', max_length=9)),
                ('medicalrecord', models.TextField(db_column='medicalrecord')),
                ('privaterecord', models.TextField(db_column='privaterecord')),
                ('adminmess', models.TextField(db_column='adminmess')),
                ('adminanswer', models.TextField(db_column='adminanswer')),
                ('age', models.IntegerField(db_column='age')),
                ('poids', models.IntegerField(db_column='poids')),
                ('taille', models.IntegerField(db_column='taille')),
                ('allergies', models.TextField(db_column='allergies')),
                ('BMI', models.IntegerField(db_column='BMI')),
                ('phone', models.CharField(db_column='phone', max_length=10)),
                ('medrecom', models.TextField(db_column='medrecom')),
                ('appointement', models.TextField(db_column='appointement')),
                ('autorizations', models.TextField(db_column='autorizations')),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]
