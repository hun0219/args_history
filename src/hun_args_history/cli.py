import pandas as pd
import argparse
from hun_args_history.db.utils import count, top, read_data
from tabulate import tabulate


def hello_msg():
    return "hello"


def cmd():
    msg = hello_msg()
    #print(msg)

    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument('-s', '--scount') 
    parser.add_argument('-t', '--top', type=int)
    parser.add_argument('-d', '--dt')
    parser.add_argument('-p', '--pret', action='store_true')
    
    args = parser.parse_args()
    print(args.scount, args.top, args.dt, args.pret)

    if args.scount:
        # TODO 명령어 카운트
        r = count(args.scount)
        print(f"{args.scount}사용 횟수는 {r}입니다.")
    elif args.top:
        # print(f"-t => {args.top}")
        #print(t)
        if args.dt:
            # TODO 특정 날짜의 명령어 TOP N
            # print(f"-d => {args.dt}")
            #t = top(args.top, args.dt, args.pret )
            #print(tabulate(t, tablefmt="outline" ))
            t = top(args.top, args.dt)
            if args.pret:
                t = top(args.top, args.dt, args.pret)
                print(t)
            else:
                print(t)
        else:
            #print("TODO - 에러 안내 메시지를 주면")
            parser.error("-t 옵션은 -d 옵션과 함께 사용하세요")
    else:
        # TODO - 사용법을 출력한다
        parser.print_help()
