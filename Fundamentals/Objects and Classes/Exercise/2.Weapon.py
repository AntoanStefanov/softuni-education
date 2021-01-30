class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


pistol = Weapon(3)

print(pistol.shoot())
print(pistol.shoot())


# Вместо да ти изкара адреса на weapon object-a ., изкарва квото имаш в repr .
print(pistol)
