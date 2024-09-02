from datetime import timedelta

class Relatorio:
    @staticmethod
    def gerar_relatorio(atendimentos):
        tempos = [atendimento.fim - atendimento.inicio for atendimento in atendimentos if atendimento.fim]
        if not tempos:
            print('Nenhum atendimento finalizado para gerar relatórios.')
            return
        tempo_medio = sum(tempos, timedelta()) / len(tempos)
        print(f'Tempo médio de atendimento: {tempo_medio}')