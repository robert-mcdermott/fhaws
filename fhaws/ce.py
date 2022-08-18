import boto3

def get_charges(profile, firstMonth, lastMonth):
    accounts = {}
    session = boto3.Session(profile_name=profile)
    client = session.client('ce')
    response = client.get_cost_and_usage(
                    #TimePeriod={'Start':firstMonth.strftime("%Y-%m-%d"),'End':lastMonth.strftime("%Y-%m-%d")},
                    TimePeriod={'Start':firstMonth,'End':lastMonth},
                    Granularity='MONTHLY',
                    Metrics=['UNBLENDED_COST'],
                    GroupBy=[
                        {'Type':'DIMENSION','Key':'LINKED_ACCOUNT'},
                        {'Type':'DIMENSION','Key':'RECORD_TYPE'}
                        ]
                    )

    for item in response['ResultsByTime'][0]['Groups']:
        accountId = item['Keys'][0]
        account_type = item['Keys'][1]
        cost = float(item['Metrics']['UnblendedCost']['Amount'])
        if accountId not in accounts:
            accounts[accountId] = {}
        if "Discount" in account_type:
            accounts[accountId]['discount'] = cost
        if account_type == "Tax":
            accounts[accountId]['tax'] = cost
        if account_type == "Usage":
            accounts[accountId]['charges'] = cost

    total_discounts = 0
    total_charges = 0
    for account in accounts:
        print(account, accounts[account])
        total_discounts += accounts[account]['discount']
        total_charges += accounts[account]['charges'] 

    return accounts

if __name__ == "__main__":
    firstMonth  = "2022-07-01"
    lastMonth = "2022-08-01"
    get_charges('default', firstMonth, lastMonth)
