import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
import matplotlib.patches
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import numpy as np

pdf = canvas.Canvas('Projeto Visualização da Informação.pdf')
df = pd.read_csv('cardio_train.csv', delimiter=';')

"""
Age | Objective Feature | age | int (days) |
Height | Objective Feature | height | int (cm) |
Weight | Objective Feature | weight | float (kg) |
Gender | Objective Feature | gender | categorical code | 1: female, 2: male |
Systolic blood pressure | Examination Feature | ap_hi | int |
Diastolic blood pressure | Examination Feature | ap_lo | int |
Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
Smoking | Subjective Feature | smoke | binary | 0: no, 1: yes |
Alcohol intake | Subjective Feature | alco | binary | 0: no, 1: yes |
Physical activity | Subjective Feature | active | binary | 0: no, 1: yes |
Presence or absence of cardiovascular disease | Target Variable | cardio | binary | 0: no, 1: yes |
"""

# """ Cabeçalho """
# pdf.drawString(20 * mm, 276 * mm, 'Nome: Renan Douglas de Souza')
# pdf.drawString(20 * mm, 271 * mm, 'RGM: 1631228348')
# pdf.drawString(20 * mm, 266 * mm, 'Instituição: CRUZEIRO DO SUL - GRADUAÇÃO EAD')
# pdf.drawString(20 * mm, 261 * mm, 'Curso: Sistemas de Informação')
# pdf.drawString(20 * mm, 251 * mm, 'Link do dataset utilizado: https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset')
# pdf.drawString(20 * mm, 246 * mm, 'Link do meu video de apresentação: ')
#
# """ Grafico um """
# pdf.setFont('Helvetica-Bold', 12)
# pdf.drawString(20 * mm, 236 * mm, 'Plot 1 - ')
# pdf.setFont('Helvetica', 12)
# pdf.drawString(36 * mm, 236 * mm, 'Estado de saúde e gênero mais afetado ')
#
# """ Gera a figura e define os eixos """
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
# fig.subplots_adjust(wspace=0)
#
# """ Parâmetros da pizza """
# health_status = df['cardio'].value_counts(normalize=True)
# overall_ratios = [health_status[1], health_status[0]]
# labels = ['Doente', 'Saudável']
# explode = [0.1, 0]
# ax1.set_title('Estado')
#
# """ Rotaciona a primeira fatia e cria o recorte do x-axis"""
# angle = -180 * overall_ratios[0]
# wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle, labels=labels, explode=explode)
#
# """ Parâmetros da barra"""
gender_filtered = df[df['cardio'] == 1]
# gender = gender_filtered['gender'].value_counts(normalize=True)
# age_ratios = [gender[1], gender[2]]
# age_labels = ['Mulher', 'Homem']
# bottom = 1
# width = .2
#
# for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
#     bottom -= height
#     bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label, alpha=0.1 + 0.25 * j)
#     ax2.bar_label(bc, labels=[f'{height:.0%}'], label_type='center')
#
# ax2.set_title('Gênero')
# ax2.legend()
# ax2.axis('off')
# ax2.set_xlim(-2.5 * width, 2.5 * width)
#
# """ ConnectionPath """
# theta1, theta2 = wedges[0].theta1, wedges[0].theta2
# center, r = wedges[0].center, wedges[0].r
# bar_height = sum(age_ratios)
#
# """ Desenha linha superior """
# x = r * np.cos(np.pi / 180 * theta2) + center[0]
# y = r * np.sin(np.pi / 180 * theta2) + center[1]
# con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData)
#
# con.set_color([0, 0, 0])
# con.set_linewidth(2)
# ax2.add_artist(con)
#
# """ Desenha linha inferior """
# x = r * np.cos(np.pi / 180 * theta1) + center[0]
# y = r * np.sin(np.pi / 180 * theta1) + center[1]
# con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData, xyB=(x, y), coordsB=ax1.transData)
#
# con.set_color([0, 0, 0])
# con.set_linewidth(2)
# ax2.add_artist(con)
#
# plt.savefig('figure1')
# plt.cla()
# plt.clf()
#
# pdf.drawImage('figure1.png', 20 * mm, 178 * mm, width=288, height=160)
#
# """ Exercise two - Mostrar """
# pdf.setFont('Helvetica-Bold', 12)
# pdf.drawString(20 * mm, 168 * mm, 'Plot 2 - ')
# pdf.setFont('Helvetica', 12)
# pdf.drawString(36 * mm, 168 * mm, 'Faixa etária das pessoas afetadas por doenças cardíacas.')
#
# age_acale_label = ['menor de 40', '41 e 50', '51 e 60', 'acima de 60']
# age_scale = [0, 0, 0, 0]
# for age in gender_filtered.iterrows():
#     if age[1][1] < 14601:
#         age_scale[0] += 1
#     elif age[1][1] < 18251:
#         age_scale[1] += 1
#     elif age[1][1] < 21901:
#         age_scale[2] += 1
#     else:
#         age_scale[3] += 1
#
# fig, ax = plt.subplots()
# bar_container = ax.bar(age_acale_label, age_scale)
#
# ax.bar_label(bar_container, fmt=lambda x: '{:.0f}'.format(x))
# ax.set(ylabel='Quantidade de pessoas', title='Quantidade de pessoas doentes por faixa etária', ylim=(0, 20000))
# ax.set_yticks([])
# plt.savefig('figure2')
# plt.cla()
# plt.clf()
#
# pdf.drawImage('figure2.png', 20 * mm, 110 * mm, width=212, height=159)

""" Exercise three """
# pdf.setFont('Helvetica-Bold', 12)
# pdf.drawString(20 * mm, 100 * mm, 'Plot 3 - ')
# pdf.setFont('Helvetica', 12)
# pdf.drawString(36 * mm, 100 * mm, 'Faixa etária')
#
# ages = ['18-20', '21-29', '30-39', '40-49', '50-59', '60 ou mais']
# data = [10, 44, 28, 12, 4, 2]
# bar_container = plt.bar(ages, data)
# plt.ylim(0, 50)
# plt.yticks([])
# plt.bar_label(
#     bar_container, fmt=lambda x: '{}%'.format(x)
# )
#
# plt.savefig('figure3')
#
# pdf.drawImage('figure3.png', 20 * mm, 42 * mm, width=212, height=159)
#
pdf.save()
