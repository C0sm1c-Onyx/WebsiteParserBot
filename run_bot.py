import sys
from pathlib import Path

from telegram_bot.core import main
import asyncio


project_root = Path(__file__).parent.absolute()
sys.path.append(str(project_root))

if __name__ == '__main__':
    asyncio.run(main()) 