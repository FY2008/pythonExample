# Generated by Django 2.0.6 on 2018-06-07 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('body', mdeditor.fields.MDTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('status', models.CharField(choices=[('d', 'part'), ('p', 'Published')], default='p', max_length=1, verbose_name='文章状态')),
                ('abstract', models.CharField(blank=True, help_text='可选项，若为空则摘取正文前54个字符。', max_length=54, null=True, verbose_name='摘要')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='article/thumbnail', verbose_name='缩略图')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('topped', models.BooleanField(default=False, verbose_name='置顶')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否已删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('name', models.CharField(max_length=50, verbose_name='名字')),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签名')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='标签名')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, default='', to='blog.Tags', verbose_name='标签'),
        ),
    ]
