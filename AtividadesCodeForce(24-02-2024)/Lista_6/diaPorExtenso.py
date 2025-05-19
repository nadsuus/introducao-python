def dia(dia, mes, ano):
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    if mes < 1 or mes > 12:
        return "Data Invalida" 
    dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dia < 1 or dia > dias_no_mes[mes - 1]:
        return "Data Invalida"
    return f"{dia:02d} de {meses[mes - 1]} de {ano}"
