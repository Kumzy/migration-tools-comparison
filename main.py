from pathlib import Path

import sqlglot 
from rich.table import Table
from rich.console import Console

from simple_ddl_parser import DDLParser

def run_sqlglot():
    pathlist = Path('sql').glob('**/*.sql')
    for path in pathlist:
        path_in_str = str(path)   
        with open(path_in_str) as sql_file:
            data = sqlglot.parse_one(sql_file.read(), dialect='postgres')
            print(path_in_str)
            print(repr(data))

def run_ddl_parser():
    pathlist = Path('sql').glob('**/*.sql')
    for path in pathlist:
        path_in_str = str(path)   
        with open(path_in_str) as sql_file:
            data = DDLParser(sql_file.read()).run()
            print(path_in_str)
            print(data)

def main():
    console = Console()

    table = Table(
        "File",
        "Simple-ddl-parser",
        "sqlglot",
        show_lines=True
    )
    ddl_count = 0
    sqlglot_count = 0
    total = 0
    pathlist = Path('sql').glob('**/*.sql')
    for path in pathlist:
        path_in_str = str(path)   
        with open(path_in_str) as sql_file:
            raw_data = sql_file.read()
            try:
                data_ddl = DDLParser(raw_data).run()
            except ValueError:
                data_ddl = 'Error'
            data_sqlglot = sqlglot.parse_one(raw_data, dialect='postgres')
            table.add_row(path_in_str,str(data_ddl), str(repr(data_sqlglot)))

    console.print(table)


if __name__ == "__main__":
    # print("SQLGLOT")
    main()
    # print("DDLPARSER")
    # # run_ddl_parser()
    # grid = Table.grid(expand=True)
    # grid.add_column()
    # grid.add_column()
    # grid.add_row("Raising shields", "[bold magenta]COMPLETED [green]:heavy_check_mark:")
    # print(grid)

    # table = Table(
    # "Released",
    # "Title",
    # Column(header="Box Office", justify="right"),
    # title="Star Wars Movies"
    # )
    # print(table)
