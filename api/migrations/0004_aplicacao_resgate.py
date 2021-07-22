# Generated by Django 3.2.5 on 2021-07-22 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_ativo_modalidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resgate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_solicitacao', models.DateField(auto_now_add=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario_em_centavos', models.PositiveIntegerField()),
                ('ativo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Aplicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_solicitacao', models.DateField(auto_now_add=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario_em_centavos', models.PositiveIntegerField()),
                ('ativo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.ativo')),
            ],
        ),
    ]