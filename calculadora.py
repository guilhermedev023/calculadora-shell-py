print("==== Calculadora Python ====")

while True:
	try:
		n1 = int(input('Digite o primeiro número: '))
		op = input('Digite a operaçào (+. -. *. / ou "sair"): ')
		if op.lower() == "sair":
			print("Encerrando...")
			break
		n2 = int(input('Digite o segundo número: '))

		if op =='+':
			r = n1 + n2
		elif op == '-':
			r = n1 - n2
		elif op == '*':
			r = n1 * n2
		elif op == '/':
			if n2 == 0:
				r = 'Erro: Divisão por zero!'
			else:
				r = n1 / n2
		else:
			r = "=== Operação Inválida ==="

		print(f'{n1} {op} {n2} = {r}')
	except ValueError:
		print("Entrada Inválida. Use apenas números.")
