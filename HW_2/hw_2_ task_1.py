# ✔ Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

def convert_num_sys_16(num: int) -> str:
    SYS = 16
    sys_value = {
        0: "0", 1: "1", 2: "2",
        3: "3", 4: "4", 5: "5",
        6: "6", 7: "7", 8: "8",
        9: "9", 10: "A", 11: "B",
        12: "C", 13: "D",
        14: "E", 15: "F"
                 }
    new_num = ""
    while num > 0:
        new_num += sys_value[num % SYS]
        num //= SYS
    return "0x" + new_num[:: -1]

for i in [5, 14, 34, 51, 56]:
    num_16 = convert_num_sys_16(i)
    print(num_16)
    num_hex = hex(i)
    print(num_hex)
    print(num_16 == num_hex)
    print()