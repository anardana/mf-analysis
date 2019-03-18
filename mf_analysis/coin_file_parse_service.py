from mf_analysis.headers import CoinExportHeaders


def parse(csv):
    transactions = []
    for line in csv:
        tokens = line.split(",")

        if len(tokens) == len(CoinExportHeaders):  # Skip empty or incomplete lines
            transaction_info = {}
            i = 0
            for field in CoinExportHeaders:
                transaction_info[field] = tokens[i]
                i = i + 1

            transactions.append(transaction_info)

    return transactions


def read_file(path):
    with open(path, "r") as file:
        file_text = file.read()
        csv_content = file_text.split("\n")[1:]

    return csv_content
