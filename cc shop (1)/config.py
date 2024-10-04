# Bot token.
BOT_TOKEN = "@END_SOFT"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 17726932
API_HASH = "@END_SOFT"

# CHAT DE ERROS
LOG_CHAT = -1001768400412

# LOGS DE COMPRAS E ADD SALDO
ADMIN_CHAT = -1001768400412

# CHAT DE COMPRAS PARA CLIENTE
CLIENT_CHAT = -1001681258433
# Quantas atualiza��es podem ser tratadas em paralelo.
# N�o use valores altos para servidores low-end.
WORKERS = 20

# Os administradores podem acessar o painel e adicionar novos materiais ao bot.
ADMINS = [5181333025]

# Sudoers t�m acesso total ao servidor e podem executar comandos.
SUDOERS = [5181333025]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []