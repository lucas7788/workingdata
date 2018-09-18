from boa.builtins import concat

from boa.interop.Ontology import Native
from boa.interop.Ontology.Native import Invoke
from boa.interop.System import Runtime
from boa.interop.System.Runtime import CheckWitness, Serialize, Deserialize, Notify
from boa.interop.System.Storage import Put, GetContext, Get

ont_addr = "AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV".ToScriptHash()
admin = "AeS7aUsTmf7egcGQGS88LZAGD8gNFmCJnD".ToScriptHash()
bondPrefix = "Bond_"
bondInvestorPrefix = "BondInvestor_"
bondPaidPrefix = "BondPaid_"

minInterval = 259200
minIssueCap = 100000
minInvestCap = 1000
minRound = 6

ctx = GetContext()

def main(operation, args):
    if operation == "IssueBond":
        if len(args) != 8:
            return False
        bond_name = args[0]
        par_value = args[1]
        start_time = args[2]
        maturity = args[3]
        interval = args[4]
        coupon_rate = args[5]
        total_amount = args[6]
        account = args[7]
        return IssueBond(bond_name, par_value, start_time, maturity, interval, coupon_rate, total_amount, account)
    if operation == "InvestBond":
        if len(args) != 3:
            return False
        bond_name = args[0]
        account = args[1]
        count = args[2]
        return InvestBond(bond_name, account, count)
    if operation == "PayInterstOrPrincipal":
        if len(args) != 2:
            return False
        bond_name = args[0]
        account = args[1]
        return PayInterstOrPrincipal(bond_name, account)
    if operation == "GetBond":
        if len(args) != 1:
            return False
        bond_name = args[0]
        return GetBond(bond_name)

def IssueBond(bondName: str, parValue: int, purchaseEndTime: int, interval: int, round: int, couponRate: int, totalCap: int, account: bytearray):
    if not CheckWitness(admin):
        return False
    if purchaseEndTime <= Runtime.GetTime():
        return False
    if totalCap < minIssueCap or round < minRound or couponRate <= 0 or interval < minInterval:
        return False
    if validateAddress(account):
        return False
    bond = {"purchaseEndTime": purchaseEndTime, "CouponRate": couponRate, "Interval": interval, "TotalCap": totalCap,
            "remainCap":totalCap, "Round": round}
    bond["Maturity"] = purchaseEndTime + round * interval
    b = Serialize(bond)
    Put(ctx, concat(bondPrefix, bondName), b)
    return True


def InvestBond(bondName: str, account: bytearray, bondNumber: int):
    if not CheckWitness(account):
        return False
    if bondNumber < 0 or not validateAddress(account) or not validateBond(bondName):
        return False
    bond = Deserialize(GetBond(bondName))

    if Runtime.GetTime() > bond["purchaseEndTime"]:
        Notify("bond subscription has been ended.")
        return False
    investValue = bondNumber * bond["ParValue"]
    if bond["remainCap"] < investValue:
        Notify("bond remain invest capacity not enough.")
        return False
    res = Native.Invoke(0, ont_addr, "transfer", [state(account, bond["Account"], investValue)])
    if res != b'\x01':
        return False
    bond["remainCap"] = bond["TotalCap"] - investValue
    investorKey = concat(bondName, account)
    balance = Get(ctx, investorKey)
    Put(ctx, investorKey, balance + investValue)
    return True

def PayInterstOrPrincipal(bondName: str, account: bytearray):
    if not validateBond(bondName):
        return False
    investorKey = concat(bondInvestorPrefix, bondName)
    investorKey = concat(investorKey, account)
    balance = Get(ctx, investorKey)
    if balance < minInvestCap:
        return False
    bond = Deserialize(GetBond(bondName))
    paidKey = concat(bondPaidPrefix, bondName)
    paidKey = concat(paidKey, account)
    paidRound = Get(ctx, paidKey)
    currentRound = (Runtime.GetTime() - bond["purchaseEndTime"]) / bond["Interval"]
    if paidRound > bond["Round"]:
        return False
    if currentRound > bond["Round"]:
        currentRound = bond["Round"]
    investValue = Get(ctx, investorKey)
    interst = (currentRound - paidRound) * (investValue * bond.CouponRate / 100)
    ret = bytearray()
    if currentRound == bond["Round"]:
        ret = Invoke(0, ont_addr, "transfer", [state(bond["Account"], account, interst + investValue)])
    else:
        ret = Invoke(0, ont_addr, "transfer", [state(bond["Account"], account, interst)])
    if ret != b'\x01':
        return False
    Put(ctx, paidKey, paidRound + 1)
    return True

def GetBond(bondName: str):
    return Get(ctx, concat(bondPrefix, bondName))

def validateAddress(address: bytearray):
    if len(address) != 20:
        return False
    return True

def validateBond(bondName: str):
    v = Get(ctx, concat(bondPrefix, bondName))
    if v == None or len(v) ==0:
        return False
    return True
