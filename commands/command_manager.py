class CommandManager:
    """Manages command registration and execution."""
    
    def __init__(self):
        self.commands = {}

    def register(self, name, command):
        """Register a new command."""
        self.commands[name] = command

    def execute(self, name):
        """Execute a registered command."""
        if name in self.commands:
            self.commands[name].execute()
        else:
            print(f"Command '{name}' not found.")
