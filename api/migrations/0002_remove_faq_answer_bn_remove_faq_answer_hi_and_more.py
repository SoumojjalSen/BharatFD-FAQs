# Generated by Django 5.1.5 on 2025-02-01 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answer_hi',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_hi',
        ),
    ]
