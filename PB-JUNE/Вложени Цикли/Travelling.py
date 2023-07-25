while True:
    destination = input()
    sum_installment = 0
    if destination == 'End':
        break
    elif destination != 'End':
        budget_needed = float(input())
        while True:
            installment = float(input())
            sum_installment += installment

            if sum_installment >= budget_needed:
                print(f'Going to {destination}!')
                break



