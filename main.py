from datetime import datetime

class Atendimento:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def iniciar_atendimento(self):
        self.inicio = datetime.now()
        print(f'Atendimento iniciado em {self.inicio}')

    def finalizar_atendimento(self):
        if self.inicio is None:
            print('O atendimento não foi iniciado.')
            return
        self.fim = datetime.now()
        tempo_atendimento = self.fim - self.inicio
        print(f'Atendimento concluído em {self.fim}')
        print(f'Tempo total de atendimento: {tempo_atendimento}')

class Relatorio:
    @staticmethod
    def gerar_relatorio(atendimentos):
        tempos = [atendimento.fim - atendimento.inicio for atendimento in atendimentos if atendimento.fim]
        if not tempos:
            print('Nenhum atendimento finalizado para gerar relatórios.')
            return
        tempo_medio = sum(tempos, timedelta()) / len(tempos)
        print(f'Tempo médio de atendimento: {tempo_medio}')

if __name__ == '__main__':
    atendimentos = []

    # Exemplo de uso
    atendimento1 = Atendimento()
    atendimento1.iniciar_atendimento()
    # Simula o tempo de atendimento
    input('Pressione Enter para finalizar o atendimento...')
    atendimento1.finalizar_atendimento()
    atendimentos.append(atendimento1)

    relatorio = Relatorio()
    relatorio.gerar_relatorio(atendimentos)