import peewee as pw


# Conexión a la base de datos en Neon
farmacia_ujat = pw.PostgresqlDatabase(
    'neondb',
    user='neondb_owner',
    password='npg_rtza0QeXhy2C',
    host='ep-winter-shape-a4p17xtq-pooler.us-east-1.aws.neon.tech',
    port=5432,
    sslmode='require'
)

# Modelo Farmaco
class Farmaco(pw.Model):
    nombre = pw.CharField(max_length=255, primary_key=True)
    descripcion = pw.CharField(max_length=255)
    categoria = pw.CharField(max_length=255)
    interacciones = pw.CharField(max_length=5000, null=True)

    class Meta:
        database = farmacia_ujat  # ← CORRECTO

# Modelo Medicamento
class Medicamento(pw.Model):
    id = pw.IntegerField(primary_key=True)
    clave = pw.CharField(max_length=255)
    descripcion = pw.CharField(max_length=255)
    presentacion = pw.CharField(max_length=255)
    clasificacion = pw.CharField(max_length=255)
    nivel_atencion = pw.CharField(max_length=255)
    nombre_farmaco = pw.ForeignKeyField(
        Farmaco,
        field=Farmaco.nombre,
        column_name="nombre_farmaco",
        null=True
    )

    class Meta:
        database = farmacia_ujat

