# Generated by Django 4.1.7 on 2023-04-01 15:06

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
            name='CategoriasModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='ClientesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('dni', models.IntegerField()),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='VentasModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('observacion', models.CharField(max_length=100)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.clientesmodel')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='ProductosModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen_url', models.TextField()),
                ('precio', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.categoriasmodel')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
        migrations.CreateModel(
            name='PagosModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
                ('venta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.ventasmodel')),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
        migrations.CreateModel(
            name='DetallesVentaModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.productosmodel')),
                ('venta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacen.ventasmodel')),
            ],
            options={
                'db_table': 'detalles_venta',
            },
        ),
    ]
