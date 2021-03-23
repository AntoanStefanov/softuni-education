from collections import deque
bullet_price = int(input())

gun_barrel_size = int(input())

bullets = deque([int(bull) for bull in input().split()])
total_bullets = len(bullets)

locks = deque([int(lock) for lock in input().split()])

price_of_intelligence = int(input())

shots = 0
while True:

    if not bullets or not locks:
        break

    bullet = bullets.pop()

    if bullet <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

    if bullets:
        shots += 1
        if shots == gun_barrel_size:
            print('Reloading!')
            shots = 0


if not locks:
    bullets_cost = (total_bullets - len(bullets)) * bullet_price

    print(f"{len(bullets)} bullets left. Earned ${price_of_intelligence - bullets_cost}")
elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
