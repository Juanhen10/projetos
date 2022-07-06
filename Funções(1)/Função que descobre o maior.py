from time import sleep
def maior(* num):
    sleep(0.5)
    print(f'Os números foram:', end='')
    for c in num:
        sleep(0.4)
        print(f' {c}', end='')
    print()
    print(f'O maior número foi: {max(num)}')
    print(f'►' * 30)


maior(1,2,3,4,5,6,7)
maior(4,8,9)
maior(10,11,15)
maior(0)
