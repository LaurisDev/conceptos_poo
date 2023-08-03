import random


class Materia:

    def __init__(self, nombre: str, creditos: int):
        self.nombre: str = nombre
        self.creditos: int = creditos


class Estudiante:

    def __init__(self, nombre: str, edad: int, nota_promedio: float):
        self.nombre: str = nombre
        self.edad: int = edad
        self.nota_promedio: float = nota_promedio
        self.materias: list[Materia] = []

    def matricular_materia(self, nombre_materia: str, creditos: int):
        materia: Materia = Materia(nombre_materia, creditos)
        self.materias.append(materia)

    def cambiar_nota(self) -> float:
        n = random.randint(1, 10)
        if n > 5:
            self.nota_promedio += 0.5
        else:
            self.nota_promedio

        return self.nota_promedio


if __name__ == "__main__":
    e1: Estudiante = Estudiante("Pedro", 18, 3.5)
    e2: Estudiante = Estudiante("Maria", 15, 3.5)
    e3: Estudiante = Estudiante("Luisa", 20, 2.8)

    e1.matricular_materia("APOO", 3)
    e1.matricular_materia("procesos", 3)




