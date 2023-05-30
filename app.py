import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import numpy as np

pdf = canvas.Canvas('Projeto Visualização da Informação.pdf')
pdf.setFontSize(size=10)
df = pd.read_csv('cardio_train.csv', delimiter=';')

""" Manipulações do dataframe pra analise"""
df['age'] = df['age'] // 365  # Passa idade de dias para anos
df['IMC'] = df['weight'] / (df['height'] / 100) ** 2  # Adiciona a coluna do IMC

# Adiciona e classifica a categoria de faixas etária
df.loc[(df.age <= 40), 'agecat'] = 1
df.loc[(df.age > 40) & (df.age <= 45), 'agecat'] = 2
df.loc[(df.age > 45) & (df.age <= 50), 'agecat'] = 3
df.loc[(df.age > 50) & (df.age <= 55), 'agecat'] = 4
df.loc[(df.age > 55) & (df.age <= 60), 'agecat'] = 5
df.loc[(df.age > 60) & (df.age <= 65), 'agecat'] = 6
df.loc[(df.age > 65) & (df.age <= 70), 'agecat'] = 7
df.loc[(df.age >= 70), 'agecat'] = 8

# Adiciona e classifica a categoria de IMC
# Base obtida da UFPEL - https://dms.ufpel.edu.br/casca/modulos/imc-calc#comp/imc-main
df.loc[(df.IMC < 18.5), 'catimc'] = 1
df.loc[(df.IMC >= 18.5) & (df.IMC < 24.9), 'catimc'] = 2
df.loc[(df.IMC >= 25) & (df.IMC < 29.9), 'catimc'] = 3
df.loc[(df.IMC >= 30) & (df.IMC < 34.9), 'catimc'] = 4
df.loc[(df.IMC >= 35) & (df.IMC < 39.9), 'catimc'] = 5
df.loc[(df.IMC >= 40), 'catimc'] = 6

""" Cabeçalho """
pdf.drawString(20 * mm, 276 * mm, 'Nome: Renan Douglas de Souza')
pdf.drawString(20 * mm, 271 * mm, 'RGM: 1631228348')
pdf.drawString(20 * mm, 266 * mm, 'Instituição: CRUZEIRO DO SUL - GRADUAÇÃO EAD')
pdf.drawString(20 * mm, 261 * mm, 'Curso: Sistemas de Informação')
pdf.drawString(20 * mm, 251 * mm,
               'Link do dataset utilizado: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset')
pdf.drawString(20 * mm, 246 * mm, 'Link do meu video de apresentação: https://www.loom.com/share/32fb9517fa714808a68b7432bdc1cb58')

""" Grafico 1 """
pdf.setFont('Helvetica-Bold', size=10)
pdf.drawString(20 * mm, 236 * mm, 'Plot 1 - ')
pdf.setFont('Helvetica', size=10)
pdf.drawString(33 * mm, 236 * mm, 'Estado de saúde dos 70.000 pacientes e gênero mais afetado dos que apresentarão'
                                  ' doenças cardíacas.')

# Gera a figura e define os eixos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))  # adicionado layout='constrained'
fig.subplots_adjust(wspace=0)

# Parâmetros da pizza
health_status = df['cardio'].value_counts(normalize=True)
overall_ratios = [health_status[1], health_status[0]]
labels = ['Doente', 'Saudável']
explode = [0.1, 0]
ax1.set_title('Estado de saúde')

# Rotaciona a primeira fatia e cria o recorte do x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle, labels=labels, explode=explode)

# Parâmetros da barra
gender_filtered = df[df['cardio'] == 1]  # DataFrame filtrado somente com doentes.
gender = gender_filtered['gender'].value_counts(normalize=True)
age_ratios = [gender[1], gender[2]]
age_labels = ['Mulher', 'Homem']
bottom = 1
width = .2

