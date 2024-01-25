class Solution:
    def invalidTransactions(self, transactions):
        transactionMap = {}
        invalidTransactions = []
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            if int(amount) > 1000:
                invalidTransactions.append(transaction)
            elif name in transactionMap:
                prev_name, prev_time, prev_amount, prev_city = transactionMap[name].split(",")
                
                if not int(time) - int(prev_time) > 60 and prev_city != city:
                    invalidTransactions.append(transaction)
                    if transactionMap[name] not in invalidTransactions: invalidTransactions.append(transactionMap[name])
            else:
                pass
            transactionMap[name] = transaction

        return invalidTransactions

sol = Solution()
print(sol.invalidTransactions(
    ["alice,20,800,mtv","bob,50,1200,mtv"]
))