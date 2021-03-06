# coding=utf-8
from commands.abstract_command import AbstractCommand
from config import Config
from model.karma import Karma


class GetLeaderBoardCommand(AbstractCommand):
    def get_purpose(self):
        return "Shows the best of the best!"

    def execute(self, size: int=3):
        return Karma.get_leader_board(size=size)

    def __init__(self):
        super(GetLeaderBoardCommand, self)
        config = Config()
        config.connect_to_db()
