from rich.console import Console
from rich.panel import Panel
from rich.box import ASCII
# from rich.markdown import Markdown
# from rich.progress import Progress
# from rich.syntax import Syntax
# from rich.table import Table
from save import Save
from function import BasicChoices


_Console = Console()
_Save = Save()



def main():
    _run: bool = True
    _data: dict = _Save.getSave()
    _visits: int = _data["visits"]
    _prefix: str = _data["prefix"]
    _vr_entry_user: str = "" 

    if _visits == 0:
        print(
            "\n\n\n"
            ":Добро пожаловать в wstCoins game!\n"
            "Если желаете пройти обучение напишите \"training\"."
        )
        # Увеличиваем "visits" на 1 и сохраняем это
        _data["visits"] += 1
        _Save.doSave(_data)
        input("/")
        
    while _run:
        # Каждый цикл переправиряем переменную
        _prefix = _Save.getSave()["prefix"]
        
        print("\n\n:HUB")
        _vr_entry_user = input(_prefix)
        
        _vr11 = BasicChoices(_vr_entry_user)
        
        
        
        
        
        
        









if __name__ == "__main__":
    try:
        main()
        
        
    except:
        _Console.print_exception()
        quit()