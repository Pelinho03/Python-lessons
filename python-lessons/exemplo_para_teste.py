'''
VALIDAR NOTAS ALUNOS
-Uma instituição de ensino superior deseja desenvolver um sistema em Python para validar e organizar as notas dos alunos. O algoritmo deverá solicitar o número de alunos, e usará o random para efetuar o seguinte:
    -> Receber notas de cinco disciplinas para cada aluno.
    -> Garantir que todas as notas inseridas estejam entre 0 e 20.
    -> Estruturar os dados em dois cursos e quatro turmas por curso.
    -> Calcular:
        -> Média geral da turma e do curso.
        -> Quantidade de notas inválidas e mostrar os cursos.
        -> Número de alunos aprovados (média igual ou superior a 10) e reprovados (média menor que 10)
'''
import random

disciplinas = ["LPP", "PEE", "CG", "GPS", "ATW"]
cursos = ["Engenharia", "Gestão"]
turmas = ["Turma A", "Turma B", "Turma C", "Turma D"]


def gerar_notas_validas():
    return [random.randint(0, 20) for _ in range(len(disciplinas))]


def validar_notas(notas):
    return all(0 <= nota <= 20 for nota in notas)


def calcular_media(notas):
    return sum(notas) / len(notas)


def processar_turma(num_alunos):
    alunos = {}
    notas_invalidas = 0
    aprovados = 0
    reprovados = 0
    medias_turma = []

    for aluno in range(1, num_alunos + 1):
        notas = gerar_notas_validas()

        if not validar_notas(notas):
            notas_invalidas += 1
        else:
            media_aluno = calcular_media(notas)
            medias_turma.append(media_aluno)

            if media_aluno >= 10:
                aprovados += 1
            else:
                reprovados += 1

            alunos[f"Aluno {aluno}"] = {
                "notas": notas,
                "média": media_aluno
            }

    media_turma = sum(medias_turma) / len(medias_turma) if medias_turma else 0
    return alunos, media_turma, notas_invalidas, aprovados, reprovados


def processar_curso(num_alunos_por_turma):
    curso_data = {}
    medias_curso = []

    for turma in turmas:
        alunos, media_turma, notas_invalidas, aprovados, reprovados = processar_turma(
            num_alunos_por_turma)

        curso_data[turma] = {
            "alunos": alunos,
            "media_turma": media_turma,
            "notas_invalidas": notas_invalidas,
            "aprovados": aprovados,
            "reprovados": reprovados
        }

        medias_curso.append(media_turma)

    media_curso = sum(medias_curso) / len(medias_curso) if medias_curso else 0
    return curso_data, media_curso


def exibir_resultados(cursos_data):
    for curso_nome, curso_info in cursos_data.items():
        print(f'\n=== Curso: {curso_nome} ===')
        print(f'Média geral do curso: {curso_info["media_curso"]:.2f}')

        for turma_nome, turma_info in curso_info["turmas"].items():
            print(f'\nTurma: {turma_nome}')
            print(f' - Média da turma: {turma_info["media_turma"]:.2f}')
            print(f' - Notas inválidas: {turma_info["notas_invalidas"]}')
            print(f' - Alunos aprovados: {turma_info["aprovados"]}')
            print(f' - Alunos reprovados: {turma_info["reprovados"]}')


# Input
num_alunos_por_turma = int(input("Digite o número de alunos por turma: "))

# Processamento dos cursos
cursos_data = {}

for curso in cursos:
    curso_data, media_curso = processar_curso(num_alunos_por_turma)
    cursos_data[curso] = {
        "turmas": curso_data,
        "media_curso": media_curso
    }

# Exibir resultados
exibir_resultados(cursos_data)
