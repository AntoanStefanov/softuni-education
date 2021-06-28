def math_operations(*args, **kwargs):
    print(type(args))
    args = list(args)
    index = 0
    is_enough = False
    while args:
        for key, value in kwargs.items():
            if key == 'a':
                kwargs[key] = value + args[index]
            elif key == 's':
                kwargs[key] = value - args[index]
            elif key == 'd':
                if args[index] == 0:
                    args.pop(index)
                    continue
                kwargs[key] = value / args[index]
            elif key == 'm':
                kwargs[key] = value * args[index]
            index += 1
            if index == len(args):
                is_enough = True
                break
        if is_enough:
            return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
