# Simulação de Ransomware
⚠️ Aviso:
Este projeto é estritamente para fins de aprendizado e pesquisa. Não utilize este projeto para atividades maliciosas. O autor não se responsabiliza por qualquer uso indevido. Este repositório contém uma simulação de ransomware promovida pelo bootcamp de cibersegurança do Santander.

🛡️ Projeto de Simulação de Ransomware
Este projeto simula um ataque de ransomware para fins educacionais. Ele demonstra como funcionam os processos de criptografia e descriptografia, utilizando uma combinação de métodos de criptografia RSA e AES. O projeto inclui scripts para criptografar arquivos (encrypter.py) e descriptografá-los (decrypter.py), mostrando princípios-chave de criptografia e boas práticas.

🚀 Funcionalidades
Geração de Chaves RSA: Gera automaticamente pares de chaves RSA (2048 bits).
Criptografia de Arquivos: Criptografa arquivos usando AES-256 para o conteúdo e RSA para proteção da chave AES.
Descriptografia de Arquivos: Descriptografa arquivos usando a chave privada RSA e restaura o conteúdo original.
Gestão de Diretórios: Organiza automaticamente os arquivos criptografados e descriptografados em pastas dedicadas.

⚙️ Requisitos
Certifique-se de ter o Python 3.8 ou superior instalado. 

🌟 Uso
Arquivos originais são carregados no diretório test_files/.
Após rodar o encrypter.py, os arquivos criptografados aparecem em test_files/encrypted/.
Após rodar o decrypter.py, os arquivos descriptografados são restaurados em test_files/decrypted/.

🛠️ Tecnologias Utilizadas
Linguagem: Python
Biblioteca de Criptografia: cryptography
Métodos: RSA e AES
