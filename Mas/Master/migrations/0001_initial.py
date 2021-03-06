# Generated by Django 3.0.6 on 2020-05-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dematad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DPID', models.TextField()),
                ('CLID', models.TextField()),
                ('TYPE', models.TextField()),
                ('SUBTYP', models.TextField()),
                ('ACCAT', models.TextField()),
                ('OCCUP', models.TextField()),
                ('NAME', models.TextField()),
                ('FNAME', models.TextField()),
                ('AD1', models.TextField()),
                ('AD2', models.TextField()),
                ('AD3', models.TextField()),
                ('AD4', models.TextField()),
                ('PIN', models.TextField()),
                ('PHONE', models.TextField()),
                ('FAX', models.TextField()),
                ('JT1', models.TextField()),
                ('FJT1', models.TextField()),
                ('JT2', models.TextField()),
                ('FJT2', models.TextField()),
                ('FILLER1', models.TextField()),
                ('FILLER2', models.TextField()),
                ('PAN1', models.TextField()),
                ('PAN2', models.TextField()),
                ('PAN3', models.TextField()),
                ('NOM', models.TextField()),
                ('NOMNAME', models.TextField()),
                ('NAD1', models.TextField()),
                ('NAD2', models.TextField()),
                ('NAD3', models.TextField()),
                ('NAD4', models.TextField()),
                ('NPIN', models.TextField()),
                ('DBMINOR', models.TextField()),
                ('MIND', models.TextField()),
                ('ACNO', models.TextField()),
                ('BANKNAME', models.TextField()),
                ('BANKAD1', models.TextField()),
                ('BANKAD2', models.TextField()),
                ('BANKAD3', models.TextField()),
                ('BANKAD4', models.TextField()),
                ('BANKPIN', models.TextField()),
                ('RBIREF', models.TextField()),
                ('RBIDATE', models.TextField()),
                ('SEBIREGNO', models.TextField()),
                ('BTAX', models.TextField()),
                ('STATUS', models.TextField()),
                ('MICRCD', models.TextField()),
                ('IFSC', models.TextField()),
                ('ACTYPE', models.TextField()),
                ('Filler3', models.TextField()),
                ('NAMEMAPIN', models.TextField()),
                ('JT1MAPIN', models.TextField()),
                ('JT2MAPIN', models.TextField()),
                ('EMAIL1', models.TextField()),
                ('EMAIL2', models.TextField()),
                ('EMAIL3', models.TextField()),
                ('RGSFLG', models.TextField()),
                ('ANREPFLG', models.TextField()),
                ('UIDISTHOL', models.TextField()),
                ('UID2NDHOL', models.TextField()),
                ('UID3RDHOL', models.TextField()),
                ('PANGAR', models.TextField()),
                ('UIDGAR', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Demathol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DPID', models.TextField()),
                ('CLID', models.TextField()),
                ('FREEHOL', models.TextField()),
                ('HOLLCK', models.TextField()),
                ('HOLBLOCK', models.TextField()),
                ('HOLPLD', models.TextField()),
                ('HOLPLDLCK', models.TextField()),
                ('HOLPLDUNC', models.TextField()),
                ('HOLPLDLCKU', models.TextField()),
                ('HOLREM', models.TextField()),
                ('HOLREMLCK', models.TextField()),
                ('HOLCMIDD', models.TextField()),
                ('HOLCMPOOL', models.TextField()),
                ('HOLSET', models.TextField()),
                ('ISEN', models.TextField()),
                ('DATE', models.TextField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='demathol',
            constraint=models.UniqueConstraint(fields=('DPID', 'CLID'), name='DEMTHOL_DPID_CLID'),
        ),
        migrations.AddConstraint(
            model_name='dematad',
            constraint=models.UniqueConstraint(fields=('DPID', 'CLID'), name='DEMATAD_DPID_CLID'),
        ),
    ]
