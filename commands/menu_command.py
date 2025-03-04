import logging

logger = logging.getLogger(__name__)

class MenuCommand:
    """Command to display available commands."""
    
    def __init__(self, command_manager):
        self.command_manager = command_manager

    def execute(self):
        logger.info("\nAvailable Commands:")
        for command in self.command_manager.commands.keys():
            logger.info(f"- {command}")
        logger.info("Type 'exit' to quit the calculator.")