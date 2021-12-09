st.write('我們是第四組:先不要)
import stream as st
car_simulation = {'gas_warning':1, 'speed_limit':100, 'temp_warning':30, '轉速':12000}
gas = st.write_input('油量的資料收集:油箱滿是10格 =>')
speed= st.write_input('車速的資料收集:限速100 =>')
temp = st.write_input('溫度的資料收集:限溫30 =>')
轉速= st.write_input('轉速資料的收集:限轉12000 =>')
confirm_input = st.button('輸入確認')
if confirm_input:
  if gas <= car_simulation.get('gas_warning'):
    print('油箱只剩', gas, '格! 準備加油!!')
  else:
    print('油箱還剩', gas, '格。')
  if speed>=car_simulation.get('speed_limit'):
    print('即將超速')
  else:
    print('安全')
  if temp>=car_simulation.get('temp_warning'):
    print('過熱')
  else:
    print('正常')
  if 轉速>=car_simulation.get('轉速'):
    print('即將超過轉速')
  else:
    print('正常')
