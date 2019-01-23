
import monkdata as monkdata
import dtree as dtree

#(ASSIGMENT 1.0) Calculate the Entropy of each dataset
print("Assigment 1")
entropyMONK1 = dtree.entropy(monkdata.monk1)
entropyMONK2 = dtree.entropy(monkdata.monk2)
entropyMONK3 = dtree.entropy(monkdata.monk3)
print("entropy monk1 = ",entropyMONK1)
print("entropy monk2 = ",entropyMONK2)
print("entropy monk3 = ",entropyMONK3)

print("//////////////////////////////////////////")

#(ASSIGMENT 3.0) Calculate the information gain of each subset
print("Assigment 2")
infGainMONK1a1 = dtree.averageGain(monkdata.monk1, monkdata.attributes[0])
infGainMONK1a2 = dtree.averageGain(monkdata.monk1, monkdata.attributes[1])
infGainMONK1a3 = dtree.averageGain(monkdata.monk1, monkdata.attributes[2])
infGainMONK1a4 = dtree.averageGain(monkdata.monk1, monkdata.attributes[3])
infGainMONK1a5 = dtree.averageGain(monkdata.monk1, monkdata.attributes[4])
infGainMONK1a6 = dtree.averageGain(monkdata.monk1, monkdata.attributes[5])

infGainMONK2a1 = dtree.averageGain(monkdata.monk2, monkdata.attributes[0])
infGainMONK2a2 = dtree.averageGain(monkdata.monk2, monkdata.attributes[1])
infGainMONK2a3 = dtree.averageGain(monkdata.monk2, monkdata.attributes[2])
infGainMONK2a4 = dtree.averageGain(monkdata.monk2, monkdata.attributes[3])
infGainMONK2a5 = dtree.averageGain(monkdata.monk2, monkdata.attributes[4])
infGainMONK2a6 = dtree.averageGain(monkdata.monk2, monkdata.attributes[5])

infGainMONK3a1 = dtree.averageGain(monkdata.monk3, monkdata.attributes[0])
infGainMONK3a2 = dtree.averageGain(monkdata.monk3, monkdata.attributes[1])
infGainMONK3a3 = dtree.averageGain(monkdata.monk3, monkdata.attributes[2])
infGainMONK3a4 = dtree.averageGain(monkdata.monk3, monkdata.attributes[3])
infGainMONK3a5 = dtree.averageGain(monkdata.monk3, monkdata.attributes[4])
infGainMONK3a6 = dtree.averageGain(monkdata.monk3, monkdata.attributes[5])

print("information-gain MONK-1, a1 = ",infGainMONK1a1)
print("information-gain MONK-1, a2 = ",infGainMONK1a2)
print("information-gain MONK-1, a3 = ",infGainMONK1a3)
print("information-gain MONK-1, a4 = ",infGainMONK1a4)
print("information-gain MONK-1, a5 = ",infGainMONK1a5)
print("information-gain MONK-1, a6 = ",infGainMONK1a6)

print("---------------------------------------------")

print("information-gain MONK-2, a1 = ",infGainMONK2a1)
print("information-gain MONK-2, a2 = ",infGainMONK2a2)
print("information-gain MONK-2, a3 = ",infGainMONK2a3)
print("information-gain MONK-2, a4 = ",infGainMONK2a4)
print("information-gain MONK-2, a5 = ",infGainMONK2a5)
print("information-gain MONK-2, a6 = ",infGainMONK2a6)

print("---------------------------------------------")

print("information-gain MONK-3, a1 = ",infGainMONK3a1)
print("information-gain MONK-3, a2 = ",infGainMONK3a2)
print("information-gain MONK-3, a3 = ",infGainMONK3a3)
print("information-gain MONK-3, a4 = ",infGainMONK3a4)
print("information-gain MONK-3, a5 = ",infGainMONK3a5)
print("information-gain MONK-3, a6 = ",infGainMONK3a6)



