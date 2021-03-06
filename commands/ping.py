from category import Category
from commands.command import Command


class Ping(Command):
    def __init__(self):
        aliases = ["ping"]
        shortdesc = "Sends 'Pong' back"
        longdesc = "This command not only allows you to check if the bot is active, it also allows you to check " \
                   "response time. "
        usage = "/".join(aliases)
        category = Category.CORE
        super().__init__(aliases , shortdesc , longdesc , usage , category)

    async def execute(self , client , message , args , **kwargs):
        # No arguments needed
        if len(args) != 0:
            return False  # Too many arguments, print syntax
        # Send back pong.
        await client.send_message(message.channel , content="Pong!")
        return True  # Command was run successfully

# TODO: Add response time in ms. Basically count ms until we receive the message "Pong!" sent by the bot then edit
#       the message. This might a little tricky since on_message is handled in constantine.py
