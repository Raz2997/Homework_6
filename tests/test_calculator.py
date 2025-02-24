import pytest
from commands.command_manager import CommandManager
from commands.basic_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from commands.menu_command import MenuCommand

@pytest.fixture
def setup_commands():
    manager = CommandManager()
    manager.register("add", AddCommand())
    manager.register("subtract", SubtractCommand())
    manager.register("multiply", MultiplyCommand())
    manager.register("divide", DivideCommand())
    manager.register("menu", MenuCommand(manager))
    return manager

def test_menu_command(setup_commands, capsys):
    setup_commands.execute("menu")
    captured = capsys.readouterr()
    assert "Available Commands:" in captured.out

@pytest.mark.parametrize("command", ["add", "subtract", "multiply", "divide", "menu"])
def test_registered_commands(setup_commands, command):
    assert command in setup_commands.commands
