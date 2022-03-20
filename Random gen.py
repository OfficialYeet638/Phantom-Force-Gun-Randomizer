import random
import time
print("Welcome to the Phantom Force Randomize Loadout!")
print()
time.sleep(0.3)
print("No AA-12 or BFG Spam anymore!")
print()
time.sleep(0.3)
print("Only suitable for Private server or high rank players with most gun unlocked.")




Primary=["Assult Rifle","PDWs","LMGs","Sniper Rifles","Carbines","DMRs","Battle Rifles","Shotguns"]
ARs=["AK12","AN-94","AS VAL","SCAR-L","AUG A1","M16A4","G36","M16A3","AUG A2","K2","FAMAS F1","AK47","AUG A3","L85A2","HK416","AK74","AKM","AK103","TAR-21","StG-44","Type 88","M231","C7A2","G11K2"]
PDWs=["MP5K","UMP45","G36C","MP7","MAC10","P90","MP5","Colt SMG 633","L2A3","MP5SD","MP10","M3A1","MP5/10","Uzi","AUG A3 Para","K7","Krinkov","PPSh-41","FAL Para Shorty","Kriss Vector","PP-19 Bizon","MP40","X95 SMG","Tommy Gun","RAMA 1130"]
LMGs=["Colt LMG","M60","AUG HBAR","MG36","RPK12","L86 LSW","RPK","HK21","SCAR HAMR","RPK74","MG3KWS"]
Snipers=["Intervention","Remington 700","Dragunov SVU","AWS","BFG 50","AWM","TRG-42","Mosin Nagant","Dragunov SVDS","K14","Hecate II","M107","Steyr Scout","WA2000","NTW-20"]
Carbines=["M4A1","G36K","M4","L22","SCAR PDW","AKU12","Groza-1","AK12C","Honey Badger","K1A","SR-3M","Groza-4","MC51SD","FAL 50.63 Para","1858 Carbine","AK105","Jury","KAC SRR","Gyrojet Carbine","X95R","HK51B"]
DMRs=["MK11","SKS","SL-8","VSS Vintorez","M21","MSG90","Beowulf TCR","SA58 SPR","SCAR SSR"]
BRs=["M18","Beowulf ECR","SCAR-H","AK12BR","G3","AG-3","HK417","Henry 45-70","FAL 50.00"]
Shotguns=["KSG-12","Remington 870","DBV12","KS-23M","Saiga-12","Stevens DB","AA-12","SPAS-12"]

Secondary=["Pistols","Machine Pistols","Revolvers","Others"]
Pistols=["M9","G17","M1911","Desert Eagle L5","Izhevsk PB","M45A1","KG-99","Five Seven","ZIP 22","Makarov PM","GB-22","Desert Eagle XIX","Gyrojet Mark I"]
MP=["G18","93R","TEC-9","Micro Uzi","Škorpion vz. 61","MP1911","Arm Pistol"]
Revolvers=["MP412 REX","Mateba 6","1858 New Army","Redhawk 44","Judge","Executioner"]
Others=["Serbu Shotgun","SFG 50","M79 Thumper","Sawed Off","Saiga-12U","Obrez"]

switcher = {
    1:ARs,
    2:PDWs,
    3:LMGs,
    4:Snipers,
    5:Carbines,
    6:DMRs,
    7:BRs,
    8:Shotguns
}

switcher2 = {
    1:Pistols,
    2:MP,
    3:Revolvers,
    4:Others
}

a=random.randint(1,8)
b=switcher[a]
randomnizer=random.randint(0,len(b))
print()
print("Your Primary Weapon is:",Primary[a-1],"-----",b[randomnizer])
time.sleep(1)

a=random.randint(1,4)
b=switcher2[a]
randomnizer=random.randint(0,len(b))
print()
print("Your Secondary Weapon is:",Secondary[a-1],"-----",b[randomnizer])
time.sleep(300)
