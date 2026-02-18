# Dependent
coin_tossed_head = 1/2
dice_rolling_6 = 1/6
print(f'P(A) * P(B) : {coin_tossed_head * dice_rolling_6 :.3f}')


#finding probability without Replacement (Independent)
red = 5
blue = 5
picking_1st_marble = red / (red+blue)
picking_2st_marble = (red-1)/(red+blue-1)

prob = picking_1st_marble * picking_2st_marble
print(f'probability that both are Red without Replacement : {prob:.2f}')
