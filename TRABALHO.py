while True:

   aluno = dict()

   aluno['nome'] = str(input('Digite o nome do aluno: '))  

   aluno['idade'] = int(input(f'Digite a idade de {aluno["nome"]}: '))

   if aluno['idade'] <= 5:

       aluno['ensino'] = 'Ensino Infantil'

   elif aluno['idade'] >= 6 and aluno['idade'] <= 13:

       aluno['ensino'] = 'Ensino Fundamental I'

   elif aluno['idade'] > 13 and aluno['idade'] <= 14:

       aluno['ensino'] = 'Ensino Fundamental II'

   elif aluno['idade'] >= 15:

       aluno['ensino'] = 'Ensino Médio'

   for k, v in aluno.items():

       print(f'{k}: {v}')

   print('\nDeseja continuar?\n[0] Não\n[1] Sim')

   option = int(input('R: '))

   if option == 0:

       break