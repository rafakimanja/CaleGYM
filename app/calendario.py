from datetime import datetime

class Calendario:

    def __init__(self, data=datetime.now()):
        self.data = data


    def get_data(self):
        return self.data.date


    def dia(self):
        dia = self.data.day
        return dia


    def dia_semana(self):
        
        semana = self.data.weekday()

        match semana:

            case 0:
                return 'Segunda-Feira'
            
            case 1:
                return 'Terça-Feira'
            
            case 2:
                return 'Quarta-Feira'
            
            case 3:
                return 'Quinta-Feira'
            
            case 4:
                return 'Sexta-Feira'
            
            case 5:
                return 'Sábado'
            
            case 6:
                return 'Domingo'


    def nome_mes(self):

        mes = self.data.month

        match mes:

            case 1:
                return 'Janeiro'
            
            case 2:
                return 'Fevereiro'
            
            case 3:
                return 'Março'
            
            case 4:
                return 'Abril'
            
            case 5:
                return 'Maio'
            
            case 6:
                return 'Junho'
            
            case 7:
                return 'Julho'
            
            case 8:
                return 'Agosto'
            
            case 9:
                return 'Setembro'
            
            case 10:
                return 'Outuburo'
            
            case 11:
                return 'Novembro'
            
            case 12:
                return 'Dezembro'


    def len_mes(self):

        mes = self.data.month
      
        match mes:

            case 1:
                return 31
            
            case 2:
                return 29
            
            case 3:
                return 31
            
            case 4:
                return 30
            
            case 5:
                return 31
            
            case 6:
                return 30
            
            case 7:
                return 31
            
            case 8:
                return 31
            
            case 9:
                return 30
            
            case 10:
                return 31
            
            case 11:
                return 30
            
            case 12:
                return 31


    def ano(self):
        ano = self.data.year
        return ano


    def calendario(self):
         
        dados = {
        'data': self.get_data(),
        'dia': self.dia(),
        'semana': self.dia_semana(),
        'mes_qtd': self.len_mes(),
        'mes_nome': self.nome_mes(),
        'ano': self.ano()
    }
        return dados