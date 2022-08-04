import boto3

def get_users(profile):
    """get_users returns a list of all IAM user objects in the accounts"""
    session = boto3.Session(profile_name=profile)
    client = session.client("iam")
    response = client.list_users()

    all_users = []

    users = response["Users"]

    while response["IsTruncated"]:
    #while "Marker" in response: # this works too
        response = client.list_users(Marker=response["Marker"])
        users.extend(response["Users"])
    
    for user in users:
        all_users.append(user)
    
    return(all_users)


def inventory_users(profile):
    """inventory_users returns a CSV of IAM users"""
    # need to add info about API keys and MFAs
    users = get_users(profile)
    inventory = ["UserName, UserId, Arn, CreateDate, PasswordLastUsed"]
    for u in users:
        username = u["UserName"]
        id = u["UserId"]
        arn = u["Arn"]
        cdate = u["CreateDate"]
        try:
            pdate = u["PasswordLastUsed"]
        except:
            pdate = "Never"
        inventory.append("%s, %s, %s, %s, %s" % (username, id, arn, cdate, pdate))

    return("\n".join(inventory))


def get_mfa(profile):
    session = boto3.Session(profile_name=profile)
    client = session.client("iam")
    response = client.list_virtual_mfa_devices()
    virtual_mfas = response['VirtualMFADevices']
    for mfa in virtual_mfas:
        print(mfa["SerialNumber"], end = '')
        try:
            print(mfa["User"]["UserName"], end = '')
            print(mfa["EnableDate"])
        except:
            print("NA, NA")

def get_api_keys(profile):
    pass

def get_ssh_keys():
    pass

if __name__ == "__main__":
    import sys
    profile = sys.argv[1]
    print(inventory_users(profile))

