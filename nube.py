import peewee as pw

farmacia_ujat = pw.PostgresqlDatabase(
    'neondb',
    user='neondb_owner',
    password='npg_rtza0QeXhy2C',
    host='ep-winter-shape-a4p17xtq-pooler.us-east-1.aws.neon.tech',
    port=5432,
    sslmode='require'
)

class Receta(pw.Model):
    medicamento = pw.CharField()
    interacciones = pw.CharField()

    class Meta:
        database = farmacia_ujat
        primary_key = False 
