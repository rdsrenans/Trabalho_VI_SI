import pandas as pd
from matplotlib import pyplot as plt
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

pdf = canvas.Canvas('Projeto Visualização da Informação.pdf')
df = pd.read_csv('cardio_train.csv', delimiter=';')

# Head
# pdf.drawString(20 * mm, 276 * mm, 'Nome: Renan Douglas de Souza')
# pdf.drawString(20 * mm, 271 * mm, 'RGM: 1631228348')
# pdf.drawString(20 * mm, 266 * mm, 'Instituição: CRUZEIRO DO SUL - GRADUAÇÃO EAD')
# pdf.drawString(20 * mm, 261 * mm, 'Curso: Sistemas de Informação')
# pdf.drawString(20 * mm, 251 * mm, 'Link do dataset utilizado: https://www.jetbrains.com/pt-br/lp/devecosystem-2022/')
# pdf.drawString(20 * mm, 246 * mm, 'Link do meu video de apresentação: ')
#
# # Exercise one
# pdf.setFont('Helvetica-Bold', 12)
# pdf.drawString(20 * mm, 236 * mm, 'Plot 1 - ')
# pdf.setFont('Helvetica', 12)
# pdf.drawString(36 * mm, 236 * mm, 'As 5 linguagens mais utilizadas pelos desenvolvedores de 2017 à 2022.')
#
# df = pd.DataFrame({'Anos': ['2017', '2018', '2019', '2020', '2021', '2022'],
#                    'JavaScript': [65, 64, 69, 70, 69, 65],
#                    'HTML/CSS': [60, 55, 61, 61, 60, 54],
#                    'Python': [32, 41, 49, 55, 52, 53],
#                    'SQL': [42, 47, 56, 56, 54, 49],
#                    'Java': [47, 51, 50, 54, 49, 48]})
#
# for y in df:
#     if y != 'Anos':
#         plt.plot('Anos', y, label=y, data=df, linewidth=2)
#
# plt.ylabel('Uso em %')
# plt.legend()
# plt.grid()
# plt.savefig('figure1')
# plt.cla()
# plt.clf()
#
# pdf.drawImage('figure1.png', 20 * mm, 178 * mm, width=212, height=159)
#
# # Exercise two
# pdf.setFont('Helvetica-Bold', 12)
# pdf.drawString(20 * mm, 168 * mm, 'Plot 2 - ')
# pdf.setFont('Helvetica', 12)
# pdf.drawString(36 * mm, 168 * mm, 'O nível em qual eles julgam-se encaixarem.')
#
labels = ['Homem', 'Mulher']
sizes = df['gender'].unique()



colors = ['#913f33', '#ff705f', '#ffaa67', '#ffdfab', '#9fb9c2']
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.0f%%', startangle=90, pctdistance=1.15)
plt.legend(patches, labels, loc="lower right")
plt.axis('equal')
plt.savefig('figure2')
plt.cla()
plt.clf()
#
# pdf.drawImage('figure2.png', 20 * mm, 110 * mm, width=212, height=159)
#
# # Exercise three
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
# pdf.save()








################################## Antes ####################################################

# # Head
# pdf.drawString(20 * mm, 276 * mm, 'Nome: Renan Douglas de Souza')
# pdf.drawString(20 * mm, 271 * mm, 'RGM: 1631228348')
# pdf.drawString(20 * mm, 266 * mm, 'Instituição: CRUZEIRO DO SUL - GRADUAÇÃO EAD')
# pdf.drawString(20 * mm, 261 * mm, 'Curso: Sistemas de Informação')
# pdf.drawString(20 * mm, 251 * mm, 'Link do dataset utilizado: https://www.jetbrains.com/pt-br/lp/devecosystem-2022/')
# pdf.drawString(20 * mm, 246 * mm, 'Link do meu video de apresentação: ')
#
# # Exercise one
# pdf.setFont('Helvetica-Bold', 12)
# pdf.drawString(20 * mm, 236 * mm, 'Plot 1 - ')
# pdf.setFont('Helvetica', 12)
# pdf.drawString(36 * mm, 236 * mm, 'As 5 linguagens mais utilizadas pelos desenvolvedores de 2017 à 2022.')
#
# df = pd.DataFrame({'Anos': ['2017', '2018', '2019', '2020', '2021', '2022'],
#                    'JavaScript': [65, 64, 69, 70, 69, 65],
#                    'HTML/CSS': [60, 55, 61, 61, 60, 54],
#                    'Python': [32, 41, 49, 55, 52, 53],
#                    'SQL': [42, 47, 56, 56, 54, 49],
#                    'Java': [47, 51, 50, 54, 49, 48]})
#
# for y in df:
#     if y != 'Anos':
#         plt.plot('Anos', y, label=y, data=df, linewidth=2)
#
# plt.ylabel('Uso em %')
# plt.legend()
# plt.grid()
# plt.savefig('figure1')
# plt.cla()
# plt.clf()
#
# pdf.drawImage('figure1.png', 20 * mm, 178 * mm, width=212, height=159)
#
# # Exercise two
# pdf.setFont('Helvetica-Bold', 12)
# pdf.drawString(20 * mm, 168 * mm, 'Plot 2 - ')
# pdf.setFont('Helvetica', 12)
# pdf.drawString(36 * mm, 168 * mm, 'O nível em qual eles julgam-se encaixarem.')
#
# labels = ['Sênior', 'Pleno', 'Junior', 'Trainee', 'Outros']
# sizes = [41, 35, 19, 4, 1]
# colors = ['#913f33', '#ff705f', '#ffaa67', '#ffdfab', '#9fb9c2']
# patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.0f%%', startangle=90, pctdistance=1.15)
# plt.legend(patches, labels, loc="lower right")
# plt.axis('equal')
# plt.savefig('figure2')
# plt.cla()
# plt.clf()
#
# pdf.drawImage('figure2.png', 20 * mm, 110 * mm, width=212, height=159)
#
# # Exercise three
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
# pdf.save()
