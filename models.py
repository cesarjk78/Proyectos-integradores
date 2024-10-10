from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    tipo_usuario = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=45)

    def __str__(self):
        return f"Profesor: {self.usuario.nombre}"

class Alumno(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=45)
    carrera = models.CharField(max_length=45)

    def __str__(self):
        return f"Alumno: {self.usuario.nombre}"

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=45)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_curso

class CursoHasAlumno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self):
        return f"Curso: {self.curso.nombre_curso} - Alumno: {self.alumno.usuario.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre

class CicloAcademico(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

class ProyectoFinal(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    ciclo = models.ForeignKey(CicloAcademico, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Evaluacion(models.Model):
    proyecto = models.ForeignKey(ProyectoFinal, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=4, decimal_places=2)
    comentarios = models.TextField()
    fecha_evaluacion = models.DateField()

    def __str__(self):
        return f"Evaluación de {self.proyecto.titulo} por {self.profesor.nombre}"
