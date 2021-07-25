from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, class_type: str, username: str):
        if class_type == 'Beginner':
            player = Beginner(username)
        else:
            player = Advanced(username)

        self.player_repository.add(player)

        return f"Successfully added player of type {class_type} with username: {username}"

    def add_card(self, class_type: str, name: str):
        if class_type == 'Magic':
            card = MagicCard(name)
        else:
            card = TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {class_type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        card = self.card_repository.find(card_name)
        player = self.player_repository.find(username)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        res = ''
        for player in self.player_repository.players:
            res += f'Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n'
            for card in player.card_repository.cards:
                res += f'### Card: {card.name} - Damage: {card.damage_points}\n'
        return res

