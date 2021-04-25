class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_info = ''
        for skill, mana_cost in self.skills.items():
            skills_info += f"==={skill} - {mana_cost}\n"
        return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{skills_info}'


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):  # Takes object of class Player
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


player = Player("George", 50, 100)
p2 = Player("Bob", 1, 2)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.assign_player(p2))
print(guild.guild_info())
