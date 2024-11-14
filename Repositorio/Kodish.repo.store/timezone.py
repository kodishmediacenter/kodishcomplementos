import datetime
import pytz

def exibir_horarios_fusos():
    # Pega o horário atual do computador
    hora_atual = datetime.datetime.now()

    # Obtém todos os fusos horários disponíveis
    todos_fusos = pytz.all_timezones

    print(f"Hora local do computador: {hora_atual.strftime('%Y-%m-%d %H:%M:%S')}")

    print("\nHorários em diferentes fusos horários:\n")
    
    # Exibe a hora correspondente em cada fuso horário
    for fuso in todos_fusos:
        fuso_horario = pytz.timezone(fuso)
        hora_fuso = hora_atual.astimezone(fuso_horario)
        print(f"{fuso}: {hora_fuso.strftime('%Y-%m-%d %H:%M:%S')}")

# Chama a função para exibir as horas em todos os fusos horários
exibir_horarios_fusos()
