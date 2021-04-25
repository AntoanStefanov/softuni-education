class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):  # Takes object of class Player
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        if player.guild != 'Unaffiliated':
            return f"Player {player.name} is in another guild."
        if player.guild == 'Unaffiliated':
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:  # Problem here?
                player.guild = 'Unaffiliated'
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = ''
        for player in self.players:
            players_info += f'{player.player_info()}'
        return f'Guild: {self.name}\n{players_info}'
