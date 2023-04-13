from dados import dados_main
import matplotlib.pyplot as plt
import json
campos_preenchidos, campos_nao_preenchidos = dados_main()
caminho_do_arquivo = 'dados.json'



with open(caminho_do_arquivo, 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    


total_pessoas = len(dados)  
    
print(f"Total de id cadastrado: {total_pessoas}")




porcentagem_preenchidos = (campos_preenchidos / total_pessoas) * 100
porcentagem_campos_nao_preenchidos = (campos_nao_preenchidos / total_pessoas) * 100


print(f'Campos preenchidos: {campos_preenchidos} ({porcentagem_preenchidos:.0f}%)')
print(f'Campos inválidos: {campos_nao_preenchidos} ({porcentagem_campos_nao_preenchidos:.0f}%)')


labels = ['Campos preenchidos', 'Campos inválidos']
sizes = [porcentagem_preenchidos, porcentagem_campos_nao_preenchidos]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%0.0f%%')
ax.axis('equal')

ax.set_title("Relatório de preenchimento de pessoas")
subtitle2 = f"Campos preenchido: {campos_preenchidos},"
subtitle3 = f"Total de id: {total_pessoas},"
subtitle = f"Campos cadastrado: {total_pessoas},"

ax.text(0.9, -0.10, subtitle, ha='center', transform=ax.transAxes)
ax.text(0.1, 0.10, subtitle2, ha='center', transform=ax.transAxes)
ax.text(0.1, -0.0, subtitle3, ha='center', transform=ax.transAxes)
plt.show()
