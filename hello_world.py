class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

def solution(queries):
    return_queries = []
    accounts = {}
    for i in queries:
        if i[0] == "CREATE_ACCOUNT":
            if i[2] not in accounts:
                account = Account(i[2])
                accounts[i[2]] = account
                return_queries.append('true')
            else:
                return_queries.append('false')
        if i[0] == "DEPOSIT":
            if i[2] in accounts:
                accounts[i[2]].balance += int(i[3])
                return_queries.append(str(accounts[i[2]].balance))
            else:
                return_queries.append("")
        if i[0] == "TRANSFER":
            if i[2] in accounts:
                if i[3] in accounts:
                    # both accounts exist
                    if accounts[i[2]].balance >= int(i[-1]):
                        # good to go
                        accounts[i[2]].balance -= int(i[-1])
                        accounts[i[3]].balance += int(i[-1])
                        return_queries.append(str(accounts[i[2]].balance))
                    else:
                        # not enough
                        return_queries.append("")
                else:
                    # not good
                    return_queries.append("")
            else:
                # not good
                return_queries.append("")
        print(f'{i}\n{return_queries}')
    return return_queries


q = [
      [
        "CREATE_ACCOUNT",
        "1",
        "acc1"
      ],
      [
        "CREATE_ACCOUNT",
        "2",
        "acc2"
      ],
      [
        "CREATE_ACCOUNT",
        "3",
        "acc3"
      ],
      [
        "CREATE_ACCOUNT",
        "4",
        "acc4"
      ],
      [
        "CREATE_ACCOUNT",
        "5",
        "acc5"
      ],
      [
        "DEPOSIT",
        "6",
        "acc1",
        "1000"
      ],
      [
        "DEPOSIT",
        "7",
        "acc2",
        "2000"
      ],
      [
        "DEPOSIT",
        "8",
        "acc3",
        "3000"
      ],
      [
        "DEPOSIT",
        "9",
        "acc4",
        "2000"
      ],
      [
        "DEPOSIT",
        "10",
        "acc5",
        "1000"
      ],
      [
        "DEPOSIT",
        "11",
        "acc6",
        "100"
      ],
      [
        "DEPOSIT",
        "12",
        "acc7",
        "1000"
      ],
      [
        "CREATE_ACCOUNT",
        "13",
        "acc5"
      ],
      [
        "CREATE_ACCOUNT",
        "14",
        "acc3"
      ],
      [
        "CREATE_ACCOUNT",
        "16",
        "acc6"
      ],
      [
        "DEPOSIT",
        "17",
        "acc6",
        "1000"
      ],
      [
        "TRANSFER",
        "18",
        "acc6",
        "acc1",
        "99"
      ],
      [
        "TRANSFER",
        "19",
        "acc6",
        "acc2",
        "2"
      ],
      [
        "TRANSFER",
        "20",
        "acc6",
        "acc3",
        "66"
      ],
      [
        "TRANSFER",
        "21",
        "acc6",
        "acc1",
        "2"
      ],
      [
        "TRANSFER",
        "22",
        "acc6",
        "acc3",
        "66"
      ],
      [
        "TRANSFER",
        "23",
        "acc6",
        "acc2",
        "99"
      ],
      [
        "TRANSFER",
        "24",
        "acc6",
        "acc1",
        "99"
      ],
      [
        "TRANSFER",
        "25",
        "acc6",
        "acc4",
        "66"
      ],
      [
        "TRANSFER",
        "26",
        "acc6",
        "acc5",
        "67"
      ],
      [
        "TRANSFER",
        "27",
        "acc6",
        "acc5",
        "66"
      ],
      [
        "TRANSFER",
        "28",
        "acc6",
        "acc2",
        "99"
      ],
      [
        "TRANSFER",
        "29",
        "acc6",
        "acc3",
        "68"
      ],
      [
        "TRANSFER",
        "30",
        "acc6",
        "acc4",
        "68"
      ],
      [
        "TRANSFER",
        "31",
        "acc6",
        "acc4",
        "66"
      ],
      [
        "TRANSFER",
        "32",
        "acc6",
        "acc5",
        "67"
      ],
      [
        "TRANSFER",
        "33",
        "acc7",
        "acc1",
        "100"
      ],
      [
        "TRANSFER",
        "34",
        "acc1",
        "acc7",
        "100"
      ],
      [
        "TRANSFER",
        "35",
        "acc6",
        "acc3",
        "1"
      ],
      [
        "TRANSFER",
        "36",
        "acc3",
        "acc3",
        "239"
      ],
      [
        "DEPOSIT",
        "37",
        "acc1",
        "800"
      ],
      [
        "DEPOSIT",
        "38",
        "acc2",
        "800"
      ],
      [
        "DEPOSIT",
        "39",
        "acc3",
        "800"
      ],
      [
        "DEPOSIT",
        "40",
        "acc4",
        "800"
      ],
      [
        "DEPOSIT",
        "41",
        "acc5",
        "800"
      ],
      [
        "DEPOSIT",
        "42",
        "acc6",
        "1000"
      ],
      [
        "TRANSFER",
        "43",
        "acc6",
        "acc3",
        "991"
      ],
      [
        "TRANSFER",
        "44",
        "acc6",
        "acc3",
        "1"
      ]
    ]
a = solution(q)

print(a)