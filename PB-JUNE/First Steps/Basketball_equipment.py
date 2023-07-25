yearly_team_fee = int(input())

shoes = 0.60 * yearly_team_fee
clothes = 0.80 * shoes
ball = 0.25 * clothes
accessories = 0.20 * ball

total_sum = shoes + clothes + ball + accessories + yearly_team_fee

print(round(total_sum, 2))
