"""
Все вспомогательные функции
"""
from rich.console import Console
from rich.panel import Panel
# from rich.box import ASCII


_Console = Console()



def BasicChoices(
    arg: str = "",
    ignore: list = []
) -> bool:
    """
    Тут обрабатываются все возможные основные варианты ответа пользователя
    :param/arg/str: То, что ввёл пользователь
    :param/ignore/list: Перечисление игнорируемых функций{
        1: help
        2: training
    }
    :return/bool: True - Если совпало, False - если ничего не совпало
    """
    
    maxHelpLists: int = 1
    
    if arg.lower().strip() in ("help", "help1", "help 1") and (ignore != 1):
        _Console.print(
            Panel(
                f"\"[#ecfb23]help <1-{maxHelpLists}>[default]\" - страница вкладки help\n"
                f"\"[#ecfb23]trainig[default]\" - пройти обучение",
                title="[#02AA02]:HELP",
                title_align="left",
                subtitle=f"[#FFFFFF][1/{maxHelpLists}]",
                subtitle_align="right",
                expand=False
            )
        )
    
    else: return False
    return True