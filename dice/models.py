from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""




class Constants(BaseConstants):
    name_in_url = 'dice'
    players_per_group = None
    num_rounds = 1
    report_coef = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dice = models.IntegerField(min=1, max=6,
                               verbose_name='Dice Number')
    report = models.StringField(verbose_name='Dice Report', blank=True)

    def set_payoff(self):
        self.payoff = Constants.report_coef * self.dice