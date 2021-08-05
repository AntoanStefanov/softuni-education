from project.player.player import Player


class BattleField:

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if type(attacker).__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if type(enemy).__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        for card in attacker.card_repository.cards:
            attacker.health += card.health_points

        for card in enemy.card_repository.cards:
            enemy.health += card.health_points

        # Attacker attacks first and after that the enemy attacks
        # (deal damage points to opponent for each card).
        # If one of the players is dead, you should stop the fight.

        for card in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)

