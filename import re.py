import re

texto = """inscrições  estaduais baixadas
123456 pag 32.1
lore inscrições estaduais baixadas 123123 gj  inscrições estaduais
 baixadas 111111  quam efficitur dignissim. Nam non 222 tortor
nisl. inscrições estaduais cpf/cnpj: 03024386700 cpf/cnpj: 162.000.127-44 Vivamus sit amet
number: 2  felis sit amet leo mattis inscrições estaduais baixadas
666666"""

print(re.findall(r'cpf/cnpj:\s(\d+)', texto))