for i, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label, alpha=0.1 + 0.25 * i)
    ax2.bar_label(bc, labels=[f'{height:.0%}'], label_type='center')

# Configurações do PLOT
ax2.set_title('Gênero')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(-2.5 * width, 2.5 * width)

# ConnectionPath
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(age_ratios)

# Desenha linha superior
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData)

con.set_color([0, 0, 0])
con.set_linewidth(2)
ax2.add_artist(con)

# Desenha linha inferior
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData)

con.set_color([0, 0, 0])
con.set_linewidth(2)
ax2.add_artist(con)

# Salva imagem e limpa axis e figure para próximo uso.
plt.savefig('figure1')
plt.cla()
plt.clf()

pdf.drawImage('figure1.png', 20 * mm, 178 * mm, width=288, height=160)  # Pega a imagem e coloca no PDF

""" Grafico 2 """
pdf.setFont('Helvetica-Bold', size=10)
pdf.drawString(20 * mm, 168 * mm, 'Plot 2 - ')
pdf.setFont('Helvetica', size=10)
pdf.drawString(33 * mm, 168 * mm, 'Faixa etária das pessoas afetadas por doenças cardíacas.')

# Manipulação dos dados
age_acale_label = ['menor de 40', '41 e 45', '46 e 50', '51 e 55', '56 e 60', 'acima de 61']
ages = gender_filtered['agecat'].value_counts(sort=False).sort_index()
age_scale = [ages[1], ages[2], ages[3], ages[4], ages[5], ages[6]]

# Configurações do PLOT
plt.plot(age_acale_label, age_scale, marker='o')
plt.yticks(np.arange(0, 11000, 1000))
plt.ylabel('Quantidade de pessoas')
plt.xlabel('Grupo de idade')
plt.title('Faixa etária das pessoas afetadas')
plt.grid()

# Salva imagem e limpa axis e figure para próximo uso.
plt.savefig('figure2')
plt.cla()
plt.clf()

pdf.drawImage('figure2.png', 20 * mm, 110 * mm, width=288, height=160)  # Pega a imagem e coloca no PDF

""" Grafico 3 """
pdf.setFont('Helvetica-Bold', size=10)
pdf.drawString(20 * mm, 100 * mm, 'Plot 3 - ')
pdf.setFont('Helvetica', size=10)
pdf.drawString(33 * mm, 100 * mm, 'Classificação pelo IMC para cada grupo.')

# Manipulação dos dados
people_healthy = df[df['cardio'] == 0]  # DataFrame filtrado somente com saudáveis.
people_disease = df[df['cardio'] == 1]  # DataFrame filtrado somente com doentes.
x_label = ['Grupo Saudável', 'Grupo Doente']
healthy = people_healthy['catimc'].value_counts(sort=False).sort_index()
disease = people_disease['catimc'].value_counts(sort=False).sort_index()

cardio_group = {
    'Baixo peso': [healthy[1], disease[1]],
    'Peso normal': [healthy[2], disease[2]],
    'Excesso de peso': [healthy[3], disease[3]],
    'Obesidade I': [healthy[4], disease[4]],
    'Obesidade II': [healthy[5], disease[5]],
    'Obesidade III': [healthy[6], disease[6]]
}

x = np.arange(len(x_label))
width = 0.15
multiplier = -1

fig, ax = plt.subplots(layout='constrained', figsize=(8, 5))

for attribute, measurement in cardio_group.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=2)
    multiplier += 1

# Configurações do PLOT
ax.set_ylabel('Quantidade de pessoas')
ax.set_title('IMC por grupo de saúde')
ax.set_xticks(x + width, x_label)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0, 20000)

# Salva imagem e limpa axis e figure para próximo uso.
plt.savefig('figure3')
plt.cla()
plt.clf()

pdf.drawImage('figure3.png', 20 * mm, 38 * mm, width=256, height=160)  # Pega a imagem e coloca no PDF

pdf.save()  # Salva o PDF
